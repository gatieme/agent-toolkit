#!/usr/bin/env python3
"""
获取 GitHub 仓库 Stars 数量并评分

支持通过 GitHub API 获取指定仓库的 stars 数量，并根据多项指标进行评分。

使用方法:
  python script/get_github_stars.py owner/repo
  python script/get_github_stars.py snarktank/ralph
  python script/get_github_stars.py owner/repo --token YOUR_TOKEN

环境变量:
  GITHUB_TOKEN: GitHub Personal Access Token (推荐用于提高速率限制)
"""

import os
import sys
import argparse
import urllib.request
import urllib.error
import json
from typing import Optional, Dict


class GitHubAPI:
    """GitHub API 客户端"""

    API_BASE = "https://api.github.com"

    def __init__(self, token: Optional[str] = None):
        """
        初始化 GitHub API 客户端

        Args:
            token: GitHub Personal Access Token，可从环境变量 GITHUB_TOKEN 读取
        """
        self.token = token or os.environ.get("GITHUB_TOKEN")

    def _make_request(self, endpoint: str) -> Dict:
        """
        发起 API 请求

        Args:
            endpoint: API 端点路径

        Returns:
            响应 JSON 数据

        Raises:
            urllib.error.HTTPError: 请求失败
            ValueError: JSON 解析失败
        """
        url = f"{self.API_BASE}{endpoint}"

        headers = {
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "agent-toolkit"
        }

        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"

        req = urllib.request.Request(url, headers=headers)

        with urllib.request.urlopen(req) as response:
            data = response.read().decode("utf-8")
            return json.loads(data)

    def get_stars(self, owner: str, repo: str) -> Dict:
        """
        获取仓库 stars 数量

        Args:
            owner: 仓库所有者
            repo: 仓库名称

        Returns:
            仓库信息字典，包含 stargazers_count 等
        """
        return self._make_request(f"/repos/{owner}/{repo}")

    def get_repository_info(self, owner: str, repo: str) -> Dict:
        """
        获取仓库完整信息

        Args:
            owner: 仓库所有者
            repo: 仓库名称

        Returns:
            仓库信息字典
        """
        return self._make_request(f"/repos/{owner}/{repo}")


class GitHubRating:
    """GitHub 仓库评分系统"""

    @staticmethod
    def _score_component(value: int, thresholds: list[int]) -> int:
        """
        基于阈值计算组件得分（1-5分）

        Args:
            value: 指标值
            thresholds: 阈值列表，如 [0, 10, 50, 200, 1000]

        Returns:
            得分（1-5）
        """
        for i, threshold in enumerate(reversed(thresholds[1:])):
            if value > threshold:
                return 5 - i
        return 1

    @staticmethod
    def calculate_score(repo_info: Dict) -> int:
        """
        计算仓库评分（1-5星）

        评分标准（阈值评分）：
        - Stars 权重 60%，阈值 [0, 50, 200, 1000, 5000]
        - Forks 权重 15%，阈值 [0, 10, 50, 200, 1000]
        - Watchers 权重 10%，阈值 [0, 10, 30, 100, 300]
        - Issues 权重 15%，阈值 [0, 5, 20, 50, 100]

        Args:
            repo_info: GitHub API 返回的仓库信息

        Returns:
            评分（1-5）
        """
        stars = repo_info.get('stargazers_count', 0)
        forks = repo_info.get('forks_count', 0)
        watchers = repo_info.get('subscribers_count', 0)
        open_issues = repo_info.get('open_issues_count', 0)

        # 阈值评分
        stars_score = GitHubRating._score_component(stars, [0, 5000, 10000, 50000, 100000])
        forks_score = GitHubRating._score_component(forks, [0, 100, 200, 1000, 5000])
        watchers_score = GitHubRating._score_component(watchers, [0, 100, 300, 1000, 5000])
        issues_score = GitHubRating._score_component(open_issues, [0, 100, 200, 500, 1000])

        # 综合评分（加权平均）
        total_score = (
            stars_score * 0.60 +
            forks_score * 0.15 +
            watchers_score * 0.10 +
            issues_score * 0.15
        )

        # 转换为 1-5 星
        if total_score >= 4.5:
            return 5
        elif total_score >= 3.5:
            return 4
        elif total_score >= 2.5:
            return 3
        elif total_score >= 1.5:
            return 2
        else:
            return 1

    @staticmethod
    def get_star_display(rating: int) -> str:
        """
        获取星号显示

        Args:
            rating: 评分（1-5）

        Returns:
            星号字符串
        """
        return "⭐" * rating

    @staticmethod
    def get_repository_data(repo_info: Dict) -> Dict:
        """
        获取仓库的完整评分数据

        Args:
            repo_info: GitHub API 返回的仓库信息

        Returns:
            包含评分和各项指标的字典
        """
        rating = GitHubRating.calculate_score(repo_info)

        return {
            'stars': repo_info.get('stargazers_count', 0),
            'forks': repo_info.get('forks_count', 0),
            'watchers': repo_info.get('subscribers_count', 0),
            'open_issues': repo_info.get('open_issues_count', 0),
            'updated_at': repo_info.get('updated_at', ''),
            'rating': rating,
            'rating_display': GitHubRating.get_star_display(rating),
            'description': repo_info.get('description', 'N/A'),
            'url': repo_info.get('html_url', 'N/A'),
            'full_name': repo_info.get('full_name', ''),
        }


