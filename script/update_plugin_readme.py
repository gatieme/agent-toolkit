#!/usr/bin/env python3
"""
更新 plugin/README.md 中的 GitHub 项目星级和 Star 数量

解析 README.md 中的 Markdown 表格，获取 GitHub 仓库信息，
并更新推荐星级和 Star 数量。

使用方法:
  python script/update_plugin_readme.py --token YOUR_TOKEN
  python script/update_plugin_readme.py --dry-run
  python script/update_plugin_readme.py --backup
"""

import os
import sys
import argparse
import re
import json
import tempfile
import shutil
from typing import Optional, Dict, List, Tuple
from datetime import datetime

# 复用 get_github_stars.py 的 GitHubAPI 类
from get_github_stars import GitHubAPI


class MarkdownTableParser:
    """Markdown 表格解析器"""

    # GitHub URL 正则模式
    GITHUB_URL_PATTERN = re.compile(
        r'https://github\.com/([^/]+)/([^/\s\)]+)'
    )

    # Markdown 链接模式 [text](url)
    MD_LINK_PATTERN = re.compile(
        r'\[([^\]]+)\]\((https://github\.com/[^/\s\)]+/[^/\s\)]+)\)'
    )

    def __init__(self, content: str):
        """
        初始化解析器

        Args:
            content: Markdown 文件内容
        """
        self.content = content
        self.lines = content.split('\n')

    def find_table_rows(self) -> List[Dict]:
        """
        查找表格行并提取 GitHub 仓库信息

        Returns:
            表格行信息列表，每行包含行号、原内容、GitHub 仓库信息等
        """
        rows = []
        in_table = False
        table_start = -1

        for i, line in enumerate(self.lines):
            # 检测表头分隔行
            if re.match(r'^[\|\s\-:]+\|?$', line):
                if table_start >= 0:
                    in_table = True
                continue

            # 检测表格开始（包含 | 分隔符）
            if '|' in line and not in_table:
                table_start = i
                continue

            # 如果在表格内
            if in_table:
                # 表格结束条件
                if '|' not in line.strip():
                    in_table = False
                    table_start = -1
                    continue

                # 跳过分隔行
                if re.match(r'^[\|\s\-:]+\|?$', line):
                    continue

                # 解析行内容
                row_info = self._parse_table_row(line, i)
                if row_info:
                    rows.append(row_info)

        return rows

    def _parse_table_row(self, line: str, line_num: int) -> Optional[Dict]:
        """
        解析单行表格内容

        Args:
            line: 表格行内容
            line_num: 行号

        Returns:
            行信息字典，包含 owner/repo、列内容等
        """
        # 提取 GitHub URL
        match = self.GITHUB_URL_PATTERN.search(line)
        if not match:
            return None

        owner = match.group(1)
        repo = match.group(2)

        return {
            'line_num': line_num,
            'original_line': line,
            'owner': owner,
            'repo': repo,
            'full_name': f'{owner}/{repo}',
        }

    def extract_github_repos(self) -> List[Dict]:
        """
        提取所有 GitHub 仓库

        Returns:
            仓库信息列表，包含 owner/repo
        """
        repos = set()  # 使用集合去重

        for line in self.lines:
            matches = self.GITHUB_URL_PATTERN.findall(line)
            for owner, repo in matches:
                repos.add((owner, repo))

        return [
            {'owner': owner, 'repo': repo, 'full_name': f'{owner}/{repo}'}
            for owner, repo in sorted(repos)
        ]

    def update_table_row(self, line_num: int, repo_data: Dict) -> str:
        """
        更新表格行

        Args:
            line_num: 行号
            repo_data: GitHub 仓库数据，包含 rating, rating_display, stars 等

        Returns:
            更新后的行内容
        """
        original_line = self.lines[line_num]
        rating_display = repo_data.get('rating_display', '⭐')
        stars = repo_data.get('stars', 0)

        # 查找第一个 | 并在该列后更新
        # 假设格式：| 项目名 | 推荐 | Stars | ...
        # 简单策略：更新包含数字的 Stars 列
        parts = original_line.split('|')

        # 寻找可能的 Stars 列（包含数字）
        for i, part in enumerate(parts):
            stripped = part.strip()
            # 查找现有的 Star 数量格式（如 1,234 或 1234）
            if re.search(r'\d[, ]?\d', stripped):
                # 替换为新的 Star 数量
                parts[i] = f' {stars:,} '
                break

        # 寻找可能的推荐列（包含 ⭐ 或空白）
        for i, part in enumerate(parts):
            stripped = part.strip()
            if stripped == '' or re.match(r'^⭐+$', stripped):
                # 替换为新的星级
                parts[i] = f' {rating_display} '
                break

        return '|'.join(parts)


