

# 1. Agent Orchestrator
-------


| 领域 | 描述 |
|:---:|:----:|
| Agent Spec Driver | 规格驱动工程, 通过 Spec 流程驱动的"规范 + 执行 + 验证" 的三层规范体系, 摸清 AI 工作的真是能力边界, 约束 Agent 按照既定规范执行, 结合 Rlaph-Loop 实现 Agent 按照 Spec 约定的规范无人值守(长时)运行. |
| (sub)Agent Team Orchestrator | 构建一套智能体元编程编排器, 对于复杂的任务, 通过 (sub)Agent Team 自适应进行任务分解, 派发, 执行和调度的工作流控制. |
| Agent Parallel Workflow | Agent Parallel Workflow 致力于组合多个 Agent 协同工作, 通过 Parallel Workflow 完成多 Agent 并行编排和管理. 最终组合多个 Agent 协同工作, 保障复杂任务的高效完成. |

> 一句话描述
>
> Agent Spec Driver 致力于通过项目的规范化流程, 约束 AGENT 执行, 防止 AGENT 跑偏.
>
> Agent Team Orchestrator 是通过单个 Coding Agent 通过配置多个 subAgent 组成 Agent Team, 从而能完成复杂工作的开发与验证.
>
> Agent Parallel Orchestration 则组合多个 Coding Agent 的能力, 并行工作, 从而可以完成整个完整项目的设计与开发.


## 1.1 Agent Spec Driver
-------

规格驱动工程, 通过 Spec 流程驱动的"规范 + 执行 + 验证" 的三层规范体系, 摸清 AI 工作的真是能力边界, 约束 Agent 按照既定规范执行.
1. 通过 Spec 驱动约束 Agent 按照既定规范执行
2. 通过 Rlaph-Loop 实现 Agent 长时无人值守运行.

### 📊 1.1.1 Specification-Driven
-------

