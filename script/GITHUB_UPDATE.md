# GitHub 评分工具使用指南

## 概述

本工具套件用于获取 GitHub 仓库的实时数据并自动更新文档中的评分和 Star 数量。

## 工具组成

### 1. get_github_stars.py - 单获取和评分工具

获取单个 GitHub 仓库的详细信息和评分。

### 2. update_plugin_readme.py - 批量更新工具

批量更新 Markdown 表格中的 GitHub 仓库信息。

## 使用方法

### get_github_stars.py

#### 基本用法

```bash
# 获取仓库信息和评分（美观输出）
python script/get_github_stars.py snarktank/ralph

# 使用 GitHub Token（推荐，提高速率限制）
python script/get_github_stars.py snarktank/ralph --token YOUR_TOKEN
```

#### 输出格式选项

```bash
# JSON 格式输出完整仓库信息
python script/get_github_stars.py snarktank/ralph --json

# 仅输出评分（用于脚本调用）
python script/get_github_stars.py snarktank/ralph --rating

# Python 可导入格式（用于其他脚本）
python script/get_github_stars.py snarktank/ralph --export
```

#### 环境变量

```bash
# 使用环境变量设置 Token（推荐方式）
export GITHUB_TOKEN=your_token_here
python script/get_github_stars.py snarktank/ralph
```

### update_plugin_readme.py

#### 基本用法

```bash
# 预览更新（不实际修改文件）
python script/update_plugin_readme.py --dry-run

# 执行更新并创建备份
python script/update_plugin_readme.py --backup

# 使用自定义 Token
python script/update_plugin_readme.py --token YOUR_TOKEN --backup
```

#### 命令行参数

| 参数 | 说明 |
|------|------|
| `--token TOKEN` | GitHub Personal Access Token（也可通过 GITHUB_TOKEN 环境变量设置） |
| `--dry-run` | 预览模式，显示将要进行的变更但不修改文件 |
| `--backup` | 创建备份文件后执行更新 |

## 评分规则

### 阈值评分系统

本工具使用阈值评分算法，根据仓库的多项指标计算综合评分：

#### 评分权重

| 指标 | 权重 | 阈值（1星-5星） |
|------|------|-------------------|
| Stars | 60% | ≤5K, ≤10K, ≤50K, ≤100K, >100K |
| Forks | 15% | ≤100, ≤200, ≤1K, ≤5K, >5K |
| Watchers | 10% | ≤100, ≤300, ≤1K, ≤5K, >5K |
| Issues | 15% | ≤100, ≤200, ≤500, ≤1K, >1K |

#### 评分等级

- ⭐⭐⭐⭐⭐ (5星): 综合得分 ≥ 4.5
- ⭐⭐⭐⭐ (4星): 综合得分 ≥ 3.5
- ⭐⭐⭐ (3星): 综合得分 ≥ 2.5
- ⭐⭐ (2星): 综合得分 ≥ 1.5
- ⭐ (1星): 综合得分 < 1.5

## 常见问题

### Q: 如何获取 GitHub Personal Access Token？

A:
1. 访问 https://github.com/settings/tokens
2. 点击 "Generate new token (classic)"
3. 选择需要的权限（最少需要 `public_repo`）
4. 生成并复制 Token
5. 设置环境变量或使用 `--token` 参数

### Q: 为什么要使用 GitHub Token？

A: 无 Token 时，GitHub API 的速率限制为每小时 60 次请求。使用 Token 后可提升到每小时 5000 次请求，对于批量更新大量仓库非常重要。

### Q: dry-run 模式会修改文件吗？

A: 不会。dry-run 模式只会显示将要进行的变更预览，不会实际修改任何文件。建议在执行实际更新前先运行 dry-run 检查结果。

### Q: 如何恢复到更新前的状态？

A: 如果使用了 `--backup` 参数，会生成 `plugin/README.md.backup` 备份文件：

```bash
# 恢复备份
cp plugin/README.md.backup plugin/README.md
```

### Q: 仓库不存在或无法访问时会发生什么？

A: 脚本会显示警告并保留原始表格内容，不会修改该行的数据。这确保即使部分仓库无法访问，其他正常仓库的数据仍能正确更新。

### Q: 支持哪些平台？

A: 当前支持 Claude Code、Cursor、Codex、OpenCode、Gemini CLI 等 AI 编码工具的文档更新。

## 示例工作流程

### 更新单个仓库评分

```bash
export GITHUB_TOKEN=your_token
python script/get_github_stars.py obra/superpowers
```

### 批量更新文档（推荐流程）

```bash
# 1. 预览更新
python script/update_plugin_readme.py --dry-run

# 2. 检查预览结果，确认无误后执行更新
python script/update_plugin_readme.py --backup

# 3. 验证更新结果
git diff plugin/README.md
```

### 自动化更新脚本

```bash
#!/bin/bash
# update_github_data.sh

export GITHUB_TOKEN="${GITHUB_TOKEN:-your_default_token}"

echo "预览更新..."
python script/update_plugin_readme.py --dry-run

read -p "确认执行更新？[y/N] " -n 1 -r
echo
if [[ $REPLY =~ ^[Yy]$ ]]; then
    python script/update_plugin_readme.py --backup
    echo "更新完成！"
fi
```

## 技术细节

### API 速率限制

- 无认证: 60 次/小时
- 有认证: 5000 次/小时

### Markdown 表格格式

工具期望的表格格式：

```markdown
| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [repo-name](https://github.com/owner/repo) | 描述文本 | 平台列表 | ⭐⭐⭐ | 123,456 |
```

## 故障排查

### 网络连接失败

检查网络连接和防火墙设置，确保可以访问 api.github.com。

### Token 无效

确认 Token 权限正确且未过期。尝试重新生成 Token。

### 速率限制错误

- 使用 GitHub Token 提升速率限制
- 或分批更新仓库，避免短时间内发送大量请求

### 编码问题

确保终端支持 UTF-8 编码，以正确显示星号（⭐）。

## 贡献

如有问题或建议，欢迎提交 Issue 或 Pull Request。