class GitHubRepoFetcher:
    """GitHub 仓库批量获取器"""

    def __init__(self, api: GitHubAPI, delay: float = 1.0):
        """
        初始化获取器

        Args:
            api: GitHub API 客户端
            delay: 请求间隔（秒），默认 1 秒
        """
        self.api = api
        self.delay = delay

    def fetch_batch(self, repos: List[Dict]) -> Dict[str, Dict]:
        """
        批量获取仓库信息

        Args:
            repos: 仓库信息列表，每个包含 full_name

        Returns:
            字典，key 为 full_name，value 为仓库评分数据
        """
        results = {}
        total = len(repos)

        for i, repo_info in enumerate(repos):
            owner = repo_info['owner']
            repo = repo_info['repo']
            full_name = repo_info['full_name']

            print(f'[{i+1}/{total}] 获取 {full_name}...', flush=True)

            try:
                repo_data = self.api.get_repository_info(owner, repo)
                # 使用 get_github_stars.py 的评分逻辑
                from get_github_stars import GitHubRating
                rating_data = GitHubRating.get_repository_data(repo_data)
                results[full_name] = rating_data
            except Exception as e:
                print(f'  警告: {e}', file=sys.stderr)
                # 失败时保留空结果
                results[full_name] = None

            # 速率限制延迟
            if i < total - 1:
                import time
                time.sleep(self.delay)

        return results


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description="更新 plugin/README.md 中的 GitHub 项目星级和 Star 数量",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 预览变更（不修改文件）
  python script/update_plugin_readme.py --dry-run

  # 使用 GitHub Token
  python script/update_plugin_readme.py --token YOUR_TOKEN

  # 备份并更新
  python script/update_plugin_readme.py --backup

  # 组合选项
  python script/update_plugin_readme.py --token YOUR_TOKEN --backup --dry-run

环境变量:
  GITHUB_TOKEN: GitHub Personal Access Token
        """
    )

    parser.add_argument(
        "--token",
        type=str,
        default=None,
        help="GitHub Personal Access Token（也可通过 GITHUB_TOKEN 环境变量设置）"
    )

    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="预览模式：显示将要进行的变更，不实际修改文件"
    )

    parser.add_argument(
        "--backup",
        action="store_true",
        help="创建备份文件：plugin/README.md.backup"
    )

    args = parser.parse_args()

    # 读取 README.md
    readme_path = "plugin/README.md"

    if not os.path.exists(readme_path):
        print(f"错误: 文件不存在 {readme_path}", file=sys.stderr)
        sys.exit(1)

    with open(readme_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # 解析 Markdown
    parser_obj = MarkdownTableParser(content)
    repos = parser_obj.extract_github_repos()

    if not repos:
        print("未找到 GitHub 仓库链接")
        return

    print(f"找到 {len(repos)} 个 GitHub 仓库")

    # 获取仓库数据
    api = GitHubAPI(token=args.token)
    fetcher = GitHubRepoFetcher(api)
    repo_data = fetcher.fetch_batch(repos)

    # 更新表格行
    rows = parser_obj.find_table_rows()
    updated_lines = parser_obj.lines.copy()

    for row in rows:
        full_name = row['full_name']
        data = repo_data.get(full_name)

        if data:
            line_num = row['line_num']
            new_line = parser_obj.update_table_row(line_num, data)
            updated_lines[line_num] = new_line
            print(f"  更新: {full_name} -> {data['rating_display']} ({data['stars']:,} stars)")

    # 输出结果
    if args.dry_run:
        print("\n=== 预览变更 ===")
        for i, (old, new) in enumerate(zip(parser_obj.lines, updated_lines)):
            if old != new:
                print(f"\n行 {i+1}:")
                print(f"  旧: {old}")
                print(f"  新: {new}")
        print("\n预览模式，未实际修改文件")
    else:
        # 创建备份
        if args.backup:
            backup_path = f"{readme_path}.backup"
            shutil.copy2(readme_path, backup_path)
            print(f"备份已创建: {backup_path}")

        # 原子性写入
        new_content = '\n'.join(updated_lines)

        with tempfile.NamedTemporaryFile(
            mode='w',
            encoding='utf-8',
            prefix='update_plugin_readme_',
            suffix='.tmp',
            dir=os.path.dirname(readme_path),
            delete=False
        ) as tmp:
            tmp.write(new_content)
            tmp_path = tmp.name

        # 重命名（原子操作）
        shutil.move(tmp_path, readme_path)
        print(f"\n已更新: {readme_path}")


if __name__ == "__main__":
    main()
