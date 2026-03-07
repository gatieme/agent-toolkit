# Skills 目录说明
-------

本目录包含了为 AI Agents 安装的所有 Skills, 按功能分类整理.

## 目录结构
-------

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
-------

### 📊 图表与可视化
-------

#### excalidraw
-------

| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [`excalidraw-diagram-generator`](https://skills.sh/github/awesome-copilot/excalidraw-diagram-generator) | [`awesome-copilot/skills/excalidraw-diagram-generator`](https://github.com/github/awesome-copilot/tree/main/skills/excalidraw-diagram-generator) | 从自然语言描述生成 `Excalidraw` 图表，支持流程图、关系图、思维导图和系统架构图. | `npx skills add https://github.com/github/awesome-copilot --skill excalidraw-diagram-generator` |
| [`excalidraw-diagram`](https://skills.sh/axtonliu/axton-obsidian-visual-skills/excalidraw-diagram) | [`axtonliu/axton-obsidian-visual-skills`](https://github.com/axtonliu/axton-obsidian-visual-skills) | 从文本内容生成 Excalidraw 图表, 支持三种输出模式(Obsidian、Standard、Animated). | `npx skills add https://github.com/axtonliu/axton-obsidian-visual-skills --skill excalidraw-diagram` |
| [`excalidraw`](https://skills.sh/davila7/claude-code-templates/excalidraw) | [`davila7/claude-code-templates`](https://github.com/davila7/claude-code-templates) | `Excalidraw` 文件操作代理, 通过子代理委托防止上下文耗尽. | `npx skills add https://github.com/davila7/claude-code-templates --skill excalidraw` |
| [`excalidraw-diagram-skill/excalidraw-diagram`](https://skills.sh/coleam00/excalidraw-diagram-skill/excalidraw-diagram) | [`coleam00/excalidraw-diagram-skill`](https://github.com/coleam00/excalidraw-diagram-skill) | 一款面向 `Excalidraw` 绘图工具的专业制图能力包, 核心是生成能实现视觉论证的. `excalidraw` 格式 `json` 文件, 而非简单的信息展示型图表, 同时定义了一套标准化、高专业性的 `Excalidraw` 制图方法论、设计规范和工作流, 适配技术、产品、教学等多场景的专业绘图需求, 集成在 `kimi-cli、gemini-cli、GitHub Copilot` 等主流开发工具中. | `npx skills add https://github.com/coleam00/excalidraw-diagram-skill --skill excalidraw-diagram` |


#### draw-io
-------

| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [`drawio`](https://skills.sh/bahayonghang/drawio-skills/drawio) | [`bahayonghang/drawio-skills`](https://github.com/bahayonghang/drawio-skills) | AI 驱动的 Draw.io 图表生成, 支持设计系统、实时浏览器预览. | `npx skills add https://github.com/bahayonghang/drawio-skills --skill drawio` |

#### mermaid
-------


| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [`mermaid-diagrams`](https://skills.sh/softaworks/agent-toolkit/mermaid-diagrams) | [`softaworks/agent-toolkit`](https://github.com/softaworks/agent-toolkit) | 使用 Mermaidia 语法创建软件图表，支持类图、时序图、流程图、ER 图等 | `npx skills add https://github.com/softaworks/agent-toolkit --skill mermaid-diagrams` |
| [`pretty-mermaid`](https://skills.sh/imxv/pretty-mermaid-skills/pretty-mermaid) | [`imxv/pretty-mermaid-skills`](https://github.com/imxv/pretty-mermaid-skills) |对 beautiful-mermaid, 使用 beautiful-mermaid 库渲染 Mermaid 图表为 SVG 或 ASCII, 支持 15+ 主题. | `npx skills add https://github.com/imxv/pretty-mermaid-skills --skill pretty-mermaid` |
| [`beautiful-mermaid`](https://skills.sh/imxv/pretty-mermaid-skills/pretty-mermaid) | 借助 `beautiful-mermaid` SKILLS 来渲染 Mermaid 图表为 SVG 和 PNG. | `npx skills add https://github.com/imxv/pretty-mermaid-skills --skill pretty-mermaid` |
| [`smart-illustrator`](https://skills.sh/axtonliu/smart-illustrator/smart-illustrator) | [`axtonliu/smart-illustrator`](https://github.com/axtonliu/smart-illustrator) | 智能配图与 PPT 信息图生成器, 支持文章配图、PPT 批量生成、封面图. | `npx skills add https://github.com/axtonliu/smart-illustrator --skill smart-illustrator` |

### 🌐 浏览器自动化
-------


| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [`agent-browser`](https://skills.sh/vercel-labs/agent-browser/agent-browser) | [`vercel-labs/agent-browser`](https://github.com/vercel-labs/agent-browser) | 浏览器自动化 CLI, 用于 AI agents 与网站交互、导航、填写表单、截图、提取数据. | `npx skills add https://github.com/vercel-labs/agent-browser --skill agent-browser` |

### 🔧 代码与开发工具
-------


| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [`git-commit`](https://skills.sh/github/awesome-copilot/git-commit) | [`github/awesome-copilot`](https://github.com/github/awesome-copilot) | 使用约定式提交信息分析、智能暂存和消息生成执行 git commit. | `npx skills add https://github.com/github/awesome-copilot --skill git-commit` |
| [`repo2skill`](https://skills.sh/zhangyanxs/repo2skill/repo2skill) | [`zhangyanxs/repo2skill`](https://github.com/zhangyanxs/repo2skill) | 将 GitHub/GitLab/Gitee 仓库转换为综合的 OpenCode Skills，支持多镜像和速率限制处理 | `npx skills add https://github.com/zhangyanxs/repo2skill --skill repo2skill` |
| [`skill-creator`](https://skills.sh/anthropics/skills/skill-creator) | [`anthropics/skills`](https://github.com/anthropics/skills) | 创建有效 Skills 的指南, 用于扩展 Claude 的特定领域知识、工作流程或工具集成. | `npx skills add https://github.com/anthropics/skills --skill skill-creator` |
| [`simplify`](https://skills.sh/brianlovin/claude-config/simplify) | simplify 是一款代码专业简化与优化技能, 核心定位为「代码清晰度专家」, 专注于在完全保留代码原有功能的前提下, 按照项目标准化规范优化代码的结构、命名、格式, 提升代码的可读性、一致性和可维护性, 拒绝过度精简的「炫技式」代码, 适配开发全流程的代码优化、规范统一需求, 目前已在 opencode、GitHub Copilot、gemini-cli 等主流开发工具中落地. | `npx skills add https://github.com/brianlovin/claude-config --skill simplify` |


### ✍️ 文本处理
-------


| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [`humanizer-zh`](https://skills.sh/op7418/humanizer-zh/humanizer-zh) | [`op7418/humanizer-zh`](https://github.com/op7418/humanizer-zh) | 去除中文文本中的 AI 生成痕迹, 使文本听起来更自然、更像人类书写. | `npx skills add https://github.com/op7418/humanizer-zh --skill humanizer-zh` |
| [`humanizer`](https://skills.sh/softaworks/agent-toolkit/humanizer) | [`softaworks/agent-toolkit`](https://github.com/softaworks/agent-toolkit) | 去除文本中的 AI 生成痕迹, 使文本听起来更自然、更像人类书写. | `npx skills add https://github.com/softaworks/agent-toolkit --skill humanizer` |


### ⚙️ 配置管理
-------

| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| `oh-my-opencode-config` | [`includewudi/oh-my-opencode-config`](https://github.com/includewudi/oh-my-opencode-config) | Oh My OpenCode 插件的 agent 模型配置管理, 查看和修改 agent 模型配置. | `git clone https://github.com/includewudi/oh-my-opencode-config.git ~/.agents/skills/oh-my-opencode-config` |

### 🔍 技能发现与管理
-------

| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [`find-skills`](https://skills.sh/vercel-labs/skills/find-skills) | [`vercel-labs/skills`](https://github.com/vercel-labs/skills) | 帮助用户发现和安装 agent skills, 当用户询问如何做某事或查找技能时使用. | `npx skills add https://github.com/vercel-labs/skills --skill find-skills` |
| [`claudeception`](https://skills.sh/blader/claudeception/claudeception) | [`blader/claudeception`](https://github.com/blader/claudeception) | 持续学习系统, 从工作会话中提取可重用知识并创建新的 Claude Code Skills. | `npx skills add https://github.com/blader/claudeception --skill claudeception` |

### 科研相关
-------


#### 论文精读
-------

| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [`read-arxiv-paper`](https://skills.sh/karpathy/nanochat/read-arxiv-paper) | [`karpathy/nanochat`](https://github.com/karpathy/nanochat) | 从 ArXiv 论文 URL 到 nanochat 项目化总结的全自动化流程, 无需人工干预 TeX 源码下载、解包、解析, 最终输出贴合 nanochat 项目的论文应用参考, 解决了 AI 助手处理学术论文时「流程繁琐、与项目脱节」的问题. |`npx skills add https://github.com/karpathy/nanochat --skill read-arxiv-paper` |
| [`paper-craft-skills/paper-analyzer`](https://skills.sh/zsyggg/paper-craft-skills/paper-analyzer) | [`zsyggg/paper-craft-skills`](https://github.com/zsyggg/paper-craft-skills) | 学术论文深度解析自动化工具, 核心基于 MinerU Cloud API 实现高精度 PDF 论文解析, 能自动提取图片、表格、LaTeX 公式等核心元素, 并支持按多种风格生成结构化的解析文章, 还可按需结合公式详解、开源代码分析, 最终输出可直接使用的 Markdown/HTML 格式内容, 大幅降低学术论文阅读、解读和分享的门槛， 适配科研、学习、技术科普等多类场景. | `npx skills add https://github.com/zsyggg/paper-craft-skills --skill paper-analyzer` |
| [`ljg-skill-xray-paper/ljg-xray-paper`](https://skills.sh/lijigang/ljg-skill-xray-paper/ljg-xray-paper) | [`lijigang/ljg-skill-xray-paper`](https://github.com/lijigang/ljg-skill-xray-paper) | 论文解读. | `npx skills add https://github.com/lijigang/ljg-skill-xray-paper --skill ljg-xray-paper` |


## 安装 Skills
-------

### 方式一：使用 npx skills（推荐）
-------

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