def parse_repo_string(repo_str: str) -> tuple[str, str]:
    """
    解析仓库字符串

    Args:
        repo_str: 仓库字符串，格式为 "owner/repo"

    Returns:
        (owner, repo) 元组

    Raises:
        ValueError: 格式错误
    """
    parts = repo_str.split("/")
    if len(parts) != 2 or not parts[0] or not parts[1]:
        raise ValueError(f"仓库格式错误: {repo_str}，正确格式应为 owner/repo")
    return parts[0], parts[1]


def format_number(num: int) -> str:
    """
    格式化数字显示

    Args:
        num: 要格式化的数字

    Returns:
        格式化后的字符串
    """
    return f"{num:,}"


def main():
    """主函数"""
    parser = argparse.ArgumentParser(
        description="获取 GitHub 仓库 Stars 数量并评分",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
示例:
  # 获取仓库信息和评分
  python script/get_github_stars.py snarktank/ralph

  # 使用 GitHub Token（提高速率限制）
  python script/get_github_stars.py owner/repo --token YOUR_TOKEN

  # 以 JSON 格式输出完整仓库信息
  python script/get_github_stars.py owner/repo --json

  # 仅输出评分（用于脚本调用）
  python script/get_github_stars.py owner/repo --rating

环境变量:
  GITHUB_TOKEN: GitHub Personal Access Token

评分标准:
  ⭐⭐⭐⭐⭐  5星: 综合得分 >= 4.5
  ⭐⭐⭐⭐    4星: 综合得分 >= 3.5
  ⭐⭐⭐      3星: 综合得分 >= 2.5
  ⭐⭐        2星: 综合得分 >= 1.5
  ⭐          1星: 综合得分 < 1.5

  评分权重：
    - Stars (60%):     1星≤5K, 2星≤10K, 3星≤50K, 4星≤100K, 5星>100K
    - Forks (15%):     1星≤100, 2星≤200, 3星≤1K,  4星≤5K,   5星>5K
    - Watchers (10%):  1星≤100, 2星≤300, 3星≤1K,  4星≤5K,   5星>5K
    - Issues (15%):    1星≤100, 2星≤200, 3星≤500, 4星≤1K,   5星>1K
        """
    )

    parser.add_argument(
        "repo",
        help="GitHub 仓库，格式为 owner/repo"
    )

    parser.add_argument(
        "--token",
        type=str,
        default=None,
        help="GitHub Personal Access Token（也可通过 GITHUB_TOKEN 环境变量设置）"
    )

    parser.add_argument(
        "--json",
        action="store_true",
        help="以 JSON 格式输出完整仓库信息"
    )

    parser.add_argument(
        "--rating",
        action="store_true",
        help="仅输出评分（1-5）和星级显示，用于脚本调用"
    )

    parser.add_argument(
        "--export",
        action="store_true",
        help="输出 Python 可导入的数据格式（可导入到其他脚本使用）"
    )

    args = parser.parse_args()

    try:
        # 解析仓库字符串
        owner, repo = parse_repo_string(args.repo)

        # 创建 API 客户端
        api = GitHubAPI(token=args.token)

        # 获取仓库信息
        if not args.json and not args.rating and not args.export:
            print(f"正在获取 {owner}/{repo} 的信息...")
        repo_info = api.get_repository_info(owner, repo)

        # 计算评分
        data = GitHubRating.get_repository_data(repo_info)

        if args.json:
            # JSON 输出
            print(json.dumps(data, indent=2, ensure_ascii=False))
        elif args.export:
            # Python 可导入格式输出
            export_data = {
                'stars': data['stars'],
                'forks': data['forks'],
                'watchers': data['watchers'],
                'issues': data['open_issues'],
                'rating': data['rating'],
                'rating_display': data['rating_display'],
            }
            print(json.dumps(export_data, ensure_ascii=False))
        elif args.rating:
            # 仅输出评分
            print(f"{data['rating']}:{data['rating_display']}:{data['stars']}")
        else:
            # 美观输出
            print("\n" + "=" * 60)
            print(f"📦 {owner}/{repo}")
            print("=" * 60)
            print(f"  ⭐ Stars:       {format_number(data['stars'])}")
            print(f"  🔀 Forks:       {format_number(data['forks'])}")
            print(f"  👀 Watchers:    {format_number(data['watchers'])}")
            print(f"  📝 Issues:      {format_number(data['open_issues'])}")
            print(f"  📅 更新时间:   {data['updated_at']}")
            print(f"  ⭐ 评分:       {data['rating_display']} ({data['rating']}星)")
            print(f"  📄 Description: {data['description']}")
            print(f"  🔗 URL:         {data['url']}")
            print("=" * 60)

    except ValueError as e:
        print(f"❌ 错误: {e}", file=sys.stderr)
        sys.exit(1)
    except urllib.error.HTTPError as e:
        print(f"❌ HTTP 错误: {e.code} - {e.reason}", file=sys.stderr)
        if e.code == 404:
            print("   仓库不存在或无法访问", file=sys.stderr)
        elif e.code == 403:
            print("   可能达到了 API 速率限制，请使用 GitHub Token", file=sys.stderr)
        sys.exit(1)
    except urllib.error.URLError as e:
        print(f"❌ 网络连接错误: {e.reason}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"❌ JSON 解析错误: {e}", file=sys.stderr)
        sys.exit(1)
    except Exception as e:
        print(f"❌ 未知错误: {e}", file=sys.stderr)
        sys.exit(1)


if __name__ == "__main__":
    main()
