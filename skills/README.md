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


# Skills 清单
-------

## 📊 图表与可视化
-------

### excalidraw
-------

| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [`excalidraw-diagram-generator`](https://skills.sh/github/awesome-copilot/excalidraw-diagram-generator) | [`awesome-copilot/skills/excalidraw-diagram-generator`](https://github.com/github/awesome-copilot/tree/main/skills/excalidraw-diagram-generator) | 从自然语言描述生成 `Excalidraw` 图表, 支持流程图、关系图、思维导图和系统架构图. | `npx skills add https://github.com/github/awesome-copilot --skill excalidraw-diagram-generator` |
| [`excalidraw-diagram`](https://skills.sh/axtonliu/axton-obsidian-visual-skills/excalidraw-diagram) | [`axtonliu/axton-obsidian-visual-skills`](https://github.com/axtonliu/axton-obsidian-visual-skills) | 从文本内容生成 Excalidraw 图表, 支持三种输出模式(Obsidian、Standard、Animated). | `npx skills add https://github.com/axtonliu/axton-obsidian-visual-skills --skill excalidraw-diagram` |
| [`excalidraw`](https://skills.sh/davila7/claude-code-templates/excalidraw) | [`davila7/claude-code-templates`](https://github.com/davila7/claude-code-templates) | `Excalidraw` 文件操作代理, 通过子代理委托防止上下文耗尽. | `npx skills add https://github.com/davila7/claude-code-templates --skill excalidraw` |
| [`excalidraw-diagram-skill/excalidraw-diagram`](https://skills.sh/coleam00/excalidraw-diagram-skill/excalidraw-diagram) | [`coleam00/excalidraw-diagram-skill`](https://github.com/coleam00/excalidraw-diagram-skill) | 一款面向 `Excalidraw` 绘图工具的专业制图能力包, 核心是生成能实现视觉论证的. `excalidraw` 格式 `json` 文件, 而非简单的信息展示型图表, 同时定义了一套标准化、高专业性的 `Excalidraw` 制图方法论、设计规范和工作流, 适配技术、产品、教学等多场景的专业绘图需求, 集成在 `kimi-cli、gemini-cli、GitHub Copilot` 等主流开发工具中. | `npx skills add https://github.com/coleam00/excalidraw-diagram-skill --skill excalidraw-diagram` |


### draw-io
-------

| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [`drawio`](https://skills.sh/bahayonghang/drawio-skills/drawio) | [`bahayonghang/drawio-skills`](https://github.com/bahayonghang/drawio-skills) | AI 驱动的 Draw.io 图表生成, 支持设计系统、实时浏览器预览. | `npx skills add https://github.com/bahayonghang/drawio-skills --skill drawio` |

### mermaid
-------


| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [`mermaid-diagrams`](https://skills.sh/softaworks/agent-toolkit/mermaid-diagrams) | [`softaworks/agent-toolkit`](https://github.com/softaworks/agent-toolkit) | 使用 Mermaidia 语法创建软件图表, 支持类图、时序图、流程图、ER 图等 | `npx skills add https://github.com/softaworks/agent-toolkit --skill mermaid-diagrams` |
| [`pretty-mermaid`](https://skills.sh/imxv/pretty-mermaid-skills/pretty-mermaid) | [`imxv/pretty-mermaid-skills`](https://github.com/imxv/pretty-mermaid-skills) |对 beautiful-mermaid 进一步封装, 使用 beautiful-mermaid 库渲染 Mermaid 图表为 SVG 或 ASCII, 支持 15+ 主题. | `npx skills add https://github.com/imxv/pretty-mermaid-skills --skill pretty-mermaid` |
| [`beautiful-mermaid`]https://skills.sh/intellectronica/agent-skills/beautiful-mermaid) | [`intellectronica/agent-skills`](https://github.com/intellectronica/agent-skills) | 借助 `beautiful-mermaid` SKILLS 来渲染 Mermaid 图表为 SVG 和 PNG. | `npx skills add https://github.com/intellectronica/agent-skills --skill beautiful-mermaid` |
| [`smart-illustrator`](https://skills.sh/axtonliu/smart-illustrator/smart-illustrator) | [`axtonliu/smart-illustrator`](https://github.com/axtonliu/smart-illustrator) | 智能配图与 PPT 信息图生成器, 支持文章配图、PPT 批量生成、封面图. | `npx skills add https://github.com/axtonliu/smart-illustrator --skill smart-illustrator` |

## 🌐 浏览器自动化
-------


| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [`agent-browser`](https://skills.sh/vercel-labs/agent-browser/agent-browser) | [`vercel-labs/agent-browser`](https://github.com/vercel-labs/agent-browser) | 浏览器自动化 CLI, 用于 AI agents 与网站交互、导航、填写表单、截图、提取数据. | `npx skills add https://github.com/vercel-labs/agent-browser --skill agent-browser` |

## 🔧 代码与开发工具
-------

### 代码提交
-------


| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [`git-commit`](https://skills.sh/github/awesome-copilot/git-commit) | [`github/awesome-copilot`](https://github.com/github/awesome-copilot) | 使用约定式提交信息分析、智能暂存和消息生成执行 git commit. | `npx skills add https://github.com/github/awesome-copilot --skill git-commit` |
| [`repo2skill`](https://skills.sh/zhangyanxs/repo2skill/repo2skill) | [`zhangyanxs/repo2skill`](https://github.com/zhangyanxs/repo2skill) | 将 GitHub/GitLab/Gitee 仓库转换为综合的 OpenCode Skills, 支持多镜像和速率限制处理 | `npx skills add https://github.com/zhangyanxs/repo2skill --skill repo2skill` |

### 代码检视
-------

[Mieluoxxx/code-review](https://github.com/Mieluoxxx/opcd/tree/opencode/.opencode/skill/code-review)
[sanyuan0704/sanyuan-skills](https://github.com/sanyuan0704/sanyuan-skills/tree/main/skills/code-review-expert)
https://github.com/win4r/agent-skills-code-review-router

### 代码重构
-------


| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [`simplify`](https://skills.sh/brianlovin/claude-config/simplify) | simplify 是一款代码专业简化与优化技能, 核心定位为「代码清晰度专家」, 专注于在完全保留代码原有功能的前提下, 按照项目标准化规范优化代码的结构、命名、格式, 提升代码的可读性、一致性和可维护性, 拒绝过度精简的「炫技式」代码, 适配开发全流程的代码优化、规范统一需求, 目前已在 opencode、GitHub Copilot、gemini-cli 等主流开发工具中落地. | `npx skills add https://github.com/brianlovin/claude-config --skill simplify` |



## ✍️ 办公
-------


### 文本写作
-------


| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [`humanizer-zh`](https://skills.sh/op7418/humanizer-zh/humanizer-zh) | [`op7418/humanizer-zh`](https://github.com/op7418/humanizer-zh) | 去除中文文本中的 AI 生成痕迹, 使文本听起来更自然、更像人类书写. | `npx skills add https://github.com/op7418/humanizer-zh --skill humanizer-zh` |
| [`humanizer`](https://skills.sh/softaworks/agent-toolkit/humanizer) | [`softaworks/agent-toolkit`](https://github.com/softaworks/agent-toolkit) | 去除文本中的 AI 生成痕迹, 使文本听起来更自然、更像人类书写. | `npx skills add https://github.com/softaworks/agent-toolkit --skill humanizer` |
| [stop-slop](https://skills.sh/hardikpandya/stop-slop/stop-slop) | [`hardikpandya/stop-slop`](https://github.com/hardikpandya/stop-slop) | 系统性消除 AI 写作中刻板、模板化的表达模式(被称为 Slop), 让 AI 生成的文本摆脱机器感, 更贴近人类自然、真实的写作风格, 同时也能指导人类作者规避同类写作陋习, 提升文本质量. | `npx skills add https://github.com/hardikpandya/stop-slop --skill stop-slop` |

### PPT/Office
-------

| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [`pptx`](https://skills.sh/anthropics/skills/pptx) | Anthropic 旗下 Claude Skills 体系的 PPTX 处理技能, 借助 [python markitdown 库](https://pypi.org/project/markitdown) 封装了 PPTX 读取、编辑、从零创建的脚本指令, 同时提供专业的 PPT 设计规范和严格的内容/视觉质检流程, 让大模型可标准化制作、处理 PPTX 文件. | `npx skills add https://github.com/anthropics/skills --skill pptx` |
| [`ppt-generation`](https://skills.sh/bytedance/deer-flow/ppt-generation) | [`bytedance/deer-flow`](https://github.com/bytedance/deer-flow) | 字节跳动 deer-flow 生态下的自动化 PPT 生成技能, 支持自然语言/结构化数据输入, 内置字节设计规范, 一键生成可编辑的 PPTX 格式文件, 适配汇报、技术分享、产品宣讲等多场景. | `npx skills add https://github.com/bytedance/deer-flow --skill ppt-generation` |
| [baoyu-slide-deck](https://skills.sh/jimliu/baoyu-skills/baoyu-slide-deck) | [宝玉大佬](https://github.com/JimLiu/baoyu-skills) 的专业的幻灯片生成 Skills, 可将文本内容转化为带视觉设计的幻灯片图片并合并为 PPTX/PDF, 内置 16 种风格预设、支持自定义风格维度和多语言, 提供标准化生成流程和完善的幻灯片修改能力. | `npx skills add https://github.com/jimliu/baoyu-skills --skill baoyu-slide-deck` |


## ⚙️ 配置管理
-------

| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| `oh-my-opencode-config` | [`includewudi/oh-my-opencode-config`](https://github.com/includewudi/oh-my-opencode-config) | Oh My OpenCode 插件的 agent 模型配置管理, 查看和修改 agent 模型配置. | `git clone https://github.com/includewudi/oh-my-opencode-config.git ~/.agents/skills/oh-my-opencode-config` |



## 🔍 技能发现与管理
-------


### Skills 查找
-------

| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [`find-skills`](https://skills.sh/vercel-labs/skills/find-skills) | [`vercel-labs/skills`](https://github.com/vercel-labs/skills) | 帮助用户发现和安装 agent skills, 当用户询问如何做某事或查找技能时使用. | `npx skills add https://github.com/vercel-labs/skills --skill find-skills` |

### Skills 创建
-------

| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [`skill-creator`](https://skills.sh/anthropics/skills/skill-creator) | [`anthropics/skills`](https://github.com/anthropics/skills) | 创建有效 Skills 的指南, 用于扩展 Claude 的特定领域知识、工作流程或工具集成. | `npx skills add https://github.com/anthropics/skills --skill skill-creator` |
| [`claudeception`](https://skills.sh/blader/claudeception/claudeception) | [`blader/claudeception`](https://github.com/blader/claudeception) | 持续学习系统, 从工作会话中提取可重用知识并创建新的 Claude Code Skills. | `npx skills add https://github.com/blader/claudeception --skill claudeception` |
| [`hao-cyber/skill-evolution`](https://github.com/hao-cyber/skill-evolution) |
| [`skill-evolution-manager`](https://github.com/KKKKhazix/Khazix-Skills/tree/main/skill-evolution-manager) |

### Skills 路由
-------

| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [skill-router](https://skills.sh/charon-fan/agent-playbook/skill-router) | [charon-fan/agent-playbook](https://github.com/charon-fan/agent-playbook) | 通用 AI 技能智能路由器, 一站式解决「不知道该用哪个技能完成任务」的核心痛点. 是所有 AI 开发工具的基础通用型技能(安装量最高, 普适性最强). | NA | `npx skills add https://github.com/charon-fan/agent-playbook --skill skill-router` |
| [recur-help](https://skills.sh/recur-tw/skills/recur-help) | [recur-tw/skills](https://github.com/recur-tw/skills) | Recur 整合入门, Recur 的专属技能导航,  聚焦 Recur 支付/订阅系统的整合开发, 是垂直技术工具的专属使用指南技能. 核心使用场景. 开发者需要在项目中接入 Recur 金流系统, 不清楚从哪开始, 通过该技能快速获取从 SDK 安装到基础配置」的一站式指引. | `npx skills add https://github.com/recur-tw/skills --skill recur-help` |
| [skill-marketplace](https://skills.sh/cityfish91159/maihouses/skill-marketplace) | [cityfish91159/maihouses](https://github.com/cityfish91159/maihouses) | AI 技能市集智能挖掘与集成工具, 突破本地技能库限制, 从 38000+ 外部技能市集中自动找、装、用适配技能, 是本地技能库的延伸补充型技能. | `npx skills add https://github.com/cityfish91159/maihouses --skill skill-marketplace` |
| skill-ten-prompt-generator | [liangdabiao/skill-ten-prompt-generator](https://github.com/liangdabiao/skill-ten-prompt-generator) | 基于 Claude Code Agent Skills 的 AI 提示词工程系统 - 10个场景化专家, 自动路由, 精准生成优秀提示词. 通过自然语言请求, 系统会自动路由到对应的专业 Skill, 帮助用户写出高质量的 AI 提示词. |


### Skills 安全检查
-------


| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [huifer/skill-security-scan](https://github.com/huifer/skill-security-scan) |

## 科研相关
-------


### 论文精读
-------

| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [`read-arxiv-paper`](https://skills.sh/karpathy/nanochat/read-arxiv-paper) | [`karpathy/nanochat`](https://github.com/karpathy/nanochat) | 从 ArXiv 论文 URL 到 nanochat 项目化总结的全自动化流程, 无需人工干预 TeX 源码下载、解包、解析, 最终输出贴合 nanochat 项目的论文应用参考, 解决了 AI 助手处理学术论文时「流程繁琐、与项目脱节」的问题. |`npx skills add https://github.com/karpathy/nanochat --skill read-arxiv-paper` |
| [`paper-craft-skills/paper-analyzer`](https://skills.sh/zsyggg/paper-craft-skills/paper-analyzer) | [`zsyggg/paper-craft-skills`](https://github.com/zsyggg/paper-craft-skills) | 学术论文深度解析自动化工具, 核心基于 MinerU Cloud API 实现高精度 PDF 论文解析, 能自动提取图片、表格、LaTeX 公式等核心元素, 并支持按多种风格生成结构化的解析文章, 还可按需结合公式详解、开源代码分析, 最终输出可直接使用的 Markdown/HTML 格式内容, 大幅降低学术论文阅读、解读和分享的门槛,  适配科研、学习、技术科普等多类场景. | `npx skills add https://github.com/zsyggg/paper-craft-skills --skill paper-analyzer` |
| [`ljg-skill-xray-paper/ljg-xray-paper`](https://skills.sh/lijigang/ljg-skill-xray-paper/ljg-xray-paper) | [`lijigang/ljg-skill-xray-paper`](https://github.com/lijigang/ljg-skill-xray-paper) | 论文解读. | `npx skills add https://github.com/lijigang/ljg-skill-xray-paper --skill ljg-xray-paper` |


## PUA
-------


| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [`pua-debugging`](https://skills.sh/tanweai/pua/pua-debugging) | [`tanweai/pua/pua-debugging`](https://github.com/tanweai/pua/tree/main/skills/pua-debugging) | 以大厂 P8 级工程师要求为核心, 融合大厂 PUA 激励话术、标准化调试方法论和强制化主动执行规则, 倒逼 AI 以工程化 Owner 视角端到端解决调试问题, 彻底规避被动排查、浅尝辄止的问题, 同时配套压力升级、抗合理化、自检清单等机制保障调试效果. 由[探微安全实验室](https://github.com/tanweai)出品. 官网 [pua-skills](https://pua-skill.pages.dev). @passluo 受此启发, [给你的 AI 一套大厂 P8 的 Soul, 让它的 Coding 表现提高 30%](https://x.com/passluo/status/2030908109145903310) | `npx skills add https://github.com/tanweai/pua --skill pua-debugging` |


## 交互
-------

| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [op7418/Claude-to-IM-skill](https://github.com/op7418/Claude-to-IM-skill) | | | `npx skills add https://github.com/op7418/claude-to-im-skill --skill claude-to-im` |

## 金融
-------


https://github.com/SunX-DEX/sunx-skills-hub
marketing-skills
https://github.com/hyperbrowserai/hyperbrowser-app-examples/tree/main/hyperskills

## 安全
-------


| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [Skill Analyzer](https://glitchward.com/skill-analyzer) | NA | 用于分析 GitHub 仓库的技能, 可获取仓库信息、问题统计和提交历史 | 需配置 GitHub API Token, 通过 SKILL.md 定义使用方法 |
| [Skill Security Scan](https://github.com/huifer/skill-security-scan) | [huifer/skill-security-scan](https://github.com/huifer/skill-security-scan) | 扫描和检测 Claude Skills 的安全风险, 防止恶意代码窃取数据或破坏系统 | `pip install skill-security-scan` 或 `pip install -e .` |
| [Context Hub](https://github.com/andrewyng/context-hub) | https://github.com/andrewyng/context-hub | 为编码代理提供经过整理的、版本化的文档, 使其能够在每个任务中变得更智能 | `npm install -g @aisuite/chub` |



# Skills 集合
-------


## Skills 市场
-------


| 市场 | 描述 |
|:---:|:----:|
| [skill.sh](https://skills.sh) | 由 Vercel 推出的开源 AI 智能体开放技能生态系统, 被称作「AI 智能体界的 npm」, 核心定位是为各类 AI Agent(智能体)提供可复用、标准化的技能能力库, 通过分离智能体的「推理」与「执行」环节, 解决 AI 智能体执行任务时不可靠、能力分散的痛点, 让开发者和使用者能通过简单命令为 AI 智能体快速扩展专业能力, 推动 AI 智能体从通用对话工具向专业执行伙伴升级. |
| [SkillsMP](https://skillsmp.com) | 全球最大的 AI Agent 技能聚合与分发平台(Agent Skills Marketplace), 定位为 AI 编码助手的「应用商店」, 是独立于 Anthropic、OpenAI 的社区型开源项目. 该平台爬取并聚合 GitHub 上符合 SKILL.md 开放标准的 Agent 技能资源, 通过智能搜索、精细化分类、质量筛选, 解决了 AI 技能资源分散、查找困难、使用繁琐的痛点, 为 Claude Code、OpenAI Codex CLI、ChatGPT 等主流 AI 编码助手提供一站式的技能发现、获取与使用服务, 覆盖开发、AI、商业、运维等全场景需求. |
| [SkillStore](https://skillstore.io/zh-hans) | 面向中文用户的 AI Agent 技能商店, 主打安全审计、质量验证、一键安装, 是适配 Claude、Codex、Claude Code 等主流 AI 编码助手的技能分发平台. 该平台区别于其他技能聚合站的核心特点是人工审核 + 中文友好, 所有技能均经过安全检测和质量验证, 同时提供全中文化的使用体验, 适配团队协作、企业合规等对技能安全性和稳定性要求较高的场景, 也适合中文开发者/普通用户快速获取可直接使用的 AI 模块化能力. |
| [agent-skills.md](https://agent-skills.md) | agent-skills.md 是一款轻量型 AI Agent 技能市集, 核心定位为 AI 智能体模块化能力的发现与检索平台, 所有技能均遵循 SKILL.md 开放标准, 适配 Claude、OpenClaw、Codex 等主流 AI 智能体/编码助手, 主打技能场景化标注、快速检索、轻量化使用, 聚焦开发调试、终端工具调用、办公自动化、本地软硬件控制等实操性场景, 是偏向开发者和技术型用户的 AI 技能实用工具库. |
| [SkillsDirectory](https://skillsdirectory.com) | Reddit 社区推荐的 SKILLs 集合, 由社区驱动的大型 AI Agent 技能目录平台, 核心定位为一站式的技能发现、安装与交流平台, 覆盖编码、研究、写作等全场景, 主打 Reddit 社区真实推荐、用户验证、终端一键安装, 区别于其他平台的算法推荐或官方审核, 该平台的技能价值由真实用户使用体验背书, 更贴合实际使用需求. |
| [agentskills](https://agentskills.me) | 开源 AI 智能体技能平台, 核心定位是为 Claude Code、Cursor、OpenCode、Codex CLI、Gemini CLI 等主流 AI 开发工具提供精选技能库, 帮助 AI 智能体快速掌握特定任务能力, 覆盖开发、设计、营销、办公等多场景需求. |
| [AgentSkillsHub](https://agentskillshub.top) | [@zhuyansen](https://github.com/zhuyansen) 搭建的 [AgentSkillsHub](https://github.com/ZhuYansen/agent-skills-hub). 设计了一套评价指标, 参考了 skillsbench, github 活跃度等对 skills 进行总和评价. |
| [SkillsFast](https://skills.fast/zh) | 面向中文用户的 AI Agent 技能快速分发与社区协作平台, 核心定位为 "AI 技能的高效流通枢纽" —— 以 "秒速发现、一键集成、社区共建" 为核心优势, 聚焦数据分析、内容创作、自动化等高频场景, 为 AI 开发者、爱好者及办公人群提供高质量 Agent 技能的查找、分享与复用服务, 完美适配 Claude Code、Cursor、Gemini CLI 等主流 AI 工具, 是连接技能创作者与使用者的轻量化桥梁. |
| [skills.homes](https://skills.homes/zh-CN) | 多语言 AI Agent 技能平台, 提供生产力工具、LLM & AI、自动化工具、调试、架构和测试等分类, 拥有大量技能资源. |


## Skills 集合仓库
-------

| 仓库 | 描述 |
|:---:|:----:|
| [anthropics/skills](https://github.com/anthropics/skills) | Anthropic 官方推出的 AI Agent 技能核心仓库, 是 SKILL.md 开放标准的源头, 收录了 PPTX 处理、代码调试、文档解析等标准化技能模板, 所有技能均经过官方验证, 适配 Claude 系列 AI 工具, 是构建合规、稳定 AI 技能的基础参考库. |
| [vercel-labs/agent-skills](https://github.com/vercel-labs/agent-skills) | Vercel 实验室主导的 AI Agent 技能库, 聚焦前端开发、云部署、自动化运维等场景, 技能与 Vercel 生态深度融合, 支持 Next.js、Vercel Deploy 等工具的自动化流程, 同时兼容主流 AI 编码助手, 主打开发效率提升. |
| [JackyST0/awesome-agent-skills](https://github.com/JackyST0/awesome-agent-skills) | 社区驱动的 AI Agent 技能精选清单, 汇总了全球优质的开源 Agent 技能, 按开发、办公、创意、科研等场景分类整理, 附带技能使用示例和适配工具说明, 是快速发现小众优质技能的一站式导航库. |
| [antfu/skills](https://github.com/antfu/skills) | 由 Vue/Vite 核心贡献者 Anthony Fu 打造的 前端生态专属 AI Agent 技能集合, 核心定位是为 AI 编程助手提供标准化的前端技术知识与最佳实践, 解决 AI 因训练数据滞后、不懂生态 "行规" 导致的代码不规范问题, 适配 Cursor、Claude Code 等主流 AI 工具, 是前端开发者提升 AI 辅助编程效率的核心工具库. |
| [ZhanlinCui/Agent-Skills-Hunter](https://github.com/ZhanlinCui/Agent-Skills-Hunter) | 聚焦 AI Agent 技能的检索与管理工具库, 提供技能自动爬取、分类、安全审计功能, 支持批量导入/导出技能, 可快速筛选符合 SKILL.md 标准的优质技能, 适配多平台 AI 工具的技能管理需求. |
| [ComposioHQ/awesome-claude-skills](https://github.com/ComposioHQ/awesome-claude-skills) | 一份精选的 Claude 技能、资源和工具列表, 用于定制 Claude AI 工作流程. |
| [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | 涵盖语言、后端/前端框架、基础设施、API、测试、DevOps、安全、数据/机器学习和平台专家的 12 个类别共 66 项专业技能. |
| [muratcankoylan/Agent-Skills-for-Context-Engineering](https://github.com/muratcankoylan/Agent-Skills-for-Context-Engineering) | 一套全面且开放的智能体技能集合, 专注于构建生产级人工智能智能体系统的上下文工程原理. 这些技能传授了策划上下文的艺术与科学, 以在任何智能体平台上最大限度地提高智能体的效率. |
| [andysingal/llm-course](https://github.com/andysingal/llm-course/blob/main/claude/skills.md) | NA |
| [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | PM 技能市场: AI 操作系统, 助力产品决策更佳. 65 项项目管理技能和 36 个链式工作流程, 分布在 8 个插件中. Claude Code、Cowork 等. 从发现到战略、执行、启动和增长. |
| [VoltAgent/awesome-agent-skills](https://github.com/VoltAgent/awesome-agent-skills) | 一个精心策划的代理技能集合, 专注于实际工程团队创建和使用的真实世界代理技能. 包含来自 Anthropic、Google Labs、Vercel、Stripe、Cloudflare、Netlify、Trail of Bits、Sentry、Expo、Hugging Face 等领先开发团队的官方技能, 以及社区构建的技能. 兼容 Claude Code、Codex、Antigravity、Gemini CLI、Cursor、GitHub Copilot、OpenCode、Windsurf 等多个平台. 是贡献最多的代理技能仓库, 由社区共同构建和维护.  |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | 一个精选的 Claude Code 相关资源列表, 包含技能、代理、插件、钩子和其他增强 Claude Code 工作流程的工具. 涵盖了代理技能、工作流与知识指南、工具、状态栏、钩子、斜杠命令、CLAUDE.md 文件、替代客户端和官方文档等多个类别. 包含来自 Trail of Bits、Anthropic 等知名团队的专业技能, 以及社区贡献的各种工具和资源.  |
| [libukai/awesome-agent-skills](https://github.com/libukai/awesome-agent-skills) | 一个遵循少而精原则的优质 Skills 资源集合, 致力于收集和分享最优质的 Skills 教程、案例和实践, 帮助更多人轻松迈出搭建 Agent 的第一步. 包含技能标准介绍、安装方法、创建指南、优质教程和精选技能等内容, 涵盖编程辅助、技术开发、内容创作、产品使用等多个领域. 提供了增强插件 Agent Skills Toolkit, 帮助快速创建和改进 Agent Skills.  |
| [MicrosoftDocs/Agent-Skills](https://github.com/MicrosoftDocs/Agent-Skills) | 一个专为 Azure 云开发设计的高质量代理技能集合, 基于 Microsoft Learn 文档编译而成. 包含 193 个技能, 涵盖计算、集成、数据与分析、AI 与机器学习、安全与身份、网络、基础设施、管理和专业领域等 19 个类别. 兼容 Claude Code、Gemini CLI、Codex CLI、Antigravity IDE、GitHub Copilot、Cursor、OpenCode 和 AdaL CLI 等多个平台. 提供了基于角色的技能包, 帮助开发者快速上手.  |


## 专用产经 SKills 合集
-------

| 项目 | 描述 | 支持 | 推荐星级 |
|:---:|:----:|:---:|:-------:|
| [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | Anthropics 官方开源的 Claude 金融服务专属插件库, 基于 Claude for Enterprise 打造, 核心目标是将通用大模型 Claude 转化为精通投行、行研、私募、财富管理等领域的专业金融分析师. |
| [phuryn/pm-skills](https://github.com/phuryn/pm-skills) |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 代理技能集合, 扩展规划、开发和工具能力. 主要包括: 规划与设计(write-a-prd、prd-to-plan、prd-to-issues、grill-me、design-an-interface、request-refactor-plan)、开发(tdd、triage-issue、improve-codebase-architecture、migrate-to-shoehorn、scaffold-exercises)、工具与设置(setup-pre-commit、git-guardrails-claude-code)、写作与知识(write-a-skill、edit-article、ubiquitous-language、obsidian-vault) 等技能. | ⭐⭐⭐ |
| [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | 基于 12,307 条推文提炼的商业诊断工具箱, 用 Claude Code skill 实现. 核心工具包括: 商业模式诊断(dbs-diagnosis)、对标分析(dbs-benchmark)、内容创作诊断(dbs-content)、执行力诊断(dbs-unblock)、概念拆解(dbs-deconstruct). 提供完整的工作流: diagnosis → benchmark → content → unblock, deconstruct 可随时使用. 每个 SKILL.md 包含完整的方法论框架、诊断流程和说话风格定义, 开箱即用. 同时提供了进行 [dbs](https://github.com/dontbesilent2025/dbskill/tree/main/skills/dbs) 路由. |
| [badlogic/pi-skills](https://github.com/badlogic/pi-skills) | 为 pi-coding-agent 提供的技能集合, 兼容 Claude Code、Codex CLI、Amp 和 Droid. 包含多个技能: Brave 搜索、浏览器工具、Google 日历/ Drive/ Gmail CLI、语音转文本、VS Code 集成、YouTube 转录等.  | 支持多种平台安装 | ⭐⭐⭐ |

# 安装 Skills
-------

## 方式一: 使用 npx skills(推荐)
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

## 方式二: 使用 Git 克隆

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

## 方式三: 手动复制

将 skill 目录复制到 Claude Code 的 skills 目录:

```bash
# macOS/Linux
cp -r skill-name ~/.claude/skills/

# Windows
xcopy skill-name %USERPROFILE%\.claude\skills\
```

# 使用 Skills

安装后, 重启 Claude Code 或重新加载 skills. Skills 会根据以下条件自动触发:

1. **语义匹配** - 根据用户请求的上下文自动加载相关技能
2. **触发词** - 在 SKILL.md 的 description 中定义的关键词
3. **命令触发** - 使用 `/skill-name` 命令手动触发

# 技能开发

如果你想创建自己的 Skill, 可以参考以下资源:

- **skill-creator** - 创建有效 Skills 的完整指南
- **claudeception** - 从工作会话中提取可重用知识的示例
- [Claude Code Skills 文档](https://docs.anthropic.com/en/docs/claude-code/skills)

# 贡献

欢迎提交 PR 添加新的 Skills 或改进现有 Skills.

# 许可

各 Skill 的许可请参考其各自的 LICENSE 文件.


# 参考
-------



| 集合 | 简要描述 | 安装方式 |
|:---:|:-------:|:-------:|
| [baoyu-skills](https://github.com/JimLiu/baoyu-skills) | 宝玉分享的 Claude Code 技能集, 提升日常工作效率. | `npx skills add jimliu/baoyu-skills` |
