# 插件列表


## 智能体编排
-------

### oh-my-zsh 系列
-------

| 技能 | 描述 | 支持 | 推荐星级 |
|:---:|:----:|:---:|:-------:|
| [oh-my-opencode](https://github.com/code-yeongyu/oh-my-openagent) | NA | opencode | NA |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | oh-my-opencode 的 [Claude Code 移植版](https://github.com/Yeachan-Heo/oh-my-claudecode/commit/cd98f12fac986bce4b7246aac3326ed107574fb3)), 之前叫 [oh-my-claude-sisyphus](https://github.com/Yeachan-Heo/oh-my-claudecode/commit/3a02feb187f1185fc51379a84ad001b114ac12af), v3.0.0 之后改名. 官网 [oh-my-claudecode-website](https://yeachan-heo.github.io/oh-my-claudecode-website) | Claude Code | NA |
| [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | oh-my-opencode 的 codex 移植版 | Codex | NA |
| [MeroZemory/oh-my-droid](https://github.com/MeroZemory/oh-my-droid) |
| [woosikkim/oh-my-claudecode-slim](https://github.com/woosikkim/oh-my-claudecode-slim) |
| [alvinunreal/oh-my-opencode-slim](https://github.com/alvinunreal/oh-my-opencode-slim) |
| [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | NA |

### Agent 调度与编排
-------

| 技能 | 描述 | 支持 | 推荐星级 |
|:---:|:----:|:---:|:-------:|
| [wshobson/agents](https://github.com/wshobson/agents) | 一个全面的 AI 开发部件, 包含了 112 个专业 AI 智能体、16 个智能体工作流编排器、146 个 Skills 和 79 个开发工具, 组织成 72 个专注于 Claude Code 的插件. | Claude Code | NA |
| [SuperClaude](https://github.com/SuperClaude-Org/SuperClaude_Framework) | 专为 Claude Code 打造的元编程配置框架, 核心作用是通过丰富的工具集和配置体系, 将 Claude Code 从基础的代码生成工具升级为结构化、专业化的智能开发平台. 包含了 22 个斜杠命令(/sc:), 14 个领域智能代理(Agents), 6 种行为模式, 官网 [superclaude](https://superclaude.netlify.app) |
| [sangrokjung/claude-forge](https://github.com/sangrokjung/claude-forge) | 开源的 Claude Code 开发环境, 提供 11 个专用智能体、40 个斜杠命令、15 个技能工作流程和 15 个自动化钩子. 它被形容为是 Claude Code 的 oh-my-zsh, 它将 Claude 代码从一个基础的 CLI 转变为一个功能齐全的开发环境. 一次安装就能提供代理、命令、技能、钩子和 9 个规则文件——全部预先布线, 随时可用. |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | Ruflo(Claude-Flow) 是一个全面的人工智能代理编排框架, 将 Claude Code 转变为强大的多代理开发平台. 它使团队能够部署、协调和优化专业的人工智能代理，协同处理复杂的软件工程任务. 支持多个 Agent 并行执行, 同时提供实时监控面板. |
| [ComposioHQ/agent-orchestrator](https://github.com/ComposioHQ/agent-orchestrator) | 生成并行的 AI 编码代理, 每个代理在自己的 git 工作树中. 代理自主修复 CI 故障, 处理审核评论, 并开放 PR——你只需在一个仪表盘上进行监督.<br>Agent Orchestrator 管理着一系列并行运行在代码库上的 AI 编码代理. 每个代理都有自己的 git 工作树、分支和 PR. 当 CI 失败时, 代理会修复它. 当审核员留下评论时, 代理人会进行回应. 只有当需要人为判断时, 你才会被拉进来. |
| [openai/symphony](https://github.com/openai/symphony) | Symphony 将项目工作转化为独立、自主的实现运行, 使团队能够管理工作, 而无需监督编码代理. | Codex | NA |
| [wozhenbang2004/AgentNexus](https://github.com/wozhenbang2004/AgentNexus) | AgentNexus 不仅仅是一个 AI 应用框架, 它是一个功能完备的智能体(Agent)基础设施, 专为解决企业在生产环境中落地复杂AI工作流的核心挑战而设计. 摒弃了硬编码的 Agent 逻辑, 通过将模型、工具(MCP)、RAG知识库、提示词等所有核心组件进行数据库持久化, 并通过 API 驱动的责任链模式在运行时动态构建 Agent, 从而赋予系统强大的动态编排、自主协作与全生命周期管理能力. |
| [cft0808/edict](https://github.com/cft0808/edict) | 三省六部(Edict), 用 1300 年前的帝国制度, 重新设计了 AI 多 Agent 协作架构. 12 个 AI Agent(11 个业务角色 + 1 个兼容角色)组成三省六部: 太子分拣、中书省规划、门下省审核封驳、尚书省派发、六部+吏部并行执行. 比 CrewAI 多一层制度性审核, 比 AutoGen 多一个实时看板. |
| [mikeyobrien/ralph-orchestrator](https://github.com/mikeyobrien/ralph-orchestrator) | Ralph Orchestrator 是一款轻量级、开源的 AI 工作流编排工具, 核心定位是「为提示词工程和 AI 任务协作提供结构化编排能力」, 主打极简部署、无代码/低代码操作、多 AI 模型适配. |

### Agent 协作与并行
-------

| 技能 | 描述 | 支持 | 推荐星级 |
|:---:|:----:|:---:|:-------:|
| [uluckyXH/OpenMOSS](https://github.com/uluckyXH/OpenMOSS) | 一个 AI 管理 AI 的平台. 多个代理自主协作——规划、执行、审查和检查——而人类只需设定目标并核对结果. OpenMOSS(多代理编排与自我演化系统)是一个基于 OpenClaw 的自组织多代理协作平台. | OpenClaw | NA |
| [fengshao1227/ccg-workflow](https://github.com/fengshao1227/ccg-workflow) | 多模型协作开发工具集. 基于 Claude Code CLI, 整合 Codex/Gemini 后端能力, 提供智能路由、代码审查、Git 工具等 17+ 个命令. | Claude Code/Codex/Gemini  | NA |
| [johannesjo/parallel-code](https://github.com/johannesjo/parallel-code) | Parallel Code 为 Claude Code、Codex CLI 和 Gemini CLI 各自自动赋予了自己的 git 分支和工作树. 没有特工互相踩到代码, 没有杂耍终端, 没有精神负担. 只需一个干净的界面, 你就能看到所有内容, 快速导航, 结果准备好时合并——并且从手机上监控. |
| [EtienneLescot/n8n-as-code](https://github.com/EtienneLescot/n8n-as-code) | 围绕 n8n(开源自动化工作流工具)打造的工具集, 核心目标是为 AI 编码代理赋予 n8n 全量能力, 同时提供 GitOps 流程、TypeScript 工作流开发、多端(VS Code/CLI/Claude)操作等能力, 实现 n8n 工作流的高效、可追溯、智能化管理. |
| [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | 一个基于 Claude 的 AI 驱动开发任务管理系统, 设计用来与 Cursor AI 无缝协作. Task Master 让 Claude Code 像项目经理一样思考, 自动拆解 PRD(需求文档), 生成任务列表, 并跟踪进度. 通过 MCP 配置, 可以轻松接入 Cursor 和 Windsurf 等开发工具. [@GitHub_Daily 的帖子](https://x.com/GitHub_Daily/status/1915556362139955323) | NA | NA |
| [skindhu/AI-TASK-MANAGER](https://github.com/skindhu/AI-TASK-MANAGER) | AI Task Master 是对原始 claude-task-manager 项目的增强和改进版本. 分析了原始项目的设计理念和能力后, 进行了升级. | NA | NA |


### Agent Full Stack 配置
-------

| 技能 | 描述 | 支持 | 推荐星级 |
|:---:|:----:|:---:|:-------:|
| [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | 由 Jeffallan 维护 Claude 配置库, 提供了一系列 Skills、功能脚本与集成示例, 旨在扩展 Claude 在不同场景下的能力边界. 项目核心目标是让开发者/使用者快速复用成熟的模板, 无需从零配置, 即可让 Claude 完成特定任务, 降低 Claude 定制化使用的门槛. | Claude Code | NA |
| [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | 涵盖 9 大领域的 Claude Code Skills 和 Plugin, 包含<br>1. 工程研发前后端全栈和 DevOps, RAG 架构师、CI/CD 构建器, 甚至还有能自我优化的自进化 Agent.<br>2. 市场增长: SEO、内容创作、转化率优化(CRO)和增长策略等等.<br>3. 高管智囊: 从战略规划、文化建设到模拟董事会会议都能参谋.<br>4. 其他辅助: 产品设计、项目管理、财务分析，甚至连最让人头疼的合规审查(医疗 MDR、GDPR、ISO)都有专门的插件. 参见 [出海去孵化器 @chuhaiqu 的帖子](https://x.com/chuhaiqu/status/2030941933418500562). | Claude Code | NA |
| [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | Claude Code 的即用配置. 一个全面的 AI 代理、自定义命令、设置、钩子、外部集成(MCP) 和项目模板，旨在提升您的开发工作流程. | Claude Code | NA |
| [ChrisWiles/claude-code-showcase](https://github.com/ChrisWiles/claude-code-showcase) | 深度配置和使用 Claude Code, 提供完整的开发配套环境. | Claude Code | NA |
| [stretchcloud/claude-code-unified-agents](https://github.com/stretchcloud/claude-code-unified-agents) | 一个全面的 Claude Code 子代理集合, 结合了多个社区仓库中的最佳功能. 该统一集合提供了 54 个智能体, 涵盖开发、基础设施、质量、AI/ML、商业、创意、元管理和专业领域. | Claude Code | NA |
| [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | Anthropic 黑客松冠军的 Claude Code 配置, 不仅仅是配置. 一个完整的系统: 技能、直觉、记忆优化、持续学习、安全扫描和以研究为先的开发. | Claude Code | NA |
| [wasabeef/claude-code-cookbook](https://github.com/wasabeef/claude-code-cookbook) | 一套集成的 Claude Code 环境, 通过 40+ 预设的命令, 8+ 智能体角色, 自动化 Hooks, 让 Claude Code 自动判断并执行常见并发任务, 比如代码修正, 测试执行, 文档更新等. | Claude Code | NA |
| [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | Claude Code 最全面的工具包, 包含 135 个代理, 35 个精选技能, 42 个命令, 121 个插件, 19 个钩子, 15 条规则, 7 个模板, 6 个 MCP 配置, 等等. | Claude Code | NA |
| [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | Claude-Code 最佳实践. 汇总了已验证过的最佳工作流程和相关的避坑经验, 以及一套 Skills, Agent, MCP 等相关配置. | Claude Code | NA |
| [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | 理念是"用 AI 组建公司", 不过当前实现中只是包含了众多 Agent 相关 Prompt. | Claude Code | NA |
| [feiskyer/claude-code-settings](https://github.com/feiskyer/claude-code-settings) | 精选的 Claude 代码设置、技能和子代理合集, 旨在提升开发流程. 该配置包括功能开发(基于规格的工作流程)、代码分析、GitHub 集成和知识管理的专业技能和子代理. | Claude Code | NA |


## 📊 工程化
-------

| 技能 | 描述 | 支持 | 推荐星级 |
|:---:|:----:|:---:|:-------:|
| [`superpowers`](https://github.com/obra/superpowers) | 一套完整的软件开发流程, 基于一套可组合的 Skills 和一些初步指令. | Claude Code<br>Cursor<br>Codex<br>OpenCode | []() |
| [planning-with-files](https://github.com/OthmanAdi/planning-with-files) | 用文件规划任务, 像 Manus 那样工作 | NA | NA |
| [](https://github.com/github/spec-kit) | 帮助你开始专业化开发的工具包, 让你专注于产品场景和可预期的结果, 而不是从零开始随意编写每一个部分. | NA | NA |
| [](https://github.com/Linfee/spec-kit-cn) | NA | NA | NA |
| [](https://github.com/Fission-AI/OpenSpec) | NA | NA | NA |


## 记忆
-------


| 技能 | 描述 | 支持 | 推荐星级 |
|:---:|:----:|:---:|:-------:|
| [AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace) | 记忆宫殿为人工智能代理提供了持久上下文和无缝的跨会话连续性. 它为 LLM 提供了持久、可搜索和可审计的历史上下文——所以你的代理在每次对话中都不会"从零开始", 通过统一的 MCP(模型上下文协议)接口, Memory Palace 为 Codex、Claude Code、Gemini CLI 和 OpenCode 提供了集成路径, 并为光标和反重力提供了文档说明. 目前已验证的范围和已知边界已在 docs/skills/SKILLS_QUICKSTART_EN.md 文献中记录. |
| [okooo5km/memory-mcp-server](https://github.com/okooo5km/memory-mcp-server) |
| [coleam00/mcp-mem0](https://github.com/coleam00/mcp-mem0) |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) |

## Token
-------


| 技能 | 描述 | 支持 | 安装 |
|:---:|:----:|:---:|:----:|
| [zenobi-us/opencode-skillful](https://github.com/zenobi-us/opencode-skillful) | 提供懒惰加载的技能发现和注入.<br>AI 有时会因为加载了太多的"系统提示词"或"操作指南"而浪费大量初始 Token.<br>核心功能是将复杂的 Prompt 碎片化为"技能"<br>默认情况下上下文是空的, 只有当 AI 识别到任务(比如"现在需要进行 Docker 部署"), 时, 它才会动态"注入"相关的专业知识和规则. 这能节省约 20%-40% 的静态上下文空间.<br>1. 在对话中, 智能体使用 skill_find 来发现技能.<br>2. 使用 skill_use "skill_name"<br>3. 代理可以用来 skill_resource skill_relative/resource/path 读取参考资料. | OpenCode | NA |
| [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | RTK 会在命令输出到达你的 LLM 上下文之前过滤和压缩它们. 单一 Rust 二进制, 零依赖, 开销 <10 ms. | NA | NA |

## 通知
-------

| 技能 | 描述 | 支持 | 安装 |
|:---:|:----:|:---:|:----:|
| [opencode-notifier](https://github.com/mohak34/opencode-notifier)
| [opencode-terminal-notifier](https://github.com/mathew-cf/opencode-terminal-notifier) |
| [opencode-smart-voice-notify](https://github.com/MasuRii/opencode-smart-voice-notify)

## 状态栏
-------


| 技能 | 描述 | 支持 | 安装 |
|:---:|:----:|:---:|:----:|
| ccstatusline |





# 参考
-------

[oh-my-opencode 和 superpowers](https://linux.do/t/topic/1445132/18)
[opencode配置文档](https://linux.do/t/topic/1415352)
[对oh-my-opencode的简单修复，节约5~10倍的API消耗。](https://linux.do/t/topic/1658684)
[`[Question]`: How to get the status of background agents? #917](https://github.com/code-yeongyu/oh-my-openagent/issues/917)


[Cranot/claude-code-guide](https://github.com/Cranot/claude-code-guide), 完整 Claude 代码 CLI 指南. 实时指南: 每两天自动更新一次, 来源于官方文档、GitHub 发布和 Anthropic 更新日志.

[FlorianBruniaux/claude-code-ultimate-guide](https://github.com/FlorianBruniaux/claude-code-ultimate-guide), 本指南教你以不同的角度看待人工智能辅助开发.