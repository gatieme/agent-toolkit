#!/usr/bin/env python3
"""
update_plugin_readme.py 集成测试

测试 Markdown 解析、表格更新、备份功能等。
"""

import pytest
import tempfile
import os
import json
import time
from unittest.mock import Mock, patch, MagicMock
from update_plugin_readme import MarkdownTableParser, GitHubRepoFetcher


class TestMarkdownTableParser:
    """测试 Markdown 表格解析器"""

    def test_extract_github_repos_basic(self):
        """测试提取基本的 GitHub 仓库链接"""
        content = """
| 项目 | Stars |
|-------|-------|
| [Test](https://github.com/test/repo) | 100 |
| [Demo](https://github.com/user/demo) | 50 |
"""
        parser = MarkdownTableParser(content)
        repos = parser.extract_github_repos()

        assert len(repos) == 2
        assert repos[0]['full_name'] == 'test/repo'
        assert repos[1]['full_name'] == 'user/demo'

    def test_extract_github_repos_dedup(self):
        """测试去重功能"""
        content = """
# 重复链接
[Link](https://github.com/test/repo)
[Another Link](https://github.com/test/repo)
[Different](https://github.com/user/demo)
"""
        parser = MarkdownTableParser(content)
        repos = parser.extract_github_repos()

        assert len(repos) == 2
        names = [r['full_name'] for r in repos]
        assert 'test/repo' in names
        assert 'user/demo' in names

    def test_extract_github_repos_with_numbers_and_dash(self):
        """测试包含数字和连字符的仓库名"""
        content = """
| 项目 | Stars |
|-------|-------|
| [Test-123](https://github.com/test-org/project-123) | 100 |
| [Demo](https://github.com/my-org_2/demo-lib) | 50 |
"""
        parser = MarkdownTableParser(content)
        repos = parser.extract_github_repos()

        assert len(repos) == 2
        # 排序后检查
        names = [r['full_name'] for r in repos]
        assert 'test-org/project-123' in names
        assert 'my-org_2/demo-lib' in names

    def test_find_table_rows(self):
        """测试查找表格行"""
        content = """# 标题

| 项目 | 推荐 | Stars | 描述 |
|-------|--------|-------|--------|
| [Test](https://github.com/test/repo) | ⭐⭐⭐ | 1,234 | 这是一个测试项目 |

其他内容。
"""
        parser = MarkdownTableParser(content)
        rows = parser.find_table_rows()

        assert len(rows) == 1
        assert rows[0]['full_name'] == 'test/repo'
        assert rows[0]['owner'] == 'test'
        assert rows[0]['repo'] == 'repo'

    def test_find_table_rows_multiple_tables(self):
        """测试查找多个表格"""
        content = """# 表格 1

| 项目 | Stars |
|-------|-------|
| [Test1](https://github.com/test/repo1) | 100 |

# 表格 2

| 项目 | Stars |
|-------|-------|
| [Test2](https://github.com/test/repo2) | 200 |
"""
        parser = MarkdownTableParser(content)
        rows = parser.find_table_rows()

        assert len(rows) == 2
        assert rows[0]['full_name'] == 'test/repo1'
        assert rows[1]['full_name'] == 'test/repo2'

    def test_update_table_row_stars(self):
        """测试更新 Stars 列"""
        content = """| [Test](https://github.com/test/repo) | ⭐⭐ | 1,000 | 描述 |"""
        parser = MarkdownTableParser(content)

        repo_data = {
            'rating_display': '⭐⭐⭐⭐',
            'stars': 5678,
        }

        updated = parser.update_table_row(0, repo_data)

        assert '5,678' in updated
        assert '⭐⭐⭐⭐' in updated

    def test_update_table_row_rating(self):
        """测试更新星级"""
        content = """| [Test](https://github.com/test/repo) | | 1,000 | 描述 |"""
        parser = MarkdownTableParser(content)

        repo_data = {
            'rating_display': '⭐⭐⭐',
            'stars': 1000,
        }

        updated = parser.update_table_row(0, repo_data)

        assert '⭐⭐⭐' in updated

    def test_update_table_row_preserve_format(self):
        """测试保持 Markdown 格式"""
        content = """| [Test](https://github.com/test/repo) | ⭐⭐ | 1,234 | 这是一个描述 |"""
        parser = MarkdownTableParser(content)

        repo_data = {
            'rating_display': '⭐⭐⭐⭐⭐',
            'stars': 99999,
        }

        updated = parser.update_table_row(0, repo_data)

        # 验证 Markdown 结构保持不变
        assert '|' in updated
        assert 'https://github.com/test/repo' in updated
        assert '99,999' in updated

    def test_update_table_row_empty_stars(self):
        """测试处理空的 Stars 列"""
        content = """| [Test](https://github.com/test/repo) | | | 描述 |"""
        parser = MarkdownTableParser(content)

        repo_data = {
            'rating_display': '⭐',
            'stars': 50,
        }

        updated = parser.update_table_row(0, repo_data)

        assert '⭐' in updated