| 技能 | 描述 | 支持 | 推荐星级 |
|:---:|:----:|:---:|:-------:|
| [`superpowers`](https://github.com/obra/superpowers) | 一套完整的软件开发流程, 基于一套可组合的 Skills 和一些初步指令. | Claude Code<br>Cursor<br>Codex<br>OpenCode | ⭐⭐⭐⭐ |
| [planning-with-files](https://github.com/OthmanAdi/planning-with-files) | 用文件规划任务, 像 Manus 那样工作. | Claude Code<br>Cursor<br>Codex<br>OpenCode | ⭐⭐⭐⭐ |
| [github/spec-kit](https://github.com/github/spec-kit) | 帮助你开始专业化开发的工具包, 让你专注于产品场景和可预期的结果, 而不是从零开始随意编写每一个部分. | Claude Code<br>Cursor<br>Codex<br>OpenCode | ⭐⭐⭐⭐ |
| [Linfee/spec-kit-cn](https://github.com/Linfee/spec-kit) | Spec Kit 的非官方中文复刻版本,对应原版 v0.1.13. 命令使用 `specify-cn` 而非 `specify` | Claude Code<br>Cursor<br>Codex<br>OpenCode | ⭐⭐⭐⭐ |
| [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | 最受喜爱的规范框架,灵活而非僵化,支持 20+ AI 代理. 哲学: 流动而非刚性, 迭代而非瀑布, 简单而非复杂, 为从现有项目构建而不仅仅是新建项目构建, 可从个人项目扩展到企业级. | Claude Code<br>Cursor<br>Codex<br>OpenCode | ⭐⭐⭐⭐ |
| [claudeforge/Forge](https://github.com/claudeforge/Forge) | Claude Code 的规范驱动人工智能开发引擎, FORGE 将 Claude Code 转变为一个强大的迭代开发系统, 该系统通过正式规范、结构化规划和完成标准验证, 自主处理复杂任务. | Claude Code | ⭐⭐ |
| [claude-code-bmad-skills](https://github.com/aj-geddes/claude-code-bmad-skills) | [BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) 的 Claude Code 插件, [BMAD-METHOD(Breakthrough Method of Agile AI-Driven Development)](https://github.com/ljxpython/bmad-method-tutorial) 突破性的敏捷 AI 驱动开发方法, 是一个内置了完整敏捷开发流程的智能体系统, BMAD Method for Claude Code skills, 则不仅仅是一套 Skills 集, 它是一套将敏捷开发方法论(Agile Methodology)与AI原生能力深度融合的工程框架. 它将 Claude Code 从一个"更聪明的 Agent" 转变为一支具备 9 种专业角色、15种标准工作流的"全栈敏捷开发团队". 参见 [Documentation Site, with examples](https://aj-geddes.github.io/claude-code-bmad-skills)  | Claude Code | ⭐ |


### 1.1.2 Rlaph-Loop
-------

| 技能 | 描述 | 支持 | 推荐星级 |
|:---:|:----:|:---:|:-------:|
| [hamelsmu/claude-review-loop](https://github.com/hamelsmu/claude-review-loop) | 一个Claude Code插件, 可将自动代码审查循环添加到您的工作流程中. 使用 `/review-loop` 时, 该插件会创建一个两阶段生命周期.<br>任务阶段: 你描述一项任务, Claude 负责执行<br>2. 审查阶段: 当 Claude 完成后, 会自动运行 Codex 进行独立代码审查, 然后要求 Claude 处理反馈意见<br>结果: 在您接受更改之前, 每项任务都会得到独立的二次审核意见. | Claude Code/Codex | ⭐⭐⭐⭐ |
| [ZhangHanDong/agent-spec](https://github.com/ZhangHanDong/agent-spec) | 智能体规范定义和管理工具，提供标准化的智能体配置和编排能力 | 多模型支持 | ⭐⭐⭐⭐ |
| [tintinweb/pi-supervisor](https://github.com/tintinweb/pi-supervisor) | Pi-Agent 扩展，监控编码代理并引导其朝向定义的目标前进，通过观察对话、注入指导消息和信号完成状态来实现监督功能 | Pi | ⭐⭐⭐ |


### 1.1.3 Agent Full Stack 配置
-------

| 技能 | 描述 | 支持 | 推荐星级 |
|:---:|:----:|:---:|:-------:|
| [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | Anthropic 黑客松冠军的 Claude Code 配置, 不仅仅是配置. 一个完整的系统: 技能、直觉、记忆优化、持续学习、安全扫描和以研究为先的开发. | Claude Code | ⭐⭐⭐⭐⭐ |
| [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | Claude-Code 最佳实践. 汇总了已验证过的最佳工作流程和相关的避坑经验, 以及一套 Skills, Agent, MCP 等相关配置. | Claude Code | ⭐⭐⭐⭐ |
| [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | 理念是"用 AI 组建公司", 不过当前实现中只是包含了众多 Agent 相关 Prompt. 一份精选的 Claude 技能、资源和工具列表, 用于定制 Claude AI 工作流程. | Claude Code | ⭐⭐⭐⭐ |
| [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) 的中文版本, AI 智能体专家团队(中文版)—80+ 个专业 AI 智能体人设, 覆盖开发、设计、营销、测试、运维等领域, 含小红书/抖音/微信等中国平台原创智能体. | Claude Code | ⭐⭐⭐⭐ |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | 一个全面的 Claude Code 资源集合, 包含各种技能、工具和最佳实践. | Claude Code | ⭐⭐⭐⭐ |
| [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | 由 Jeffallan 维护 Claude 配置库, 提供了一系列 Skills、功能脚本与集成示例, 旨在扩展 Claude 在不同场景下的能力边界. 项目核心目标是让开发者/使用者快速复用成熟的模板, 无需从零配置, 即可让 Claude 完成特定任务, 降低 Claude 定制化使用的门槛. | Claude Code | ⭐⭐⭐⭐ |
| [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | 涵盖 9 大领域的 Claude Code Skills 和 Plugin, 包含<br>1. 工程研发前后端全栈和 DevOps, RAG 架构师、CI/CD 构建器, 甚至还有能自我优化的自进化 Agent.<br>2. 市场增长: SEO、内容创作、转化率优化(CRO)和增长策略等等.<br>3. 高管智囊: 从战略规划、文化建设到模拟董事会会议都能参谋.<br>4. 其他辅助: 产品设计、项目管理、财务分析，甚至连最让人头疼的合规审查(医疗 MDR、GDPR、ISO)都有专门的插件. 参见 [出海去孵化器 @chuhaiqu 的帖子](https://x.com/chuhaiqu/status/2030941933418500562). | Claude Code | ⭐⭐⭐⭐ |
| [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | Claude Code 的即用配置. 一个全面的 AI 代理、自定义命令、设置、钩子、外部集成(MCP) 和项目模板，旨在提升您的开发工作流程. | Claude Code | ⭐⭐⭐⭐ |
| [ChrisWiles/claude-code-showcase](https://github.com/ChrisWiles/claude-code-showcase) | 深度配置和使用 Claude Code, 提供完整的开发配套环境. | Claude Code | ⭐⭐⭐⭐ |
| [stretchcloud/claude-code-unified-agents](https://github.com/stretchcloud/claude-code-unified-agents) | 一个全面的 Claude Code 子代理集合, 结合了多个社区仓库中的最佳功能. 该统一集合提供了 54 个智能体, 涵盖开发、基础设施、质量、AI/ML、商业、创意、元管理和专业领域. | Claude Code | ⭐⭐⭐⭐ |
| [wasabeef/claude-code-cookbook](https://github.com/wasabeef/claude-code-cookbook) | 一套集成的 Claude Code 环境, 通过 40+ 预设的命令, 8+ 智能体角色, 自动化 Hooks, 让 Claude Code 自动判断并执行常见并发任务, 比如代码修正, 测试执行, 文档更新等. | Claude Code | ⭐⭐⭐⭐ |
| [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | Claude Code 最全面的工具包, 包含 135 个代理, 35 个精选技能, 42 个命令, 121 个插件, 19 个钩子, 15 条规则, 7 个模板, 6 个 MCP 配置, 等等. | Claude Code | ⭐⭐⭐ |
| [feiskyer/claude-code-settings](https://github.com/feiskyer/claude-code-settings) | 精选的 Claude 代码设置、技能和子代理合集, 旨在提升开发流程. 该配置包括功能开发(基于规格的工作流程)、代码分析、GitHub 集成和知识管理的专业技能和子代理. | Claude Code | ⭐⭐⭐ |
| [UfoMiao/zcf](https://github.com/UfoMiao/zcf) | Zero-Config Code Flow，为 Claude Code 和 Codex 提供零配置、一键设置，支持双语、智能代理系统和个性化 AI 助手 | Claude Code/Codex | ⭐⭐⭐⭐ |


## 1.2 (sub)Agent Team Orchestrator
-------

智能体编排器(Agent Team Orchestrator)通过在单个 Coding Agent 中构建 (sub)Agent Team, 对 (sub)Agent Team 进行协调调度, 任务自适应划分，subAgent 并行和管理, 实现任务规划,  分配和工作流控制, 实现元编程调度框架. 具体包括:
1. (sub)多智能体并行管理：生成并管理多个并行运行的 AI 编码代理，为每个代理分配独立的工作环境;
2. 自主任务处理：代理能够自主修复 CI 故障、处理代码审查评论、自动创建和管理 PR;
3. 监控与协调：提供仪表盘式监控界面，协调多个代理之间的工作;
4. 工作流优化：将复杂任务分解为可管理的子任务，优化工作流程;
5. 多模型支持：兼容多种 AI 模型，根据任务类型选择合适的模型.

### 1.2.1 oh-my-zsh 系列
-------

| 技能 | 描述 | 支持 | 推荐星级 |
|:---:|:----:|:---:|:-------:|
| [oh-my-opencode](https://github.com/code-yeongyu/oh-my-openagent) | 开源的 AI 编码代理编排框架，提供丰富的技能和工具集成 | OpenCode | ⭐⭐⭐⭐ |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | oh-my-opencode 的 [Claude Code 移植版](https://github.com/Yeachan-Heo/oh-my-claudecode/commit/cd98f12fac986bce4b7246aac3326ed107574fb3)), 之前叫 [oh-my-claude-sisyphus](https://github.com/Yeachan-Heo/oh-my-claudecode/commit/3a02feb187f1185fc51379a84ad001b114ac12af), v3.0.0 之后改名. 官网 [oh-my-claudecode-website](https://yeachan-heo.github.io/oh-my-claudecode-website) | Claude Code | ⭐⭐⭐⭐ |
| [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | oh-my-opencode 的 codex 移植版 | Codex | ⭐⭐⭐⭐ |
| [MeroZemory/oh-my-droid](https://github.com/MeroZemory/oh-my-droid) | Factory Droid 的多智能体编排器, 零学习曲线. 基于 oh-my-claudecode 实现. | Factory Droid | ⭐⭐⭐⭐ |
| [woosikkim/oh-my-claudecode-slim](https://github.com/woosikkim/oh-my-claudecode-slim) | oh-my-claudecode 的精简版. | Claude Code | ⭐⭐⭐ |
| [alvinunreal/oh-my-opencode-slim](https://github.com/alvinunreal/oh-my-opencode-slim) | oh-my-opencode 的精简版. | OpenCode | ⭐⭐⭐ |
| [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | 终端 AI 编码代理, 基于 badlogic/pi-mono, 提供完整的开发工具链. | Pi | ⭐⭐⭐⭐ |

### 1.2.2 Agent 调度与编排
-------

| 技能 | 描述 | 支持 | 推荐星级 |
|:---:|:----:|:---:|:-------:|
| [wshobson/agents](https://github.com/wshobson/agents) | 一个全面的 AI 开发部件, 包含了 112 个专业 AI 智能体、16 个智能体工作流编排器、146 个 Skills 和 79 个开发工具, 组织成 72 个专注于 Claude Code 的插件. | Claude Code | ⭐⭐⭐⭐ |
| [SuperClaude](https://github.com/SuperClaude-Org/SuperClaude_Framework) | 专为 Claude Code 打造的元编程配置框架, 核心作用是通过丰富的工具集和配置体系, 将 Claude Code 从基础的代码生成工具升级为结构化、专业化的智能开发平台. 包含了 22 个斜杠命令(/sc:), 14 个领域智能代理(Agents), 6 种行为模式, 官网 [superclaude](https://superclaude.netlify.app) | Claude Code | ⭐⭐⭐⭐ |
| [sangrokjung/claude-forge](https://github.com/sangrokjung/claude-forge) | 开源的 Claude Code 开发环境, 提供 11 个专用智能体、40 个斜杠命令、15 个技能工作流程和 15 个自动化钩子. 它被形容为是 Claude Code 的 oh-my-zsh, 它将 Claude 代码从一个基础的 CLI 转变为一个功能齐全的开发环境. 一次安装就能提供代理、命令、技能、钩子和 9 个规则文件——全部预先布线, 随时可用. | Claude Code | ⭐⭐⭐⭐ |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | Ruflo(Claude-Flow) 是一个全面的人工智能代理编排框架, 将 Claude Code 转变为强大的多代理开发平台. 它使团队能够部署、协调和优化专业的人工智能代理，协同处理复杂的软件工程任务. 支持多个 Agent 并行执行, 同时提供实时监控面板. | Claude Code | ⭐⭐⭐⭐ |
| [ComposioHQ/agent-orchestrator](https://github.com/ComposioHQ/agent-orchestrator) | 生成并行的 AI 编码代理, 每个代理在自己的 git 工作树中. 代理自主修复 CI 故障, 处理审核评论, 并开放 PR——你只需在一个仪表盘上进行监督.<br>Agent Orchestrator 管理着一系列并行运行在代码库上的 AI 编码代理. 每个代理都有自己的 git 工作树、分支和 PR. 当 CI 失败时, 代理会修复它. 当审核员留下评论时, 代理人会进行回应. 只有当需要人为判断时, 你才会被拉进来. | 多模型支持 | ⭐⭐⭐ |
| [openai/symphony](https://github.com/openai/symphony) | Symphony 将项目工作转化为独立、自主的实现运行, 使团队能够管理工作, 而无需监督编码代理. | Codex | ⭐⭐⭐ |
| [wozhenbang2004/AgentNexus](https://github.com/wozhenbang2004/AgentNexus) | AgentNexus 不仅仅是一个 AI 应用框架, 它是一个功能完备的智能体(Agent)基础设施, 专为解决企业在生产环境中落地复杂AI工作流的核心挑战而设计. 摒弃了硬编码的 Agent 逻辑, 通过将模型、工具(MCP)、RAG知识库、提示词等所有核心组件进行数据库持久化, 并通过 API 驱动的责任链模式在运行时动态构建 Agent, 从而赋予系统强大的动态编排、自主协作与全生命周期管理能力. | 多模型支持 | ⭐⭐ |
| [cft0808/edict](https://github.com/cft0808/edict) | 三省六部(Edict), 用 1300 年前的帝国制度, 重新设计了 AI 多 Agent 协作架构. 12 个 AI Agent(11 个业务角色 + 1 个兼容角色)组成三省六部: 太子分拣、中书省规划、门下省审核封驳、尚书省派发、六部+吏部并行执行. 比 CrewAI 多一层制度性审核, 比 AutoGen 多一个实时看板. | 多模型支持 | ⭐⭐⭐⭐ |
| [mikeyobrien/ralph-orchestrator](https://github.com/mikeyobrien/ralph-orchestrator) | Ralph Orchestrator 是一款轻量级、开源的 AI 工作流编排工具, 核心定位是「为提示词工程和 AI 任务协作提供结构化编排能力」, 主打极简部署、无代码/低代码操作、多 AI 模型适配. | 多模型支持 | ⭐⭐⭐ |
| [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | 完整的 AI 编码工作流系统，提供经过实战验证的工作流模式、自我纠正记忆、并行工作树、结束仪式和 80/20 AI 编码比例，支持 Claude Code、Cursor 和 32+ 个其他代理 | 多模型支持 | ⭐⭐  |
| [samibs/skillfoundry](https://github.com/samibs/skillfoundry) | AI 工程框架，提供质量门控、持久记忆和多平台支持，适用于 Claude Code、Cursor、Copilot、Codex 和 Gemini | 多模型支持 | ⭐ |
| [agent-sh/agentsys](https://github.com/agent-sh/agentsys) | AI 编码自动化系统，提供 15 个插件、35 个智能体和 32 个技能，支持 Claude Code、OpenCode、Codex、Cursor 和 Kiro 等多种编码工具 | 多模型支持 | ⭐⭐⭐ |
| [claudeforge/orchestrator](https://github.com/claudeforge/orchestrator) | 为 Claude Code 设计的自主开发系统, 提供自动化开发流程和工作流管理. | Claude Code | ⭐⭐ |
| [shinpr/claude-code-workflows](https://github.com/shinpr/claude-code-workflows) | 为 Claude Code 设计的生产就绪开发工作流，由专门的 AI 智能体提供支持，涵盖代码质量、开发工作流和提示工程等多个方面 | Claude Code | ⭐ |


## 1.3 Agent Parallel Workflow
-------

Agent Parallel Workflow 致力于组合多个 Agent 协同工作, 通过 Parallel Workflow 完成多 Agent 并行编排和管理. 最终组合多个 Agent 协同工作, 保障复杂任务的高效完成.

| 技能 | 描述 | 支持 | 推荐星级 |
|:---:|:----:|:---:|:-------:|
| [uluckyXH/OpenMOSS](https://github.com/uluckyXH/OpenMOSS) | 一个 AI 管理 AI 的平台. 多个代理自主协作——规划、执行、审查和检查——而人类只需设定目标并核对结果. OpenMOSS(多代理编排与自我演化系统)是一个基于 OpenClaw 的自组织多代理协作平台. | OpenClaw | ⭐⭐⭐⭐ |
| [fengshao1227/ccg-workflow](https://github.com/fengshao1227/ccg-workflow) | 多模型协作开发工具集. 基于 Claude Code CLI, 整合 Codex/Gemini 后端能力, 提供智能路由、代码审查、Git 工具等 17+ 个命令. | Claude Code/Codex/Gemini  | ⭐⭐⭐⭐ |
| [johannesjo/parallel-code](https://github.com/johannesjo/parallel-code) | Parallel Code 为 Claude Code、Codex CLI 和 Gemini CLI 各自自动赋予了自己的 git 分支和工作树. 没有特工互相踩到代码, 没有杂耍终端, 没有精神负担. 只需一个干净的界面, 你就能看到所有内容, 快速导航, 结果准备好时合并——并且从手机上监控. | Claude Code/Codex/Gemini | ⭐⭐⭐⭐ |
| [EtienneLescot/n8n-as-code](https://github.com/EtienneLescot/n8n-as-code) | 围绕 n8n(开源自动化工作流工具)打造的工具集, 核心目标是为 AI 编码代理赋予 n8n 全量能力, 同时提供 GitOps 流程、TypeScript 工作流开发、多端(VS Code/CLI/Claude)操作等能力, 实现 n8n 工作流的高效、可追溯、智能化管理. | 多模型支持 | ⭐⭐⭐⭐ |
| [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | 一个基于 Claude 的 AI 驱动开发任务管理系统, 设计用来与 Cursor AI 无缝协作. Task Master 让 Claude Code 像项目经理一样思考, 自动拆解 PRD(需求文档), 生成任务列表, 并跟踪进度. 通过 MCP 配置, 可以轻松接入 Cursor 和 Windsurf 等开发工具. [@GitHub_Daily 的帖子](https://x.com/GitHub_Daily/status/1915556362139955323) | Claude Code | ⭐⭐⭐⭐ |
| [skindhu/AI-TASK-MANAGER](https://github.com/skindhu/AI-TASK-MANAGER) | AI Task Master 是对原始 claude-task-manager 项目的增强和改进版本. 分析了原始项目的设计理念和能力后, 进行了升级. | Claude Code | ⭐⭐⭐⭐ |
| [stellarlinkco/myclaude](https://github.com/stellarlinkco/myclaude) | 多智能体编排工作流系统，支持 Claude Code、Codex、Gemini、OpenCode 多后端执行，提供多种开发工作流程模块（do、omo、bmad等）和可单独安装的技能 | 多模型支持 | ⭐⭐⭐⭐ |
| [axtonliu/ai-pair](https://github.com/axtonliu/ai-pair) | 异构 AI 团队协作工具, 协调多个 AI 模型(Claude + GPT + Gemini)作为一个团队工作, 一个创作, 两个审查, 利用不同模型的不同视角, 是一个 Claude Code Skill. [我开源了一个让 Claude、GPT、Gemini 组队的 Skill](https://x.com/AxtonLiu/status/2031732461982416898). | Claude Code/Codex/Gemini | ⭐⭐⭐⭐ |
| [MistRipple/magi-code](https://github.com/MistRipple/magi-code) | 多智能体工程编排系统, 在 VSCode 中将复杂开发任务自动拆解为可执行合同, 调度异构 Worker 并行协作, 完成从规划、执行、验收到知识沉淀的全流程闭环. | 多模型支持 | ⭐⭐⭐⭐ |
| [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | 多平台 AI 编码框架, 用来统一 AI 编程工具的上下文. 提供自动注入规范、任务中心工作流、并行代理执行、项目记忆和团队共享标准等功能<br>当前多个 AI Coding Agent 并发工作时, 每个工具的规范和历史记录都不互通. Trellis 的做法是在项目中建一个 `.trellis/` 目录, 把代码规范, 任务 PRD, 工作流都存进去. 不管切换到任意 AI 工具, 都能把这些上下文注意进入. 通过 git worktrees 让多个 AI 任务并行执行. 团队里一个人写好规范, 其他人开箱即用. | Claude Code、Cursor、OpenCode、iFlow、Codex、Kilo、Kiro、Gemini CLI、Antigravity 和 Qoder | ⭐⭐⭐⭐ |

# 2 上下文工程
-------

## 2.1 记忆
-------


### 2.1.2 记忆管理
-------

| 技能 | 描述 | 支持 | 推荐星级 |
|:---:|:----:|:---:|:-------:|
| [AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace) | 记忆宫殿为人工智能代理提供了持久上下文和无缝的跨会话连续性. 它为 LLM 提供了持久、可搜索和可审计的历史上下文——所以你的代理在每次对话中都不会"从零开始", 通过统一的 MCP(模型上下文协议)接口, Memory Palace 为 Codex、Claude Code、Gemini CLI 和 OpenCode 提供了集成路径, 并为光标和反重力提供了文档说明. 目前已验证的范围和已知边界已在 docs/skills/SKILLS_QUICKSTART_EN.md 文献中记录. | Codex/Claude Code/Gemini/OpenCode | ⭐⭐⭐⭐ |
| [okooo5km/memory-mcp-server](https://github.com/okooo5km/memory-mcp-server) | MCP 知识图谱管理服务器, Swift 实现, 为 LLM 提供持久记忆能力. 知识图谱存储、实体管理、关系跟踪、观察系统、强大搜索. | Claude/Cursor/Chatwise | ⭐⭐⭐⭐ |
| [coleam00/mcp-mem0](https://github.com/coleam00/mcp-mem0) | 集成 Mem0 的 MCP 服务器, 提供长期记忆和语义搜索能力. 支持 save_memory、get_all_memories、search_memories 三个核心工具. | 多种 MCP 客户端 | ⭐⭐⭐⭐ |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | 为 Claude Code 构建的持久记忆压缩系统,自动捕获工具使用并生成语义摘要. 提供 5 个生命周期钩子、Web 查看器 UI、mem-search 技能、渐进式披露. | Claude Code | ⭐⭐⭐⭐ |
| [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory) | 高级记忆管理系统，为 AI 代理提供持久化记忆和上下文管理能力 | 多模型支持 | ⭐⭐⭐ |
| [tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem) | OpenCode 的记忆管理插件，提供持久化记忆和上下文管理能力 | OpenCode | ⭐⭐⭐ |
| [rizal72/true-mem](https://github.com/rizal72/true-mem) | 真实记忆管理系统，为 AI 代理提供持久化记忆和上下文管理能力 | 多模型支持 | ⭐⭐⭐ |
| [Alenryuichi/openmemory-plus](https://github.com/Alenryuichi/openmemory-plus) | 增强型记忆管理系统，为 AI 代理提供持久化记忆和上下文管理能力 | 多模型支持 | ⭐⭐⭐ |
| [clopca/open-mem](https://github.com/clopca/open-mem) | 开源记忆管理系统，为 AI 代理提供持久化记忆和上下文管理能力 | 多模型支持 | ⭐⭐⭐ |


### 2.1.3 记忆共享
-------

| 技能 | 描述 | 支持 | 推荐星级 |
|:---:|:----:|:---:|:-------:|
| [mem0ai/mem0-mcp](https://github.com/mem0ai/mem0-mcp) | Mem0 MCP 服务器，将 Mem0 Memory API 包装为 Model Context Protocol (MCP) 服务器，支持添加、搜索、更新和删除长期记忆，适用于 MCP 兼容客户端（Claude Desktop、Cursor、自定义代理） | 多模型支持 | ⭐⭐⭐⭐ |



## 2.2 Token 治理
-------

| 技能 | 描述 | 支持 | 推荐星级 |
|:---:|:----:|:---:|:-------:|
| [zenobi-us/opencode-skillful](https://github.com/zenobi-us/opencode-skillful) | 提供懒惰加载的技能发现和注入.<br>AI 有时会因为加载了太多的"系统提示词"或"操作指南"而浪费大量初始 Token.<br>核心功能是将复杂的 Prompt 碎片化为"技能"<br>默认情况下上下文是空的, 只有当 AI 识别到任务(比如"现在需要进行 Docker 部署"), 时, 它才会动态"注入"相关的专业知识和规则. 这能节省约 20%-40% 的静态上下文空间.<br>1. 在对话中, 智能体使用 skill_find 来发现技能.<br>2. 使用 skill_use "skill_name"<br>3. 代理可以用来 skill_resource skill_relative/resource/path 读取参考资料. | OpenCode | ⭐⭐⭐⭐ |
| [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | RTK 会在命令输出到达你的 LLM 上下文之前过滤和压缩它们. 单一 Rust 二进制, 零依赖, 开销 <10 ms. | 多模型支持 | ⭐⭐⭐⭐ |
| [mksglu/context-mode](https://github.com/mksglu/context-mode) | 上下文模式管理工具, 帮助优化和管理 AI 代理的上下文使用, 减少 Token 消耗. | 多模型支持 | ⭐⭐⭐⭐ |

## 2.3 状态监控
-------

### 2.3.1 通知
-------

| 技能 | 描述 | 支持 | 推荐星级 |
|:---:|:----:|:---:|:-------:|
| [opencode-notifier](https://github.com/mohak34/opencode-notifier) | OpenCode 桌面通知插件 (仓库可能已下线) | OpenCode | ⭐⭐ |
| [opencode-terminal-notifier](https://github.com/mathew-cf/opencode-terminal-notifier) | OpenCode 终端通知插件,通过终端本身发送通知,点击通知可跳回正确的终端会话. 支持 Ghostty/iTerm2/Kitty/WezTerm 桌面通知,其他终端声音+dock bounce | OpenCode | ⭐⭐⭐⭐ |
| [opencode-smart-voice-notify](https://github.com/MasuRii/opencode-smart-voice-notify) | OpenCode 智能语音通知插件 (仓库可能已下线) | OpenCode | ⭐⭐ |

### 2.3.2 会话管理
-------

[](https://x.com/juristr/status/2031820737745682520)

| 技能 | 描述 | 支持 | 推荐星级 |
|:---:|:----:|:---:|:-------:|
| [hallucinogen/agent-viewer](https://github.com/hallucinogen/agent-viewer) | OpenCode 状态栏插件,显示当前会话信息 | OpenCode | ⭐⭐⭐ |
| [Frayo44/agent-view](https://github.com/Frayo44/agent-view) | 基于 tmux 实现的轻量级会话管理器, 支持 Claude Code, Gemini CLI, OpenCode, Codex CLI 等主流 AI 编程工具. 可以实时状态监控面板, 能看到每个智能体的状态. | Claude Code/Gemini/OpenCode/Codex | ⭐⭐⭐⭐ |
| [fynnfluegge/agtx](https://github.com/fynnfluegge/agtx) | 用于管理 agent coding 会话的原生终端看板, 可以接入 Claude Code、Codex、Gemini、OpenCode、Copilot 等任何现有的规范驱动开发框架, 或指定一个具有分阶段技能的自定义插件. | Claude Code/Codex/Gemini/OpenCode/Copilot | ⭐⭐⭐⭐ |
| [batrachianai/toad](https://github.com/batrachianai/toad) | TUI 界面的终端 AI 智能体管理器. | 多模型支持 | ⭐⭐⭐⭐ |
| [standardagents/dmux](https://github.com/standardagents/dmux) | 开发代理多路复用器，用于在隔离的 git worktrees 中管理多个 AI 编码代理，支持并行分支、开发和合并，兼容多种代理（Claude Code、Codex、OpenCode、Gemini 等） | 多模型支持 | ⭐⭐⭐⭐ |
| [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) |
| [conductor.build](https://www.conductor.build) |
| [superset-sh/superset](https://github.com/superset-sh/superset) |
| [paperclipai/paperclip](https://github.com/paperclipai/paperclip) |
| [Dimillian/CodexMonitor](https://github.com/Dimillian/CodexMonitor) |
| [supacode.sh](https://supacode.sh) |
| [](https://www.agentastic.dev)  |
| [](https://thecommander.app/) |
| [](https://mux.coder.com/) |
| [](https://smithers.sh/introduction)

### 2.3.3 状态管理
-------

| 技能 | 描述 | 支持 | 推荐星级 |
|:---:|:----:|:---:|:-------:|
| ccstatusline | OpenCode 状态栏插件,显示当前会话信息 | OpenCode | ⭐⭐⭐ |
| [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | Claude Code 的 HUD 界面，提供实时状态监控和交互能力 | Claude Code | ⭐⭐⭐⭐ |
| [Link-Start/my-claude-hud](https://github.com/Link-Start/my-claude-hud) | Claude Code 的自定义 HUD 界面，提供实时状态监控和交互能力 | Claude Code | ⭐⭐⭐⭐ |
| [matt1398/claude-devtools](https://github.com/matt1398/claude-devtools) | Claude Code 的开发工具集，提供调试、监控和优化能力 | Claude Code | ⭐⭐⭐⭐ |


# 参考
-------

[oh-my-opencode 和 superpowers](https://linux.do/t/topic/1445132/18)
[opencode配置文档](https://linux.do/t/topic/1415352)
[对oh-my-opencode的简单修复，节约5~10倍的API消耗。](https://linux.do/t/topic/1658684)
[`[Question]`: How to get the status of background agents? #917](https://github.com/code-yeongyu/oh-my-openagent/issues/917)


[Cranot/claude-code-guide](https://github.com/Cranot/claude-code-guide), 完整 Claude 代码 CLI 指南. 实时指南: 每两天自动更新一次, 来源于官方文档、GitHub 发布和 Anthropic 更新日志.

[FlorianBruniaux/claude-code-ultimate-guide](https://github.com/FlorianBruniaux/claude-code-ultimate-guide), 本指南教你以不同的角度看待人工智能辅助开发.
