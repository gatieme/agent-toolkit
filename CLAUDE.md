# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## 项目概述

这是 agent-toolkit 仓库，包含 OpenCode 的配置文件和技能（skills）集合。主要集成 Superpowers 框架，提供完整的软件开发工作流。

## 目录结构

```
agent-toolkit/
├── opencode/              # OpenCode 配置文件目录
│   ├── oh-my-opencode-*.jsonc  # Oh-My-OpenCode 配置文件
│   ├── superpowers/        # Superpowers 集成（软链接）
│   └── skills/            # Superpowers 技能（软链接）
├── skills/                # 自定义技能仓库
│   ├── agent-browser/
│   ├── claudeception/
│   ├── git-commit/
│   ├── pptx/
│   └── ...
├── script/                # 实用脚本
│   └── sync.py           # 配置同步工具
└── plugin/                # 插件相关文档
```

## 常用命令

### 配置同步（推荐使用 Python 脚本）

```bash
# 更新模式：从仓库选择配置文件更新到安装目录
python script/sync.py update

# 备份模式：从安装目录选择配置文件备份回仓库
python script/sync.py backup
```

同步脚本依赖：
```bash
pip3 install prompt_toolkit --user
```

### 快速同步（使用 bash 脚本）

```bash
# 备份安装目录的配置到仓库（覆盖式）
./sync.sh
```

### 验证配置

```bash
# 验证 Oh-My-OpenCode 配置
bunx oh-my-opencode doctor

# 查看可用的技能
/skills
```

## 配置文件

### OpenCode 配置文件位置

| 仓库路径 | 安装路径 |
|---------|---------|
| `opencode/` | `~/.config/opencode` |
| `skills/` | `~/.agents/skills` |

### 主要配置文件

- `opencode/oh-my-opencode.jsonc` - 标准配置
- `opencode/oh-my-opencode-interactive.jsonc` - 交互式配置
- `opencode/oh-my-opencode-ultraworker.jsonc` - Ultraworker 配置
- `opencode/oh-my-opencode-native.jsonc` - 原生配置

## Superpowers 工作流

Superpowers 是一个完整的软件开发工作流框架，包含以下核心技能：

### 新功能开发流程

1. **brainstorming** - 探索用户意图、需求和设计
2. **writing-plans** - 编写详细的实现计划
3. **subagent-driven-development** - 通过子智能体协作实现
4. **test-driven-development** - TDD 开发，先写测试
5. **verification-before-completion** - 完成前验证
6. **requesting-code-review** - 请求代码审查

### Bug 修复流程

1. **systematic-debugging** - 找到根本原因
2. **test-driven-development** - 编写失败测试，修复
3. **verification-before-completion** - 验证修复
4. **requesting-code-review** - 代码审查

## Agents 配置

| Agent | 描述 | 主要技能 |
|-------|------|---------|
| sisyphus | 主协调器 | brainstorming, dispatching-parallel-agents, verification |
| hephaestus | 代码构建专家 | subagent-driven-development, executing-plans, tdd |
| oracle | 架构设计专家 | systematic-debugging |
| prometheus | 任务规划专家 | writing-plans |
| momus | 代码审查专家 | systematic-debugging, tdd |

## Categories 配置

| Category | 描述 | 工作流 |
|----------|------|--------|
| visual-engineering | 前端、UI/UX | 完整 Superpowers |
| ultrabrain | 逻辑密集型复杂任务 | 完整 Superpowers |
| deep | 目标导向的自主问题解决 | 完整 Superpowers + TDD |
| artistry | 非常规创造性任务 | Brainstorming |
| quick | 简单快速任务 | 直接开发 |
| writing | 文档、写作 | 直接开发 |

## 技能开发

Superpowers 技能位于 `opencode/superpowers/skills/` 目录，每个技能包含：

- `SKILL.md` - 技能定义文件（YAML 前置元数据 + Markdown 内容）
- 可选参考文档和示例

创建新技能时参考 `writing-skills` 技能的最佳实践。

## Git 提交规范

使用 `git-commit` 技能确保提交信息符合 Conventional Commits 规范：

```bash
# 技能会自动分析 diff 并生成标准化的提交信息
# 或者使用交互模式指定类型/范围/描述
```

Conventional Commit 格式：
```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

类型包括：feat, fix, docs, style, refactor, perf, test, build, ci, chore, revert

## 重要原则

1. **配置同步**：修改配置文件后，使用 `sync.py` 脚本进行双向同步
2. **配置验证**：重大配置变更后运行 `bunx oh-my-opencode doctor` 验证
3. **备份习惯**：在更新配置前，先使用备份模式保存当前配置
4. **技能自动加载**：Superpowers 技能通过配置文件自动加载，无需手动调用

## 相关文档

- `opencode/WORKFLOW_CONFIG.md` - 详细工作流配置说明
- `opencode/AGENTS.md` - AI 行为准则和开发规范
- `opencode/superpowers/README.md` - Superpowers 官方文档
- `script/README.md` - 同步脚本详细文档
