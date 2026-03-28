# Brainstorm: 更新 plugin/README.md 的 GitHub 项目星级和 Star 数量

## 需求背景

plugin/README.md 中列出了大量 Claude Code、OpenCode 相关的插件和工具，以 Markdown 表格形式组织。当前存在以下问题：

1. 大部分项目的 "Star 数量" 列为空
2. "推荐星级" 列的值是静态的，没有基于实际 GitHub 数据动态更新
3. 需要自动化工具来获取 GitHub 仓库的实时数据并更新

## 目标

1. 增强 `script/get_github_stars.py` 的评分系统
2. 创建新脚本 `script/update_plugin_readme.py` 自动更新 plugin/README.md

## 现状分析

### 现有工具

**script/get_github_stars.py**
- 已有 GitHub API 客户端
- 当前评分算法：线性评分（Stars 每50星1分，Forks 每2个fork 1分等）
- 支持 `--json` 和 `--rating` 输出格式

**script/github_repo_rating.py**
- 阈值评分算法（更合理）
- 支持生成 Markdown 表格行
- 权重：Stars 40%, Forks 25%, Watchers 20%, Issues 15%

### README.md 表格格式

```markdown
| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [`superpowers`](https://github.com/obra/superpowers) | 一套完整的软件开发流程... | Claude Code<br>Cursor | ⭐⭐⭐⭐ |
```

## 实现方案

### 1. 更新 `script/get_github_stars.py`

**评分规则优化**（参考 `github_repo_rating.py` 的阈值算法）：

- Stars 权重：60%
  - 阈值：[0, 50, 200, 1000, 5000]
- Forks 权重：15%
  - 阈值：[0, 10, 50, 200, 1000]
- Watchers 权重：10%
  - 阈值：[0, 10, 30, 100, 300]
- Issues 权重：15%（活跃度指标）
  - 阈值：[0, 5, 20, 50, 100]

**API 增强**：
- 添加 `--export` 选项：输出 Python 可导入的数据格式
- 保持现有 `--json` 和 `--rating` 选项

### 2. 创建 `script/update_plugin_readme.py`

**功能**：
1. 读取 `plugin/README.md` 文件
2. 使用正则表达式提取所有 GitHub 链接（owner/repo）
3. 批量调用 GitHub API 获取每个仓库的信息
4. 解析现有表格行的结构（保留描述、支持列）
5. 更新每一行的：
   - 推荐星级（基于评分算法）
   - Star 数量
6. 写回 `plugin/README.md` 文件

**命令行选项**：
- `--token`：GitHub Personal Access Token（推荐）
- `--dry-run`：预览变更，不实际修改文件
- `--backup`：更新前创建备份文件

**实现细节**：
- 复用 `get_github_stars.py` 中的 `GitHubAPI` 和 `GitHubRating` 类
- 正则表达式：`\[`([^\]]+)\]\(https://github\.com/([^/]+)/([^)]+)\)`
- API 速率限制控制（使用 time.sleep）
- 错误处理：仓库不存在或无权限时保留原值并记录警告

## 验证步骤

1. 测试 `get_github_stars.py` 的新评分算法
   ```bash
   python script/get_github_stars.py obra/superpowers --json
   ```

2. 使用 dry-run 模式测试更新脚本
   ```bash
   python script/update_plugin_readme.py --dry-run
   ```

3. 确认无误后执行更新（带备份）
   ```bash
   python script/update_plugin_readme.py --backup
   ```

4. 检查 `plugin/README.md` 表格更新结果

## 关键文件

- `script/get_github_stars.py` - 现有 GitHub API 客户端（需更新）
- `script/github_repo_rating.py` - 另一个评分实现（参考算法）
- `script/update_plugin_readme.py` - 新建更新脚本
- `plugin/README.md` - 需要更新的 Markdown 文档
