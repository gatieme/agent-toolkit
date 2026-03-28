[Harness Engineering 深度解析: AI Agent 时代的工程范式革命](https://zhuanlan.zhihu.com/p/2014014859164026634)


| 支柱 | 概述 | 描述 |
|:---:|:----:|:----:|
| 结构化执行(Structured Execution) | 规格驱动工程, 通过 Spec 流程驱动的"规范 + 执行 + 验证" 的三层规范体系, 摸清 AI 工作的真是能力边界, 约束 Agent 按照既定规范执行, 结合 Rlaph-Loop 实现 Agent 按照 Spec 约定的规范无人值守(长时)运行. 致力于通过项目的规范化流程, 约束 AGENT 执行, 防止 AGENT 跑偏. |
| Agent 专业化(Agent Specialization) | 通过专业的 Agent 角色(项目经理, 架构师, 开发, 测试等)组合成 Agent Teams(公司), 通过 subAgents Orchestrator 编排 Workflow 协调各专家各司其职. 通过 multiAgent Parallel 组合多个 Coding Agent 的能力, 取长补短, 从而可以完成整个完整项目的设计与开发. |
| 持久化记忆(Persistent Memory) | 进度持久化在文件系统上, 而非上下文窗口中. 每次新 Agent 会话从零开始, 通过文件系统制品重建上下文. |
| 上下文架构(Context Architecture) | Agent 应当恰好获得当前任务所需的上下文——不多不少. 每个团队都独立发现, 将所有指令塞进一个文件无法扩展, 解决方案是分层上下文与渐进式披露. |


# 📊 1 结构化执行(Structured Execution)
-------

规格驱动工程, 通过 Spec 流程驱动的"规范 + 执行 + 验证" 的三层规范体系, 摸清 AI 工作的真是能力边界, 约束 Agent 按照既定规范执行.
1. 通过 Spec 驱动约束 Agent 按照既定规范执行
2. 通过 Rlaph-Loop 实现 Agent 长时无人值守运行.

## 1.1 Specification-Driven
-------


[微信公众号--牛马也卷 AI--企业存量系统的"考古"指南: OpenSpec + Superpowers 实战](https://mp.weixin.qq.com/s/Gg3fMo2_iKdl28j3vhy5eQ) 介绍了一种 OpenSpec + Superpowers 系统工作的实战技巧, 用 OpenSpec + Superpowers 这套组合, 带你系统化地梳理存量系统——让 AI 成为你的"分析助手", 而不是"万能钥匙". 背景是只用 Superpowers: 容易跑偏, 只用 OpenSpec: 规范落地难. 两者协同工作实现目标对齐 + 系统执行, ① 先对齐目标, OpenSpec 帮你定义"要分析什么";  ② 再系统执行——Superpowers 按任务清单执行不遗漏; ③ 任务粒度可控——每个任务 2-5 分钟, 不会追飞; ④ 可追溯 —— 规范文档记录决策过程.

[OpenCode 配置 OpenSpec + Superpowers + Oh-My-OpenCode 指南](https://github.com/wentietie/tools-config/blob/main/OpenCode-%E9%85%8D%E7%BD%AE%E6%8C%87%E5%8D%97-OpenSpec-Superpowers.md)


| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [`superpowers`](https://github.com/obra/superpowers) | 一套完整的软件开发流程, 基于一套可组合的 Skills 和一些初步指令. | Claude Code<br>Cursor<br>Codex<br>OpenCode | ⭐⭐⭐⭐ | 119,869 |
| [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | 用文件规划任务, 像 Manus 那样工作. | Claude Code<br>Cursor<br>Codex<br>OpenCode | ⭐⭐⭐ | 17,511 |
| [github/spec-kit](https://github.com/github/spec-kit) | 帮助你开始专业化开发的工具包, 让你专注于产品场景和可预期的结果, 而不是从零开始随意编写每一个部分. | Claude Code<br>Cursor<br>Codex<br>OpenCode | ⭐⭐⭐⭐ | 83,109 |
| [Linfee/spec-kit-cn](https://github.com/Linfee/spec-kit) | Spec Kit 的非官方中文复刻版本,对应原版 v0.1.13. 命令使用 `specify-cn` 而非 `specify` | Claude Code<br>Cursor<br>Codex<br>OpenCode | ⭐⭐⭐⭐ |
| [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | 最受喜爱的规范框架,灵活而非僵化,支持 20+ AI 代理. 哲学: 流动而非刚性, 迭代而非瀑布, 简单而非复杂, 为从现有项目构建而不仅仅是新建项目构建, 可从个人项目扩展到企业级. | Claude Code<br>Cursor<br>Codex<br>OpenCode | ⭐⭐⭐ | 35,059 |
| [claudeforge/Forge](https://github.com/claudeforge/Forge) | Claude Code 的规范驱动人工智能开发引擎, FORGE 将 Claude Code 转变为一个强大的迭代开发系统, 该系统通过正式规范、结构化规划和完成标准验证, 自主处理复杂任务. | Claude Code | ⭐ | 11 |
| [claude-code-bmad-skills](https://github.com/aj-geddes/claude-code-bmad-skills) | [BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) 的 Claude Code 插件, [BMAD-METHOD(Breakthrough Method of Agile AI-Driven Development)](https://github.com/ljxpython/bmad-method-tutorial) 突破性的敏捷 AI 驱动开发方法, 是一个内置了完整敏捷开发流程的智能体系统, BMAD Method for Claude Code skills, 则不仅仅是一套 Skills 集, 它是一套将敏捷开发方法论(Agile Methodology)与AI原生能力深度融合的工程框架. 它将 Claude Code 从一个"更聪明的 Agent" 转变为一支具备 9 种专业角色、15种标准工作流的"全栈敏捷开发团队". 参见 [Documentation Site, with examples](https://aj-geddes.github.io/claude-code-bmad-skills), [敏捷开发「BMAD」也推出了Agent Skills, CC直接用｜ 斩获2.6万star](https://cloud.tencent.com/developer/news/3408673) | Claude Code | ⭐ | 355 |
| [shotgun-sh/shotgun](https://github.com/shotgun-sh/shotgun) | Spec-Driven Development, 核心解决 AI 编码代理在大型开发任务中上下文丢失、偏离需求、重复造轮子、生成超大 PR 难以评审的核心痛点. 给 AI 编码代理做 "开发规划师", 先让 Shotgun 吃透你的整个代码库, 生成结构化、分阶段的开发规范/步骤, 再让 AI 代理按规范分步开发, 输出可评审、可落地的小 PR, 而非无章法的大段代码. | Claude Code | ⭐ | 705 |
| [danielmiessler/Personal_AI_Infrastructure](https://github.com/danielmiessler/Personal_AI_Infrastructure) | PAI 是一个通过功能齐全的智能人工智能平台来理解、表达并实现其主体目标的系统. 基于 Claude Code 构建, 定位为「增强人类能力的智能体平台」, 区别于传统无记忆的聊天机器人和仅具备工具调用能力的智能体平台, 实现了以用户为核心的目标导向、持续学习型 AI 交互.<br>1. 定义了 AGENT 的三层进化: Chatbots(聊天机器人) -> Agentic Platforms(智能平台) -> Personal_AI_Infrastructure(PAI, 个人人工智能基础设施).<br>2. PAI 的核心竞争力在于以用户为中心的设计, 体现出三大核心差异化因素: 目标导向(Goal Orientation), 追求最佳输出(Pursuit of Optimal Output), 持续学习(Continuous Learning). 以及 16 条设计原则(PAI Principles).<br>3. PAI 提供独立可安装的功能包(Available Packs), 无需安装完整 PAI 系统, 可单独部署, 每个包由 AI 自动安装(5 阶段向导: 系统分析→用户提问→备份→安装→验证), 覆盖 12 类核心能力. | Claude Code | ⭐⭐⭐ | 10,599 |
| [nizos/tdd-guard](https://github.com/nizos/tdd-guard) | 一个为 Claude Code 设计的自动化测试驱动开发(TDD)强制执行工具. 确保 Claude Code 遵循 TDD 原则, 当代理尝试跳过测试或过度实现时, TDD Guard 会阻止操作并解释正确的做法. 核心特性包括测试优先强制执行、最小实现、 lint 集成、多语言支持、可自定义规则、灵活验证和会话控制. 支持 JavaScript/TypeScript(Vitest、Jest、Storybook)、Python(pytest)、PHP(PHPUnit)、Go 和 Rust 等多种语言和测试框架. 通过 Claude Code 钩子系统实现. | Claude Code | ⭐ | 1,945 |
| [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done) | 轻量级且强大的元提示、上下文工程和规格驱动开发系统, 解决上下文腐烂问题, 为多个 AI 编码代理提供可靠的开发流程. 核心功能包括: 上下文工程管理、XML 提示格式、多智能体编排、原子 Git 提交、模块化设计和波次执行. 支持完整的开发工作流: 初始化项目 → 讨论阶段 → 计划阶段 → 执行阶段 → 验证工作 → 发布. 这个项目砍掉了那些繁琐的开发流程, 核心只解决一件事: 防止上下文污染, 也就是不让 AI 被过长的聊天记录拖垮.<br>1. 每次任务重置上下文: 它会把你的大需求拆解成一个个细分任务. 执行每个小任务时, 都会分配一个全新的、干净的上下文窗口. 这样 Claude 就不会被之前的历史对话干扰, 始终保持清醒.<br>2. 主程序只负责分派任务: 采用多 Agent 架构. 主程序自己不处理复杂的逻辑, 而是生成专门的虚拟助手分别去做调研、规划、执行和测试. 跑完直接汇总结果, 保证响应速度. <br>3. 做一步存一步的自动存档: 每个小任务完成后, 会自动生成一个独立的 Git 提交, 就相当于打游戏时的分步自动存档. 好处是如果哪一步跑崩了, 能直接定位到具体的错误步骤, 一键回滚. | Claude Code<br>OpenCode<br>Gemini CLI<br>Codex<br>Copilot<br>Cursor<br>Antigravity | ⭐⭐⭐ | 43,744 |
| [ZhangHanDong/agent-spec](https://github.com/ZhangHanDong/agent-spec) | 智能体规范定义和管理工具, 提供标准化的智能体配置和编排能力 | 多 Agent 支持 | ⭐ | 78 |
| [tintinweb/pi-supervisor](https://github.com/tintinweb/pi-supervisor) | Pi-Agent 扩展, 监控编码代理并引导其朝向定义的目标前进, 通过观察对话、注入指导消息和信号完成状态来实现监督功能 | Pi | ⭐ | 28 |


## 1.2 Ralph-Loop
-------

Ralph 是一个基于 Geoffrey Huntley 提出的 Ralph 循环模式设计的 AI 编程工具, 旨在解决从 PRD 到可直接上线代码的自动化流程问题. 它通过 Bash 循环脚本不断启动新的 AI 实例(Amp 或 Claude Code), 逐条处理 PRD 中的任务, 直到所有事项完成为止. 核心设计每轮迭代使用全新上下文窗口, 通过外部存储(Git 历史、progress.txt、prd.json)来获取状态, 避免了上下文累积的限制.

[微信公众号--被AI榨干的--AI 编程不需要 10x 工程师, 需要 10x 产品经理](https://mp.weixin.qq.com/s/Q2O1j9NRQStCi7HAbv-kRQ) 则**建议用户应该作为 PM, 通过 Harness Engineering 和 Ralph Loop 来规范化 AI 的行为**, Harness Engineering 5 条原则来约束 AI 行为: 所有决策推进代码仓库、问"缺什么能力"而不是"为什么出错"、用代码强制约束、构建反馈闭环、写地图不写说明书. 借助 7 份文档来规划任务 story.md, user-journey.md, uiux-review.md, visual-system.md, architecture.md, design-assets.md, test-plan.md 来规划和工作, Ralph Loop 通过约定的 7 条迭代规则来保障 AI 按照预期行为工作.

[Ralph Wiggum as a "software engineer"](https://ghuntley.com/ralph)

[snwfdhmp/awesome-ralph](https://github.com/snwfdhmp/awesome-ralph), 关于 Ralph (Ralph Wiggum) 技术的精选资源列表, 包括官方资源、实践指南、实现、教程、文章、视频和社区资源等.

[如何让 Claude Code 长时间工作](https://datawhalechina.github.io/easy-vibe/zh-cn/stage-3/core-skills/long-running-tasks/)

立党大佬的插件 [lidangzzz/goal-driven](https://github.com/lidangzzz/goal-driven) 是 Ralph 的最简(提示词)实现, **通过一套标准的目标驱动(Goal-Driven)的提示词, 组合 subAgent 来保持 Ralph 运行**. 其要求 Ralph ① 目标(Goal): 必须以 goal 作为 alignment 的唯一目标, ② 成功标准(Criteria): 必须设计一个以大量 test 作为唯一评判标准的 criteria, ③ 主智能体(Master Agent)和子智能体(Subagent): 必须设置一个 master agent 来 supervise 你的真正执行任务的 subagent, 时刻确保向着 goal 方向推进. 核心理念非常简单: 当 Goal-Driven 流程启动时, 主智能体创建一个子智能体, 并指示它持续致力于解决问题并达成目标.<br>主智能体定期检查子智能体是否活跃. 如果子智能体变得不活跃、声称完成或进入空闲状态, 主智能体必须根据标准评估当前结果. 如果结果未能满足标准, 它会命令子智能体继续工作, 重复这个循环直到标准被满足. 一旦子智能体的输出满足标准, 系统停止并宣布成功完成.

anthropics 官方的 [claude-plugins-official/ralph-loop](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/ralph-loop) 插件是 Ralph 的最简(脚本/插件)实现, 通过 [`/ralph-loop/ralph-loop` 的 Claude Code commands](https://github.com/anthropics/claude-plugins-official/blob/main/plugins/ralph-loop/commands/ralph-loop.md)来主导 Ralph 运行, 其**核心机制是 [Stop Hook](https://github.com/anthropics/claude-plugins-official/blob/main/plugins/ralph-loop/hooks). 当 Claude 想要退出时, Stop Hook 会拦截这个退出信号. 然后系统会检查: 输出了特定的完成标记吗? 如果没有找到完成标记, 就重新注入原始 prompt, 开始下一轮迭代. 如果找到了完成标记, 才允许 Claude 退出**. 但是其每次迭代并不是一个干净的上下文, 只是把原始 prompt 和迭代计数重新喂给 Claude, 因此可能会浪费 Token.

[微信公众号--技术极简主义--从 PRD 到代码: Ralph 驱动的自治 AI 智能体执行循环](https://mp.weixin.qq.com/s/iVfaAJx4DuFuzihf0TouHA) 通过一次对 [snarktank/ralph](https://github.com/snarktank/ralph) 的工程实践案例, 这个工具提供了一个 [ralph skills](https://github.com/snarktank/ralph/blob/main/skills/ralph/SKILL.md), 可以**将 prd.md 转换为 Ralph 能理解的 prd.json. 最后 [ralph.sh](https://github.com/snarktank/ralph/blob/main/ralph.sh) 会按照 prd.json 中制定的计划和任务来执行: 创建功能分支 -> 选择下一个任务 -=> 专注于单个任务的实现 -> 提交代码 -> 更新任务状态 -> 记录学习内容 -> 循环或退出**. 作者提供了一个[交互式的流程图](https://snarktank.github.io/ralph) 来了解 Ralph 的执行流. 这个工具并不是 Cluade 内置插件, 而是通过 [ralph.sh](https://github.com/snarktank/ralph/blob/main/ralph.sh) 启动 claude code 来运行, 每次迭代都是一个干净的上下文, 工作进度和状态通过文件系统传递, 而非对话上下文. 这样可以有效防止上下文窗口膨胀, 任务可重启, 方便调试. 脚本中缺乏 Orchestrator, 因此建议每次迭代的任务尽可能单一, 更适合串行任务. 当然可以在 Claude Code 中配置 Orchestrator 来组合使用.

[微信公众号--CIT云原生--手搓了个 long-running-skill 和 Agent 开源教程网站](https://mp.weixin.qq.com/s/MKYwEIuWEJiKCbIaHhGiAw)


| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [lidangzzz/goal-driven](https://github.com/lidangzzz/goal-driven) | 立党大佬的插件, 通过 Prompt 来实现目标驱动的多智能体系统, 通过主代理+子代理架构实现超过300小时的复杂问题解决能力. 采用循环验证机制: 主代理创建子代理执行任务, 每5分钟检查进度, 根据预定义标准评估结果, 未达标则继续循环直至成功. 适用于编译器设计、数学定理证明、数据库架构等高度复杂、逻辑抽象的系统级任务. 已实践项目包括 C++ 实现的 TypeScript 编译器、Rust 实现的 SQLite 等. | Claude Code<br>Codex<br>OpenClaw | ⭐ | 583 |
| [anthropics/claude-plugins-official/ralph-loop](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/ralph-loop) | 官方 Ralph Wiggum 技术实现, 通过 Stop hook 创建自引用反馈循环, 实现 Claude Code 的迭代开发. 核心功能: 使用 `/ralph-loop` 命令启动循环, 自动拦截退出尝试并重复执行相同提示, 直到完成任务. 支持设置最大迭代次数和完成承诺短语. 适用于有明确成功标准的任务、需要迭代改进的任务(如测试通过)、可以离开的新项目. | Claude Code | ⭐⭐⭐ | 15,092 |
| [snarktank/ralph](https://github.com/snarktank/ralph) | 基于 Geoffrey Huntley 的 Ralph 模式实现自主 AI 代理循环系统, 运行 AI 编码工具(Amp 或 Claude Code)重复执行直到所有 PRD 项目完成. 提供 [snarktank/ralph/prd](https://skills.sh/snarktank/ralph/prd) 和 [snarktank/ralph/ralph](https://skills.sh/snarktank/ralph/ralph) 两个 skills 和一套 ralph 脚本 [ralph.sh](https://github.com/snarktank/ralph/blob/main/ralph.sh). 每次迭代都是一个具有干净上下文的新实例, 记忆通过 git 历史、progress.txt 和 prd.json 持久化. 核心功能包括: 支持 Amp 和 Claude Code、PRD 生成和转换、自动分支创建、质量检查、提交管理和进度跟踪. | Amp CLI<br>Claude Code | ⭐⭐⭐ | 13,918 |
| [frankbria/ralph-claude-code](https://github.com/frankbria/ralph-claude-code) | Ralph Loop 的 Claude Code 增强实现, 提供 ralph 命令来实现迭代开发能力, 后端对接 Claude Code, 在官方插件的基础上增加了更多安全机制.<br>1. 双重退出条件. 官方 Ralph 只需要检查完成标记, 但增强版需要同时满足完成标记和显式 EXIT_SIGNAL 才会真正停止. 这意味着即使 Claude 输出了完成标记, 如果它没有明确表示要退出, 循环还会继续, 可以进一步验证和改进.<br>2. 速率限制功能. 默认设置为 100 次/小时, 防止因为某种 bug 导致无限循环时, API 账单爆炸. 你可以根据需要调整这个限制. <br>3. 智能熔断器. 如果系统连续 5 次检测到完成标记, 会强制退出. 这是为了防止某种边缘情况导致循环无法正常结束. <br>5. 实时仪表盘. 增强版提供了一个命令行界面, 可以显示当前迭代次数、任务进度、预估成本等信息, 让你随时掌握状态.<br>只是每次并不重置上下文, 因此可能会造成累积上下文, 爆掉. | Claude Code | ⭐⭐ | 8,234 |
| [subsy/ralph-tui](https://github.com/subsy/ralph-tui) | Ralph 循环的 TUI 界面实现, 提供可视化的循环管理和监控功能. | 多平台 | ⭐ | 2,181 |
| [michaelshimeles/ralphy](https://github.com/michaelshimeles/ralphy) | 自主 AI 编码循环系统, 运行 AI 代理直到任务完成. 支持单一任务和任务列表两种模式, 多种 AI 引擎, 并行执行, 浏览器自动化等功能. 核心特点包括: 多引擎支持(Claude Code、OpenCode、Cursor、Codex、Qwen-Code、Factory Droid、GitHub Copilot、Gemini CLI)、并行执行(git worktrees 或 sandbox 模式)、多种任务源(Markdown、YAML、JSON、GitHub Issues)、项目配置和规则管理、webhook 通知等. | 多 Agent 支持 | ⭐ | 2,674 |
| [Th0rgal/open-ralph-wiggum](https://github.com/Th0rgal/open-ralph-wiggum) | 自主代理循环工具, 支持 Claude Code、Codex、Copilot CLI 和 OpenCode. 基于 Geoffrey Huntley 的 Ralph Wiggum 技术, 实现自主代理循环, 让 AI 编码代理重复接收相同的提示直到完成任务. 核心特点包括: 多代理支持、自我纠正循环、自主执行、任务跟踪、实时监控、中间循环提示注入等. 支持 Tasks Mode 进行结构化任务管理, 以及代理轮换功能. 技术实现基于 Bun 运行时, 状态存储在 `.ralph/` 目录中, 提供完整的 CLI 命令集和任务管理功能. | 多 Agent 支持 | ⭐ | 1,357 |
| [hamelsmu/claude-review-loop](https://github.com/hamelsmu/claude-review-loop) | 一个Claude Code插件, 可将自动代码审查循环添加到您的工作流程中. 使用 `/review-loop` 时, 该插件会创建一个两阶段生命周期.<br>任务阶段: 你描述一项任务, Claude 负责执行<br>2. 审查阶段: 当 Claude 完成后, 会自动运行 Codex 进行独立代码审查, 然后要求 Claude 处理反馈意见<br>结果: 在您接受更改之前, 每项任务都会得到独立的二次审核意见. | Claude Code/Codex | ⭐ | 620 |
| [AnandChowdhary/continuous-claude](https://github.com/AnandChowdhary/continuous-claude) | 自动化工作流, 在连续循环中编排 Claude Code, 自主创建 PR、等待检查并合并, 使多步骤项目在你睡觉时完成. 核心功能包括持续循环执行、PR 生命周期自动化、上下文连续性、并行执行支持等. | Claude Code | ⭐ | 1,274 |
| [mikeyobrien/ralph-orchestrator](https://github.com/mikeyobrien/ralph-orchestrator) | Ralph Orchestrator 是一款轻量级、开源的 AI 工作流编排工具, 核心定位是「为提示词工程和 AI 任务协作提供结构化编排能力」, 主打极简部署、无代码/低代码操作、多 AI 模型适配. | 多 Agent 支持 | ⭐ | 2,397 |


# 💻 2 Agent 专业化(Agent Specialization)
-------


| 领域 | 描述 |
|:---:|:----:|
| Agent Teams | 理念是"用 AI 组建公司", 专注于特定领域、拥有受限工具的 Agent 优于拥有全部权限的通用 Agent. 通过配置多种 Agent 角色来辅助工作. |
| Agent Spec Driver | 规格驱动工程, 通过 Spec 流程驱动的"规范 + 执行 + 验证" 的三层规范体系, 摸清 AI 工作的真是能力边界, 约束 Agent 按照既定规范执行, 结合 Rlaph-Loop 实现 Agent 按照 Spec 约定的规范无人值守(长时)运行. |
| (sub)Agent Team Orchestrator | 构建一套智能体元编程编排器, 对于复杂的任务, 通过 (sub)Agent Team 自适应进行任务分解, 派发, 执行和调度的工作流控制. |
| (multi)Agent Parallel Workflow | Agent Parallel Workflow 致力于组合多个 Agent 协同工作, 通过 Parallel Workflow 完成多 Agent 并行编排和管理. 最终组合多个 Agent 协同工作, 保障复杂任务的高效完成. |

> 一句话描述
>
> Agent Spec Driver 致力于通过项目的规范化流程, 约束 AGENT 执行, 防止 AGENT 跑偏.
>
> Agent Team Orchestrator 是通过单个 Coding Agent 通过配置多个 subAgent 组成 Agent Team, 从而能完成复杂工作的开发与验证.
>
> Agent Parallel Orchestration 则组合多个 Coding Agent 的能力, 并行工作, 从而可以完成整个完整项目的设计与开发.


## 2.1 Agent Teams
-------


| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | 理念是"用 AI 组建公司", 不过当前实现中只是包含了众多 Agent 相关 Prompt. 一份精选的 Claude 技能、资源和工具列表, 用于定制 Claude AI 工作流程. | Claude Code | ⭐⭐⭐⭐ | 64,682 |
| [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) 的中文版本, AI 智能体专家团队(中文版)—80+ 个专业 AI 智能体人设, 覆盖开发、设计、营销、测试、运维等领域, 含小红书/抖音/微信等中国平台原创智能体. | Claude Code | ⭐ | 2,916 |
| [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | 核心提供 148 个开箱即用的生产级 AI Agent 模板(基于 SOUL.md 配置文件), 覆盖 23 个业务 / 生活领域, 同时配套完整的部署、使用、贡献体系, 是 OpenClaw 框架的核心生态资源库, 整体定位为无代码 / 低代码 AI Agent 落地的一站式模板中心. 23 个分类覆盖个人、团队、企业、技术、业务全场景, 其中Productivity(生产力)、Development(开发)、Marketing(营销)、DevOps(运维)为核心高频分类, 同时包含 Moltbook、Supply Chain、Compliance、Voice、Customer Success5 个新增分类, 贴合最新的 AI Agent 落地需求. | OpenClaw | ⭐ | 2,101 |
| [Gentleman-Programming/agent-teams-lite](https://github.com/Gentleman-Programming/agent-teams-lite) | 基于 AI 子代理编排的结构化功能开发工具, 核心解决 AI 编码助手在复杂功能开发中面临的上下文过载、无结构化、无审核节点、无持久化记忆等问题, 采用轻量协调器 + 专业化子代理的架构, 零依赖、纯 Markdown 编写, 可适配各类 AI 编码助手, 是介于基础子代理模式和全量 Agent Teams 运行时之间的轻量化解决方(Level 2). 可以使用 [gentle-ai](https://github.com/Gentleman-Programming/gentle-ai) TUI 工具安装和配置 agent-teams-lite 到 Claude Code、OpenCode、Cursor、Copilot、Gemini 等 Agent. | Claude Code<br>OpenCode<br>Cursor<br>Copilot<br>Gemini | ⭐ | 1,078 |
| [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | 革命性的 AI 智能体群体智能框架, 实现"单智能体→智能体集群"的进化. 通过一行命令让AI智能体自主组建团队、分配任务、实时协调并交付结果. 支持任意 CLI 智能体(Claude Code、Codex、OpenClaw 等), 采用 Git 工作树隔离机制, 提供任务依赖管理、智能体间消息通信、实时监控面板等功能. 核心特色包括: 智能体自组织、工作空间隔离、任务跟踪依赖、智能体间消息、监控仪表板、团队模板等. 适用于自动化 ML 研究、群体软件工程、AI 对冲基金等多智能体协作场景. | Claude Code<br>Codex<br>OpenClaw | ⭐ | 3,869 |
| [ClawTeam-OpenClaw](https://github.com/win4r/ClawTeam-OpenClaw) | HKUDS/ClawTeam 的分支, 默认集成 OpenClaw, 支持每代理会话隔离、执行批准自动配置和生产级生成后端, 适用于多智能体集群协调、自主ML研究、软件工程和投资分析等场景 | OpenClaw<br>Claude Code<br>Codex<br>nanobot<br>Cursor | ⭐ | 848 |
| [VoltAgent/awesome-codex-subagents](https://github.com/VoltAgent/awesome-codex-subagents) | 一个全面的 Codex 子代理集合, 包含 136+ 个专门针对不同开发任务的子代理, 分为 10 个类别. 每个子代理使用 Codex 原生的 .toml 格式定义, 包含智能模型路由和沙盒模式设置. 覆盖核心开发、语言专家、基础设施、质量与安全、数据与 AI、开发者体验、专业领域、业务与产品、元与编排、研究与分析等多个领域. 支持全局和项目特定的子代理安装, 通过明确委托方式使用. | Codex | ⭐ | 2,970 |


## 2.2 (sub)Agent Team Orchestrator
-------

智能体编排器(Agent Team Orchestrator)通过在单个 Coding Agent 中构建 (sub)Agent Team, 对 (sub)Agent Team 进行协调调度, 任务自适应划分, subAgent 并行和管理, 实现任务规划,  分配和工作流控制, 实现元编程调度框架. 具体包括:
1. (sub)多智能体并行管理: 生成并管理多个并行运行的 AI 编码代理, 为每个代理分配独立的工作环境;
2. 自主任务处理: 代理能够自主修复 CI 故障、处理代码审查评论、自动创建和管理 PR;
3. 监控与协调: 提供仪表盘式监控界面, 协调多个代理之间的工作;
4. 工作流优化: 将复杂任务分解为可管理的子任务, 优化工作流程;
5. 多 Agent 支持: 兼容多种 AI 模型, 根据任务类型选择合适的模型.

### 2.2.1 oh-my-zsh 系列
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [oh-my-opencode](https://github.com/code-yeongyu/oh-my-openagent) | 开源的 AI 编码代理编排框架, 提供丰富的技能和工具集成 | OpenCode | ⭐⭐⭐ | 44,319 |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | oh-my-opencode 的 [Claude Code 移植版](https://github.com/Yeachan-Heo/oh-my-claudecode/commit/cd98f12fac986bce4b7246aac3326ed107574fb3)), 之前叫 [oh-my-claude-sisyphus](https://github.com/Yeachan-Heo/oh-my-claudecode/commit/3a02feb187f1185fc51379a84ad001b114ac12af), v3.0.0 之后改名. 官网 [oh-my-claudecode-website](https://yeachan-heo.github.io/oh-my-claudecode-website) | Claude Code | ⭐⭐⭐ | 14,409 |
| [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | oh-my-opencode 的 codex 移植版 | Codex | ⭐ | 2,747 |
| [MeroZemory/oh-my-droid](https://github.com/MeroZemory/oh-my-droid) | Factory Droid 的多智能体编排器, 零学习曲线. 基于 oh-my-claudecode 实现. | Factory Droid | ⭐ | 11 |
| [woosikkim/oh-my-claudecode-slim](https://github.com/woosikkim/oh-my-claudecode-slim) | oh-my-claudecode 的精简版. | Claude Code | ⭐ | 1 |
| [alvinunreal/oh-my-opencode-slim](https://github.com/alvinunreal/oh-my-opencode-slim) | oh-my-opencode 的精简版. | OpenCode | ⭐ | 2,455 |
| [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | 终端 AI 编码代理, 基于 badlogic/pi-mono, 提供完整的开发工具链. | Pi | ⭐ | 2,427 |

### 2.2.2 Agent 调度与编排
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [wshobson/agents](https://github.com/wshobson/agents) | 一个全面的 AI 开发部件, 包含了 112 个专业 AI 智能体、16 个智能体工作流编排器、146 个 Skills 和 79 个开发工具, 组织成 72 个专注于 Claude Code 的插件. | Claude Code | ⭐⭐⭐ | 32,438 |
| [SuperClaude](https://github.com/SuperClaude-Org/SuperClaude_Framework) | 专为 Claude Code 打造的元编程配置框架, 核心作用是通过丰富的工具集和配置体系, 将 Claude Code 从基础的代码生成工具升级为结构化、专业化的智能开发平台. 包含了 22 个斜杠命令(/sc:), 14 个领域智能代理(Agents), 6 种行为模式, 官网 [superclaude](https://superclaude.netlify.app) | Claude Code | ⭐⭐⭐ | 22,000 |
| [sangrokjung/claude-forge](https://github.com/sangrokjung/claude-forge) | 开源的 Claude Code 开发环境, 提供 11 个专用智能体、40 个斜杠命令、15 个技能工作流程和 15 个自动化钩子. 它被形容为是 Claude Code 的 oh-my-zsh, 它将 Claude 代码从一个基础的 CLI 转变为一个功能齐全的开发环境. 一次安装就能提供代理、命令、技能、钩子和 9 个规则文件——全部预先布线, 随时可用. | Claude Code | ⭐ | 612 |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | Ruflo(Claude-Flow) 是一个全面的人工智能代理编排框架, 将 Claude Code 转变为强大的多代理开发平台. 它使团队能够部署、协调和优化专业的人工智能代理, 协同处理复杂的软件工程任务. 支持多个 Agent 并行执行, 同时提供实时监控面板. | Claude Code | ⭐⭐⭐ | 27,722 |
| [ComposioHQ/agent-orchestrator](https://github.com/ComposioHQ/agent-orchestrator) | 生成并行的 AI 编码代理, 每个代理在自己的 git 工作树中. 代理自主修复 CI 故障, 处理审核评论, 并开放 PR——你只需在一个仪表盘上进行监督.<br>Agent Orchestrator 管理着一系列并行运行在代码库上的 AI 编码代理. 每个代理都有自己的 git 工作树、分支和 PR. 当 CI 失败时, 代理会修复它. 当审核员留下评论时, 代理人会进行回应. 只有当需要人为判断时, 你才会被拉进来. | 多 Agent 支持 | ⭐⭐ | 5,544 |
| [openai/symphony](https://github.com/openai/symphony) | Symphony 将项目工作转化为独立、自主的实现运行, 使团队能够管理工作, 而无需监督编码代理. | Codex | ⭐⭐⭐ | 14,163 |
| [wozhenbang2004/AgentNexus](https://github.com/wozhenbang2004/AgentNexus) | AgentNexus 不仅仅是一个 AI 应用框架, 它是一个功能完备的智能体(Agent)基础设施, 专为解决企业在生产环境中落地复杂AI工作流的核心挑战而设计. 摒弃了硬编码的 Agent 逻辑, 通过将模型、工具(MCP)、RAG知识库、提示词等所有核心组件进行数据库持久化, 并通过 API 驱动的责任链模式在运行时动态构建 Agent, 从而赋予系统强大的动态编排、自主协作与全生命周期管理能力. | 多 Agent 支持 | ⭐ | 112 |
| [cft0808/edict](https://github.com/cft0808/edict) | 三省六部(Edict), 用 1300 年前的帝国制度, 重新设计了 AI 多 Agent 协作架构. 12 个 AI Agent(11 个业务角色 + 1 个兼容角色)组成三省六部: 太子分拣、中书省规划、门下省审核封驳、尚书省派发、六部+吏部并行执行. 比 CrewAI 多一层制度性审核, 比 AutoGen 多一个实时看板. | 多 Agent 支持 | ⭐⭐⭐ | 13,307 |
| [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | 完整的 AI 编码工作流系统, 提供经过实战验证的工作流模式、自我纠正记忆、并行工作树、结束仪式和 80/20 AI 编码比例, 支持 Claude Code、Cursor 和 32+ 个其他代理 | 多 Agent 支持 | ⭐ | 1,465 |
| [samibs/skillfoundry](https://github.com/samibs/skillfoundry) | AI 工程框架, 提供质量门控、持久记忆和多平台支持, 适用于 Claude Code、Cursor、Copilot、Codex 和 Gemini | 多 Agent 支持 | ⭐ | 6 |
| [agent-sh/agentsys](https://github.com/agent-sh/agentsys) | AI 编码自动化系统, 提供 15 个插件、35 个智能体和 32 个技能, 支持 Claude Code、OpenCode、Codex、Cursor 和 Kiro 等多种编码工具 | 多 Agent 支持 | ⭐ | 662 |
| [claudeforge/orchestrator](https://github.com/claudeforge/orchestrator) | 为 Claude Code 设计的自主开发系统, 提供自动化开发流程和工作流管理. | Claude Code | ⭐ | 37 |
| [shinpr/claude-code-workflows](https://github.com/shinpr/claude-code-workflows) | 为 Claude Code 设计的生产就绪开发工作流, 由专门的 AI 智能体提供支持, 涵盖代码质量、开发工作流和提示工程等多个方面 | Claude Code | ⭐ | 253 |
| [HazAT/pi-interactive-subagents](https://github.com/HazAT/pi-interactive-subagents) | 为 pi 提供交互式子代理功能, 支持在多路复用器面板中生成、编排和管理子代理会话, 内置多种代理角色(planner、scout、worker、reviewer、visual-tester), 实现完整的规划到实现工作流. | Pi | ⭐ | 223 |
| [AI Team OS](https://github.com/CronusL-1141/AI-company) | 将 Claude Code 转变为自动驾驶的 AI 公司, 实现自主运行、学习和进化. 核心功能包括自主操作引擎、自我改进系统、26 个专业 Agent 模板、8 个结构化会议模板、决策透明度和 4 层防御规则系统. 技术架构采用 5 层设计, 包括 Web 仪表板、CLI + REST API、团队编排器、记忆管理器和存储. 适用于自主软件开发、持续集成、团队协作和项目管理等场景. | 多 Agent 支持 | ⭐ | 142 |
| [Citadel](https://github.com/SethGammon/Citadel) | 运行自主编码活动的工具, 根据任务规模路由到合适的工具. 提供 18 个技能(代码审查、测试生成、文档生成等)、3 个自主代理、8 个生命周期钩子、活动持久性和 fleet 协调. 编排阶梯分为四个层次, 从简单技能到复杂舰队协调. 适用于从单行修复到多天并行活动的各种编码任务. | Claude Code | ⭐ | 375 |

### 2.2.3 Agent Teams Workflow
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [jayminwest/overstory](https://github.com/jayminwest/overstory) | 多智能体编排工具, 将单个编码会话转变为多智能体团队, 通过 tmux 在 git 工作树中生成工作代理, 通过自定义 SQLite 邮件系统协调它们, 并通过分层冲突解决合并它们的工作. 可插拔的 AgentRuntime 接口允许在 Claude Code、Pi、Gemini CLI 或自定义适配器之间切换. | 多 Agent 支持 | ⭐ | 1,132 |
| [AndyMik90/Aperant](https://github.com/AndyMik90/Aperant) | 自主多代理编码框架, 能够为您规划、构建和验证软件. 前身为 Auto Claude, 主要功能包括: 自主任务执行(描述目标, 代理处理规划、实现和验证)、并行执行(最多12个代理终端)、隔离工作区(使用git worktrees确保主分支安全)、自验证QA、AI驱动的合并、跨会话记忆层、GitHub/GitLab集成、Linear集成、跨平台支持(Windows、macOS、Linux)和自动更新. | 多 Agent 支持 | ⭐⭐⭐ | 13,606 |
| [Dicklesworthstone/claude_code_agent_farm](https://github.com/Dicklesworthstone/claude_code_agent_farm) | 强大的多智能体编排框架, 可并行运行 20+ 个 Claude Code 代理, 支持 34 种技术栈(Next.js、Python、Rust、Go、Java 等), 提供 bug 修复、最佳实践实现和多代理协作工作流, 具有智能监控、自动恢复、冲突预防和详细的 HTML 运行报告等功能 | Claude Code |

## 2.3 (multi)Agent Parallel Workflow(Swarm)
-------

Agent Parallel Workflow 致力于组合多个 Agent 协同工作, 通过 Parallel Workflow 完成多 Agent 并行编排和管理. 最终组合多个 Agent 协同工作, 保障复杂任务的高效完成.

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [uluckyXH/OpenMOSS](https://github.com/uluckyXH/OpenMOSS) | 一个 AI 管理 AI 的平台. 多个代理自主协作——规划、执行、审查和检查——而人类只需设定目标并核对结果. OpenMOSS(多代理编排与自我演化系统)是一个基于 OpenClaw 的自组织多代理协作平台. | OpenClaw | ⭐ | 1,016 |
| [fengshao1227/ccg-workflow](https://github.com/fengshao1227/ccg-workflow) | 多模型协作开发工具集. 基于 Claude Code CLI, 整合 Codex/Gemini 后端能力, 提供智能路由、代码审查、Git 工具等 17+ 个命令. | Claude Code/Codex/Gemini | ⭐ | 4,498 |
| [johannesjo/parallel-code](https://github.com/johannesjo/parallel-code) | Parallel Code 为 Claude Code、Codex CLI 和 Gemini CLI 各自自动赋予了自己的 git 分支和工作树. 没有特工互相踩到代码, 没有杂耍终端, 没有精神负担. 只需一个干净的界面, 你就能看到所有内容, 快速导航, 结果准备好时合并——并且从手机上监控. | Claude Code/Codex/Gemini | ⭐ | 416 |
| [EtienneLescot/n8n-as-code](https://github.com/EtienneLescot/n8n-as-code) | 围绕 n8n(开源自动化工作流工具)打造的工具集, 核心目标是为 AI 编码代理赋予 n8n 全量能力, 同时提供 GitOps 流程、TypeScript 工作流开发、多端(VS Code/CLI/Claude)操作等能力, 实现 n8n 工作流的高效、可追溯、智能化管理. | 多 Agent 支持 | ⭐ | 591 |
| [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | 一个基于 Claude 的 AI 驱动开发任务管理系统, 设计用来与 Cursor AI 无缝协作. Task Master 让 Claude Code 像项目经理一样思考, 自动拆解 PRD(需求文档), 生成任务列表, 并跟踪进度. 通过 MCP 配置, 可以轻松接入 Cursor 和 Windsurf 等开发工具. [官网文档](https://task-master.dev), [@GitHub_Daily 的帖子](https://x.com/GitHub_Daily/status/1915556362139955323), [微信公众号--妙想栈--26.1k Star！这个 AI 任务管理神器让 Cursor 和 Claude Code 效率翻倍](https://mp.weixin.qq.com/s/3klm_RKTniT0izX1Wn-QDA) | Claude Code | ⭐⭐⭐ | 26,251 |
| [skindhu/AI-TASK-MANAGER](https://github.com/skindhu/AI-TASK-MANAGER) | AI Task Master 是对原始 claude-task-manager 项目的增强和改进版本. 分析了原始项目的设计理念和能力后, 进行了升级. | Claude Code | ⭐ | 190 |
| [stellarlinkco/myclaude](https://github.com/stellarlinkco/myclaude) | 多智能体编排工作流系统, 支持 Claude Code、Codex、Gemini、OpenCode 多后端执行, 提供多种开发工作流程模块(do、omo、bmad等)和可单独安装的技能 | 多 Agent 支持 | ⭐ | 2,534 |
| [axtonliu/ai-pair](https://github.com/axtonliu/ai-pair) | 异构 AI 团队协作工具, 协调多个 AI 模型(Claude + GPT + Gemini)作为一个团队工作, 一个创作, 两个审查, 利用不同模型的不同视角, 是一个 Claude Code Skill. [我开源了一个让 Claude、GPT、Gemini 组队的 Skill](https://x.com/AxtonLiu/status/2031732461982416898). | Claude Code/Codex/Gemini | ⭐ | 137 |
| [MistRipple/magi-code](https://github.com/MistRipple/magi-code) | 多智能体工程编排系统, 在 VSCode 中将复杂开发任务自动拆解为可执行合同, 调度异构 Worker 并行协作, 完成从规划、执行、验收到知识沉淀的全流程闭环. | 多 Agent 支持 | ⭐ | 183 |
| [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | 多平台 AI 编码框架, 用来统一 AI 编程工具的上下文. 提供自动注入规范、任务中心工作流、并行代理执行、项目记忆和团队共享标准等功能<br>当前多个 AI Coding Agent 并发工作时, 每个工具的规范和历史记录都不互通. Trellis 的做法是在项目中建一个 `.trellis/` 目录, 把代码规范, 任务 PRD, 工作流都存进去. 不管切换到任意 AI 工具, 都能把这些上下文注意进入. 通过 git worktrees 让多个 AI 任务并行执行. 团队里一个人写好规范, 其他人开箱即用. | Claude Code、Cursor、OpenCode、iFlow、Codex、Kilo、Kiro、Gemini CLI、Antigravity 和 Qoder | ⭐ | 4,322 |
| [claude-octopus](https://github.com/nyldn/claude-octopus) | Claude Code 插件, 协调 Codex, Gemini, Claude, Perplexity, OpenRouter, Ollama, Copilot 等 7 家 Agent 以不同角色工作, Octopus 为每个模型分配了独特的角色——Codex 负责实现深度, Gemini 负责生态系统广度, Claude 负责综具有对抗性审查和共识门控. 主要功能包括: 三脑工作流、跨会话持久记忆(深度集成 claude-mem)、从规范到软件的暗黑工厂模式、基于 Double Diamond 框架的方法论、32 个专业角色、39 个命令、50 个技能等. | 多 Agent 支持 | ⭐ | 2,141 |
| [gabrielkoerich/orch](https://github.com/gabrielkoerich/orch) | 一个自主任务编排器, 将工作委托给 AI 编码代理(Claude、Codex、OpenCode、Kimi、MiniMax). 作为后台服务运行, 管理隔离的工作树, 与 GitHub Issues 同步, 并处理从路由到 PR 创建的完整任务生命周期. 支持多项目管理、基于复杂性的路由、代理记忆、实时会话流等功能. | 多 Agent 支持 | ⭐ | 8 |
| [ChesterRa/cccc](https://github.com/ChesterRa/cccc) | 本地优先的多智能体协作内核, 提供轻量级且具有基础设施级别可靠性的多智能体框架. 采用单一写入守护进程设计, 通过只追加账本记录所有消息和事件, 实现可靠的消息传递语义和统一控制平面. 支持 Claude Code、Codex CLI、Gemini CLI 等 8 种一流运行时的协作. | 多 Agent 支持 | ⭐ | 593 |
| [agtx](https://github.com/fynnfluegge/agtx) | 用于管理 agent coding 会话的原生终端看板, 可以接入 Claude Code、Codex、Gemini、OpenCode、Copilot 等任何现有的规范驱动开发框架, 或指定一个具有分阶段技能的自定义插件. 核心功能包括: 1) 编排代理: 自主管理看板、委派任务、推进阶段、检查合并冲突; 2) 多代理任务生命周期: 为每个工作流阶段配置不同代理; 3) 并行执行: 每个任务获得自己的 git worktree 和 tmux 窗口; 4) 规范驱动插件: 支持 GSD、Spec-kit、OpenSpec、BMAD、Superpowers 等; 5) 多项目仪表板: 通过单个 TUI 管理所有项目的代理会话. | Claude Code/Codex/Gemini/OpenCode/Copilot | ⭐ | 705 |
| [swarms](https://github.com/kyegomez/swarms) | 企业级生产就绪的多智能体编排框架, 提供完整的多智能体基础设施平台, 支持生产级部署和与现有系统的无缝集成. 核心功能包括: 层次化智能体集群、并行处理管道、顺序工作流编排、基于图的智能体网络、动态智能体组合、智能体注册表管理等. 支持多种智能体架构如 SequentialWorkflow、ConcurrentWorkflow、AgentRearrange、GraphWorkflow、MixtureOfAgents、GroupChat、HierarchicalSwarm 等, 适用于复杂业务流程自动化、可扩展任务分配、灵活的工作流适应等场景. | 多 Agent 支持 | ⭐⭐ | 6,145 |


# 📝 3 持久化记忆(Persistent Memory)
-------

## 3.1 记忆管理
-------

参见[大佬 Leo(@runes_leo) 的帖子](https://x.com/runes_leo/status/2033324111615693168), 让 AI Agent 越用越懂你, 有两条路.

| 路线 | 描述 |
|:---:|:----:|
| Prompt 层 | 对话结束自动沉淀经验到 markdown 文件, 可以按照级别. 下次启动时加载. 改的是 context 而不是权重, 零 GPU, 零成本. |
| Embedding | 走的是权重层——拦截你的对话, 后台异步跑 RL 训练, 模型参数直接更新. 零标注, 边聊边练. |

两条路的终点一样: 用得越久, agent 越像你的分身. 区别在于 prompt 层有天花板(context 窗口), 权重层没有.


### 3.1.1 Prompt 层
-------



| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace) | 记忆宫殿为人工智能代理提供了持久上下文和无缝的跨会话连续性. 它为 LLM 提供了持久、可搜索和可审计的历史上下文——所以你的代理在每次对话中都不会"从零开始", 通过统一的 MCP(模型上下文协议)接口, Memory Palace 为 Codex、Claude Code、Gemini CLI 和 OpenCode 提供了集成路径, 并为光标和反重力提供了文档说明. 目前已验证的范围和已知边界已在 docs/skills/SKILLS_QUICKSTART_EN.md 文献中记录. | Codex/Claude Code/Gemini/OpenCode | ⭐ | 218 |
| [okooo5km/memory-mcp-server](https://github.com/okooo5km/memory-mcp-server) | MCP 知识图谱管理服务器, Swift 实现, 为 LLM 提供持久记忆能力. 知识图谱存储、实体管理、关系跟踪、观察系统、强大搜索. | Claude/Cursor/Chatwise | ⭐ | 104 |
| [coleam00/mcp-mem0](https://github.com/coleam00/mcp-mem0) | 集成 Mem0 的 MCP 服务器, 提供长期记忆和语义搜索能力. 支持 save_memory、get_all_memories、search_memories 三个核心工具. | 多种 MCP 客户端 | ⭐ | 664 |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | 为 Claude Code 构建的持久记忆压缩系统,自动捕获工具使用并生成语义摘要. 提供 5 个生命周期钩子、Web 查看器 UI、mem-search 技能、渐进式披露. | Claude Code | ⭐⭐⭐ | 41,810 |
| [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory) | 高级记忆管理系统, 为 AI 代理提供持久化记忆和上下文管理能力 | 多 Agent 支持 | ⭐⭐⭐ | 20,035 |
| [tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem) | OpenCode 的记忆管理插件, 提供持久化记忆和上下文管理能力 | OpenCode | ⭐ | 332 |
| [rizal72/true-mem](https://github.com/rizal72/true-mem) | 真实记忆管理系统, 为 AI 代理提供持久化记忆和上下文管理能力 | 多 Agent 支持 | ⭐ | 112 |
| [Alenryuichi/openmemory-plus](https://github.com/Alenryuichi/openmemory-plus) | 增强型记忆管理系统, 为 AI 代理提供持久化记忆和上下文管理能力 | 多 Agent 支持 | ⭐ | 17 |
| [clopca/open-mem](https://github.com/clopca/open-mem) | 开源记忆管理系统, 为 AI 代理提供持久化记忆和上下文管理能力 | 多 Agent 支持 | ⭐ | 10 |
| [varun29ankuS/shodh-memory](https://github.com/varun29ankuS/shodh-memory) | 轻量级、纯离线、超高性能、自学习/自衰减的持久化内存系统, 基于神经科学理论设计, 通过算法实现智能的记忆存储、检索、衰减和关联. 实现 "记住重要的、忘记无关的、越用越智能". | 多 Agent 支持 | ⭐ | 180 |
| [topoteretes/cognee](https://github.com/topoteretes/cognee) | 为 AI Agents 提供持久记忆能力的工具, 通过6行代码即可实现, 结合向量搜索与图数据库, 将原始数据转化为结构化的知识图谱, 支持多种数据类型和部署方式 | 多 Agent 支持 | ⭐⭐⭐ | 14,715 |
| [peterskoett/self-improving-agent](https://github.com/peterskoett/self-improving-agent) | OpenClaw Skill, 让 Agent 记录犯过的错、学到的东西和用户纠正, 结构化存储到 .learnings 目录, 实现自我进化 | OpenClaw | ⭐ | 404 |
| [loryoncloud/Memory-Like-A-Tree](https://github.com/loryoncloud/Memory-Like-A-Tree) | 为AI Agent设计的记忆管理系统, 核心理念是"Agent正常工作, 树自动生长". 采用树状结构管理知识, 包括萌芽、绿叶、黄叶、枯叶和土壤等状态, 基于置信度的记忆管理, 支持知识的索引、搜索、衰减和清理, 提供自动化的Cron任务, 支持多Agent配置和Obsidian同步. | 多 Agent 支持 | ⭐ | 122 |
| [MemTensor/MemOS](https://github.com/MemTensor/MemOS) | 为LLM和AI Agent设计的记忆操作系统, 提供统一的记忆API、多模态记忆支持、多立方体知识库管理、异步摄取和记忆反馈纠正功能. 支持云服务和本地部署两种方式, 可与OpenClaw集成, 实现72% lower token usage和多Agent记忆共享. | 多 Agent 支持 | ⭐⭐ | 7,900 |
| [gavdalf/total-recall](https://github.com/gavdalf/total-recall) | 为 OpenClaw 自治智能体打造的全自动记忆管理系统, 核心特点是无需人工干预、无数据库/ 向量库依赖, 通过五层观测记忆架构和夜间记忆整合(Dream Cycle)实现智能体对话内容的自动压缩、整合、归档与检索, 整体使用成本极低(月均$0.03-$0.10).<br>借鉴人类记忆的工作机制: 海马体捕捉即时体验, 睡眠时进行记忆整合(强化重要记忆、剔除无效信息), 对应到系统中:<br>1. 「五层架构」负责即时记忆捕捉与初步整合, 避免记忆遗漏;<br>Observer(观察者)→Reflector(反射器)→Session Recovery(会话恢复)→Reactive Watcher(反应式监控)→Pre-compaction hook(预压缩钩子);<br>2. 「Dream Cycle」负责夜间深度整合, 实现记忆的分类、归档、降冗余, 保持智能体上下文轻量化. 对 observations.md 进行深度处理, 仅归档不删除, 通过语义钩子保证归档内容可检索, 是实现记忆轻量化的核心.<br>与其他智能体记忆工具的核心区别: 无需人工触发记忆保存/整理, 系统自主监控、自动处理, 零维护成本. | Claude Code | ⭐ | 244 |
| [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | 火山引擎(ByteDance Volcengine) Viking 团队开源的专为 AI Agents 设计的上下文数据库, 核心基于文件系统范式统一管理 AI 智能体所需的记忆、资源、技能等上下文, 解决传统 RAG 与 Agent 开发中的上下文碎片化、检索低效、不可观测等核心问题, 目前仓库处于早期开发阶段(2026 年 1 月开源), 整体架构清晰、功能针对性强, 以下从仓库基础信息、核心定位与解决的问题、核心设计与功能、技术架构、使用与部署、社区与开发状态、优势与待完善点七个维度做详细分析. | Claude Code | ⭐⭐⭐ | 19,606 |
| [websitebutlers/codefire-app](https://github.com/websitebutlers/codefire-app) | 为 AI 编码代理提供持久化记忆的跨平台伴侣应用, 支持Claude Code、Gemini CLI 等主流 AI 编码工具, 通过 MCP 协议提供63种工具包括任务跟踪、语义代码搜索、浏览器自动化等功能, 采用 Swift/SwiftUI 和 Electron/React 双架构实现. | Claude Code<br>Gemini CLI | ⭐ | 189 |
| [powermem](https://github.com/oceanbase/powermem) | 与 OpenClaw 集成的智能记忆系统, 为 AI 智能体提供准确、敏捷、经济的记忆能力. 主要特点包括: 48.77% 准确率提升、91.83% 响应速度提升、Token 减少 96.53%. 核心功能: 智能记忆管理(基于艾宾浩斯遗忘曲线)、用户档案支持、多智能体支持(共享/隔离记忆)、多模态支持(文本、图像、音频)、深度优化的数据存储(子存储支持、混合检索). | OpenClaw | ⭐ | 587 |
| [runesleo/claude-code-workflow](https://github.com/runesleo/claude-code-workflow) | 为 Claude Code 提供的经过实战测试的工作流模板, 包含记忆管理、上下文工程和任务路由功能. 采用三层架构设计: 自动加载的规则、按需加载的文档和热数据. 核心功能包括: 记忆管理、上下文管理、任务路由、完成前验证和自动保存. | Claude Code | ⭐ | 539 |
| [nhevers/MoltBrain](https://github.com/nhevers/MoltBrain) | 为 OpenClaw、MoltBook 和 Claude Code 提供的长期记忆层, 自动学习和回忆项目上下文. 核心功能包括: 自动捕获发现和决策、语义搜索、Web 查看器、分析跟踪、标签和过滤器、收藏功能、导出功能等. 技术架构基于 SQLite 数据库、ChromaDB 向量搜索和 Web 查看器 UI, 支持多平台集成和 x402 微支付存储服务. | OpenClaw<br>MoltBook<br>Claude Code | ⭐ | 395 |
| [memvid/claude-brain](https://github.com/memvid/claude-brain) | 为 Claude Code 提供持久化记忆的插件, 解决会话间无记忆的问题. 核心目标是让 Claude Code 能够记住之前的对话、决策和解决方案, 实现类似人类的记忆能力. 技术上通过单个文件(.claude/mind.mv2)存储记忆, 无需数据库或云服务, 基于 Rust 核心实现亚毫秒级搜索速度. 主要功能包括: 会话上下文自动捕获、记忆搜索、自然语言查询、记忆统计等. 使用场景包括: 跨会话的项目开发、持续的调试过程、团队协作中的知识共享等. 特点是 100% 本地存储、支持版本控制、可轻松传输和共享. | Claude Code | ⭐ | 336 |


### 3.1.2 Embedding 向量化
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | 完全异步的强化学习框架, 通过日常对话训练个性化 AI 代理, 支持在终端、GUI、SWE 和工具调用等真实场景中进行大规模 RL 训练, 提供 Binary RL、OPD 和 Combination 三种优化方法. 基于 4 组件异步架构(服务、收集、评估、训练), 支持本地部署和云端 Tinker 部署, 无需手动标注数据, 通过用户反馈自动优化策略. 适用于个人 AI 助手优化和通用代理训练. | 多 Agent 支持 | ⭐ | 4,343 |
| [Martian-Engineering/lossless-claw](https://github.com/Martian-Engineering/lossless-claw) | 基于 Voltropy LCM 论文的无损上下文管理插件, 用 DAG-based 摘要系统替代 OpenClaw 内置的滑动窗口压缩. 通过 SQLite 数据库存储所有消息, 将旧消息分层摘要形成有向无环图, 支持智能上下文组装和精确检索. 提供 lcm_grep、lcm_describe、lcm_expand 等工具实现历史记录搜索和详情召回, 确保对话历史完全无损且可查询. | 上下文管理 | ⭐ | 3,625 |


### 3.1.3 记忆共享
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [mem0ai/mem0-mcp](https://github.com/mem0ai/mem0-mcp) | Mem0 MCP 服务器, 将 Mem0 Memory API 包装为 Model Context Protocol (MCP) 服务器, 支持添加、搜索、更新和删除长期记忆, 适用于 MCP 兼容客户端(Claude Desktop、Cursor、自定义代理) | 多 Agent 支持 | ⭐ | 642 |
| [cctrace](https://github.com/jimmc414/cctrace) | Claude Code会话导出和导入工具, 支持将会话提取为可移植格式用于归档、分析或共享. 提供两种导出模式: 经典导出(到~/claude_sessions/exports/)和可移植导出(到仓库内的.claude-sessions/), 支持导入会话继续工作, 包含文件历史、待办事项、计划和配置的完整迁移 | Claude Code | ⭐ | 172 |
| [claude-peers-mcp](https://github.com/louislva/claude-peers-mcp) | 让多个 Claude Code 实例能够相互发现并通信的 MCP 服务器, 支持在不同项目的多个会话之间即时消息传递. 核心功能包括: 实例发现、即时消息发送、工作状态摘要、消息检查等. 基于 Bun 运行时, 使用 SQLite 数据库存储信息, 本地服务器运行在 localhost:7899, 支持通过 claude/channel 协议推送消息. 可选集成 OpenAI API 用于自动生成摘要. 适用于多项目并行开发、跨会话信息传递和团队协作场景. | 多 Agent 支持 | ⭐ | 1,318 |

## 3.2 上下文工程
-------

### 3.2.1 Token 治理
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [zenobi-us/opencode-skillful](https://github.com/zenobi-us/opencode-skillful) | 提供懒惰加载的技能发现和注入.<br>AI 有时会因为加载了太多的"系统提示词"或"操作指南"而浪费大量初始 Token.<br>核心功能是将复杂的 Prompt 碎片化为"技能"<br>默认情况下上下文是空的, 只有当 AI 识别到任务(比如"现在需要进行 Docker 部署"), 时, 它才会动态"注入"相关的专业知识和规则. 这能节省约 20%-40% 的静态上下文空间.<br>1. 在对话中, 智能体使用 skill_find 来发现技能.<br>2. 使用 skill_use "skill_name"<br>3. 代理可以用来 skill_resource skill_relative/resource/path 读取参考资料. | OpenCode | ⭐ | 247 |
| [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | RTK 会在命令输出到达你的 LLM 上下文之前过滤和压缩它们. 单一 Rust 二进制, 零依赖, 开销 <10 ms. | 多 Agent 支持 | ⭐⭐⭐ | 14,678 |
| [mksglu/context-mode](https://github.com/mksglu/context-mode) | 上下文模式管理工具, 帮助优化和管理 AI 代理的上下文使用, 减少 Token 消耗. | 多 Agent 支持 | ⭐⭐ | 6,089 |
| [open-compress/claw-compactor](https://github.com/open-compress/claw-compactor) | **OpenClaw 上下文压缩优化工具** - 专为 OpenClaw 设计的 Token 消耗优化解决方案, 通过智能上下文压缩算法减少 45% 的 Token 使用量. 核心功能包括:<br>1). 激进式上下文修剪: 将 TTL 从默认 1 小时缩短至 5 分钟, 配合 0.5 的 hardClearRatio 及时清理过期工具结果;<br>2). 智能缓存保活: 针对 Anthropic Claude 系列模型, 通过 55 分钟心跳机制保持缓存温热状态, 避免昂贵的重写成本;<br>3). 本地化记忆搜索: 集成本地 Embedding 模型替代云端 API 调用, 将 Embedding 成本降至零;<br>4). 多层压缩策略: 结合 micro-compact、auto-compact 和 manual compact 三层压缩机制, 实现上下文的无损压缩与持久化存储.<br>实测数据显示: 平均上下文长度从 128k 降至 70k, 缓存写入频率降低 90%, 特别适用于长对话场景和复杂任务处理. | OpenClaw | ⭐ | 2,100 |
| [SocratiCode](https://github.com/giancarloerra/SocratiCode) | 为 AI 助手提供整个代码库的深度语义理解, 零配置、完全私有、免费, 支持大规模代码库(超过4000万行代码). 核心功能包括混合搜索(语义搜索 + BM25 词汇搜索)、AST 感知的代码分块、多语言代码依赖图、可搜索的上下文工件等. 基于 Qdrant 向量数据库, 支持多种嵌入提供商(Ollama、OpenAI、Google Gemini), 实现了增量索引、批处理、实时文件监控和多代理支持. 适用于代码库探索、架构分析、跨文件和跨语言推理等场景. | 多 Agent 支持 | ⭐ | 653 |
| [Narwhal-Lab/MagicSkills](https://github.com/Narwhal-Lab/MagicSkills) |
| [tokf](https://github.com/mpecan/tokf) |
| [.claudeignore]()
| [CompactMode]()
| [PTC]()

### 3.2.2 Prompt
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [DannyMac180/ace-platform](https://github.com/DannyMac180/ace-platform) | 一款开源的自进化 AI Agent 平台, 由 Dan McAteer 基于 ace-agent/ace 复刻并深度开发, 核心价值是将一次性的 AI 提示词转化为可持续进化的工作手册(Playbooks), 让 AI 工作流在实际使用中持续优化, 减少提示词漂移、降低重复错误, 提升 AI 输出的稳定性. | NA | ⭐ | 145 |
| [linshenkx/prompt-optimizer](https://github.com/linshenkx/prompt-optimizer) | 一个强大的AI提示词优化工具, 帮助用户编写更好的AI提示词, 提升AI输出质量. 支持Web应用、桌面应用、Chrome插件和Docker部署四种使用方式. 核心特性包括智能优化、双模式优化(系统提示词和用户提示词)、对比测试、多模型集成、图像生成、高级测试模式、安全架构、多端支持、访问控制和MCP协议支持. 适用于角色扮演对话、知识图谱提取、诗歌写作等场景, 可帮助激发小模型潜力、保障生产环境稳定性、辅助创意探索与需求定制. | 多平台 | ⭐⭐⭐ | 25,627 |
| [annotated-autoresearch](https://github.com/delip/mini-apps/tree/main/annotated-autoresearch) | 一个实验性项目, 旨在让 LLM 进行自主研究. 核心功能是通过固定时间预算(5分钟)的训练循环, 让 LLM 自动修改 train.py 文件, 尝试不同的模型架构、优化器和超参数, 以达到最低的 val_bpb 指标. 包含完整的实验设置、运行流程、结果记录和评估标准. 适用于 AI 自主研究和模型优化场景. 参见 [mini-apps/annotated-autoresearch](https://delip.github.io/mini-apps/annotated-autoresearch). | NA | ⭐ | 2 |


### 3.2.3 Code Mode
-------

#### 3.2.3.1 Code Mode

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [code-mode](https://github.com/universal-tool-calling-protocol/code-mode) | 将 AI 代理从笨拙的工具调用者转变为高效的代码执行器, 只需 3 行代码. 通过让 LLM 执行 TypeScript 代码来访问整个工具包, 支持多协议集成(MCP、HTTP、File、CLI), 提供安全的 VM 沙箱、超时保护、完整的可观测性和零外部依赖, 大幅提高复杂工作流的执行效率. | 多平台 | ⭐ | 1,408 |


#### 3.2.3.2 Code Graph
-------



| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | 一款为 Claude Code 打造的本地代码知识图谱工具, 核心解决 Claude Code 在代码审查时重复读取整个代码库、token 消耗过高、审查效率低的问题, 通过构建代码结构化图谱实现增量更新和精准的上下文提取, 大幅降低 token 消耗同时提升审查质量. | Claude Code | ⭐ | 3,739 |
| [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | 一款为 Claude Code 打造的语义代码智能工具, 通过构建本地代码知识图谱, 实现 30% 更少的 token 消耗和 25% 更少的工具调用. 支持 19+ 种编程语言, 提供语义搜索、影响分析、智能上下文构建等功能, 100% 本地运行, 无需外部服务. 可通过 MCP 服务器与 Claude Code 集成, 大幅提升代码探索和分析效率. | Claude Code | ⭐ | 343 |

#### 3.2.3.3 Context
-------


| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [upstash/context7](https://github.com/upstash/context7) | 一个为 AI 编码助手提供最新代码文档的平台, 能够从源代码中提取最新的、特定版本的文档和代码示例并直接放入提示中. 支持 CLI + Skills 和 MCP 两种工作模式, 可通过 `npx ctx7 setup` 快速安装. 核心功能包括库文档检索、版本匹配、API 参考等, 解决 LLM 依赖过时信息的问题. | 通用 | ⭐⭐⭐⭐ | 50,877 |
| [ForLoopCodes/contextplus](https://github.com/ForLoopCodes/contextplus) | 一个为开发者设计的 MCP 服务器, 要求 99% 准确性. 通过结合 RAG、Tree-sitter AST、谱聚类和 Obsidian 风格链接, 将大型代码库转变为可搜索的分层特征图. 提供 17 个 MCP 工具, 包括结构分析、语义搜索、代码操作、版本控制和记忆图等功能. 支持多种 IDE 和编码助手, 可通过 `npx contextplus init` 快速配置. | 通用 | ⭐ | 1,683 |

## 3.3 自我进化
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [BayramAnnakov/claude-reflect](https://github.com/BayramAnnakov/claude-reflect) | 一个为 Claude Code 设计的自学习系统, 能够捕获用户的纠正并发现工作流模式, 将它们转化为永久记忆和可重用技能. 核心功能包括从纠正中学习、发现工作流模式、多语言支持和技能改进. 通过两阶段流程(自动捕获和手动处理)实现, 使用混合检测方法(正则表达式和语义 AI 验证)确保准确性. 支持将学习内容同步到多个目标文件, 并能从会话历史中发现重复模式生成可重用技能. 适用于提高 Claude Code 的准确性和自动化程度. | Claude Code | ⭐ | 861 |
| [primeline-ai/evolving-lite](https://github.com/primeline-ai/evolving-lite) | 一个为 Claude Code 设计的自学习系统, 能够从用户的纠正中学习, 记住有效的解决方案, 并在后续会话中自动应用这些知识. 采用四层反馈循环(学习、上下文、自我修复、进化)和分层激活机制, 从安全监控到深度记忆逐步提升. | Claude Code | ⭐ | 34 |

# 🎨 4 状态监控
-------

## 4.1 通知
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [opencode-notifier](https://github.com/mohak34/opencode-notifier) | OpenCode 桌面通知插件 (仓库可能已下线) | OpenCode | ⭐ | 376 |
| [opencode-terminal-notifier](https://github.com/mathew-cf/opencode-terminal-notifier) | OpenCode 终端通知插件,通过终端本身发送通知,点击通知可跳回正确的终端会话. 支持 Ghostty/iTerm2/Kitty/WezTerm 桌面通知,其他终端声音+dock bounce | OpenCode | ⭐ | 2 |
| [opencode-smart-voice-notify](https://github.com/MasuRii/opencode-smart-voice-notify) | OpenCode 智能语音通知插件 (仓库可能已下线) | OpenCode | ⭐ | 47 |
| [claude-code-sound-notification](https://github.com/EryouHao/claude-code-sound-notification) | Claude Code 声音通知插件, 使用 SND01 "sine" 声音套件, 在等待用户确认和 Claude 完成响应时提供声音提示 | Claude Code | ⭐ | 22 |
| [peon-ping](https://github.com/PeonPing/peon-ping) | 为 AI 编码代理提供游戏角色语音和视觉覆盖通知, 支持 Claude Code、Amp、GitHub Copilot、Cursor、OpenCode 等多种工具, 当代理完成任务或需要权限时通过声音和视觉提示提醒用户 | 多平台支持 | ⭐ | 4,217 |

## 4.2 会话管理
-------

[总结多会话管理编排的帖子](https://x.com/juristr/status/2031820737745682520)


### 4.2.1 会话监控
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck) | AI 代理命令中心, 支持多平台, 提供会话管理、MCP 池化等功能, 适用于 Claude Code、OpenCode 等多种 AI 编程工具 | 多 Agent 支持 | ⭐ | 1,773 |
| [Frayo44/agent-view](https://github.com/Frayo44/agent-view) | 轻量级基于终端的代理编排器, 用于管理多个 AI 编码助手, 支持实时状态监控、智能通知、会话管理、Git Worktree 集成和远程会话管理, 适用于 Claude Code、Gemini CLI、OpenCode、Codex CLI 等多种 AI 编程工具 | Claude Code/Gemini/OpenCode/Codex | ⭐ | 340 |
| [hallucinogen/agent-viewer](https://github.com/hallucinogen/agent-viewer) | OpenCode 状态栏插件,显示当前会话信息 | OpenCode | ⭐ | 354 |
| [fynnfluegge/agtx](https://github.com/fynnfluegge/agtx) | 用于管理 agent coding 会话的原生终端看板, 可以接入 Claude Code、Codex、Gemini、OpenCode、Copilot 等任何现有的规范驱动开发框架, 或指定一个具有分阶段技能的自定义插件. | Claude Code/Codex/Gemini/OpenCode/Copilot | ⭐ | 705 |
| [batrachianai/toad](https://github.com/batrachianai/toad) | TUI 界面的终端 AI 智能体管理器. | 多 Agent 支持 | ⭐ | 2,710 |
| [conductor.build](https://www.conductor.build) | 创建并行的Codex + Claude Code代理, 在隔离的工作区中, 一目了然地查看它们正在做什么, 然后审查和合并更改.  | Claude Code/Codex | ⭐⭐⭐⭐ |
| [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | Node.js服务器和React UI, 编排一组AI代理来运行业务, 具有组织结构图、预算、治理、目标对齐和代理协调功能. | 多 Agent 支持 | ⭐⭐⭐⭐ | 36,199 |
| [Dimillian/CodexMonitor](https://github.com/Dimillian/CodexMonitor) | Tauri应用, 用于在本地工作区中编排多个Codex代理, 提供侧边栏管理项目, 主屏幕用于快速操作, 以及由Codex app-server协议支持的对话视图. | Codex | ⭐ | 3,380 |
| [agentastic.dev](https://www.agentastic.dev) | Agentic开发环境, 支持运行30+并行编码代理(Claude Code、Codex、Gemini、Cursor等), 使用Git worktrees或Docker容器进行完全隔离, 每个代理都有自己的内置IDE、Ghostty终端和浏览器.  | 多 Agent 支持 | ⭐⭐⭐⭐⭐ |
| [agent-sessions](https://github.com/jazzyalex/agent-sessions) | 统一会话浏览器, 支持Codex CLI、Claude Code、Gemini CLI、GitHub Copilot CLI、Droid (Factory CLI)和OpenCode, 提供搜索、浏览和恢复过去的AI编码会话的本地优先macOS应用 | macOS 14+ | ⭐ | 413 |
| [claudex](https://github.com/kunwar-shah/claudex) | 专业的 Claude Code 会话查看器和分析工具, 是一个全栈 web 应用, 为开发人员、QA 工程师和研究人员提供检查、搜索和分析 Claude Code 对话历史的能力. 主要功能包括: MCP 服务器(为 Claude Code 提供跨会话持久记忆)、结构化记忆系统、自动项目发现、全文搜索(SQLite FTS5)、通用模板支持、智能内容渲染、会话分析、导出选项、现代 UI 等. 技术栈: React、Fastify、SQLite、Docker. 适用于 Claude Code 对话分析、搜索、记忆管理等场景 | Claude Code | ⭐ | 67 |
| [illegalstudio/lazyagent](https://github.com/illegalstudio/lazyagent) | 一个单一界面监控所有编码代理(Claude Code、Cursor、pi、OpenCode)的工具, 提供终端 UI、macOS 菜单栏应用和 HTTP API, 无锁定、无服务器、纯观察性. 支持活动状态检测、Git worktree 检测、令牌使用和成本估算、实时活动火花图等功能. | 多 Agent 支持 | ⭐ | 111 |
| [dcosson/h2](https://github.com/dcosson/h2) | 一个代理运行器、消息传递和编排层, 用于 AI 编码代理. 它是一个三层系统: 1) 代理运行器: 启动、监控和管理 AI 编码代理, 支持后台运行、状态跟踪和权限管理; 2) 消息传递: 代理可以相互发现和通信, 用户可以通过 Telegram 机器人与它们通信; 3) 编排: 定义具有角色和指令的代理团队, 然后一起启动它们处理项目. 支持 Claude Max 和 ChatGPT Pro 计划, 无需 API 密钥. | 多 Agent 支持 | ⭐ | 103 |
| [Ataraxy-Labs/opensessions](https://github.com/Ataraxy-Labs/opensessions) | 一个终端会话管理器, 具有实时代理状态、Git 分支、未读通知和即时切换功能. 运行在终端内, 与现有快捷键配合使用, 无需配置. 主要功能包括代理状态监控、Git 分支可见性、代理完成时的未读标记、按索引即时切换会话, 以及与 tmux + 任何终端的开箱即用兼容性. 使用 Solid-js TUI、Bun、WebSockets 和 Catppuccin 构建. 注意: 此项目标记为「即将推出」. | 多 Agent 支持 | ⭐ | 172 |
| [hridaya423/conductor-tasks](https://github.com/hridaya423/conductor-tasks/) | 一个智能任务管理助手, 将需求转化为可操作的任务, 生成实施计划, 跟踪进度并加速开发. 支持通过 MCP 集成到编辑器或作为独立 CLI 工具使用, 利用多个 LLM 来简化从规划到执行的开发过程. | 多 Agent 支持 | ⭐ | 75 |
| [FlorianBruniaux/ccboard](https://github.com/FlorianBruniaux/ccboard) | 一个开源的 TUI/Web 仪表盘, 用于 Claude Code 会话监控、成本跟踪和配置管理. 核心功能包括 11 个交互式标签页(仪表盘、会话、配置、钩子、代理、成本、历史、MCP、分析、活动、搜索)、实时监控、SQLite 缓存(89x 启动速度提升)、跨平台支持和零配置. 技术栈: Rust、Ratatui、Axum、Leptos WASM. | Claude Code | ⭐ | 35 |
| [conductor.build](https://conductor.build) | 用于创建并行 Codex 和 Claude Code 智能体的工具, 在隔离的工作区中运行. 主要功能包括: 添加仓库(Conductor 克隆并在 Mac 上工作)、部署智能体(每个 Claude Code 获得隔离工作区)、管理(查看谁在工作、需要注意什么、审查代码). 技术栈: 基于 git worktree, 支持 Claude Code 和 Codex. 适用于多智能体并行开发、代码审查、团队协作等场景 | 多 Agent 支持 | ⭐⭐ |
| [Markus](https://www.markus.global/) | 开源平台, 用于设计、部署和管理自主 AI 代理和团队, 具有任务治理、知识系统和多渠道通信能力. 主要特点包括: 自主代理(带角色、技能、记忆和心跳驱动的主动工作)、多代理团队(角色分配和治理策略)、任务治理(看板、审批工作流、交付审查)、技能和工具(符合 Agent Skills 开放标准)、外部代理集成(通过 A2A 协议)、通信中心(Web UI 聊天和多渠道集成)、知识系统(三层记忆)、信任和治理(渐进式信任级别)、项目管理、代理构建器、GUI 自动化和社区中心. 技术栈: TypeScript、React、SQLite/PostgreSQL、本地优先、LLM 无关. 许可证: AGPL-3.0. 适用于构建、管理和扩展 AI 工作队伍、多代理协作项目、任务治理和审批工作流、跨渠道 AI 通信等场景 | 多 Agent 支持 | ⭐⭐ |

### 4.2.2 会话画布/终端
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | 基于Ghostty的macOS终端, 具有垂直标签和AI编码代理通知, 支持通知环、通知面板、应用内浏览器、垂直+水平标签等功能, 原生macOS应用, 使用Swift和AppKit构建. | 多 Agent 支持 | ⭐⭐⭐ | 11,067 |
| [vaayne/mori](https://github.com/vaayne/mori) | 一款原生 macOS 工作区终端, 围绕项目和工作树组织, 由 tmux 和 libghostty 驱动. 类似于 cmux, 方便同时管理多个 worktree. superset 太慢, conductor 不是 macos 原生, cmutx 太丑. | 多 Agent 支持 | ⭐ | 129 |
| [superset-sh/superset](https://github.com/superset-sh/superset) | 涡轮终端, 允许运行任何CLI编码代理, 同时运行多个代理而不会有上下文切换开销, 每个任务在自己的git worktree中隔离, 内置差异查看器和编辑器. | 多 Agent 支持 | ⭐⭐ | 8,105 |
| [standardagents/dmux](https://github.com/standardagents/dmux) | 开发代理多路复用器, 用于在隔离的 git worktrees 中管理多个 AI 编码代理, 支持并行分支、开发和合并, 兼容多种代理(Claude Code、Codex、OpenCode、Gemini 等) | 多 Agent 支持 | ⭐ | 1,287 |
| [supacode.sh](https://supacode.sh) | AI编码代理管理工具, 提供多代理并行执行和监控能力.  | 多 Agent 支持 | ⭐⭐⭐ |
| [thisguymartin/grove](https://github.com/thisguymartin/grove) | AI原生终端工作区, 为同时在多个git分支上工作的开发人员设计, 运行一个命令即可获得完全连接的Zellij会话, 每个worktree一个彩色编码的标签, 每个标签预加载LazyGit、AI代理和shell. | Claude Code/Gemini/OpenCode | ⭐ | 58 |
| [thecommander.app](https://thecommander.app/) | AI编码代理管理工具, 提供多代理并行执行和监控能力.  | 多 Agent 支持 | ⭐⭐⭐ |
| [mux.coder.com](https://mux.coder.com/) | 开发代理多路复用器, 用于管理多个AI编码代理.  | 多 Agent 支持 | ⭐⭐⭐ |
| [smithers.sh](https://smithers.sh/introduction) | TypeScript框架, 用于使用JSX构建确定性、可恢复的AI工作流, 处理执行顺序、持久状态持久化、结构化输出验证和崩溃恢复.  | 多 Agent 支持 | ⭐⭐⭐⭐ |
| [ghostty-org/ghostty](https://github.com/ghostty-org/ghostty) | 快速、原生、功能丰富的终端模拟器, 提供速度、功能和原生 UI 的平衡. 主要特点包括: 标准合规的终端模拟、竞争性性能(多渲染器架构, Linux 使用 OpenGL, macOS 使用 Metal)、基本可定制性(字体、背景颜色等)、丰富的窗口功能(多窗口、标签、窗格)、原生平台体验、跨平台 libghostty 库用于嵌入式终端. 技术栈: Zig(核心)、SwiftUI(macOS)、GTK(Linux)、Metal/OpenGL(渲染). 适用于作为现有终端模拟器的替代品、嵌入到其他应用程序中、需要高性能终端的开发环境、需要现代终端功能的 CLI 工具开发等场景 | 多平台支持 |
| [zellij-org/zellij](https://github.com/zellij-org/zellij) | 面向开发人员、运维人员和终端爱好者的工作区, 是一个终端多路复用器. 主要特点包括: 开箱即用的良好体验、深度可定制性、通过布局实现个人自动化、真正的多人协作、独特的 UX 功能(如浮动和堆叠窗格)、插件系统(支持任何编译为 WebAssembly 的语言)、内置 Web 客户端(使终端成为可选). 技术栈: Rust. 适用于终端工作区管理、多路复用终端会话、多人协作开发、定制化终端环境等场景 | 多平台支持 | ⭐⭐⭐ | 30,527 |
| [ai-genius-automations/octoally](https://github.com/ai-genius-automations/octoally) | 为 Claude Code 提供的本地优先编排仪表盘, 支持多智能体蜂巢思维会话、单智能体工作流和交互式终端, 提供实时流式输出的美观 Web UI. 主要功能包括: 活动会话网格、蜂巢思维会话、智能体会话、交互式终端、内置 Web 浏览器、Git 源代码控制、文件浏览器、会话持久性、实时流式传输、多项目支持、语音听写和桌面应用. 技术栈: 前端(React 19, Vite, Tailwind CSS 4)、后端(Fastify, TypeScript, SQLite)、桌面应用(Electron)、会话管理(tmux, Claude Code + RuFlo). 适用于多智能体并行开发、AI 编码会话管理、项目管理、Git 操作等场景. | Claude Code/RuFlo | ⭐ | 67 |
| [collaborator-ai/collab-public](https://github.com/collaborator-ai/collab-public) | 协作者是一个端到端的代理开发环境. 终端、上下文文件和运行中的代码——全部集中在无限画布上. 没有上下文切换, 没有找标签. 只有你的经纪人和你的工作, 并肩而立. | 多 Agent 支持 | ⭐ | 1,886 |


### 4.2.3 会话分析
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [RubyRose2001/claudeInsight](https://github.com/RubyRose2001/claudeInsight) | 完全本地化的 Claude AI 对话历史管理和分析工具, 帮助开发者管理和回顾与 Claude 的对话历史. 主要功能包括: 历史记录扫描与管理、项目管理、会话查看与搜索、模型配置管理、技能管理、工作区管理. 技术栈: 后端(Fastify, TypeScript)、前端(Vue 3, TypeScript, Vite, Radix Vue, Tailwind CSS, Pinia, Monaco Editor, Chart.js)、包管理(pnpm). 适用于 Claude AI 对话历史管理、多项目对话记录管理、会话搜索与分析、模型和技能管理等场景. | Claude AI |

## 4.3 状态管理
-------

### 4.3.1 状态栏增强
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [ccstatusline](https://github.com/sirmalloc/ccstatusline) | Claude Code 状态栏插件,显示当前会话信息 | Claude Code | ⭐⭐ | 6,124 |
| [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | Claude Code 的 HUD 界面, 提供实时状态监控和交互能力 | Claude Code | ⭐⭐⭐ | 14,518 |
| [Link-Start/my-claude-hud](https://github.com/Link-Start/my-claude-hud) | Claude Code 的自定义 HUD 界面, 提供实时状态监控和交互能力 | Claude Code | ⭐ | 3 |
| [AwesomeJun/awesome-claude-plugins](https://github.com/AwesomeJun/awesome-claude-plugins) | 一个为 Claude Code 打造的插件市场, 核心提供 Awesome Statusline 插件, 具有美观的 Catppuccin 主题状态栏、实时 API 监控、多显示模式等功能 | Claude Code | ⭐ | 46 |
| [NoobyGains/claude-pulse](https://github.com/NoobyGains/claude-pulse) | 一个为 Claude Code 打造的实时使用监控工具, 提供彩色编码进度条、10 种内置主题、彩虹动画、自动更新通知等功能, 实时显示会话使用情况、剩余时间、每周使用情况等 | Claude Code | ⭐ | 278 |
| [junhoyeo/tokscale](https://github.com/junhoyeo/tokscale) | 一个高性能的 CLI 工具和可视化仪表板, 用于跟踪多个 AI 编码代理的令牌使用情况和成本, 支持 OpenCode、Claude Code、Codex CLI、Cursor IDE 等多种平台, 提供交互式 TUI、实时定价计算、详细的令牌使用分解、原生 Rust 核心(10倍更快处理)、Web 可视化和社交平台等功能 | 多平台 | ⭐ | 1,387 |

### 4.3.2 状态管理
-------


| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [matt1398/claude-devtools](https://github.com/matt1398/claude-devtools) | Claude Code 的开发工具集, 提供调试、监控和优化能力 | Claude Code | ⭐ | 2,730 |
| [blader/taskmaster](https://github.com/blader/taskmaster) | 编码代理的完成保护工具, 解决代理在完成用户目标之前就停止的问题, 要求代理发出明确的完成令牌, 支持Codex和Claude两种代理. | Codex/Claude Code | ⭐ | 491 |
| [nicobailon/pi-design-deck](https://github.com/nicobailon/pi-design-deck) | 一个用于 Pi 编码代理的工具, 提供多页视觉决策卡. 在 macOS 上, 使用 Glimpse 在原生 WKWebView 窗口中渲染; 在其他平台上, 它会回到浏览器标签页. 每张幻灯片会展示 2 到 4 个高保真预览——代码差异、架构图、界面模型——你可以每张幻灯片选择一个. 代理会获得干净的选择映射, 然后进入实现阶段. | OpenClaw<br>Pi | ⭐ | 165 |
| [automazeio/ccpm](https://github.com/automazeio/ccpm) | 使用 Claude Code 工作流程, 利用基于规格的开发、GitHub issue、Git 工作树以及多个并行运行的 AI 代理, 实现更快的发布. 防止上下文丢失, 防止任务阻塞, 保障质量. 这个经过实战验证的系统将 PRD 变成史诗级. | Claude Code |
| [hridaya423/conductor-tasks](https://github.com/hridaya423/conductor-tasks) | 智能助手, 用于将需求转化为可操作的任务, 生成实施计划, 跟踪进度, 并加速开发过程. 主要功能包括: AI 驱动的任务生成、智能任务扩展和规划、强大的 CLI 自动化、多功能任务模板、可视化任务管理(看板、依赖树、摘要仪表板)、多提供商 LLM 灵活性(支持 OpenAI、Anthropic、Groq、Mistral、Google Gemini、Perplexity、xAI、Azure OpenAI 等). 技术栈: JavaScript/TypeScript (Node.js), 支持 MCP 集成和独立 CLI 使用. 适用于开发项目规划和任务管理、PRD 解析和任务生成、开发流程自动化、项目可视化和进度跟踪等场景 | 多 Agent 支持 | ⭐ | 75 |
| [tweakcc](https://github.com/Piebald-AI/tweakcc) | CLI 工具, 用于升级 Claude Code 体验, 支持自定义系统提示、主题、工具集和 UI, 提供 API 接口和自定义补丁功能, 支持多种安装方式(npm、原生二进制)<br>Claude Code 原生版本在开发者使用中存在系统提示词不可修改、工具集全量加载占用上下文以及终端交互体验单一等限制. 开源工具 tweakcc通 过切入底层 cli.js, 提供了重写系统提示词、按需动态加载工具集、实现 Opus 混合模式处理超大项目以及优化终端视觉与性能的能力. 该工具核心代码不到 500 行, 旨在帮助开发者夺回对 AI 助手的控制权. | Claude Code | ⭐ | 1,462 |
| [cc-enhanced](https://github.com/melonicecream/cc-enhanced) | 非官方的 Claude Code 项目管理 TUI 仪表盘, 支持实时项目监控、使用分析、智能待办系统和现代 UI 主题, 基于 Rust 开发, 提供性能优化的用户体验. | Claude Code | ⭐ | 19 |
| [777genius/claude_agent_teams_ui](https://github.com/777genius/claude_agent_teams_ui) | AI 代理团队任务管理工具, 让代理自主工作、相互通信、互相审查, 用户只需查看看板. 支持跨团队通信、代理间消息传递、任务附件、代码审查、实时进程监控等功能, 100% 免费开源, 完全本地运行 | Claude Code | ⭐ | 194 |


## 4.4 配置管理
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [SaladDay/cc-switch-cli](https://github.com/SaladDay/cc-switch-cli) | 为Claude Code、Codex、Gemini和OpenCode CLI提供统一的命令行管理工具, 支持提供商配置、MCP服务器、技能、提示、本地代理路由和环境检查. 使用Rust开发, 支持多平台, 提供交互式和命令行两种操作模式, 具备WebDAV同步和多语言支持. | 多 Agent 支持 |
| [tylergraydev/claude-code-tool-manager](https://github.com/tylergraydev/claude-code-tool-manager) | 一款桌面应用程序, 用于管理多个AI编码助手的MCP服务器、命令、技能、子代理和钩子. 支持Claude Code、OpenCode、Codex CLI、GitHub Copilot CLI、Cursor和Gemini CLI, 提供可视化界面、MCP测试、AI可控性、配置文件管理、状态行构建器、使用分析等功能. | 多 Agent 支持 | ⭐ | 269 |
| [DatafyingTech/Claude-Agent-Team-Manager](https://github.com/DatafyingTech/Claude-Agent-Team-Manager) | 一款基于 Claude Code 打造的 AI 代理团队管理桌面应用(简称 ATM), 核心解决 Claude 代理散落在 markdown 文件中难以管理、部署、自动化的痛点, 通过可视化组织架构、一键部署、任务调度等能力, 让用户快速搭建并运行可自动化的 AI 代理团队. | 多 Agent 支持 | ⭐ | 111 |
| [cc-mirror](https://github.com/numman-ali/cc-mirror) | Claude Code 多分身隔离环境, 带有自定义提供商、提示包和经过实战测试的增强功能. 无需切换, 直接分身. 每个分身一套目录, 一套会话,一套模型映射. 主要功能包括: 将 Claude Code 克隆到隔离实例、配置提供商端点、模型映射和环境默认值、应用提示包和 tweakcc 主题、安装可选技能、将所有内容打包到单个命令中. 支持多种提供商: Mirror Claude、Kimi、MiniMax、Z.ai、OpenRouter、Vercel、Ollama、NanoGPT、CCRouter、GatewayZ 等. | Claude Code | ⭐ | 2,149 |

## 4.5 互联
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [chenhg5/cc-connect](https://github.com/chenhg5/cc-connect) | 控制本地AI代理从任何聊天应用, 桥接运行在用户机器上的AI代理到消息平台. 支持7个AI代理(Claude Code、Codex、Cursor Agent等)和9个聊天平台(Feishu、DingTalk、Slack、Telegram等), 提供多代理编排、完整聊天控制、持久内存、智能调度、多模态支持等功能. | 多 Agent 支持 | ⭐ | 3,377 |
| [Claude-Code-Remote](https://github.com/JessyTsui/Claude-Code-Remote) | 远程控制Claude Code通过多个消息平台, 支持Email、Telegram、LINE和桌面通知. 提供双向控制、安全验证、群组支持、智能命令、多行支持、智能监控、tmux集成和执行跟踪等功能. | 多平台支持 | ⭐ | 1,189 |
| [claude-plugin-weixin](https://github.com/m1heng/claude-plugin-weixin) | 为Claude Code提供微信通道插件, 允许在终端中直接接收和回复微信消息. 使用微信iLink Bot API和HTTP长轮询, 无需公共webhook. 支持二维码登录、本地MCP服务器运行、微信账号配对等功能. | 微信集成 | ⭐ | 540 |



## 4.6 交互
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [Masko](https://masko.ai) | AI 驱动的品牌平台, 可快速创建和动画化吉祥物. 支持从单张图片生成姿势、动画和交互, 提供全球托管和透明背景. 包含多种风格预设、徽标生成等功能, 即将推出开发者 API 和 MCP 集成.  | 多平台支持 | ⭐⭐⭐⭐ |
| [Confirmo](https://confirmo.love) | 桌面 AI 编码助手, 可在多种平台上运行, 包括 macOS (Apple Silicon 和 Intel)、Windows 和 Linux. 提供直观的界面和精灵画廊, 为开发者提供实时编码支持.  | 多平台支持 | ⭐⭐⭐ |
| [lil-agents](https://github.com/ryanstephen/lil-agents) | macOS 应用程序, 在 dock 上显示动画角色, 点击即可打开 AI 终端. 支持 Claude Code、OpenAI Codex 和 GitHub Copilot CLIs, 提供主题切换、思考气泡和音效等功能. 所有数据本地运行, 不发送个人数据. | macOS | ⭐ | 586 |


# 🔌 5 Agent Full Stack 配置
-------

## 5.1 通用配置
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code) | Anthropic 黑客松冠军的 Claude Code 配置, 不仅仅是配置. 一个完整的系统: 技能、直觉、记忆优化、持续学习、安全扫描和以研究为先的开发. | Claude Code | ⭐⭐⭐⭐ | 113,788 |
| [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | Claude-Code 最佳实践. 汇总了已验证过的最佳工作流程和相关的避坑经验, 以及一套 Skills, Agent, MCP 等相关配置. | Claude Code | ⭐⭐⭐ | 22,947 |
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | 一个全面的 Claude Code 资源集合, 包含各种技能、工具和最佳实践. | Claude Code | ⭐⭐⭐ | 33,509 |
| [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) | 专业的Claude Code子代理集合, 涵盖10大类别(核心开发、语言专家、基础设施、质量与安全、数据与AI、开发者体验、专业领域、业务与产品、元与编排、研究与分析), 提供多种安装方式和详细的子代理结构. | Claude Code | ⭐⭐⭐ | 15,436 |
| [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | 由 Jeffallan 维护 Claude 配置库, 提供了一系列 Skills、功能脚本与集成示例, 旨在扩展 Claude 在不同场景下的能力边界. 项目核心目标是让开发者/使用者快速复用成熟的模板, 无需从零配置, 即可让 Claude 完成特定任务, 降低 Claude 定制化使用的门槛. | Claude Code | ⭐⭐ | 7,411 |
| [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | 涵盖 9 大领域的 Claude Code Skills 和 Plugin, 包含<br>1. 工程研发前后端全栈和 DevOps, RAG 架构师、CI/CD 构建器, 甚至还有能自我优化的自进化 Agent.<br>2. 市场增长: SEO、内容创作、转化率优化(CRO)和增长策略等等.<br>3. 高管智囊: 从战略规划、文化建设到模拟董事会会议都能参谋.<br>4. 其他辅助: 产品设计、项目管理、财务分析, 甚至连最让人头疼的合规审查(医疗 MDR、GDPR、ISO)都有专门的插件. 参见 [出海去孵化器 @chuhaiqu 的帖子](https://x.com/chuhaiqu/status/2030941933418500562). | Claude Code | ⭐⭐ | 7,570 |
| [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | Claude Code 的即用配置. 一个全面的 AI 代理、自定义命令、设置、钩子、外部集成(MCP) 和项目模板, 旨在提升您的开发工作流程. | Claude Code | ⭐⭐⭐ | 23,725 |
| [ChrisWiles/claude-code-showcase](https://github.com/ChrisWiles/claude-code-showcase) | 深度配置和使用 Claude Code, 提供完整的开发配套环境. | Claude Code | ⭐⭐ | 5,600 |
| [stretchcloud/claude-code-unified-agents](https://github.com/stretchcloud/claude-code-unified-agents) | 一个全面的 Claude Code 子代理集合, 结合了多个社区仓库中的最佳功能. 该统一集合提供了 54 个智能体, 涵盖开发、基础设施、质量、AI/ML、商业、创意、元管理和专业领域. | Claude Code | ⭐ | 736 |
| [wasabeef/claude-code-cookbook](https://github.com/wasabeef/claude-code-cookbook) | 一套集成的 Claude Code 环境, 通过 40+ 预设的命令, 8+ 智能体角色, 自动化 Hooks, 让 Claude Code 自动判断并执行常见并发任务, 比如代码修正, 测试执行, 文档更新等. | Claude Code | ⭐ | 1,050 |
| [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | Claude Code 最全面的工具包, 包含 135 个代理, 35 个精选技能, 42 个命令, 121 个插件, 19 个钩子, 15 条规则, 7 个模板, 6 个 MCP 配置, 等等. | Claude Code | ⭐ | 933 |
| [feiskyer/claude-code-settings](https://github.com/feiskyer/claude-code-settings) | 精选的 Claude 代码设置、技能和子代理合集, 旨在提升开发流程. 该配置包括功能开发(基于规格的工作流程)、代码分析、GitHub 集成和知识管理的专业技能和子代理. | Claude Code | ⭐ | 1,376 |
| [UfoMiao/zcf](https://github.com/UfoMiao/zcf) | Zero-Config Code Flow, 为 Claude Code 和 Codex 提供零配置、一键设置, 支持双语、智能代理系统和个性化 AI 助手 | Claude Code/Codex | ⭐⭐ | 5,815 |
| [NeoLabHQ/context-engineering-kit](https://github.com/NeoLabHQ/context-engineering-kit) | 面向 AI 代码助手的上下文工程工具集, 核心围绕大语言模型(LLM)的上下文优化、多智能体编排打造, 提供了一系列可插拔的插件和工程化模式, 旨在提升 LLM 生成代码的质量、可预测性, 同时降低 token 消耗.<br>包括 13 款可插拔插件实现, 每个插件聚焦一个具体的研发环节, 覆盖「研发流程(Spec-Driven Development (SDD), Test-Driven Development (TDD), Subagent-Driven Development (SADD), Domain-Driven Development (DDD))、代码生成(Reflexion, )、质量保障(Code Review)、持续改进、文档编写」等全研发流程. | Claude Code<br>Cursor<br>Codex<br>OpenCode | ⭐ | 721 |
| [vstorm-co/full-stack-ai-agent-template](https://github.com/vstorm-co/full-stack-ai-agent-template) | 全栈 AI 代理模板, 提供完整的前后端架构, 用于快速构建和部署 AI 代理应用 | 多 Agent 支持 | ⭐ | 955 |
| [fcakyon/claude-codex-settings](https://github.com/fcakyon/claude-codex-settings) | Claude Code 和 OpenAI 一套开箱即用配置, 包含经过实战考验的技能、命令、钩子、代理和 MCP 服务. |
| [centminmod/my-claude-code-setup](https://github.com/centminmod/my-claude-code-setup) | 是面向开发者优化 Claude Code 使用体验的核心配置仓库, 核心提供 Claude Code 的自定义配置、子代理(Subagents)、斜杠命令(Slash Commands)、MCP 服务器集成等能力, 让开发者能快速搭建高定制化、高生产力的 Claude Code 开发环境. | Claude Code | ⭐ | 2,122 |
| [full-stack-ai-agent-template](https://github.com/vstorm-co/full-stack-ai-agent-template) | 生产级AI/LLM应用模板, 提供FastAPI后端、Next.js前端、PydanticAI/LangChain集成、WebSocket流式响应、会话持久化、多数据库支持、认证、可观测性等20+企业级集成, 让您在几分钟内构建生产就绪的AI应用 | 多平台 | ⭐ | 955 |
| [aiagentskit/claude-agents-library](https://github.com/aiagentskit/claude-agents-library) | 34 个生产就绪的 Claude AI 代理配置库, 分为 7 个专业类别(工程、产品、营销、设计、项目管理、工作室运营、测试). 每个代理包含详细的目的、核心职责、关键技能、沟通风格、示例提示和相关代理信息. 支持 MCP 集成(7 种集成模式), 提供成本优化策略(最多节省 82% 的 Claude API 成本), 包含模型选择矩阵和代理选择指南. 适用于各种专业角色, 可复制、粘贴并针对具体需求定制. | 多平台 | ⭐ | 699 |
| [vibeeval/vibecosystem](https://github.com/vibeeval/vibecosystem) | 将 Claude Code 转变为完整的 AI 软件团队, 包含 119 个专业代理、202 个技能、48 个钩子和 17 个规则, 能够规划、构建、审查、测试并从错误中学习. 支持 5 个阶段的工作流程, 包括发现、开发、审查、QA 循环和最终学习. 具有自学习管道、跨项目学习、Canavar 交叉训练和自适应钩子加载等核心功能. | Claude Code | ⭐ | 307 |
| [FradSer/dotclaude](https://github.com/FradSer/dotclaude) | Claude Code配置管理工具, 提供点文件(dotfiles)风格的配置模板和最佳实践. 支持CLAUDE.md项目配置文件的标准化生成、管理和同步, 帮助开发者建立一致的项目规范和工作流程. 包含丰富的配置模板、自动化脚本和项目脚手架, 适用于个人和团队的Claude Code环境标准化管理. | Claude Code | ⭐ | 510 |

## 5.2 PM 工作流
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [garrytan/gstack](https://github.com/garrytan/gstack) | 核心理想是将 AI 智能体转换为虚拟软件开发团队, 通过自定义指令让 AI 扮演不同角色, 为 Claude Code 提供 9种 工作流技能, 包括产品规划、计划审查、代码审查、一键部署、浏览器自动化、QA测试和工程回顾等, 支持多会话并行运行. [gstack: YC CEO开源的工具集中各角色分工](https://x.com/Gorden_Sun/status/2034937498020061486), 其中文翻译版本参见 [XLearnity/gstack](https://github.com/XLearnity/gstack/tree/feat/zh-cn-skill-prompts). | Claude Code | ⭐⭐⭐⭐ | 53,321 |
| [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | PM 技能市场: AI 操作系统, 助力产品决策更佳. 65 项项目管理技能和 36 个链式工作流程, 分布在 8 个插件中. Claude Code、Cowork 等. 从发现到战略、执行、启动和增长. | ⭐⭐ |
| [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | ⭐⭐ |
| [TraderAlice/OpenAlice](https://github.com/TraderAlice/OpenAlice) | AI 交易 Agent, 集成顶尖调研, 量化团队, 风控中心, 交易中心. | ⭐⭐ |
| [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | Anthropic 为 Claude Cowork(兼容 Claude Code)打造的开源知识工作插件集合, 核心目标是将通用 AI 助手 Claude 转化为适配不同职业角色、企业团队的专业型助手, 实现 AI 与企业实际工作流程的深度融合. 其设计理念和架构甚至引发了传统办公软件领域的市值波动. 以下从仓库基础信息、核心价值与定位、11 款核心插件详情、插件架构设计、使用与定制方式、技术亮点、生态与贡献七大维度展开详细分析. | ⭐⭐ |

## 5.3 完整工作流
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [0xNyk/lacp](https://github.com/0xNyk/lacp) | 本地代理控制平面系统, 为 Claude/Codex 提供可审计、可验证、策略驱动的安全执行环境. 基于5层记忆架(会话记忆、知识图谱、摄取管道、代码智能、代理身份), 提供风险分层执行(safe/review/critical)、预算控制、上下文契约门控. 支持本地沙箱和远程沙箱(Daytona/E2B), 提供完整的任务规划、验证、执行、监控闭环, 是 AI 代理生产级部署的控制平面解决方案. | Claude Code<br>Codex | ⭐ | 84 |
| [FradSer/dotclaude](https://github.com/FradSer/dotclaude) | Frad LEE 开发的一套专为 Claude Code 打造的插件合集, 核心定位是通过专业化的 Agent(智能代理)和自动化工具增强开发者的研发工作流, 覆盖版本控制、代码评审、重构、工程化配置、办公文档生成等全开发环节. 仓库包含10 个核心插件, 分为开发类和生产力类两大类别, 每个插件均提供独立的技能(Skill)和 Agent, 包含开发类插件: git-自动化插件、GitFlow-工作流插件、refactor-代码重构插件、SwiftUI-架构插件; 生产力类插件: GitHub-操作插件、review-多 Agent 代码评审插件、superpowers- 全流程开发工作流插件、claude-config-配置生成插件、office-专利与文档生成插件、plugin-optimizer-Claude插件优化插件. | Claude Code | ⭐ | 510 |
| [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | 将单个 Claude Code 会话转变为完整的游戏开发工作室, 包含 48 个专业代理(分为导演、部门主管、专家三个层级)、37 个工作流程、8 个自动化钩子、11 个路径范围的编码标准和 29 个文档模板. 支持 Godot 4、Unity 和 Unreal Engine 5, 遵循专业游戏开发实践(MDA 框架、自我决定理论、流状态设计、Bartle 玩家类型、验证驱动开发). 提供结构化的代理协调模型, 确保代码质量和项目组织, 从概念到发布的完整工作流程. | Claude Code | ⭐⭐ | 6,951 |


# 参考
-------

[oh-my-opencode 和 superpowers](https://linux.do/t/topic/1445132/18)
[opencode配置文档](https://linux.do/t/topic/1415352)
[对oh-my-opencode的简单修复, 节约5~10倍的API消耗. ](https://linux.do/t/topic/1658684)
[`[Question]`: How to get the status of background agents? #917](https://github.com/code-yeongyu/oh-my-openagent/issues/917)


[Cranot/claude-code-guide](https://github.com/Cranot/claude-code-guide), 完整 Claude 代码 CLI 指南. 实时指南: 每两天自动更新一次, 来源于官方文档、GitHub 发布和 Anthropic 更新日志.

[FlorianBruniaux/claude-code-ultimate-guide](https://github.com/FlorianBruniaux/claude-code-ultimate-guide), 本指南教你以不同的角度看待人工智能辅助开发.

[Claude-Code-Everything-You-Need-to-Know](https://github.com/wesammustafa/Claude-Code-Everything-You-Need-to-Know)

[2025Emma/vibe-coding-cn](https://github.com/2025Emma/vibe-coding-cn), Vibe Coding 指南

[ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips),

[Claude Code 实战课程](https://note.mowen.cn/detail/1_ZEnLT5BCYVsix54iB77)

[joeseesun/lennys-podcast-newsletter](https://github.com/joeseesun/lennys-podcast-newsletter), Lenny Rachitsky 播客与 Newsletter 知识库 — 用自然语言搜索、阅读和学习 638 篇硅谷顶级产品内容. [产品大神Lenny所有Newsletter和Podcast文字版](https://xiangyangqiaomu.feishu.cn/wiki/S97awc7EeiyjNdkJsM4czn71nxb)

https://github.com/199-biotechnologies/claude-deep-research-skill
https://github.com/uditgoenka/autoresearch
https://github.com/karpathy/autoresearch
https://github.com/anthropics/knowledge-work-plugins