class TestGitHubRepoFetcher:
    """测试 GitHub 仓库批量获取器"""

    def test_init(self):
        """测试初始化"""
        api = Mock()
        fetcher = GitHubRepoFetcher(api, delay=2.0)

        assert fetcher.api == api
        assert fetcher.delay == 2.0

    @patch('time.sleep')
    @patch('get_github_stars.GitHubRating')
    def test_fetch_batch_success(self, mock_rating, mock_sleep):
        """测试批量获取成功"""
        # Mock API 响应
        mock_api = Mock()
        mock_api.get_repository_info.return_value = {
            'stargazers_count': 1000,
            'forks_count': 100,
            'subscribers_count': 50,
            'open_issues_count': 10,
            'description': 'Test',
            'html_url': 'https://github.com/test/repo',
            'full_name': 'test/repo',
        }

        # Mock 评分结果
        mock_rating.get_repository_data.return_value = {
            'rating': 3,
            'rating_display': '⭐⭐⭐',
            'stars': 1000,
        }

        fetcher = GitHubRepoFetcher(mock_api, delay=0.5)
        repos = [
            {'owner': 'test', 'repo': 'repo', 'full_name': 'test/repo'},
        ]

        results = fetcher.fetch_batch(repos)

        assert 'test/repo' in results
        assert results['test/repo'] is not None

    @patch('time.sleep')
    def test_fetch_batch_with_error(self, mock_sleep):
        """测试处理错误情况"""
        mock_api = Mock()
        mock_api.get_repository_info.side_effect = Exception("404 Not Found")

        fetcher = GitHubRepoFetcher(mock_api, delay=0.5)
        repos = [
            {'owner': 'test', 'repo': 'repo', 'full_name': 'test/repo'},
        ]

        results = fetcher.fetch_batch(repos)

        # 错误时应该返回 None
        assert 'test/repo' in results
        assert results['test/repo'] is None


class TestIntegration:
    """集成测试"""

    def test_parse_and_update_flow(self):
        """测试完整的解析和更新流程"""
        content = """# 测试文档

## 项目列表

| 项目 | 推荐 | Stars |
|-------|--------|-------|
| [Project A](https://github.com/user/project-a) | ⭐⭐ | 100 |
| [Project B](https://github.com/user/project-b) | | 200 |

其他内容。
"""

        # 解析
        parser = MarkdownTableParser(content)
        repos = parser.extract_github_repos()

        assert len(repos) == 2

        # 模拟 GitHub 数据
        mock_data = {
            'user/project-a': {
                'rating_display': '⭐⭐⭐⭐',
                'stars': 1234,
            },
            'user/project-b': {
                'rating_display': '⭐⭐⭐',
                'stars': 567,
            },
        }

        # 查找表格行
        rows = parser.find_table_rows()
        assert len(rows) == 2

        # 更新行
        updated_lines = parser.lines.copy()
        for row in rows:
            full_name = row['full_name']
            if full_name in mock_data:
                new_line = parser.update_table_row(row['line_num'], mock_data[full_name])
                updated_lines[row['line_num']] = new_line

        # 验证更新
        updated_content = '\n'.join(updated_lines)
        assert '1,234' in updated_content
        assert '567' in updated_content
        assert '⭐⭐⭐⭐' in updated_content
        assert '⭐⭐⭐' in updated_content

    def test_no_github_links(self):
        """测试没有 GitHub 链接的情况"""
        content = """# 普通文档

这是一份没有 GitHub 链接的文档。

- 项目 A
- 项目 B
"""
        parser = MarkdownTableParser(content)
        repos = parser.extract_github_repos()

        assert len(repos) == 0

    def test_preserve_non_github_links(self):
        """测试保留非 GitHub 链接"""
        content = """| 项目 | 链接 |
|-------|-------|
| [GitHub](https://github.com/test/repo) | stars |
| [GitLab](https://gitlab.com/test/repo) | forks |
"""
        parser = MarkdownTableParser(content)
        repos = parser.extract_github_repos()

        assert len(repos) == 1
        assert repos[0]['full_name'] == 'test/repo'
