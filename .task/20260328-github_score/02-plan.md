# 实现计划：更新 plugin/README.md 的 GitHub 项目星级和 Star 数量

## Context

plugin/README.md 中列出了大量 Claude Code、OpenCode 相关的插件和工具。当前存在的问题是：

1. 大部分项目的 "Star 数量" 列为空
2. "推荐星级" 列是静态值，没有基于实际 GitHub 数据动态更新
3. 需要自动化工具来获取 GitHub 仓库的实时数据并更新

本计划的目的是创建一套完整的自动化工具，实现：
- 改进的评分算法（基于阈值而非线性评分）
- 自动更新 Markdown 表格的脚本
- 完整的测试覆盖

## 关键文件

- `script/get_github_stars.py` - 现有 GitHub API 客户端（需更新评分算法）
- `script/github_repo_rating.py` - 阈值评分算法（参考）
- `script/update_plugin_readme.py` - 新建更新脚本
- `plugin/README.md` - 需要更新的 Markdown 文档

## 实现计划

### 阶段 1：更新评分算法（使用 subAgent 并行工作）

#### 任务 1.1：更新 get_github_stars.py 的评分算法

**评分规则**（参考 github_repo_rating.py 的阈值算法）：

| 指标 | 权重 | 阈值 |
|------|------|------|
| Stars | 60% | [0, 5000, 10000, 50000, 100000] |
| Forks | 15% | [0, 100, 200, 200, 1000, 5000] |
| Watchers | 10% | [0, 100, 300, 1000, 5000] |
| Issues | 15% | [0, 100, 200, 500, 1000] |

**实现要点**：
1. 添加 `_score_component()` 方法实现阈值评分
2. 修改 `calculate_score()` 方法使用阈值算法
3. 添加 `--export` 选项输出 Python 可导入的数据格式
4. 保持现有 `--json` 和 `--rating` 选项兼容

**文件修改**：`script/get_github_stars.py`

#### 任务 1.2：创建单元测试

为评分算法创建完整的单元测试：

**测试用例**：
1. 阈值边界测试（0, 5000, 10000, 50000, 100000 stars）
2. 综合评分测试（模拟不同仓库数据）
3. JSON 输出格式验证
4. Rating 输出格式验证

**新建文件**：`script/test_github_stars.py`

### 阶段 2：创建更新脚本（使用 subAgent）

#### 任务 2.1：创建 update_plugin_readme.py

**功能模块**：
1. **Markdown 解析器**
   - 提取所有 GitHub 链接（使用正则）
   - 识别表格行结构
   - 保留描述、支持列

2. **GitHub API 客户端**
   - 复用 `get_github_stars.py` 的 GitHubAPI 类
   - 批量获取仓库信息
   - 速率限制控制

3. **表格更新器**
   - 计算新评分
   - 更新 "推荐星级" 列
   - 更新 "Star 数量" 列
   - 保持格式一致性

4. **文件操作**
   - 备份原文件
   - 原子性写入
   - 生成变更报告

**命令行选项**：
- `--token`：GitHub Personal Access Token
- `--dry-run`：预览变更，不修改文件
- `--backup`：更新前创建备份

**新建文件**：`script/update_plugin_readme.py`

#### 任务 2.2：创建集成测试

**测试场景**：
1. 读取测试 Markdown 文件
2. 提取 GitHub 仓库列表
3. Mock GitHub API 响应
4. 验证表格更新逻辑
5. 验证 dry-run 模式
6. 验证备份功能

**新建文件**：`script/test_update_plugin_readme.py`

### 阶段 3：执行与验证（使用 Agent Team 并行工作）

#### 任务 3.1：并行测试脚本

启动 2 个 subAgent 并行运行：

1. **Agent 1 - 单元测试**
   - 运行 `python script/test_github_stars.py`
   - 验证评分算法正确性
   - 确保测试覆盖率 > 80%

2. **Agent 2 - 集成测试**
   - 运行 `python script/test_update_plugin_readme.py`
   - 验证 Markdown 解析和更新逻辑
   - 确保测试覆盖率 > 80%

#### 任务 3.2：预览更新

运行 dry-run 模式预览变更：
```bash
python script/update_plugin_readme.py --dry-run
```

#### 任务 3.3：执行更新（用户确认后）

```bash
python script/update_plugin_readme.py --backup
```

#### 任务 3.4：验证结果

1. 检查 `plugin/README.md` 表格更新
2. 验证所有 GitHub 仓库都有星级和 Star 数量
3. 确认评分分布合理

### 阶段 4：文档更新

#### 任务 4.1：更新脚本文档

更新 `script/get_github_stars.py` 的帮助信息：
- 添加新评分规则说明
- 添加 `--export` 选项文档

#### 任务 4.2：创建使用指南

新建 `script/GITHUB_UPDATE.md` 包含：
- 功能概述
- 使用方法
- 示例命令
- 常见问题

## 验证计划

### 测试命令

```bash
# 单元测试
pytest script/test_github_stars.py -v --cov=script/get_github_stars

# 集成测试
pytest script/test_update_plugin_readme.py -v --cov=script/update_plugin_readme

# Dry-run 预览
python script/update_plugin_readme.py --dry-run

# 实际更新（带备份）
python script/update_plugin_readme.py --backup --token $GITHUB_TOKEN
```

### 验收标准

1. ✅ 所有测试通过，覆盖率 > 80%
2. ✅ Dry-run 模式正确预览变更
3. ✅ 更新后所有项目都有星级和 Star 数量
4. ✅ 评分分布合理（3星及以上占多数）
5. ✅ Markdown 格式保持一致
6. ✅ 备份文件正确生成

## 风险与应对

| 风险 | 应对措施 |
|------|----------|
| GitHub API 速率限制 | 使用 Token（提高限额），添加请求间隔 |
| 仓库不存在/无权限 | 保留原值，记录警告 |
| Markdown 格式复杂 | 使用正则 + 手动验证，先小范围测试 |
| 大量仓库更新耗时 | 添加进度显示，支持断点续传 |

## 执行顺序

1. 阶段 1（更新评分算法）→ 阶段 2（创建更新脚本）→ 阶段 3（测试与执行）
2. 阶段 3.1 使用 Agent Team 并行运行测试
3. 阶段 3.2-3.4 顺序执行（需要用户确认）
