# Skills 目录说明

本目录包含了为 AI Agents 安装的所有 Skills，按功能分类整理。

## 目录结构

```
skills/
├── 图表与可视化/
│   ├── excalidraw-diagram-generator/
│   ├── excalidraw-diagram/
│   ├── excalidraw/
│   ├── drawio/
│   ├── mermaid-diagrams/
│   ├── pretty-mermaid/
│   ├── beautiful-mermaid/
│   └── smart-illustrator/
├── 浏览器自动化/
│   └── agent-browser/
├── 代码与开发工具/
│   ├── git-commit/
│   ├── repo2skill/
│   └── skill-creator/
├── 文本处理/
│   └── humanizer-zh/
├── 配置管理/
│   └── oh-my-opencode-config/
└── 技能发现与管理/
    ├── find-skills/
    └── claudeception/
```

## 分类说明

### 📊 图表与可视化

| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|---------|--------------|-----------|---------|---------|
| [excalidraw-diagram-generator](https://skills.sh/DayuanJiang/next-ai-draw-io/excalidraw-diagram-generator) | [](https://github.com/DayuanJiang/next-ai-draw-io) | 从自然语言描述生成 Excalidraw 图表，支持流程图、关系图、思维导图和系统架构图 | `npx skills add DayuanJiang/next-ai-draw-io@excalidraw-diagram-generator` |
| **excalidraw-diagram** | - | 从文本内容生成 Excalidraw 图表，支持三种输出模式（Obsidian、Standard、Animated） | 手动安装到 `~/.claude/skills/` |
| **excalidraw** | - | Excalidraw 文件操作代理，通过子代理委托防止上下文耗尽 | 手动安装到 `~/.claude/skills/` |
| [drawio](https://skills.sh/DayuanJiang/next-ai-draw-io/drawio) | https://github.com/DayuanJiang/next-ai-draw-io | AI 驱动的 Draw.io 图表生成，支持设计系统、实时浏览器预览 | `npx skills add DayuanJiang/next-ai-draw-io@drawio` |
| **mermaid-diagrams** | - | - | 使用 Mermaidia 语法创建软件图表，支持类图、时序图、流程图、ER 图等 | 手动安装到 `~/.claude/skills/` |
| **pretty-mermaid** | https://skills.sh/imxv/Pretty-mermaid-skills/pretty-mermaid | https://github.com/imxv/Pretty-mermaid-skills | 使用 beautiful-mermaid 库渲染 Mermaid 图表为 SVG 或 ASCII，支持 15+ 主题 | `npx skills add imxv/Pretty-mermaid-skills@pretty-mermaid` |
| **beautiful-mermaid** | - | - | 使用 beautiful-mermaid 库渲染 Mermaid 图表为 SVG 和 PNG | 手动安装到 `~/.claude/skills/` |
| **smart-illustrator** | https://skills.sh/axtonliu/smart-illustrator/smart-illustrator | https://github.com/axtonliu/smart-illustrator | 智能配图与 PPT 信息图生成器，支持文章配图、PPT 批量生成、封面图 | `npx skills add axtonliu/smart-illustrator@smart-illustrator` |

### 🌐 浏览器自动化

| 技能名称 | skills.sh 地址 | GitHub 地址 | 简要描述 | 安装方式 |
|---------|--------------|-----------|---------|---------|
| **agent-browser** | - | - | 浏览器自动化 CLI，用于 AI agents 与网站交互、导航、填写表单、截图、提取数据 | 手动安装到 `~/.claude/skills/` |

### 🔧 代码与开发工具

| 技能名称 | skills.sh 地址 | GitHub 地址 | 简要描述 | 安装方式 |
|---------|--------------|-----------|---------|---------|
| **git-commit** | - | - | 使用约定式提交信息分析、智能暂存和消息生成执行 git commit | 手动安装到 `~/.claude/skills/` |
| **repo2skill** | - | - | 将 GitHub/GitLab/Gitee 仓库转换为综合的 OpenCode Skills，支持多镜像和速率限制处理 | 手动安装到 `~/.claude/skills/` |
| **skill-creator** | - | - | 创建有效 Skills 的指南，用于扩展 Claude 的特定领域知识、工作流程或工具集成 | 手动安装到 `~/.claude/skills/` |

### ✍️ 文本处理

| 技能名称 | skills.sh 地址 | GitHub 地址 | 简要描述 | 安装方式 |
|---------|--------------|-----------|---------|---------|
| **humanizer-zh** | https://skills.sh/op7418/Humanizer-zh/humanizer-zh | https://github.com/op7418/Humanizer-zh | 去除文本中的 AI 生成痕迹，使文本听起来更自然、更像人类书写 | `npx skills add op7418/Humanizer-zh@humanizer-zh` |

### ⚙️ 配置管理

| 技能名称 | skills.sh 地址 | GitHub 地址 | 简要描述 | 安装方式 |
|---------|--------------|-----------|---------|---------|
| **oh-my-opencode-config** | https://skills.sh/includewudi/oh-my-opencode-config/oh-my-opencode-config | https://github.com/includewudi/oh-my-opencode-config | Oh My OpenCode 插件的 agent 模型配置管理，查看和修改 agent 模型配置 | `npx skills add includewudi/oh-my-opencode-config@oh-my-opencode-config` |

### 🔍 技能发现与管理

| 技能名称 | skills.sh 地址 | GitHub 地址 | 简要描述 | 安装方式 |
|---------|--------------|-----------|---------|---------|
| **find-skills** | - | - | 帮助用户发现和安装 agent skills，当用户询问如何做某事或查找技能时使用 | 手动安装到 `~/.claude/skills/` |
| **claudeception** | https://skills.sh/blader/claudeception/claudeception | https://github.com/blader/claudeception | 持续学习系统，从工作会话中提取可重用知识并创建新的 Claude Code Skills | `npx skills add blader/claudeception@claudeception` |

### 论文

| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|----------|----------|----------|----------|
| [read-arxiv-paper](https://skills.sh/karpathy/nanochat/read-arxiv-paper) | [karpathy/nanochat](https://github.com/karpathy/nanochat) | 从 ArXiv 论文 URL 到 nanochat 项目化总结的全自动化流程, 无需人工干预 TeX 源码下载、解包、解析, 最终输出贴合 nanochat 项目的论文应用参考, 解决了 AI 助手处理学术论文时「流程繁琐、与项目脱节」的问题. |`npx skills add https://github.com/karpathy/nanochat --skill read-arxiv-paper` | 

## 安装 Skills

### 方式一：使用 npx skills（推荐）

```bash
# 安装公开的 skill
npx skills add <owner/repo>@skill

# 示例
npx skills add DayuanJiang/next-ai-draw-io@excalidraw-diagram-generator
npx skills add imxv/Pretty-mermaid-skills@pretty-mermaid
npx skills add axtonliu/smart-illustrator@smart-illustrator
npx skills add op7418/Humanizer-zh@humanizer-zh
npx skills add includewudi/oh-my-opencode-config@oh-my-opencode-config
npx skills add blader/claudeception@claudeception
```

### 方式二：使用 Git 克隆

```bash
# 克隆到 Claude Code 的 skills 目录
git clone <repository-url> ~/.claude/skills/<skill-name>

# 示例
git clone https://github.com/DayuanJiang/next-ai-draw-io.git ~/.claude/skills/excalidraw-diagram-generator
git clone https://github.com/imxv/Pretty-mermaid-skills.git ~/.claude/skills/pretty-mermaid
git clone https://github.com/axtonliu/smart-illustrator.git ~/.claude/skills/smart-illustrator
git clone https://github.com/op7418/Humanizer-zh.git ~/.claude/skills/humanizer-zh
git clone https://github.com/includewudi/oh-my-opencode-config.git ~/.claude/skills/oh-my-opencode-config
git clone https://github.com/blader/claudeception.git ~/.claude/skills/claudeception
```

### 方式三：手动复制

将 skill 目录复制到 Claude Code 的 skills 目录：

```bash
# macOS/Linux
cp -r skill-name ~/.claude/skills/

# Windows
xcopy skill-name %USERPROFILE%\.claude\skills\
```

## 使用 Skills

安装后，重启 Claude Code 或重新加载 skills。Skills 会根据以下条件自动触发：

1. **语义匹配** - 根据用户请求的上下文自动加载相关技能
2. **触发词** - 在 SKILL.md 的 description 中定义的关键词
3. **命令触发** - 使用 `/skill-name` 命令手动触发

## 技能开发

如果你想创建自己的 Skill，可以参考以下资源：

- **skill-creator** - 创建有效 Skills 的完整指南
- **claudeception** - 从工作会话中提取可重用知识的示例
- [Claude Code Skills 文档](https://docs.anthropic.com/en/docs/claude-code/skills)

## 贡献

欢迎提交 PR 添加新的 Skills 或改进现有 Skills。

## 许可

各 Skill 的许可请参考其各自的 LICENSE 文件。
