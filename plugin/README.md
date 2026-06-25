# 0 Harness
-------

## 0.1 历程追溯
-------

| 日期 | 工程 | 核心定位 | 核心方案 | 何为"人" | 适用场景 | 局限性 | 追溯 |
|:---:|:---:|:-------:|:-------:|:-------:|:-------:|:-----:|:---:|
| 2024 | Prompt Engineering(提示词工程) | 解决 「怎么问 AI」 的问题, 优化指令本身, 让模型精准理解需求、按规范输出结果. | 优化单条指令措辞, 一次一问一答.<br>设计指令措辞、角色设定、输出格式、示例引导、分步要求等. | 人是操作者: 手写 prompt、看结果、再改 prompt. | 边界清晰的单次任务, 如文案撰写、文章摘要、要点提取、简单表格生成. | 仅靠指令无法应对复杂任务, AI 会因缺少背景信息、历史上下文而出错. | 1. 2020/05: OpenAI 发布GPT-3, 论文《Language Models are Few-Shot Learners》展示了通过自然语言指令 + 示例就能让模型干活, 奠定 "提示" 范式.<br>2. 2020 年底–2021 年: 研究者(如 Gwern Branwen)开始用 "prompt engineering" 指代 "设计更好的指令".<br>3. 2022 年底–2023 年: ChatGPT(2022.11) 发布, 普通人也能上手, Prompt Engineering 变成全民技能, CoT、Few-shot、Role-play 等技巧大量普及. |
| 2025/06/25 | Context Engineering(上下文工程) | 解决 「给 AI 看什么」 的问题, 管理输入模型的全部附属信息, 是 Prompt 的信息底座. | 优化窗口内信息(文档、历史、工具、格式).<br>筛选、组织、精简、持久化任务相关信息, 包括代码文件、日志、项目规范、历史对话、历史决策、文档资料等; 同时判断保留/丢弃/加载哪些上下文. | 人是信息编排者: 给模型 "对的上下文", 让单次回答更准. | 信息过少会缺失判断依据, 信息过多会干扰重点, 信息错误会引导 AI 走向错误方向. | 所有后续工程(Loop/Harness)都必须建立在合理的上下文管理之上. | 1. 前身(2000–2001): 学术界很早就有 "context-aware computing"(上下文感知计算), 但和大模型无关.<br>2. 2025/06/19: Shopify CEO Tobi Lütke 在 X 发文: "I prefer 'context engineering' over 'prompt engineering'", 强调核心是给模型提供完整背景信息.<br>3. 2025/06/20: Andrej Karpathy 转发并 + 1, 解释: 工业级 LLM 应用, 关键是精心组装上下文, 而不只是写 prompt.<br>4. 2025/06/25: Karpathy 再发长文系统阐述, Context Engineering 正式出圈, 成为 AI Agent 时代核心话题. |
| 2026/02/04 | Harness Engineering(缰绳工程) | 解决 「Agent 在什么环境安全稳定运行」 的问题, 为整套 Agent 搭建底层运行框架与管控规则. | 加结构化流程与校验(链式调用、评审、回滚).<br>定义工具权限、沙箱环境、日志记录、状态管理、异常兜底、人工接管机制、访问白名单等.  | 人是流程设计者: 定义 "生成→检查→重试" 的简单流水线. | 模型是发动机, Harness 就是车身、刹车、安全带、道路规则, 决定 Agent能做什么、不能做什么、出错如何止损. | NA | 1. 2026/02/05: HashiCorp 联合创始人 Mitchell Hashimoto 发布博客, 首次提出 Harness Engineering 定义: "每次 Agent 犯错, 就工程化一套方案, 让它以后不再犯. "<br>2. 2026/02/11: OpenAI 发布《百万行代码实验报告》, 正式采用 Harness 术语, 描述 "给 AI 搭建可控运行环境".<br>3. 2026/02/04: Martin Fowler 等大佬跟进撰文, Harness Engineering 成为 2026 上半年 AI 工程热词. |
| 2026/06/07 | Loop Engineering(循环工程) | 解决 「Agent 如何持续推进任务」 的问题, 设计自动化闭环工作流, 把人工驱动的多轮交互转为系统自动循环. | 设计自治系统, 让 AI 自动 "Prompt→执行→评估→修正→再 Prompt".<br>任务输入 → Agent 执行 → 工具校验 → 失败反馈 → 自动修正 → 状态记录 → 人工接管(必要时终止). | 人是架构师: 写循环规则、质量门禁、停止条件, 不再手动发 prompt. | 代码修 Bug、CI 故障排查、Issue 处理、PR 生成、长链路内容生产(资料收集→写作→校验→润色). | 摆脱人工逐轮推动, 让 AI 自主完成执行 - 检查 - 修正的迭代. | 1. 2025 年底–2026 年初: Anthropic(Claude Code 团队)内部开始说: "我们不再写 prompt, 我们写 loop".<br>2. 2026/06/07: Google 工程师 Addy Osmani 发布博文《Loop Engineering》, 正式命名并系统化: "你不再 prompt agent, 而是设计 prompt agent 的系统. "<br>3. 2026/06/08–10: OpenClaw 创始人 Peter Steinberger、Claude Code 负责人 Boris Cherny 相继在 X 发声, 观点一致: 手动 prompt 已过时, 未来是设计循环, 引发全网刷屏讨论.  |



## 0.2 你不知道的 Harness Engineering
-------

### 0.2.1 你不知道的
-------

1. [2026/03/12, Tw93 @HiTw93, 你不知道的 Claude Code: 架构、治理与工程实践](https://x.com/HiTw93/status/2032091246588518683)
2. [2026/03/19, Tw93 @HiTw93, 你不知道的 Agent: 原理、架构与工程实践](https://x.com/HiTw93/status/2034627967926825175)
3. [2026/04/03, Tw93 @HiTw93, 你不知道的大模型训练: 原理、路径与新实践](https://x.com/HiTw93/status/2040047268221608281)
4. [2026/06/26, Tw93 @HiTw93, 你不知道的 AI Coding: 非技术人的上手、场景与实战](https://x.com/HiTw93/status/2048230976447557787)
5. [2026/05/01, Tw93 @HiTw93, 你不知道的 GEO: AI 可见性的原理、实践与取舍](https://x.com/HiTw93/status/2050189572999618982)
6. [2026/06/07, Tw93 @HiTw93, 你不知道的具身智能: 从小机器狗到 Optimus](https://x.com/HiTw93/status/2063447352346812576)


[2026/05/19, 艾略特 @elliotchen100, Claude 用户五级进阶: 从搜索框到可编程系统](https://x.com/elliotchen100/status/2056560995305390146) 这篇整理来自 [NerdHack/Nate Herk 的 YouTube 视频《Every Level of Claude Explained in 21 Minutes》](https://www.youtube.com/watch?v=ZRb7D6R64hM&t=17s). Nate Herk 在 Claude 里泡了 400 小时, 把用户分成了 5 级: ① Level 1-把 Claude 当搜索引擎, ② Level 2-让 Claude 记住你, ③ Level 3-让 Claude 自己跑, ④ Level 4-上下文工程, ⑤ Level 5-不再亲自坐镇. 其中 Level 1 到 Level 3 是「会用」, Level 4 开始是「会想」. 99% 的人不是技能不够, 是没意识到 Claude 已经从一个 chat 工具变成一个能被「编程」的系统. 你给它多少结构, 它就还你多少杠杆.

[2026/05/17, How Claude Code works in large codebases: Best practices and where to start](https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start)

[微信公众号 -- 机器之心 -- 全网疯传 fork！刚刚, Claude Code 源代码泄露被开源了](https://mp.weixin.qq.com/s/G9Az9csTs6_WLKt6uu4q_Q)

[2026/06/14, 老卫的 X 日报, 2026年6月: 我所知的每个Agentic Engineering技巧](https://x.imwsl.com/2026/06/14/3)

### 0.2.2 The Harness Is The Product
-------

[My AI Adoption Journey – Mitchell Hashimoto](https://mitchellh.com/writing/my-ai-adoption-journey)

[Harness Engineering: 基于 Claude Code 的完全指南](https://wanlanglin.github.io/-awesome-cc-harness/zh)

[Harness Engineering 学习指南](https://github.com/deusyu/harness-engineering), 一个从概念理解到独立实践的 Harness Engineering 深度学习档案


[2026/03/26, 微信公众号-北方的方北, 程序员三大流派](https://mp.weixin.qq.com/s/8NpvNVwLgnXKwvgyv0F84Q)

[2026/05/27, 空谷 Arvin Xu @arvin17x, 需要自进化的不是 Agent, 而是 Harness](https://x.com/arvin17x/status/2059489592097849698)

[2026/06/03, Lonely @Lonely__MH, 每项任务都有一个 harness: Claude Code 中的动态工作流「译」.](https://x.com/Lonely__MH/status/2061982988758556747)

[2026/06/02, 老金 @freeman1266, 你以为缺的是 Harness, 其实可能连方向都还没有](https://x.com/freeman1266/status/2061808312883282359)

[2026/06/09, 马东锡 NLP @dongxi_nlp, The Harness Is The Product](https://x.com/dongxi_nlp/status/2064098727867163124)

[2026/04/15, indigo @indigox, 极简科普 - 关于智能体(Agentic AI)的六个最重要的术语！来自@victorialslocum 的总结, MCP 与 Skills 大家应该很熟悉了](https://x.com/indigox/status/2044291024726700320), [2026/04/14, Victoria Slocum @victorialslocum, Here are the six most important terms you should know if you're working with agentic AI:](https://x.com/victorialslocum/status/2044018978322874462), 如下所示:

| 项 | 描述 |
|:--:|:---:|
| 模型上下文协议(Model Context Protocol) | 一种标准化的方式, 用于 AI 系统访问和交互外部数据源和工具. 可以把它看作是一个通用适配器, 让代理能够持续与不同服务通信. |
| 特工技能(Agent Skills) | 预设功能, 编码代理可以用来编写更好的代码. Weaviate 的 Agent Skills 仓库( https://github.com/weaviate/agent-skills )就是一个很好的例子——它连接了 Claude Code、Cursor 和 GitHub Copilot 等编码代理与 Weaviate 的基础设施, 让你的代理获得适合集群管理、数据导入和搜索操作的上下文. |
| 智能体 RAG(Agentic RAG) | 将 AI 智能体融入检索过程的 RAG 管道. 与传统 RAG 的线性流程不同, 智能体 RAG 利用智能体将查询路由到特定的知识源、验证检索到的上下文, 甚至重新构建查询. |
| 单智能体架构(Single Agent Architecture) | 最简单的智能体设置——本质上是一个路由. 您拥有多个知识源(数据库、API、工具), 由一个智能体根据用户的请求决定查询哪一个. 清晰且直接. |
| 多智能体架构(Multi Agent Architecture) | 多个专门的智能体协同工作, 每个智能体处理特定的任务. 像 CrewAI 这样的编排框架可以帮助协调这些智能体, 管理任务交接, 并确保所有部分流畅协作. |
| 记忆 (Memory) | 存储上下文、先前的交互以及任务执行期间收集的数据的组件. 它既包括短期记忆(在上下文窗口中), 也包括长期记忆(按需检索). 这是衡量智能体系统运行状况的一个重要区别因素, 特别是在多智能体系统中. |

[Harness Engineering 深度解析: AI Agent 时代的工程范式革命](https://zhuanlan.zhihu.com/p/2014014859164026634)


| 支柱 | 描述 |
|:---:|:----:|
| 结构化执行 (Structured Execution) | 规格驱动工程, 通过 Spec 流程驱动的 "规范 + 执行 + 验证" 的三层规范体系, 摸清 AI 工作的真是能力边界, 约束 Agent 按照既定规范执行, 结合 Rlaph-Loop 实现 Agent 按照 Spec 约定的规范无人值守(长时) 运行. 致力于通过项目的规范化流程, 约束 AGENT 执行, 防止 AGENT 跑偏. |
| Agent 专业化 (Agent Specialization) | 通过专业的 Agent 角色(项目经理, 架构师, 开发, 测试等) 组合成 Agent Teams(公司), 通过 subAgents Orchestrator 编排 Workflow 协调各专家各司其职. 通过 multiAgent Parallel 组合多个 Coding Agent 的能力, 取长补短, 从而可以完成整个完整项目的设计与开发. |
| 持久化记忆(Persistent Memory) | 进度持久化在文件系统上, 而非上下文窗口中. 每次新 Agent 会话从零开始, 通过文件系统制品重建上下文. |
| 上下文架构(Context Architecture) | Agent 应当恰好获得当前任务所需的上下文——不多不少. 每个团队都独立发现, 将所有指令塞进一个文件无法扩展, 解决方案是分层上下文与渐进式披露. |


### 0.2.3 Loop Engineering
-------


[2026/06/09, 陈成 @chenchengpro, 解读 Claude Code 负责人 @bcherny 说他已经不 prompt Claude 了. 是循环在 prompt Claude、在决定下一步, 他的活变成了写那个循环. Addy Osmani 给这事起了个名, 叫 loop engineering: 你不再是那个一轮轮敲 prompt 的人, 而是搭一个会自己找活、分发、检查、记账、定下一步的系统, 让它去捅 agent.](https://x.com/chenchengpro/status/2064221035734646916)

[2026/06/09, Cell 细胞 @cellinlab, [译] Loop Engineering](https://x.com/cellinlab/status/2064144608242679822) 传统模式是人手动给编码 Agent 写提示词、逐轮交互, Loop Engineering 则转变为人设计一套自动化运行系统(循环), 由系统持续调度、驱动 Agent 完成任务, 是下一代人与编码 Agent 的协作范式. Loop 的六大核心组件: ① Automations(自动化调度), 实现任务定时/触发式自动运行、问题分拣归档; 通过 `/loop` 循环执行、`/goal` 持续运行至满足终止条件, 脱离人工逐轮操作; ② Worktrees(工作区隔离), 基于 Git 工作区做多 Agent 并行隔离, 避免多 Agent 同时修改文件产生代码冲突; ③ Skills(项目能力库), 沉淀项目规范、流程、历史经验等固定信息, 避免 Agent 每次会话重新猜测, 降低重复上下文成本, 可打包为插件跨项目复用; ④ Connectors(连接适配器), 基于 MCP 协议打通工单、数据库、IM、CI/API 等外部工具, 让 Loop 不只是输出方案, 还能在真实业务环境中执行操作. ⑤ Sub-agents(子 Agent), 拆分编写者与审核者两类角色(可使用不同模型), 解决自研自查的疏漏问题, 提升产出质量; 终止条件校验也由独立 Agent 完成; ⑥ Memory(持久化状态存储), 脱离单次对话上下文, 用文件、看板等外部载体记录任务进度、待办、结果, 保证长周期 Loop 可断点续跑.

[2026/06/09, Smartpig @Smartpigai, Loop Engineering: Agent时代最被低估的能力](https://x.com/Smartpigai/status/2064209609896968679) AI 前期, 提示词工程是驾驭模型的核心, 主打精准输入、优化 AI 初始输出, 决定任务起点. 但随着智能 Agent 普及, 核心能力已转向循环工程. 传统大模型为单次推理, 易出现幻觉、输出错误等问题, 而循环工程可构建反馈迭代闭环, 让 AI 具备执行、校验、纠错、复盘迭代能力, 实现能力质变. 未来提示词工程价值将普惠弱化, 循环工程成为拉开AI能力差距的核心壁垒, 搭建迭代闭环的能力, 也是AI从业者的核心竞争力.

[2026/06/09, Mr Panda @PandaTalk8, LOOP ENGINEERING: 当工程回归哲学](https://x.com/PandaTalk8/status/2064336598075154694) 本文解读了新兴的 Loop Engineering(循环工程), 其核心是思考 — 行动 — 观察 — 调整的 AI 自主循环机制, 底层为基础 while 循环, 是各类 AI 智能体的通用核心逻辑. 循环是智能的底层架构, 源自反馈回路、思辨探究等古今智能理论. 它颠覆传统编程的过程控制, 依靠 Prompt 定义目标与约束, 实现目标治理. AI 工程技术门槛大幅降低, 目标定义、价值思辨等哲学思维取代编码能力成为核心竞争力, 未来行业突破将依托深度思考与系统认知.

[2026/06/14, Niko爱学习 @ai_super_niko, Loop Engineering 火了: 你真的需要吗？](https://x.com/ai_super_niko/status/2066164194546991185) Loop Engineering 在 AI 编程圈走红, 是 AI 使用从 Prompt、Context、Harness 进阶而来的调度层. 它靠多组件与状态文件实现自主循环, 但需满足任务重复、可自动验证等四个前提. 其暗藏烧 Token、形成代码黑盒、产生理解债等风险. 多数开发者暂不适用, 作者建议先夯实 Harness, 循序渐进落地.

[2026/06/12, [AINews] Loopcraft: The Art of Stacking Loops](https://www.latent.space/p/ainews-loopcraft-the-art-of-stacking)

[2026/06/16, Sydney Runkle @sydneyrunkle, The Art of Loop Engineering](https://x.com/sydneyrunkle/article/2066928783534289358)

[2026/06/10, Ray Fu @rayycfu, Loop Engineering: The New Skill That Matters More Than Knowing How to Prompt AI](https://x.com/rayycfu/status/2064697410807328779)

[2026/06/15, Loop Engineering: Stop Asking Me What It Is](https://github.com/alchaincyf/loop-engineering-orange-book) 别再问我什么是 Loop Engineering — 橙皮书系列. A plain-language guide to loop engineering (中文 + English PDF).


很多人理解 Loop Engineering 的方式是"让 AI 自己跑, 我去喝咖啡". 你确实不该再坐在屏幕前一轮一轮地发提示词, 那是在用人力模拟循环. 但循环跑起来不等于你可以消失. 无人值守地运行, 就是无人值守地出错. [2026/06/18, 老金 @freeman1266, Loop Engineering 里, 人到底该干什么](https://x.com/freeman1266/status/2067514380263239697) 探讨了人的位置. 人的角色没消失, 只是移动了. 以前你的工作是: 写提示词 → 看输出 → 改提示词 → 再看输出. 你是中间那个传话筒. 现在你的工作是: 定义目标 → 设计循环 → 审查结果 → 处理循环搞不定的事. 中间那些机械性的"执行-检验-重试", 交给循环. 你只管入口和出口. 但要求其实更高了. 你在入口定义的东西, 会被循环放大执行几十次. 一个模糊的目标, 循环会帮你把模糊放大成灾难. 人要设定可量化停止标准、处理循环无法解决的复杂问题、终审产出规避理解力债务. 仅可逆、可核验、低风险工作可交由循环, 它只做预处理, 关键决策仍由人把控.

# 📊 1 结构化执行(Structured Execution)
-------

规格驱动工程, 通过 Spec 流程驱动的 "规范 + 执行 + 验证" 的三层规范体系, 摸清 AI 工作的真是能力边界, 约束 Agent 按照既定规范执行.
1. 通过 Spec 驱动约束 Agent 按照既定规范执行
2. 通过 Rlaph-Loop 实现 Agent 长时无人值守运行.


[微信公众号 -- 被 AI 榨干的 --AI 编程不需要 10x 工程师, 需要 10x 产品经理](https://mp.weixin.qq.com/s/Q2O1j9NRQStCi7HAbv-kRQ) 则 **建议用户应该作为 PM, 通过 Harness Engineering 和 Ralph Loop 来规范化 AI 的行为**, Harness Engineering 5 条原则来约束 AI 行为: 所有决策推进代码仓库、问 "缺什么能力" 而不是 "为什么出错"、用代码强制约束、构建反馈闭环、写地图不写说明书. 借助 7 份文档来规划任务 story.md, user-journey.md, uiux-review.md, visual-system.md, architecture.md, design-assets.md, test-plan.md 来规划和工作, Ralph Loop 通过约定的 7 条迭代规则来保障 AI 按照预期行为工作.

| 领域 | 描述 |
|:---:|:----:|
| Specification-Driven | 规格驱动工程, 通过 Spec 流程驱动的 "规范 + 执行 + 验证" 的三层规范体系, 摸清 AI 工作的真是能力边界, 约束 Agent 按照既定规范执行. |
| Ralph-Loop | 实现 Agent 按照 Spec 约定的规范无人值守 (长时) 运行. |


## 1.1 Specification-Driven
-------

[Structured-Prompt-Driven Development (SPDD)](https://martinfowler.com/articles/structured-prompt-driven)

[Putting Spec Kit Through Its Paces: Radical Idea or Reinvented Waterfall?](https://blog.scottlogic.com/2025/11/26/putting-spec-kit-through-its-paces-radical-idea-or-reinvented-waterfall.html)

[微信公众号 -- 牛马也卷 AI-- 企业存量系统的" 考古 "指南: OpenSpec + Superpowers 实战](https://mp.weixin.qq.com/s/Gg3fMo2_iKdl28j3vhy5eQ) 介绍了一种 OpenSpec + Superpowers 系统工作的实战技巧, 用 OpenSpec + Superpowers 这套组合, 带你系统化地梳理存量系统——让 AI 成为你的 "分析助手", 而不是 "万能钥匙". 背景是只用 Superpowers: 容易跑偏, 只用 OpenSpec: 规范落地难. 两者协同工作实现目标对齐 + 系统执行, ① 先对齐目标, OpenSpec 帮你定义 "要分析什么";  ② 再系统执行——Superpowers 按任务清单执行不遗漏; ③ 任务粒度可控——每个任务 2-5 分钟, 不会追飞; ④ 可追溯 —— 规范文档记录决策过程.

[OpenCode 配置 OpenSpec + Superpowers + Oh-My-OpenCode 指南](https://github.com/wentietie/tools-config/blob/main/OpenCode-%E9%85%8D%E7%BD%AE%E6%8C%87%E5%8D%97-OpenSpec-Superpowers.md)

[2026/3/29, @Voxyz_ai, I Compared gstack, Superpowers, and Compound Engineering. They Solve Three Completely Different Prob](https://x.com/Voxyz_ai/status/2038237755654783107)

[2026/04/08, 微信公众号--产品化AI--codex+superpowers太重了, 我把 AGENTS.md 拆成了两个版本](https://mp.weixin.qq.com/s/f85KjZD8DH3JjTa6TKv1WA)

[2026/04/30, Joruno @wsl8297, OpenSpec + Superpowers 工作流: AI 辅助开发从「写代码」到「按规格交付」的完整闭环.](https://x.com/wsl8297/status/2049725845040922705) 展示了自己结合 的 AI 工作流, 两个工具, 各司其职: OpenSpec 管规格和记忆, Superpowers 管设计和执行. 核心价值: OpenSpec 让每次变更都沉淀成规格文档, AI 不再重复摸索; Superpowers 用头脑风暴深入细节 + TDD 保证代码质量; 子代理读取 specs/ 执行任务, 每个环节都基于统一上下文; verification 跑过才算完, 质量有保障. 这套流程解决了 AI 开发最大的两个痛点: 缺记忆和缺纪律.

[Saito @SaitoWu, Garry Tan 有一个很关键的 skill, 叫 Plan-Eng-Review. ](https://x.com/SaitoWu/status/2052968430685573379), 其大致思路是先让 agent 做规划, 再让 agent 画 ASCII 图, 把数据流、用户流程、状态机全部画出来. 然后再进入代码实现, 最后 review 测试. 很多人用 AI 写代码, 最大的问题是上来就让它写, 结果 agent 很快跑偏. Garry 的方法是, 写代码之前必须先画图. 让 agent 把结构、状态和流程讲清楚, 再动手实现.

[2026/06/01, AI搞钱研究院 @gaoqian2580, Vibe Coding 不翻车: 用 PRD-Manager 把脑子里的想法翻译给 AI](https://x.com/gaoqian2580/status/2057261855568191495).

[2026/05/31, affe @affe_is_me, 分享一个我怎么使用 ralph-loop  的提示词流程:](https://x.com/affe_is_me/status/2060973994829037677)


### 1.1.1 Specification Driven WorkFlow
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [`superpowers`](https://github.com/obra/superpowers) | 一套完整的软件开发流程, 基于一套可组合的 Skills 和一些初步指令. | Claude Code<br>Cursor<br>Codex<br>OpenCode | ⭐⭐⭐⭐⭐ | 141,819 |
| [`superpowers-zh`](https://github.com/jnMetaCode/superpowers-zh) | superpowers 完整汉化 + 6 个中国原创 skills, 让 17 款 AI 编程工具真正会干活, 包含方法论内核、工具一键适配、国内 Git/CI 生态和中文化表达习惯. | Claude Code<br>Copilot CLI<br>Hermes Agent<br>Cursor<br>Windsurf<br>Kiro<br>Gemini CLI<br>Claw Code<br>等 17 款工具 | ⭐ | 1,638 |
| [github/spec-kit](https://github.com/github/spec-kit) | 帮助你开始专业化开发的工具包, 让你专注于产品场景和可预期的结果, 而不是从零开始随意编写每一个部分. | Claude Code<br>Cursor<br>Codex<br>OpenCode | ⭐⭐⭐⭐ | 86,346 |
| [Linfee/spec-kit-cn](https://github.com/Linfee/spec-kit-cn) | Spec Kit 的非官方中文复刻版本, 对应原版 v0.1.13. 命令使用 `specify-cn` 而非 `specify` | Claude Code<br>Cursor<br>Codex<br>OpenCode | ⭐ | 632 |
| [Fission-AI/OpenSpec](https://github.com/Fission-AI/OpenSpec) | 最受喜爱的规范框架, 灵活而非僵化, 支持 20+ AI 代理. 哲学: 流动而非刚性, 迭代而非瀑布, 简单而非复杂, 为从现有项目构建而不仅仅是新建项目构建, 可从个人项目扩展到企业级. | Claude Code<br>Cursor<br>Codex<br>OpenCode | ⭐⭐⭐ | 38,418 |
| [claudeforge/Forge](https://github.com/claudeforge/Forge) | Claude Code 的规范驱动人工智能开发引擎, FORGE 将 Claude Code 转变为一个强大的迭代开发系统, 该系统通过正式规范、结构化规划和完成标准验证, 自主处理复杂任务. | Claude Code | ⭐ | 11 |
| [claude-code-bmad-skills](https://github.com/aj-geddes/claude-code-bmad-skills) | [BMAD-METHOD](https://github.com/bmad-code-org/BMAD-METHOD) 的 Claude Code 插件, [BMAD-METHOD(Breakthrough Method of Agile AI-Driven Development)](https://github.com/ljxpython/bmad-method-tutorial) 突破性的敏捷 AI 驱动开发方法, 是一个内置了完整敏捷开发流程的智能体系统, BMAD Method for Claude Code skills, 则不仅仅是一套 Skills 集, 它是一套将敏捷开发方法论 (Agile Methodology) 与 AI 原生能力深度融合的工程框架. 它将 Claude Code 从一个 "更聪明的 Agent" 转变为一支具备 9 种专业角色、15 种标准工作流的 "全栈敏捷开发团队". 参见 [Documentation Site, with examples](https://aj-geddes.github.io/claude-code-bmad-skills), [敏捷开发「BMAD」也推出了 Agent Skills, CC 直接用｜ 斩获 2.6 万 star](https://cloud.tencent.com/developer/news/3408673) | Claude Code | ⭐ | 368 |
| [shotgun-sh/shotgun](https://github.com/shotgun-sh/shotgun) | Spec-Driven Development, 核心解决 AI 编码代理在大型开发任务中上下文丢失、偏离需求、重复造轮子、生成超大 PR 难以评审的核心痛点. 给 AI 编码代理做 "开发规划师", 先让 Shotgun 吃透你的整个代码库, 生成结构化、分阶段的开发规范 / 步骤, 再让 AI 代理按规范分步开发, 输出可评审、可落地的小 PR, 而非无章法的大段代码. | Claude Code | ⭐ | 714 |
| [danielmiessler/Personal_AI_Infrastructure](https://github.com/danielmiessler/Personal_AI_Infrastructure) | PAI 是一个通过功能齐全的智能人工智能平台来理解、表达并实现其主体目标的系统. 基于 Claude Code 构建, 定位为「增强人类能力的智能体平台」, 区别于传统无记忆的聊天机器人和仅具备工具调用能力的智能体平台, 实现了以用户为核心的目标导向、持续学习型 AI 交互.<br>1. 定义了 AGENT 的三层进化: Chatbots(聊天机器人) -> Agentic Platforms(智能平台) -> Personal_AI_Infrastructure(PAI, 个人人工智能基础设施).<br>2. PAI 的核心竞争力在于以用户为中心的设计, 体现出三大核心差异化因素: 目标导向(Goal Orientation), 追求最佳输出(Pursuit of Optimal Output), 持续学习(Continuous Learning). 以及 16 条设计原则(PAI Principles).<br>3. PAI 提供独立可安装的功能包(Available Packs), 无需安装完整 PAI 系统, 可单独部署, 每个包由 AI 自动安装(5 阶段向导: 系统分析→用户提问→备份→安装→验证), 覆盖 12 类核心能力. | Claude Code | ⭐⭐⭐ | 11,201 |
| [open-gsd/get-shit-done-redux](https://github.com/open-gsd/get-shit-done-redux) | AI 编程时上下文窗口被填满后输出质量下降的问题, GSD(Getting Shit Done) 是一套轻量级且强大的元提示、上下文工程和规格驱动开发系统, 通过结构化文档和多智能体编排保持代码质量稳定, 解决上下文腐烂问题, 为 AGENT 提供可靠的开发流程. 原仓库地址 [gsd-build/get-shit-done](https://github.com/gsd-build/get-shit-done). 切换原因参见 [https://github.com/open-gsd/get-shit-done-redux/discussions/109](https://github.com/open-gsd/get-shit-done-redux/discussions/109) 核心解决"上下文衰减"问题: 会话越长, AI 输出越差. 做法有三个: ① 把繁重工作放到子智能体的全新上下文里: 主程序只负责分派任务, 采用多 Agent 架构. 主程序自己不处理复杂的逻辑, 而是生成专门的虚拟助手分别去做调研、规划、执行和测试. 跑完直接汇总结果, 保证响应速度; 每次任务重置上下文, 它会把你的大需求拆解成一个个细分任务. 执行每个小任务时, 都会分配一个全新的、干净的上下文窗口. 这样 Claude 就不会被之前的历史对话干扰; ② 用 PROJECT.md、ROADMAP.md 等结构化文档跨会话保持状态: 做一步存一步的自动存档, 每个小任务完成后, 会自动生成一个独立的 Git 提交, 就相当于打游戏时的分步自动存档. 好处是如果哪一步跑崩了, 能直接定位到具体的错误步骤, 一键回滚; ③ 专门加一个验证步骤确认代码真能用. (六个命令组成主循环)支持完整的开发工作流: 初始化项目 → 讨论决策 → 规划任务 → 并行执行 → 验证成果 → 发布里程碑. 支持交互式和自动审批模式, 配置灵活. | Claude Code<br>OpenCode<br>Gemini CLI<br>Codex<br>Copilot<br>Cursor<br>Antigravity | ⭐⭐⭐ | 49,559 |
| [ZhangHanDong/agent-spec](https://github.com/ZhangHanDong/agent-spec) | 智能体规范定义和管理工具, 提供标准化的智能体配置和编排能力 | 多 Agent 支持 | ⭐ | 102 |
| [tintinweb/pi-supervisor](https://github.com/tintinweb/pi-supervisor) | Pi-Agent 扩展, 监控编码代理并引导其朝向定义的目标前进, 通过观察对话、注入指导消息和信号完成状态来实现监督功能 | Pi | ⭐ | 30 |
| [garrytan/gstack](https://github.com/garrytan/gstack) | 核心理想是将 AI 智能体转换为虚拟软件开发团队, 通过自定义指令让 AI 扮演不同角色, 为 Claude Code 提供 9 种 工作流技能, 包括产品规划、计划审查、代码审查、一键部署、浏览器自动化、QA 测试和工程回顾等, 支持多会话并行运行. [gstack: YC CEO 开源的工具集中各角色分工](https://x.com/Gorden_Sun/status/2034937498020061486), 其中文翻译版本参见 [XLearnity/gstack](https://github.com/XLearnity/gstack/tree/feat/zh-cn-skill-prompts) 和 [2026/05/10, Nainsi Dwivedi, @NainsiDwiv50980, Gstack 这个仓库感觉不像开发工具, 更像是软件未来走向的预览](https://x.com/NainsiDwiv50980/status/2053416104899522783). | Claude Code | ⭐⭐⭐⭐ | 67,446 |
| [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | 实现 "复合工程" 理念的插件, 通过 "80% 规划和审查, 20% 执行" 的模式, 让每个工程工作单元都比前一个更容易. 提供完整工作流: `Ideate → Brainstorm → Plan → Work → Review → Compound → Repeat`, 包含多个专用命令如 `/ce:brainstorm`、`/ce:plan`、`/ce:work` 等, 支持多平台转换和配置同步. 参见 [微信公众号 -- 老季聊 AI--AI 复利编程的秘密——Claude Code ×  Compound Engineering Plugin 使用指南](https://mp.weixin.qq.com/s/1BACTJjdq60bQZbeojG9dA) 和 [@Voxyz_ai, I Compared gstack, Superpowers, and Compound Engineering. They Solve Three Completely Different Prob](https://x.com/Voxyz_ai/status/2038237755654783107). | Claude Code<br>Cursor<br>OpenCode<br>Codex<br>Droid<br>Pi<br>Gemini<br>Copilot<br>Kiro<br>Windsurf<br>OpenClaw<br>Qwen | ⭐⭐⭐ | 14,948 |
| [addyosmani/agent-skills](https://github.com/addyosmani/agent-skills) | 为 AI 编码代理提供生产级工程技能的项目, 编码了高级工程师在构建软件时使用的工作流程、质量门控和最佳实践. 19 个工程技能, +7 个斜杠命令, 把 Google 级别的工程文化直接灌进 AI 编程代理. Define: 先写规格, 再写代码 → Plan: 拆解成小粒度可验证任务 → Build: 增量实现, 上下文工程, 干净的 API 设计 → Verify: TDD、浏览器测试、系统化调试 → Review: 代码质量、安全加固、性能优化 → Ship: Git 工作流、CI/CD、架构决策记录、上线清单. | Claude Code<br>Cursor<br>Gemini CLI<br>Windsurf<br>GitHub Copilot<br>Codex | ⭐⭐⭐ | 50,389 |
| [stephenleo/bmad-autonomous-development](https://github.com/stephenleo/bmad-autonomous-development) | BMad 方法的自主开发编排器, 运行完全自主、并行的多代理管道, 贯穿整个故事生命周期(创建 → 开发 → 审查 → PR), 由 sprint backlog 和依赖图驱动. 此外还有 [NathanJ60/bmad-ralph-loop](https://github.com/NathanJ60/bmad-ralph-loop) BMad 方法的 Ralph 循环实现, 用于长时间运行的自主开发任务 和 [qianxiaofeng/bmad-ralph](https://github.com/qianxiaofeng/bmad-ralph) BMad 方法的 Ralph 循环实现, 用于自主开发流程 | BMad Method | BMad Method | ⭐ | 43 |
| [tw93/Waza](https://github.com/tw93/Waza) | 将工程习惯转化为 Claude 可运行的技能, 包含 8 个核心技能: 思考(`/think`)、设计(`/design`)、检查(`/check`)、调试(`/hunt`)、写作(`/write`)、学习(`/learn`)、阅读(`/read`)和健康检查(`/health`), 每个技能都有明确的触发条件和执行流程 | Claude Code<br>多代理支持 | ⭐ | 1900 |
| [spec-kitty](https://github.com/Priivacy-ai/spec-kitty) | 开源的规范驱动开发 CLI 工作流工具, 帮助团队将产品意图转化为实现, 通过 spec -> plan -> tasks -> agent loop -> review -> merge 的可重复路径. 核心特性包括规范驱动的 artifacts、工作包执行、并行实现模型、实时项目可见性、审查弹性和多代理支持. | Claude Code<br>GitHub Copilot<br>Gemini CLI<br>Cursor<br>Qwen Code<br>opencode<br>Windsurf<br>Kilo Code<br>Auggie CLI<br>Roo Code<br>Codex CLI<br>Mistral Vibe<br>Kiro CLI | ⭐⭐⭐⭐ | 1,071 |
| [Steffen025/pai-opencode](https://github.com/Steffen025/pai-opencode) | Daniel Miessler 的 Personal AI Infrastructure 的 Opencode 社区移植版本, 提供个人人工智能基础设施. | Claude Code | ⭐ | 132 |
| [WorkPlan with AI](https://github.com/MakotoArai-CN/WorkPlan-with-AI) | 融合AI能力的跨平台任务规划与管理系统, 支持Windows、macOS、Linux和Android, 通过接入大语言模型自动生成任务清单、拆分子步骤、搜索网页资料和读写本地文件. 支持多模型接入(OpenAI、DeepSeek、通义千问等). 适用于个人任务管理、AI辅助工作规划、多平台协作等场景. | 多平台 | ⭐ | 9 |
| [LichAmnesia/lich-skills](https://github.com/LichAmnesia/lich-skills) | 个人专业技能集合, 为 Claude Code、Gemini CLI 和 OpenAI Codex 提供电报风格、有观点、无填充的工程判断技能. 包含 7 个核心技能: ① `spec-driven-dev` - 完整 SDLC 工作流(Spec → Plan → Build → Test → Review → Ship, 反理性化表格 + 验证门控 + 原子提交); ② `debug-hypothesis` - 科学方法调试(Observe → Hypothesize → Experiment → Conclude, 反 bulldoze 规则 + 最大 5 行实验 + 强制 `DEBUG.md` 证据链); ③ `wiki-aggregate` - 聚合式研究(N≥3 原始研究制品 → 1 结构化 pack, 每个 claim 有 `path:line` provenance + 跨源矛盾记录); ④ `tavily-search` - 网络搜索 + 内容提取(事实核查、文档查找、引用研究); ⑤ `nano-banana` - 文本转图像(支持 512/1K/2K/4K 分辨率); ⑥ `frontend-design` - 前端设计(生产级界面 + 独特美学方向 + 有意排版 + 避免 generic AI-slop UI); ⑦ `subagent-brief` - 子代理预检(≤200 word brief 模板 + 反理性化表格, 基于 arXiv 2604.25899). | Claude Code<br>Gemini CLI<br>OpenAI Codex | ⭐ | 216 |
| [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | 同上行 85. 复合工程理念的实现之一, "80% 规划和审查, 20% 执行", 包含 37 个技能和 51 个代理, 提供 `/ce-brainstorm`、`/ce-plan`、`/ce-work` 等完整工作流. | Claude Code<br>Cursor<br>OpenCode<br>Codex<br>Droid<br>Pi<br>Gemini<br>Copilot<br>Kiro<br>Windsurf<br>OpenClaw<br>Qwen | ⭐⭐⭐ | 16,518 |
| [statewright/statewright](https://github.com/statewright/statewright) | 通过状态机约束 AI Agent 在每个阶段可用的工具, 防止模型在复杂任务中迷失或滥用权限. Statewright 给 AI Agent 加了层状态机护栏, 规划时只能读, 写代码时才能改, 测试时只能跑测试. 工具一少, 模型就不容易晕, 也不会反复读同一个文件五遍不动手. 实测 13-20GB 的本地模型在 SWE-bench 子集上从 2/10 干到 10/10. | 支持 Claude Code、Codex、Cursor 等主流 Agent. | ⭐ | 294 |
| [EveryInc/compound-engineering-plugin](https://github.com/EveryInc/compound-engineering-plugin) | 实现"复合工程"(Compound Engineering)理念的AI编码插件,核心理念是"80%规划和审查,20%执行",让每个工程工作单元都比前一个更容易. 提供完整工作流: Ideate → Brainstorm → Plan → Work → Review → Compound → Repeat,包含37个技能和51个代理,提供/ce:brainstorm、/ce:plan、/ce:work等专用命令. | Claude Code<br>Cursor<br>OpenCode<br>Codex<br>Droid<br>Pi<br>Gemini<br>Copilot<br>Kiro<br>Windsurf<br>OpenClaw<br>Qwen | ⭐⭐⭐ | 17,422 |
| [zhu1090093659/spec_driven_develop](https://github.com/zhu1090093659/spec_driven_develop) | 面向AI编码代理的结构化开发方法论,受钱学森工程控制论启发,采用闭环反馈控制保持计划与实际对齐. 纯Markdown实现,平台无关,6阶段流水线(项目分析→分阶段任务分解→文档驱动进度追踪→执行). 检测GitHub仓库时自动创建Issues、Milestones和Labels. | 任何能读Markdown的AI编码代理(Claude Code、Codex、Cursor等) | ⭐ | 887 |
| [awslabs/aidlc-workflows](https://github.com/awslabs/aidlc-workflows) | AWS Labs开发的AI驱动生命周期(AI-DLC)自适应工作流引导规则,为AI编码代理提供结构化软件开发工作流引导. 包含核心工作流规则、详细阶段特定规则和评估框架. 30+贡献者. | AI编码代理(通用规则,适配Claude Code、Codex等) | ⭐ | 2,673 |
| [ChenJazzyBoss/superSpec](https://github.com/ChenJazzyBoss/superSpec) | AI 原生规格管理工具, 为 Claude Code 提供自然语言到结构化规格文档的完整流水线. 核心功能包括: ① 规格生成(自然语言→含9条验证规则的结构化文档); ② 自动验证(检测缺失 SHALL、模糊用词、不完整场景); ③ 深度分析(--deep 模式:逻辑矛盾检测、覆盖缺口分析); ④ 自动图表(Mermaid 流程图/状态图嵌入); ⑤ 源码追踪(代码变更但 spec 未更新时警告); ⑥ Delta 合并(增量式 ADDED/MODIFIED/REMOVED 更新, 支持 dry-run); ⑦ 反幻觉(Red flag 表+完成清单+HARD-GATE 标签阻止 AI 跳步或伪造完成); ⑧ SkillGuard(程序化检测 AI 跳步模式); ⑨ 7阶段 DAG 工作流(brainstorm→generate-spec→validate-spec→write-plan→implement→verify→archive, 含前置/后置条件、上下文传递、失败重试). 技术栈: TypeScript 98.8%. 适用于需要严格规格驱动开发的团队、防止 AI 编码代理跳步或伪造完成的场景. | Claude Code | ⭐ | 75 |
| [s0912758806p/agentic-sop-to-work](https://github.com/s0912758806p/agentic-sop-to-work) | 将人工 SOP 转化为确定性、闸门式、人核准的 agentic 工作流, 杜绝臆造和 mega-agent 退化. 核心功能包括: ① 2支 Skills(agentic-sop 方法论入口+智慧意图分流, agentic-workflow-audit 唯读稽核者); ② 确定性编排引擎(4类硬闸门: cmd_gate/schema_gate/trace_gate/recompute_gate, 零LLM, fail即停); ③ ALCOA+ 资料完整性 linter(确定性检查+【待補】人工判断清单); ④ Plugin linter+scaffolder(plugin-forge); ⑤ Stop-hook 回归闸门; ⑥ 可攜 kit 复制到任何项目即可运行. 铁则: 事实只来自输入缺的标【待補】绝不杜撰, 确定性工作在代码闸门零LLM, 所有产出一律 DRAFT高风险判定人拥有. 技术栈: Python 99.2% + Go Template 0.8%. 适用于合规性要求高的团队、需要确定性编排而非"让AI自由发挥"的场景. | Claude Code | ⭐ | 179 |



### 1.1.2 Specification With Files
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [anombyte93/prd-taskmaster](https://github.com/anombyte93/prd-taskmaster) | AI 驱动的产品需求文档(PRD)生成技能, 为 Claude Code 和 Codex 提供从想法到完整验证 PRD 的自动化流程. 核心特性包括: ① 12+ 详细问题提取用户意图和需求; ② comprehensive PRD 模板生成(包含 executive summary、problem statement、goals & metrics、user stories、functional requirements、technical considerations 等 12 个关键章节); ③ Taskmaster 集成(自动创建 `.taskmaster/` 目录结构、放置 PRD、配置 `.gitignore`); ④ 13 种自动化质量验证(检查必需章节、测试性要求、SMART 成功指标、技术架构考虑、任务分解提示等); ⑤ CLAUDE.md/codex.md TDD 工作流指南(RED → GREEN → REFACTOR 循环、blind-validator agent 使用、并行任务执行、质量门控、agent 使用指南). 技术栈: Python 76.6% + Shell 23.4%. 使用场景: AI 辅助开发工作流中快速生成详细 PRD、使用 Taskmaster 等任务分解工具、需要详细规划再编码的团队、希望减少手动 PRD 编写时间的开发者. | Claude Code<br>Codex | ⭐ | 260 |
| [OthmanAdi/planning-with-files](https://github.com/OthmanAdi/planning-with-files) | 用文件规划任务, 像 Manus 那样工作. | Claude Code<br>Cursor<br>Codex<br>OpenCode | ⭐⭐⭐ | 18,339 |
| [nizos/tdd-guard](https://github.com/nizos/tdd-guard) | 一个为 Claude Code 设计的自动化测试驱动开发 (TDD) 强制执行工具. 确保 Claude Code 遵循 TDD 原则, 当代理尝试跳过测试或过度实现时, TDD Guard 会阻止操作并解释正确的做法. 核心特性包括测试优先强制执行、最小实现、 lint 集成、多语言支持、可自定义规则、灵活验证和会话控制. 支持 JavaScript/TypeScript(Vitest、Jest、Storybook)、Python(pytest)、PHP(PHPUnit)、Go 和 Rust 等多种语言和测试框架. 通过 Claude Code 钩子系统实现. | Claude Code | ⭐ | 1,975 |
| [wlzh/prd-manager](https://github.com/wlzh/prd-manager) | prd-manager v2.0.0, [kociii/prd-manager](https://github.com/kociii/prd-manager) 的升级版本, 一个辅助 Vibe Coding 的 Skill 工具, 通过生成结构化的版本需求文档(PRD、Design、Dev、Plan、Ops、Test), 指导 AI 进行 Coding, 提升 Coding 的准确性. 支持完整的文档生命周期管理(8 种文档类型)、语义化版本管理和测试驱动开发. 参见 [2026/06/01, AI搞钱研究院 @gaoqian2580, Vibe Coding 不翻车: 用 PRD-Manager 把脑子里的想法翻译给 AI](https://x.com/gaoqian2580/status/2057261855568191495).
| [piercelamb/deep-project](https://github.com/piercelamb/deep-project) | Claude Code 插件, 将模糊的软件想法转化为可单独规划的组件, 通过 AI 辅助访谈和分解过程, 确保考虑软件的每个主要组件并为 /deep-plan 做准备. 属于 The Deep Trilogy 系列的第一步, 与 /deep-plan 和 /deep-implement 一起构成完整的开发流程. | Claude Code | ⭐⭐ | 85 |
| [Archon](https://github.com/coleam00/Archon) | 开源的 AI 编码工作流引擎, 通过 YAML 定义开发流程, 使 AI 编码变得可预测和可重复. 核心特点包括: 可重复的工作流执行、隔离的 git worktree 环境、可组合的节点(bash 脚本、测试、git 操作与 AI 节点)、可移植的工作流定义. 技术栈以 TypeScript 为主(98.0%), 支持 Web UI、多种平台集成(Slack、Telegram、GitHub、Discord), 提供 17 个默认工作流. 适用于需要标准化开发流程、提高 AI 编码可靠性的场景. | Claude Code | ⭐⭐⭐⭐ | 19,000 |
| [stvlynn/agentic-coding](https://github.com/stvlynn/agentic-coding) | 语言和框架无关的 Agent 驱动项目模板, 任何 Agent 打开仓库应先读 AGENTS.md 获取规则、文档地图和演进策略. 提供完整文档体系: docs/project/(项目概览、架构、边界)、docs/frontend/(Feature-Sliced Design 约定)、docs/backend/(Domain-Driven Design 分层约定)、docs/operations/(开发、CI/CD、部署指南)、docs/quality/(测试与代码审查期望)、docs/decisions/(架构决策记录 ADR)、deploy/(Docker/Kubernetes 部署资产). 技术栈: Makefile 100%(纯模板仓库). 适用于需要标准化项目结构和文档体系、让 AI Agent 快速理解项目约定的团队. | 任何能读 Markdown 的 AI 编码代理 | ⭐ | 28 |



## 1.2 Long-Running/Long-Horizon
-------

[2026/05/13, 思维怪怪 @0xLogicrw, 智谱 AI 创始人兼首席科学家唐杰预测, 今年大模型的最大突破将是长周期任务(Long-Horizon Tasks), AI 能在真实环境中持续运转并解决复杂问题.](https://x.com/0xLogicrw/status/2054471661014098300)

[2026/06/08, 烟花老师 @teach_fireworks, 基于本地文件系统+git 仓库进行长时间运行 agent 的一种方式:](https://x.com/teach_fireworks/status/2063994579255464122)

[2026/06/02, 老金 @freeman1266, Spec + ReAct + Ralph: 这三层架构, 才是 Agent 长任务真正能跑通的工程基础.](https://x.com/freeman1266/status/2061712333131649086) 指出: 做 Agent 长任务, 你需要三层结构:

| 层级 | 项 | 概述 | 解决的问题 | 描述 |
|:---:|:--:|:---:|:---------:|:---:|
| 第一层 | Spec | 把任务拆清楚 | 解决任务定义 | 没有清晰的任务定义, Agent 只会做到哪算哪. Spec 的核心是把目标、验证条件、约束边界都写明白——不是写进 prompt, 而是挂到 Session 上, 让整个任务有一个持续存在的完成条件. |
| 第二层 | ReAct | 让模型进入执行现场 | 解决执行循环 | ReAct 的循环是: 思考 → 行动 → 观察 → 再思考.<br>Agent 才不是在"回答问题", 而是在"做事".<br>PlanAct 管规划, CodeAct 管代码行动, MultiAgent 管协作——但底层都跑在这个循环上. |
| 第三层 | Ralph | 在外面套一层 LoopControl | 解决完成判断 | Ralph 是外部控制器, 负责判断任务有没有真正完成. 模型觉得差不多, 不代表任务完成. Ralph 持续检查: 继续、暂停、完成, 还是停下来等人确认. |

### 1.2.1 Ralph-Loop
-------

Ralph 是一个基于 Geoffrey Huntley 提出的 Ralph 循环模式设计的 AI 编程工具, 旨在解决从 PRD 到可直接上线代码的自动化流程问题, 达成 Long-Running 开发. 它通过 Bash 循环脚本不断启动新的 AI 实例 (Amp 或 Claude Code), 逐条处理 PRD 中的任务, 直到所有事项完成为止. 核心设计每轮迭代使用全新上下文窗口, 通过外部存储(Git 历史、progress.txt、prd.json) 来获取状态, 避免了上下文累积的限制.

[Ralph Wiggum as a"software engineer"](https://ghuntley.com/ralph), 关于 Ralph (Ralph Wiggum) 技术的介绍.

[snwfdhmp/awesome-ralph](https://github.com/snwfdhmp/awesome-ralph), 关于 Ralph (Ralph Wiggum) 技术的精选资源列表, 包括官方资源、实践指南、实现、教程、文章、视频和社区资源等.

[微信公众号 --Amaker--AI 时代的软件开发新范式: Anthropic《Harness design for long-running application development》深度解读](https://mp.weixin.qq.com/s/yDf10mwBRfIZLOHcITZ3Iw)

[微信公众号 --CIT 云原生 -- 手搓了个 long-running-skill 和 Agent 开源教程网站](https://mp.weixin.qq.com/s/MKYwEIuWEJiKCbIaHhGiAw)

[微信公众号 --Assistant Hub -- Ralph让AI自主循环, 直到全部完成](https://mp.weixin.qq.com/s/E8txOLwW6gNPgp2GVZNpmw)

[微信公众号 --TecNote 技术思维 -- 长时间运行任务的实践方案](https://mp.weixin.qq.com/s/rThX118rOuAOjkZY_GZHxw) 介绍了 3 种 Ralph 达成 Long-Running 的实现思路. 三个层次: 架构层(Initializer + Coding)、流程层(Todo List 循环)、工具层(Background + Scheduled). 选择哪个取决于任务规模. 参见 [Autonomous Coding Agent Demo, anthropics](https://github.com/anthropics/claude-quickstarts/tree/main/autonomous-coding), 主体思路就是把连续的大任务拆成离散的小任务, 每个小任务都能独立完成、独立验证、独立回滚. 不管用哪个方案, 记住两点: 给 Claude 验证能力, 每次只做一件事.

| 方案 | 层级 | 描述 | 对应实现 | 适用场景 | 复杂度️ | 持续时间 |
|:---:|:----:|:---:|:-------:|:-----:|:-----:|:-------:|
| Initializer + Coding Agent | 架构层 | Anthropic 官方推荐的架构, 把任务拆成两种 agent, Initializer 初始化任务列表, 通过 progress 文档跟踪任务状态, Coding Agent 负责循环运行, 每次 session 只做一件事, 完成之后, 更新 progress 状态, 所有任务都完成后停止. | ⭐⭐⭐ | 14,688 | 高 | 数天 |
| Todo List 循环 | 流程层 | NA | NA | 中等任务 | 中 | 数小时 |
| Background Tasks | 工具层 | NA | NA | 监控类 | 低 | 持续运行 |

[datawhalechina 博客 -- 如何让 Claude Code 长时间工作](https://datawhalechina.github.io/easy-vibe/zh-cn/stage-3/core-skills/long-running-tasks) 采用循序渐进的方式, 由浅入深讲解了五种让 Claude Code Ralph-Loop/Long-Running 的方法. 依次是: ① While True Bash Loop(最原始的方法) Promp 方式, 类似于 [lidangzzz/goal-driven](https://github.com/lidangzzz/goal-driven), ② 极简插件 [anthropics/claude-plugins-official/ralph-loop](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/ralph-loop), ③ 增强插件 [frankbria/ralph-claude-code](https://github.com/frankbria/ralph-claude-code), ④ Agent Teams(多 Agent 并行), ⑤ 后台任务(Ctrl+B).

1. anthropics 官方的 [claude-plugins-official/ralph-loop](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/ralph-loop) 插件是 Ralph 的最简 (脚本 / 插件) 实现, 通过 [`/ralph-loop/ralph-loop` 的 Claude Code commands](https://github.com/anthropics/claude-plugins-official/blob/main/plugins/ralph-loop/commands/ralph-loop.md)来主导 Ralph 运行, 其 **核心机制是 [Stop Hook](https://github.com/anthropics/claude-plugins-official/blob/main/plugins/ralph-loop/hooks). 当 Claude 想要退出时, Stop Hook 会拦截这个退出信号. 然后系统会检查: 输出了特定的完成标记吗? 如果没有找到完成标记, 就重新注入原始 prompt, 开始下一轮迭代. 如果找到了完成标记, 才允许 Claude 退出**. 但是其每次迭代并不是一个干净的上下文, 只是把原始 prompt 和迭代计数重新喂给 Claude, 因此可能会浪费 Token.

2. [微信公众号 -- 技术极简主义 -- 从 PRD 到代码: Ralph 驱动的自治 AI 智能体执行循环](https://mp.weixin.qq.com/s/iVfaAJx4DuFuzihf0TouHA) 通过一次对 [snarktank/ralph](https://github.com/snarktank/ralph) 的工程实践案例, 这个工具提供了一个 [ralph skills](https://github.com/snarktank/ralph/blob/main/skills/ralph/SKILL.md), 可以 **将 prd.md 转换为 Ralph 能理解的 prd.json. 最后 [ralph.sh](https://github.com/snarktank/ralph/blob/main/ralph.sh) 会按照 prd.json 中制定的计划和任务来执行: 创建功能分支 -> 选择下一个任务 -=> 专注于单个任务的实现 -> 提交代码 -> 更新任务状态 -> 记录学习内容 -> 循环或退出**. 作者提供了一个[交互式的流程图](https://snarktank.github.io/ralph) 来了解 Ralph 的执行流. 这个工具并不是 Cluade 内置插件, 而是通过 [ralph.sh](https://github.com/snarktank/ralph/blob/main/ralph.sh) 启动 claude code 来运行, 每次迭代都是一个干净的上下文, 工作进度和状态通过文件系统传递, 而非对话上下文. 这样可以有效防止上下文窗口膨胀, 任务可重启, 方便调试. 脚本中缺乏 Orchestrator, 因此建议每次迭代的任务尽可能单一, 更适合串行任务. 当然可以在 Claude Code 中配置 Orchestrator 来组合使用.

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [autonomous-loops@everything-claude-code](https://github.com/affaan-m/everything-claude-code/blob/main/skills/autonomous-loops/SKILL.md) | 来自 everything-claude-code 项目的自主循环执行技能, 实现 Claude Code 的持续任务执行能力. 该项目是一个强大的 agent harness 性能优化系统, 包含 28 个子智能体、116 个技能包、59 个斜杠命令, 支持 12 种语言生态. autonomous-loops 技能可能类似于 Ralph Loop 机制, 通过循环执行确保任务完成, 结合项目的 continuous-learning-v2 系统实现技能的持续优化和跨项目复用. | Claude Code | ⭐⭐⭐⭐ | 147,133 |
| [code-yeongyu/oh-my-openagent/ralph-loop](https://github.com/code-yeongyu/oh-my-openagent/tree/dev/src/hooks/ralph-loop) | oh-my-openagent 项目中的 Ralph Loop 实现, 提供自引用开发循环功能. 基于 Geoffrey Huntley 的 Ralph Wiggum 技术, 通过 `/ralph-loop` 命令启动循环, 持续迭代直到代理发出 `<promise>DONE</promise>` 信号或达到最大迭代次数. 核心功能包括: 状态持久化到 `.sisyphus/ralph-loop.local.md`、会话崩溃恢复、自定义完成信号、最大迭代次数控制等. 技术实现基于 TypeScript, 集成到 OpenCode 插件系统中, 适用于长时间运行的 AI 开发任务、需要迭代改进的任务以及可以离开的新项目. 参见 [OpenCode + Oh My OpenCode 高级使用教程: 掌握 ulw、ralph-loop 与高效玩法.](https://www.cnblogs.com/gyc567/p/19483739) | OpenCode | ⭐⭐⭐ | 49,716 |
| [anthropics/claude-plugins-official/ralph-loop](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/ralph-loop) | 官方 Ralph Wiggum 技术实现, 通过 Stop hook 创建自引用反馈循环, 实现 Claude Code 的迭代开发. 核心功能: 使用 `/ralph-loop` 命令启动循环, 自动拦截退出尝试并重复执行相同提示, 直到完成任务. 支持设置最大迭代次数和完成承诺短语. 适用于有明确成功标准的任务、需要迭代改进的任务(如测试通过)、可以离开的新项目. | Claude Code | ⭐⭐⭐ | 16,389 |
| [snarktank/ralph](https://github.com/snarktank/ralph) | 基于 Geoffrey Huntley 的 Ralph 模式实现自主 AI 代理循环系统, 运行 AI 编码工具 (Amp 或 Claude Code) 重复执行直到所有 PRD 项目完成. 提供 [snarktank/ralph/prd](https://skills.sh/snarktank/ralph/prd) 和 [snarktank/ralph/ralph](https://skills.sh/snarktank/ralph/ralph) 两个 skills 和一套 ralph 脚本 [ralph.sh](https://github.com/snarktank/ralph/blob/main/ralph.sh). 每次迭代都是一个具有干净上下文的新实例, 记忆通过 git 历史、progress.txt 和 prd.json 持久化. 核心功能包括: 支持 Amp 和 Claude Code、PRD 生成和转换、自动分支创建、质量检查、提交管理和进度跟踪. | Amp CLI<br>Claude Code | ⭐⭐⭐ | 14,688 |
| [iannuttall/ralph](https://github.com/iannuttall/ralph) | Ralph 是一个最小化、基于文件的代理循环系统, 用于自主编码. 每次迭代从头开始, 读取相同的磁盘状态, 一次为一个故事提交工作. Ralph 将文件和 git 视为记忆, 而不是模型上下文. PRD (JSON) 定义故事、关卡和状态; 循环每次迭代执行一个故事; 状态持久化在 .ralph/ 目录中. 核心特点: 全局 CLI 工具、可自定义的模板层级、支持多种代理(Codex、Claude、Droid、OpenCode)、状态文件(progress.md、guardrails.md、activity.log、errors.log、runs). | Codex<br>Claude Code<br>Factory Droid<br>OpenCode | ⭐⭐ | 918 |
| [frankbria/ralph-claude-code](https://github.com/frankbria/ralph-claude-code) | Ralph Loop 的 Claude Code 增强实现, 提供 ralph 命令来实现迭代开发能力, 后端对接 Claude Code, 在官方插件的基础上增加了更多安全机制.<br>1. 双重退出条件. 官方 Ralph 只需要检查完成标记, 但增强版需要同时满足完成标记和显式 EXIT_SIGNAL 才会真正停止. 这意味着即使 Claude 输出了完成标记, 如果它没有明确表示要退出, 循环还会继续, 可以进一步验证和改进.<br>2. 速率限制功能. 默认设置为 100 次 / 小时, 防止因为某种 bug 导致无限循环时, API 账单爆炸. 你可以根据需要调整这个限制.<br>3. 智能熔断器. 如果系统连续 5 次检测到完成标记, 会强制退出. 这是为了防止某种边缘情况导致循环无法正常结束.<br>5. 实时仪表盘. 增强版提供了一个命令行界面, 可以显示当前迭代次数、任务进度、预估成本等信息, 让你随时掌握状态.<br> 只是每次并不重置上下文, 因此可能会造成累积上下文, 爆掉. | Claude Code | ⭐⭐ | 8,548 |
| [subsy/ralph-tui](https://github.com/subsy/ralph-tui) | Ralph 循环的 TUI 界面实现, 提供可视化的循环管理和监控功能. | 多平台 | ⭐ | 2,209 |
| [michaelshimeles/ralphy](https://github.com/michaelshimeles/ralphy) | 自主 AI 编码循环系统, 运行 AI 代理直到任务完成. 支持单一任务和任务列表两种模式, 多种 AI 引擎, 并行执行, 浏览器自动化等功能. 核心特点包括: 多引擎支持(Claude Code、OpenCode、Cursor、Codex、Qwen-Code、Factory Droid、GitHub Copilot、Gemini CLI)、并行执行(git worktrees 或 sandbox 模式)、多种任务源(Markdown、YAML、JSON、GitHub Issues)、项目配置和规则管理、webhook 通知等. | 多 Agent 支持 | ⭐ | 2,733 |
| [Th0rgal/open-ralph-wiggum](https://github.com/Th0rgal/open-ralph-wiggum) | 自主代理循环工具, 支持 Claude Code、Codex、Copilot CLI 和 OpenCode. 基于 Geoffrey Huntley 的 Ralph Wiggum 技术, 实现自主代理循环, 让 AI 编码代理重复接收相同的提示直到完成任务. 核心特点包括: 多代理支持、自我纠正循环、自主执行、任务跟踪、实时监控、中间循环提示注入等. 支持 Tasks Mode 进行结构化任务管理, 以及代理轮换功能. 技术实现基于 Bun 运行时, 状态存储在 `.ralph/` 目录中, 提供完整的 CLI 命令集和任务管理功能. | 多 Agent 支持 | ⭐ | 1,517 |
| [AnandChowdhary/continuous-claude](https://github.com/AnandChowdhary/continuous-claude) | 自动化工作流, 在连续循环中编排 Claude Code, 自主创建 PR、等待检查并合并, 使多步骤项目在你睡觉时完成. 核心功能包括持续循环执行、PR 生命周期自动化、上下文连续性、并行执行支持等. | Claude Code | ⭐ | 1,291 |
| [mikeyobrien/ralph-orchestrator](https://github.com/mikeyobrien/ralph-orchestrator) | Ralph Orchestrator 是一款轻量级、开源的 AI 工作流编排工具, 核心定位是「为提示词工程和 AI 任务协作提供结构化编排能力」, 主打极简部署、无代码 / 低代码操作、多 AI 模型适配. | 多 Agent 支持 | ⭐ | 2,482 |
| [superpowers@FradSer/dotclaude](https://github.com/FradSer/dotclaude) | dotclaude 是 Frad LEE 开发的一套专为 Claude Code 打造的插件合集, 其中对 superpowers 做了深度改造, 引入了 Superpowers Ralph-Loop 和 Work Verification 能力. 通过 hooks 来保证 Ralph 运行, task-start.sh 保存任务状态, stop-hook.sh 循环检查 + 验证, track-changes.sh 追踪修改文件.<br>1. Superpower Loop(循环模式), 通过 `/superpower-loop`(slash command) 启动, setup-superpower-loop.sh 启动后 LOOP_ACTIVE 被设置, 由于使用自引用循环, stop-hook.sh 每次讲相同的 prompt 被反复喂给模型, 每次迭代都能看到前次工作的文件变化, 因此可能存在上下文污染的问题. 当满足 <promise> 文本</promise> OR max_iterations 时循环结束.<br> 参见 [feat(sp): add ralph loop to superpowers v1.6.0](https://github.com/FradSer/dotclaude/commit/0171eb07e5aee98ef661abae397dd4c95590f82f) 和 [refactor(sp): rename ralph-loop to superpower-loop](https://github.com/FradSer/dotclaude/commit/b81fcb098cc4e54048c38e060480eefab32095ee).<br>2. Work Verification(验证模式), 通过 `/need-vet`(skills) 来启动, task-start.sh 启动后 NEED_VET 被置位, 任务完成后会启动验证流程, Stop hook 中则会等验证完成后输出 `<verified>Fully Vetted.</verifie>` 才允许退出. 参见 [feat(sp): add vet skill and update plugin metadata](https://github.com/FradSer/dotclaude/commit/d6013818a6395e90eb8b93b2d9f437959bfe7b2a) | Claude Code | ⭐ | 527 |
| [kunchenguid/gnhf](https://github.com/kunchenguid/gnhf) | ralph 风格的编排器, 让 AI 代理在用户睡觉时持续运行, 宗旨是 "Before I go to bed, I tell my agents:Good Night, Have Fun", 每次迭代都朝着目标做一个小的、已提交的、有文档记录的更改. 开箱即用(通过一个 gnhf 命令启动主循环)、长时间运行(成功迭代提交, 失败回滚)、 Agent 无关(支持 Claude Code、Codex、Rovo Dev、OpenCode)、增量提交、运行时上限控制、共享内存(通过 notes.md 跨迭代通信)、支持恢复. 适用于代码库复杂性降低、持续迭代开发等场景. | Claude Code<br>Codex<br>Rovo Dev<br>OpenCode | ⭐ | 310 |
| [yzddp/harnesscode](https://github.com/yzddp/harnesscode) | 基于 Harness 架构的长时无人值守 AI 驱动开发框架, 通过专业化 Agent 团队(Orchestrator、Coder、Tester、Fixer、Reviewer)协作完成开发任务, 支持 OpenCode 和 Claude Code 双引擎, 技术栈无关, 实现完全自主开发和人机协作. 核心特点包括持久化记忆、结构化执行和规范驱动工程. | OpenCode<br>Claude Code | ⭐ | 47 |
| [Git-on-my-level/codex-autorunner](https://github.com/Git-on-my-level/codex-autorunner) | CAR 是一个编码代理的元编排器(meta-harness), 不是编码代理本身. 它的核心理念是:「计划一次, 然后让你喜欢的编码代理在你睡觉时处理工单 — 当它们卡壳时通过 Telegram 或 Discord 通知你」. CAR 是一个状态机: 当有未完成的工单时, 选择下一个并针对代理运行它. 工单是控制平面, 代理是执行层. 支持 Web UI、CLI、Telegram/Discord 和 Project Manager Agent (PMA) 四种交互方式. 技术上以文件系统为一等数据平面, 依赖代理已熟悉的工具(git、python、markdown). 适用于需要运行长周期代理工作流的开发者. | Codex<br>Hermes<br>OpenCode | ⭐⭐⭐ | 777 |
| [ByBrawe/opencode-loop](https://github.com/ByBrawe/opencode-loop) | 为 OpenCode 提供 Claude Code 风格的自动继续循环功能, 使 AI 代理能在空闲时自动继续工作. 支持 TUI 插件模式和后台守护进程(opencode-loopd), 提供 15 个斜杠命令和丰富的控制选项(运行控制、验证机制、分支管理、停止控制). 核心功能包括自动继续循环、间隔循环、进度文件驱动、测试修复循环、压缩调度、Git 检查点、安全模式和多循环管理. 适用于长时间编码会话、TODO 自动化、测试驱动修复和定期维护任务. | OpenCode | ⭐ | 30 |
| [breezewish/CodexPotter](https://github.com/breezewish/CodexPotter) | 实现 Ralph Wiggum 模式的自动化工作流驱动器, 通过多轮审查和对齐机制确保代码符合用户要求. 采用 Rust(99.0%)实现, 核心特性包括 Codex-First 设计、Auto-Review/Reconcile、Clean-Room 模式、文件系统记忆、轻量级 Prompt(<1k tokens)、内置知识库和 Hooks 系统. 支持配置系统(TOML)、交互式命令和实验性 xmodel(gpt-5.2 先行, gpt-5.5 交叉审查). 适用于明确目标的任务、需要多轮迭代的任务、规划和执行分离的任务以及代码重构和优化. | OpenAI Codex CLI | ⭐ | 527 |
| [yzddp/harnesscode](https://github.com/yzddp/harnesscode) | AI驱动的Human-in-the-Loop开发框架,实现从PRD到完整代码的全自动化开发流程,采用Orchestrator、Coder、Tester、Fixer、Reviewer五个Agent协作架构,支持双引擎执行和技术栈无关 | OpenCode<br>Claude Code | ⭐ | 72 |
| [michaelshimeles/ralphy](https://github.com/michaelshimeles/ralphy) | 自主 AI 编码循环工具, 持续运行 AI 代理直到任务完成. 支持 8 种 AI 引擎(Claude Code、OpenCode、Cursor、Codex、Qwen-Code、Factory Droid、GitHub Copilot、Gemini CLI). 核心功能包括: ① 单任务模式(ralphy "add dark mode"直接执行); ② 任务列表模式(从 PRD.md/YAML/JSON/GitHub Issues 读取逐项执行); ③ 并行执行(多代理并行, 每代理独立 worktree/分支); ④ 分支工作流(--branch-per-task+--create-pr 自动分支与 PR); ⑤ Sandbox 模式(符号链接替代 worktree, 适合大型仓库); ⑥ 浏览器自动化(--browser 启用 agent-browser); ⑦ Webhook 通知(Discord/Slack); ⑧ 项目配置(--init 生成 .ralphy/config.yaml); ⑨ 重试与容错(--max-retries、自动回退 sandbox、检测 rate-limit); ⑩ GitHub Issue 同步(--sync-issue 实时同步 PRD 进度到 Issue). 技术栈: TypeScript 75.8% + Shell 23.2%. 适用于长时间运行的编码任务、需要多代理并行处理的团队、PRD 驱动的迭代开发场景. | Claude Code<br>OpenCode<br>Cursor<br>Codex<br>Qwen-Code<br>Droid<br>Copilot<br>Gemini CLI | ⭐ | 2,887 |



### 1.2.2 Goal-Driven
-------


#### 1.2.2.1 Goal Long Running
-------

Goal-Driven 的 Long-Running/Long-Horizon 则通过 Prompt Engineering + Suagent Workflow 协作的方式, 保证 Agent 达成 Goal 目标.

1. 立党大佬的插件 [lidangzzz/goal-driven](https://github.com/lidangzzz/goal-driven) 是 Ralph 的最简 (提示词) 实现, **通过一套标准的目标驱动 (Goal-Driven) 的提示词, 组合 subAgent 来保持 Ralph 运行**. 其要求 Ralph ① 目标 (Goal): 必须以 goal 作为 alignment 的唯一目标, ② 成功标准(Criteria): 必须设计一个以大量 test 作为唯一评判标准的 criteria, ③ 主智能体(Master Agent) 和子智能体(Subagent): 必须设置一个 master agent 来 supervise 你的真正执行任务的 subagent, 时刻确保向着 goal 方向推进. 核心理念非常简单: 当 Goal-Driven 流程启动时, 主智能体创建一个子智能体, 并指示它持续致力于解决问题并达成目标.<br> 主智能体定期检查子智能体是否活跃. 如果子智能体变得不活跃、声称完成或进入空闲状态, 主智能体必须根据标准评估当前结果. 如果结果未能满足标准, 它会命令子智能体继续工作, 重复这个循环直到标准被满足. 一旦子智能体的输出满足标准, 系统停止并宣布成功完成. 参见 [
lidang 立党 @lidangzzz, 只有人类设置一个目标(goal), 一个判据(criteria, 比如几百个unit test), 一个master agent执行判据, 监督subagent,
一个subagent无限循环工作, 才能把人的工作彻底解放出来. ](https://x.com/lidangzzz/status/2044235116281471169).

2. OpenAI Codex 0.128.0 引入了 `/goal` 来支持 Long-Running. 参见 [OpenAI Codex /goal: The New Long-Horizon Mode for Agentic Coding](https://kingy.ai/ai/openai-codex-goal-the-new-long-horizon-mode-for-agentic-coding). /goal 允许用户为 Codex 定义一个更长期的目标, 而不是一次发出一条孤立指令. 与其让 Codex "下一步做这件事", 不如给它设定一个目标, 并且一直与线索相关. 实现后, Codex 提供了持久状态记录、应用-服务器 API、受限模型工具、运行时延续行为以及终端界面控件以管理该目标. `/goal` 为用户提供了一套指令, 用于 `/goal <objective>` 创建目标、查看、 `/goal pause` 暂停、`/goal unpause` 继续和 `/goal clear` 清除目标. 参见 [2026/06/04, bbshare @shadouyoua, Codex Goal Mode 入门: 怎样给 AI 设目标、验收标准, 让它持续干活](https://x.com/shadouyoua/status/2062433257522897183)

> 参见 Codex 源代码 [codex-rs/core/templates/goals](https://github.com/openai/codex/tree/main/codex-rs/core/templates/goals), 通过 Prompt Engineering 来完成协作, 其中:
> objective_updated.md 更新 Goal, 引导 AGENT 调整工作方向; 目标更新后, AGENT 调整当前 turn, 放弃只服务于旧目标的工作.
> continuation.md 负责自动续接, 当系统空闲(无活跃 turn、无队列输入)且 Goal 状态为 Active 时, 向 AGENT 注入该 Prompt, 从而引导 AGENT 继续推进目标; 该工作 ① **强调**目标持久性: 一个 turn 结束不代表目标完成; ② **要求**保真执行: 不缩小目标范围, 不做"最小安全子集". ③ **完成**审计规则: 必须逐项验证每个需求, 禁止部分完成就标记 `complete`. ④ **显示**预算信息:  tokens_used/token_budget/remaining_tokens.
> budget_limit.md 进行预算限制, 指导 AGENT 收尾并总结进展: 如果已达到 token 预算(`tokens_used >= token_budget`), 但是 Goal 可能仍未完成, Goal 状态自动转为 `BudgetLimited`, 并通知 AGENT  指导收尾工作, 总结进展、指出剩余工作、给用户清晰下一步. 明确禁止继续实质性工作.

3. 随后社区有大佬将 Codex 的 `/goal` 实现移植到了 Claude Code, 参见 [2026/05/10, 雪踏乌云 @Pluvio9yte, 这篇文章写了如何把 OpenAI Codex 最新内测的 `/goal` 命令, 完整复刻成 Claude Code 的自定义 Skill](https://x.com/Pluvio9yte/status/2053350405661430175), 原文 [2026/05/09, 实践哥MinLi @MinLiBuilds, 一个Skill让Claude Code智力加满](https://x.com/MinLiBuilds/status/2053099063982407818). 三个实现技巧: 技巧1: 把用户目标包成 `<untrusted_objective>` 格式的数据, 而不是指令(防 prompt 注入). 技巧2: 所有要求都写得极度具体, 绝不用"认真", "仔细", "所有"这类虚词. 技巧3: 一句话改默认值, 把模型的"乐观偏见"扭成"悲观"(不确定 = 未完成). [2026/05/08, 微信公众号--Feisky--Codex /goal 上线后, 我把 Ralph loop 卸了](https://mp.weixin.qq.com/s/qwjxsGpMacLNy93g6dz4Aw)

4. 紧随其后的是, Hermes Agent [v0.13.0 (v2026.5.7)](https://github.com/NousResearch/hermes-agent/blob/main/RELEASE_v0.13.0.md) 也实现了 `/goal` 的支持.

4. 紧随其后, Claude Code [2.1.139 (v2026/05/11) 也推出了 `/goal`](https://www.claudeupdates.dev/version/2.1.139).  Anthropic 把整个 pattern 包装成一行命令: `/goal <完成条件>`. 背后猜测可能还是 `prompt-based Stop hook`, 但引入了独立的 `Haiku` 模型当评估器, 替代原来 [claude-plugins-official/ralph-loop](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/ralph-loop) 等实现上简单的字符串匹配. 参见 [微信公众号--码读时光--一文讲透 Claude Code 的 /goal 功能](https://mp.weixin.qq.com/s/9pibBDS-S1IXM2k1-CFWQw) 和 [Claude Code Docs/Keep Claude working toward a goal](https://code.claude.com/docs/en/goal). Anthropic 旧的 Ralph 实现是 「考试只看最后那道选择题填了啥」. 你做的过程对不对它判不了, 只能看你最后那张写有「我做完了」的纸条. 这就是 「字面裁判」. 而 `/goal` 是 「考试请了个真人阅卷老师」. 它能读懂你过程里的每个步骤, 告诉你「还差第 3 题没答」. 这就是 「智能裁判」.


| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [lidangzzz/goal-driven](https://github.com/lidangzzz/goal-driven) | 立党大佬的插件, 通过 Prompt 来实现目标驱动的多智能体系统, 通过主代理 + 子代理架构实现超过 300 小时的复杂问题解决能力. 采用循环验证机制: 主代理创建子代理执行任务, 每 5 分钟检查进度, 根据预定义标准评估结果, 未达标则继续循环直至成功. 适用于编译器设计、数学定理证明、数据库架构等高度复杂、逻辑抽象的系统级任务. 已实践项目包括 C++ 实现的 TypeScript 编译器、Rust 实现的 SQLite 等. | Claude Code<br>Codex<br>OpenClaw | ⭐ | 695 |
| [tolibear/goal-maker](https://github.com/tolibear/goal-maker) | GoalBuddy - OpenAI Codex 本地辅助工具, 解决开放性、长期运行的 Codex 任务容易偏离目标、缺乏验证和过早完成的问题. 将模糊需求转化为可审查的目标板、角色分工的任务系统(Scout/Judge/Worker)和结构化的收据和验证机制. 核心特性包括智能 intake(需求摄入)、任务板管理、收据系统、12+ 可选扩展模块和 CLI 工具. 适用于开放性长期任务、高风险多日执行、多步骤规划执行和恢复/审计场景. | OpenAI Codex | ⭐ | 142 |
| [fitchmultz/pi-codex-goal](https://github.com/fitchmultz/pi-codex-goal) | 为 Pi 终端 AI 编码代理提供的 Codex 风格目标跟踪工具, 添加 `/goal` 命令和 get_goal/create_goal/update_goal 三个模型可调用工具. 目标状态存储在 Pi 会话中, 无需外部数据库, 支持目标创建、暂停、恢复和 Token 使用跟踪. | Pi | ⭐ | 38 |
| [tolibear/goalbuddy](https://github.com/tolibear/goalbuddy) | GoalBuddy 是 Codex 和 Claude Code 的长期目标驱动辅助工具, 提供 `/goal` 命令和本地工作空间(charter、board、notes、receipts), 采用 Scout/Judge/Worker 角色分工, 实现目标分解、仓库映射、任务分配和验证循环. | Claude Code<br>Codex | ⭐ | 317 |
| [limin112/claude-goal-skill](https://github.com/limin112/claude-goal-skill) | 一个 Claude Code skill, 把 OpenAI Codex CLI 的 /goal 命令移植到 Claude Code 上. 你给一个长期目标, 它一轮一轮自己往前推, 直到完成或被暂停. | Claude Code/OpenCode | ⭐ | 13 |
| [flyingsquirrel0419/oh-my-goal](https://github.com/flyingsquirrel0419/oh-my-goal) | 为 OpenCode 提供 Codex 风格的自主执行能力. 用户只需设置一个目标(如 "/goal fix the flaky login test"), AI Agent 会持续执行直到任务完成、受阻、暂停或超出预算. 该插件专注于简单轻量, 而非复杂的多 Agent 协调. 核心特性包括一行式自主执行、项目本地状态存储(.opencode/goal.json)、智能续循环、完成检测机制(GOAL_ACHIEVED/GOAL_BLOCKED)、预算保护、压缩安全等. 支持多种控制命令(status、pause、resume、clear)和可配置预算参数(--token-budget). 技术栈: TypeScript + Node.js + npm + OpenCode Plugin API + JSON 状态存储. 适用于修复特定 Bug、提升测试覆盖率、完成单一明确的开发任务等场景. | OpenCode | ⭐ | 0 |
| [mirsella/opencode-goal](https://github.com/mirsella/opencode-goal) | 为 OpenCode 提供 Codex 风格的 /goal 命令, 实现长时间运行任务的自动继续功能. 解决复杂多步骤任务在会话空闲中断的问题, 让 OpenCode 能够持续追踪和执行目标直到完成. 提供完整的 /goal 命令集(创建、显示、追加、暂停、resume、清除), 利用 session.idle 事件驱动自动继续, 状态持久化到磁盘(~/.local/state/opencode-goal)支持会话重启恢复, 提供 update_goal 工具标记任务完成并停止循环, 活跃时间追踪. 技术栈: TypeScript 100% + Bun + OpenCode server plugin API. 适用于复杂多步骤开发任务(重构、迁移、大型功能开发)和长时间运行的工作流场景. | OpenCode | ⭐ | 2 |
| [prevalentWare/opencode-goal-plugin](https://github.com/prevalentWare/opencode-goal-plugin) | 为 OpenCode 提供 Codex 风格的长时间运行目标模式. 让 AI Agent 在明确的长期目标下持续工作, 直到完成或遇到阻塞, 解决 Agent 容易偏离目标或提前终止的问题. 提供目标命令系统(/goal 命令集)、Agent 工具套件(get_goal、create_goal、set_goal、update_goal、clear_goal)、目标完成机制(需提供验证证据)、UI 可视化(侧边栏目标指示器)、会话级持久化($XDG_DATA_HOME/opencode-goal-plugin/goals.json)、可选自动续期功能、可配置选项(auto_continue、max_auto_turns、min_continue_interval_seconds 等)和分离的 server/tui 模块架构. 技术栈: TypeScript 98.7% + JavaScript 1.3% + Bun + React + OpenCode Plugin API. 适用于长时间运行的复杂编程任务、需要明确范围和验证路径的任务、跨多文件的系统性改造等场景. | OpenCode | ⭐ | 2 |
| [jthack/claude-goal](https://github.com/jthack/claude-goal) | 为 Claude Code 提供 Codex 风格的 /goal 命令功能, 让 Claude 自主持续工作直到完成指定的工程目标(如 API 迁移、重构、修复测试等), 无需用户每个回合手动重新提示. 采用 Python + SQLite 实现持久化目标状态(存储在 ~/.claude/goal/goals.sqlite), 提供完整的生命周期控制(/goal pause、resume、clear、status), 通过 Stop Hook 阻止 Claude 在目标活跃时停止, 支持 Token 预算管理(--tokens 参数)、时间追踪、完成审计防护(需通过审计才能标记完成)、防失控保护(默认最多 500 次 Stop-hook 继续, 可配置环境变量 CLAUDE_GOAL_MAX_STOP_CONTINUES)、线程级持久化(支持 /resume 后继续). 使用小模型(Haiku)评估完成条件. 技术栈: Python 95% + Shell 5% + SQLite + Claude Code Skills 系统 + Stop Hook. 适用于长周期工程任务(API 迁移、包重构、模块升级)、测试修复循环(修复 flaky 测试、提升覆盖率)、Bug 追踪与修复、研究与原型开发、会话中断恢复等场景. | Claude Code | ⭐ | 80 |
| [smallnest/goal-workflow](https://github.com/smallnest/goal-workflow) | Goal Workflow 是一套基于 Claude Code / Codex 的 AI 研发工作流技能集, 将软件开发的完整生命周期拆分为四个标准化步骤(① `/prd`--需求规划, `/prd-to-spec`--PRD 转技术方案; ② `/goal`-功能实现; ③ `/review-it`--代码审查; ④ `/ship-it`--提交交付), 每一步都由一个专属 Skill 驱动. 它让 AI Agent 能够像一个有经验的工程师一样——从理解需求、拆解任务、编写代码、审查质量, 到最终提交合入——全流程自主完成. 你只需描述功能想法, 剩下的交给工作流. [2026/05/18, 微信公众号--百度 Geek 说--PRD → Goal → After-Goal: AI 主导全流程研发实践](https://mp.weixin.qq.com/s/0dSfok0fLN-OTIIYIYZ5rg), [官网](https://goal.rpcx.io). | Claude Code<br>Codex<br>OpenCode | ⭐ | 34 |


#### 1.2.2.2 Super Meta Goal
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [robzilla1738/supergoal](https://github.com/robzilla1738/supergoal) | 规划并自主构建软件任务的端到端工具, 生成一条可直接粘贴的 /goal 命令, 自适应阶段数, 记忆预加载+写回, 3-strike 自愈恢复. 核心功能包括: ① 深度规划(/supergoal 触发7阶段: 加载记忆→意图收集→并行侦察→风险识别→自适应分阶段→写入规格→自我批判+计划审查+预检); ② 一次性自治执行(生成可直接粘贴的 /goal 命令, 粘贴后全自动执行所有阶段); ③ 3-strike 自愈恢复(失败自动重试→写修复规格内联执行→3次失败交还人工); ④ 记忆读写(每阶段结束自动写入学习内容, 未来任务自动加载相关记忆); ⑤ 最终审计(重新对照 ROADMAP 验收、重跑构建/lint/测试、跨阶段回归检测、最多3轮自修复); ⑥ 运行隔离(.supergoal/<slug>-<id>/ 独立目录); ⑦ 清洁度检查(grep 检查未清理的 debug 输出、临时 TODO、死代码导入). 技术栈: Shell 100%(纯脚本). 适用于需要端到端自主规划+执行+验证的长期开发任务. | Claude Code<br>Codex CLI | ⭐ | 331 |
| [joeseesun/qiaomu-goal-meta-skill](https://github.com/joeseesun/qiaomu-goal-meta-skill) | 将模糊或复杂的 Codex 任务转化为带验证、约束、边界、迭代策略、完成证据的强力 /goal 命令. 核心功能包括: ① 模糊需求转可执行 goal(将"帮我做个 App"转化为带 Outcome/Verification/Constraints/Boundaries 的 /goal 指令); ② 推荐执行版优先(默认生成可直接复制的完整 /goal 命令含中文版); ③ 高风险暂停机制(凭证/账号/支付、生产数据、法律/医疗/金融判断自动写入暂停条件); ④ 陌生领域发现优先(医疗、金融等专业领域生成"先发现再实现"的 goal); ⑤ 模糊词转验证("高级""专业"等词翻译成设计方向、截图检查、3轮视觉改进); ⑥ 本地质量检查 linter(lint_goal_command.py 拦住不可执行前缀、占位符、空验证、宽权限、无限重试). 技术栈: Python 100%. 适用于开发网站/App/游戏/插件/脚本、修 bug/重构/加测试、UI 设计原型等需要将模糊想法转化为可执行目标命令的场景. | Claude Code<br>Codex | ⭐ | 626 |


### 1.2.3 Loop-Driven
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [Loops](https://loops.elorm.xyz/loops) | 专门收集各种现成的 Agent Loop 模板, 核心理念: 别再一直手动 prompt 了, 设计好 loop 让 agent 自己跑完任务. 里面有 Test Until Green、Fix CI Until Green、Build Until Green 等常用 loop, 每个都配好了目标、检查命令和退出条件. 把 Loop Engineering 从理论落地成可操作的工具. 特别适合用 Claude Code 和 Cursor 的朋友, 直接复制就能用. [2026/06/15, 码良 @cxjwin, 发现一个很实用的网站, 专门收集各种现成的 Agent Loop 模板.](https://x.com/cxjwin/status/2066210637311860916) | ALL | ⭐ | 暂未开源 |
| [valkor-ai/loom](https://github.com/valkor-ai/loom) | Loop Engineering 驱动的编码代理交付框架, 将每个需求变成"规划-构建-验证-修复-预览-移交"的自适应循环. 核心功能包括: ① 动态工作流路由(将交付目标转化为自适应循环: 澄清→规划→执行→验证→修复→交付); ② 项目本地交付状态(.loom/ 目录持久化存储上下文、任务合约、审查结果); ③ 任务合约(将宽泛目标拆分为有边界的任务含源引用、验收意图、结果文件); ④ Token 节省上下文包(项目摘要、任务图替代每次全量重读仓库); ⑤ 验证-修复循环(烟雾测试→检查→日志→错误摘要→修复请求→再验证); ⑥ 多 Agent 协议(支持 Claude Code、Codex、OpenCode 共享同一交付流程); ⑦ 需求澄清智能(确认范围、业务规则成为结构化上下文); ⑧ 后端就绪追踪(DB、认证、存储、函数作为交付状态的一部分); ⑨ 本地部署预览(Docker Compose 本地预览、验证、修复指引). 技术栈: TypeScript 61.5% + JavaScript 38.5%. 适用于需要标准化交付流程、中断后可从断点继续的长期开发任务. | Claude Code<br>Codex<br>OpenCode | ⭐ | 272 |
| [Loops.fyi](https://loops.fyi/) | 可复用 Agent 循环的目录网站, 为 Claude Code、Codex、Cowork、Cursor 等平台提供精选、可运行的 Agent 循环模式和 Harness. 提供循环目录浏览(按类别、字母序、最新筛选)、键盘导航(j/k 移动)、一键安装(复制命令直接粘贴到 Agent CLI)、社区提交和官方插件集成(Anthropic Ralph 插件) 适用于需要快速找到现成 Agent Loop 模板的开发者. | Claude Code<br>Codex<br>Cowork<br>Cursor | ⭐ | 暂未开源 |
| [Loop Library](https://signals.forwardfuture.ai/loop-library) | Loop 不是孤立的 prompt, 将其可复用、可迭代的工作单元. Matthew Berman 创建的 Loop Library, 目标就是让大家不用每次都从零设计 loop. 把各种 agent loop 集中起来, 找现成模板、提交自己的, 一键就能用. 这个仓库专门收集可直接拿来用的 agent 循环流程, 从简单的任务自动化到复杂的多步工作流. 想找现成的就去搜, 想贡献自己的就直接提交. 以前做 agent 最费时间的就是设计循环结构: 怎么退出、怎么验证、怎么处理失败. 这其实在把agent开发从"每次都要重新发明轮子"往"搭积木"方向推. 把这些loop开源和社区化, 相当于给agent生态建了一个公共的"流程市场". | Cluade Code | ⭐ | 暂不开源 |

## 1.3 Workflow
-------

[Awesome Workflow Automation Software, Tools & Apps](https://github.com/dariubs/awesome-workflow-automation)

### 1.3.1 WorkFlow
------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [pony-maggie/code_minions](https://github.com/pony-maggie/code_minions) | AI 原生的软件研发交付工作流引擎, 打通从 PRD 到代码实现、验证、审查、交付报告再到 GitHub PR/GitLab MR 的完整研发闭环. 核心架构包括工作流引擎(DAGRunner)、技能运行时、Git Worktree 隔离和质量门禁. 内置 4 个工作流(hello-world, summarize-file, prd-to-commit, prd-to-pr)、4 种技术栈预设、7 个技能(parse-prd, plan-tasks, create-jira-tickets, implement-with-tdd 等)和 Web Dashboard. 支持多模型提供商(Anthropic, OpenAI, Gemini, DeepSeek, MiniMax, Ollama)和 MCP 协议集成. 适用于自动化需求交付、技术债务清理、TDD 和多技术栈项目. | 多平台支持 | ⭐ | 111 |
| [fabro-sh/fabro](https://github.com/fabro-sh/fabro) | 面向专家工程师的开源暗软件开发工厂, 通过确定性工作流图(Graphviz DOT)约束非确定性 AI 代理. 核心特性包括确定性工作流图、人在回路审批、多模型路由(CSS 样式表方式)、云沙箱执行(Daytona)、Git 检查点、自动回顾和完整 API(REST + SSE + React Web UI). 支持 9 种 AI 平台(Anthropic, OpenAI, Gemini, Inception, Kimi, Minimax, ZAI 等)和 Brave Search、GitHub、Slack 集成. 适用于延长脱离时间、集成智能、团队最佳实践、降低 Token 成本、提高代理安全性、24/7 运行和复合工程. | 多平台支持 | ⭐ | 762 |


### 1.3.2 控制流
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [narcotic-sh/modafinil](https://github.com/narcotic-sh/modafinil) | macOS 菜单栏应用, 防止 MacBook 合盖时进入睡眠, 同时允许显示器正常关闭以节省电量. 专为让编码代理在携带 MacBook 移动时持续运行而设计, 支持 Apple Silicon 和 macOS 13+. | macOS | ⭐ | 81 |
| [regent-vcs/re_gent](https://github.com/regent-vcs/re_gent) | AI 代理活动的版本控制系统. 跟踪代理执行了哪些操作、哪个 Prompt 写了哪行代码, 并在出错时回滚. 提供 rgt log(活动历史)、rgt blame(代码行来源)和 rgt show(完整上下文)等命令, 基于 BLAKE3 + SQLite 实现. | Claude Code<br>多 Agent 支持 | ⭐ | 383 |
| [fu5ha/pi-treebase](https://github.com/fu5ha/pi-treebase) | Pi 终端 AI 编码代理的会话历史管理工具, 结合 `/tree` 命令和类似 `git rebase --interactive` 的功能. 支持 Pick(保留)、Low/High(低/高重要性摘要)或 Drop(删除)操作, 创建新的合成历史分支. | Pi | ⭐ | 28 |


# 💻 2 Agent 专业化(Agent Specialization)
-------


[《织·经 Claude Code 多 Agent 编排实战手册》](https://github.com/AGI-is-going-to-arrive/workflow-cookbook)
[Amazon Bedrock AgentCore Samples, Deploy and operate AI agents securely at scale - using any framework and model](https://github.com/awslabs/agentcore-samples)


| 领域 | 描述 |
|:---:|:----:|
| Agent Teams | 理念是 "用 AI 组建团队(公司)", 专注于特定领域、拥有受限工具的 Agent 优于拥有全部权限的通用 Agent. 通过配置多种 Agent 角色来辅助工作. |
| (sub)Agent Team Orchestrator | 构建一套智能体元编程编排器, 对于复杂的任务, 通过组合 subAgent 或者 Agent Team 自适应进行任务分解, 派发, 执行和调度的工作流控制. |
| (multi)Agent Parallel Workflow | Agent Parallel Workflow 致力于组合多个 Agent 协同工作, 通过 Parallel Workflow 完成多 Agent 并行编排和管理. 最终组合多个 Agent 协同工作, 保障复杂任务的高效完成. |
| Agent Operating System | 端到端 Agent 编排工作流, 将 Agent 变成一个公司, 变成一个操作系统. |


> 一句话描述
>
> Agent Spec Driver 致力于通过项目的规范化流程, 约束 AGENT 执行, 防止 AGENT 跑偏.
>
> (sub)Agent Team Orchestrator 是通过单个 Coding Agent 通过配置多个 subAgent 组成 Agent Team, 从而能完成复杂工作的开发与验证.
>
> Agent Parallel Orchestration 则组合多个 Coding Agent 的能力, 并行工作, 从而可以完成整个完整项目的设计与开发.


[2026/04/14, 岚叔 @LufzzLiz, Anthropic 出了一篇多 Agent 协作模式指南, 总结了 5 种架构和适用场景. ](https://x.com/LufzzLiz/status/2043839678252761117)

[Multi-agent coordination patterns: Five approaches and when to use them](https://claude.com/blog/multi-agent-coordination-patterns)

[2026/04/14, KK.aWSB @KKaWSB, Anthropic刚发了官方指南: 五种多Agent协作模式, 从"一人干活一人检查"到"去中心化黑板协作". ](https://x.com/KKaWSB/status/2043997692599382385)

[2026/05/28, Addy Osmani @addyosmani, The Orchestration Tax](https://x.com/addyosmani/status/2059844244907696186)
[2026/05/29, Viking @vikingmute, The Orchestration Tax 解读](https://x.com/vikingmute/status/2060289011579859152)
[2026/05/29, 陈成 @chenchengpro, The Orchestration Tax 解读](https://x.com/chenchengpro/status/2060256868958892308)

[2026/05/29, 老金 @freeman1266, (译)用动态工作流大规模编排子 Agent](https://x.com/freeman1266/status/2060274657807540382)

[2026/05/31, 土豆本豆 @Potatoloogs, 目前Agent的发展分成了两条路线. 大部分讨论都集中在第一条上, 但第二条可能更值得关注.](https://x.com/Potatoloogs/status/2060982941711491494): 第一条: Harness 式多 Agent 系统, 第二条: Protocol-Native Agent System.

[2026/05/18, Russell @Russell3402, 多智能体协作调查: Agent 到底该怎么分工](https://x.com/Russell3402/status/2056331558223786416) 从触发, 拓扑和调用链几个维度对多智能体协作进行了分类, 并分析了 Codex、Claude Code、OpenClaw、Hermes Agent 是怎么做多智能体协作的. 最终总结出一套多智能体协作的方法论, 工程上更稳定的顺序是: (触发方式上)先决定调度方式, 再决定状态放哪里; (拓扑结构上)先决定上下文和权限边界, 再决定拓扑; (调用链)先决定谁 reduce, 再决定开几个 worker. 如果一个任务只是需要更快地查四条线, 用星型 subagents. 如果一个问题需要多方互相挑战, 用 team mesh. 如果消息来自不同渠道和身份, 用 Gateway routing.
如果任务要跨天、重试、等待人类, 用 durable board. 如果多个 worker 会写同一片代码, 先停下来, 把 ownership 写清楚. 先设计边界, 再增加 agent 数量.
这个顺序不会显得炫, 但它更接近真实工程.

第一个问题是触发: 系统什么时候从单 agent 变成多 agent?

| 触发方式 | 描述 | 举例 |
|:-------:|:---:|:---:|
| 显式触发 | 用户直接说"use parallel subagents", "spawn one agent per review category", "delegate this work in parallel". | Codex 主要属于这一类. 它不会因为任务看起来复杂就擅自开一堆 worker, 而是把并行授权留给用户和主 agent. |
| 语义触发 | 主 agent 根据任务内容和 subagent description 判断是否调用某个专家 agent. | Claude Code 的普通 subagent 主要属于这一类. description 写得越像触发条件, 系统越容易在合适的时间调用它; description 写得越像一句愿望, 系统越容易乱叫人. |
| 路由触发 | 系统不是先问"这个任务复杂吗", 而是先看消息来自哪里. | OpenClaw 会根据 channel、account、thread、peer、guild、role 等入口信息选择 agent. Slack ops channel 进 ops agent, 私人 Telegram 进 deep work agent, 家庭入口进低权限 assistant. |
| 队列触发 | 任务被写进 board、queue、cron 或 background job, 由 dispatcher 按状态和 assignee 拉起 worker. | Hermes Kanban 属于这一类. 这里的关键不再是本轮对话里能不能马上返回, 而是任务能不能跨 turn、跨天、跨重启、跨人类介入. |

第二个问题是拓扑: 一旦变成多 agent, 它们怎么组织？是主 agent 派几个 worker 后统一收口, 还是 worker 之间能互相通信？是当前 turn 里等结果回来, 还是把任务放进持久队列, 明天再继续？


| 拓扑结构 | 形态 | 描述 |
|:-------:|:---:|:---:|
| 单 agent | 默认形态. | 需求模糊、修改很小、步骤强依赖时, 单 agent 往往最稳定. 很多任务不需要多智能体, 只需要更好的上下文和更短的反馈循环. |
| 星型 fan-out/fan-in | 最常见的 subagent 形态. | 一个主 agent 派多个 worker, worker 之间不直接协商, 结果回到主 agent, 主 agent 做 reduce. Codex subagents、Claude 普通 subagents、Hermes delegate_task 都主要是这种结构. 它的优点是责任中心清楚, 缺点是 worker 之间不能互相纠错, 所有冲突都压到主 agent 的 merge 阶段. |
| 链式 pipeline | 适合强顺序任务. | 比如先定位 bug, 再写修复, 再补测试, 再 review. 硬把这种任务并行化, 通常只会让后面的 worker 在错误假设上浪费时间. |
| 树型 | 适合大任务分层. | main agent 派一个 orchestrator, orchestrator 再派几个 leaf worker. 树型看起来强, 但要严格限制 depth 和并发, 否则 fan-out 会指数级膨胀. OpenClaw 和 Hermes 都把默认深度压得很低, 就是在控制这个风险. |
| 网状 team | 适合多假设问题. | 比如生产登录故障可能来自前端状态、后端 token、数据库 session、缓存或部署配置, 多个 teammate 可以分别验证假设, 并互相挑战. 网状结构的代价也很直接: 消息更多、上下文更多、协调成本更高, 写文件冲突也更容易出现. |
| Gateway routing | 适合常驻多入口系统. | 它不是"一个任务拆给多个 agent", 而是"不同入口进入不同 agent". OpenClaw 的多 agent 价值, 很大一部分在这里. |
| Durable board | 适合长期协作. | 任务、评论、handoff、阻塞状态、重试记录都落到持久化存储里. |

```cpp
input event
  -> router / dispatcher
  -> context builder
  -> worker profile selection
  -> execution sandbox
  -> state store
  -> merge / reduce
  -> final output or next task
```

| 调用链 | 描述 |
|:-------:|:---:|
| input event | NA |
| router/dispatcher | 负责决定是否拆任务, 以及拆给谁. Codex 里这个判断主要来自用户显式授权和主 agent, Claude Code 里会受 description 匹配影响, OpenClaw 里很多时候由入口绑定决定, Hermes 里短任务可能由父 agent 调 delegate_task, 也可能由模型按任务复杂度自动选择 delegation; 长任务则可能由 Kanban dispatcher 按 assignee 拉起 worker. |
| context builder | 负责决定 worker 知道什么. 子 agent 没有足够上下文, 跑偏很正常. 你不能把一个 worker 拉进来只说"修一下", 然后期待它理解项目路径、错误现场、相关文件、验收标准、禁止事项和输出格式. 对 subagent 来说, 委派信息就是需求文档.
| worker profile selection | 决定用什么角色. 一般有只读 explorer, 能改代码的 worker, security reviewer, test reviewer, 有长期 memory 的 profile, 一次性 child. 角色选错了, 后面的权限和输出也会跟着错. |
| execution sandbox | 决定 worker 能做什么. 它能不能跑 shell？能不能联网？能不能写文件？能不能继续 spawn child？能不能访问用户凭据？这些都不只是安全配置, 也会直接改变协作模式. 只读 reviewer 和可写 implementer 是两种完全不同的 agent. |
| state store | 决定状态放在哪里. 一次性 subagent 的状态通常只活在本轮任务里, 最后返回 summary. OpenClaw 的 agent 有自己的 session store. Hermes Kanban 会把 task、comment、handoff、blocked/retry 状态写进数据库. 状态放在哪里, 决定了系统能不能跨 turn、跨天、跨重启. |
| merge/reduce | 负责收口. 多个 worker 给出结果后, 谁判断冲突, 谁取舍, 谁写最终 patch, 谁对用户负责？很多多智能体 demo 看起来漂亮, 是因为它跳过了 merge 难题. 真实工程里, merge 才是多智能体成败的地方. |
| final output or next task | 最后还要看取消和失败传播. 父任务被中断时, 子任务要不要一起停？worker 超时怎么办？两个 worker 给出相反结论怎么办？一个 worker 写了错误 patch, 另一个 worker 的测试基于这个 patch 继续跑, 系统怎么回滚？这些不是模型能力问题, 而是运行时设计问题. |

| AGENT | 触发 | 拓扑 | 调用链 |
|:-----:|:---:|:----:|:----:|:
| Codex | 显式 fan-out | 星型 | Codex 适合显式、可控的星型并行. |
| Claude Code | description+team | subagent 仍然是星型. Agent Teams 更接近 team mesh | Claude Code 适合 description 驱动的专家委派, 也能在 team 和 batch 场景里做更复杂的协作. |
| OpenClaw | Gateway+后台任务 | 它更像 agent 操作系统或消息网关, 而不是单次 coding task 的并行器. | OpenClaw 适合多入口、常驻、带权限隔离的 agent 网络. |
| Hermes | 短任务 RPC, 长任务 durable queue | NA | Hermes 适合把短程并行和长期队列分开, 用 delegate_task 管临时 fork/join, 用 Kanban 管跨 turn 的工作流. |


## 2.1 Agent/subAgent Teams
-------

[2026/05/30, darkzodchi @zodchiii, How to build a 4-agent team, that ships a feature while you sleep (Exact Setup Inside)](https://x.com/zodchiii/status/2060674246880149900) 介绍了一个四 AI 代理流水线, 可夜间自动完成功能开发. 流程为规划师→编码员→测试员→审核员, 依靠共享文件自动交接任务, 各司其职、保证质量. 各代 AGENT 工明确、使用适配模型, 由一条指令串联全流程. 也可借助 Teamly 平台, 免手动配置交接逻辑, 快速搭建多类型 AI 团队.

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) | 理念是 "用 AI 组建公司", 不过当前实现中只是包含了众多 Agent 相关 Prompt. 一份精选的 Claude 技能、资源和工具列表, 用于定制 Claude AI 工作流程. | Claude Code | ⭐⭐⭐⭐ | 76,002 |
| [jnMetaCode/agency-agents-zh](https://github.com/jnMetaCode/agency-agents-zh) | [msitarzewski/agency-agents](https://github.com/msitarzewski/agency-agents) 的中文版本, AI 智能体专家团队(中文版)—80+ 个专业 AI 智能体人设, 覆盖开发、设计、营销、测试、运维等领域, 含小红书 / 抖音 / 微信等中国平台原创智能体. | Claude Code | ⭐⭐ | 5,134 |
| [mergisi/awesome-openclaw-agents](https://github.com/mergisi/awesome-openclaw-agents) | 核心提供 148 个开箱即用的生产级 AI Agent 模板 (基于 SOUL.md 配置文件), 覆盖 23 个业务 / 生活领域, 同时配套完整的部署、使用、贡献体系, 是 OpenClaw 框架的核心生态资源库, 整体定位为无代码 / 低代码 AI Agent 落地的一站式模板中心. 23 个分类覆盖个人、团队、企业、技术、业务全场景, 其中 Productivity(生产力)、Development(开发)、Marketing(营销)、DevOps(运维) 为核心高频分类, 同时包含 Moltbook、Supply Chain、Compliance、Voice、Customer Success5 个新增分类, 贴合最新的 AI Agent 落地需求. | OpenClaw | ⭐ | 2,707 |
| [Gentleman-Programming/agent-teams-lite](https://github.com/Gentleman-Programming/agent-teams-lite) | 基于 AI 子代理编排的结构化功能开发工具, 核心解决 AI 编码助手在复杂功能开发中面临的上下文过载、无结构化、无审核节点、无持久化记忆等问题, 采用轻量协调器 + 专业化子代理的架构, 零依赖、纯 Markdown 编写, 可适配各类 AI 编码助手, 是介于基础子代理模式和全量 Agent Teams 运行时之间的轻量化解决方(Level 2). 可以使用 [gentle-ai](https://github.com/Gentleman-Programming/gentle-ai) TUI 工具安装和配置 agent-teams-lite 到 Claude Code、OpenCode、Cursor、Copilot、Gemini 等 Agent. | Claude Code<br>OpenCode<br>Cursor<br>Copilot<br>Gemini | ⭐ | 1,137 |
| [HKUDS/ClawTeam](https://github.com/HKUDS/ClawTeam) | 革命性的 AI 智能体群体智能框架, 实现 "单智能体→智能体集群" 的进化. 通过一行命令让 AI 智能体自主组建团队、分配任务、实时协调并交付结果. 支持任意 CLI 智能体(Claude Code、Codex、OpenClaw 等), 采用 Git 工作树隔离机制, 提供任务依赖管理、智能体间消息通信、实时监控面板等功能. 核心特色包括: 智能体自组织、工作空间隔离、任务跟踪依赖、智能体间消息、监控仪表板、团队模板等. 适用于自动化 ML 研究、群体软件工程、AI 对冲基金等多智能体协作场景. | Claude Code<br>Codex<br>OpenClaw | ⭐ | 4,591 |
| [ClawTeam-OpenClaw](https://github.com/win4r/ClawTeam-OpenClaw) | HKUDS/ClawTeam 的分支, 默认集成 OpenClaw, 支持每代理会话隔离、执行批准自动配置和生产级生成后端, 适用于多智能体集群协调、自主 ML 研究、软件工程和投资分析等场景 | OpenClaw<br>Claude Code<br>Codex<br>nanobot<br>Cursor | ⭐ | 1,087 |
| [VoltAgent/awesome-codex-subagents](https://github.com/VoltAgent/awesome-codex-subagents) | 一个全面的 Codex 子代理集合, 包含 136+ 个专门针对不同开发任务的子代理, 分为 10 个类别. 每个子代理使用 Codex 原生的 .toml 格式定义, 包含智能模型路由和沙盒模式设置. 覆盖核心开发、语言专家、基础设施、质量与安全、数据与 AI、开发者体验、专业领域、业务与产品、元与编排、研究与分析等多个领域. 支持全局和项目特定的子代理安装, 通过明确委托方式使用. | Codex | ⭐ | 3,703 |
| [russelleNVy/three-man-team](https://github.com/russelleNVy/three-man-team) | 结构化的三智能体 AI 开发团队(Architect, Builder, Reviewer), 从生产使用中构建, 令牌优化, 支持 Claude Code、VS Code、Cursor 等多种 AI 工具. 基于 DeepMind 的多智能体研究, 采用三智能体架构实现有意义的审查和协作, 提供完整的工作流管理和令牌优化策略. | Claude Code<br>VS Code<br>Cursor<br>多代理支持 | ⭐ | 501 |
| [geekjourneyx/agora](https://github.com/geekjourneyx/agora) | 31 位思想家组成的多 Agent 审议系统, 覆盖工程、商业、人生抉择、关系、心理、创作六大领域. 采用黑格尔正反合结构, 通过智能路由自动分析问题并导向正确的审议室, 实现深度辩证. 包含 6 个审议室、31 位思想家(13 位专属 + 18 位来自 Council), 8 步结构化流程, 基于 Claude Code 构建, 自包含无需安装其他技能. | Claude Code | ⭐ | 136 |
| [onevcat/argue](https://github.com/onevcat/argue) | 结构化多智能体辩论引擎. 多个 AI Agent 独立分析同一个问题, 跨轮次互相质疑彼此的主张, 最终通过投票达成共识——比任何单个 Agent 都能产出更高质量的结果. 给它一个问题, 拿回经过交叉审查的主张、量化了共识程度的投票结果, 以及一份基于同行评审打分的代表性报告. 更少幻觉, 更多严谨. | Claude Code | ⭐⭐⭐ | 144 |
| [liuzhengdongfortest/CodeStable](https://github.com/liuzhengdongfortest/CodeStable) | 面向严肃工程的 AI 编码工作流, 围绕"人在环"理念编排软件生命周期(需求/架构/路线图/特性/问题/知识六个实体), 而非编排 Agent. 提供 22 个技能、3 个核心流程(特性引入、问题修改、代码重构), 所有产物聚合在 `codestable/` 目录下. | Claude Code<br>OpenCode<br>Codex | ⭐ | 699 |
| [A List of Claude Code Agents](https://github.com/hesreallyhim/a-list-of-claude-code-agents) | 社区维护的 Claude Code Sub-Agents 资源列表, 收录 6 个 Agent 定义(后端TS架构师/Python后端专家/React编码/代码审查/UI工程)和 4 个编排框架(Code By Agents/EquilateralAgents 等). 被动维护, 接受 PR 不做主动筛选, 适合发现 sub-agent 配置、学习编写范式和比较编排框架. | Claude Code | ⭐ | 1,275 |
| [msitarzewski/agency-agents-app](https://github.com/msitarzewski/agency-agents-app) | [agency-agents](https://github.com/msitarzewski/agency-agents) 仓库的原生桌面应用, 为 AI 编码代理提供 Agent 人设的浏览、安装和管理功能. 核心功能包括: 可搜索的三栏 Agent 目录浏览(按部门和角色分类)、安装追踪(记录每个安装的来源哈希、渲染哈希、目标工具、路径等)、漂移检测(检测文件是否在应用外被修改)、确定性渲染(将人设转换为各工具格式)、GitHub 集成(可选 OAuth Device Flow)和离线优先设计(内置目录基线, 无遥测无账号). 技术栈: Tauri 2 + Svelte 5 + Rust 后端, 跨平台支持(macOS/Windows/Linux). 适用于需要在多个 AI 编码工具(Claude Code、Codex、Cursor、Gemini CLI、OpenCode 等)中统一安装和管理 Agent 人设的场景. | Claude Code<br>Codex<br>Cursor<br>Gemini CLI<br>OpenCode<br>多平台 | ⭐ | 27 |


## 2.2 (sub)Agent Team Orchestrator
-------

智能体编排器 (Agent Team Orchestrator) 通过在单个 Coding Agent 中构建 (sub)Agent Team, 对 (sub)Agent Team 进行协调调度, 任务自适应划分, subAgent 并行和管理, 实现任务规划,  分配和工作流控制, 实现元编程调度框架. 具体包括:
1. (sub)多智能体并行管理: 生成并管理多个并行运行的 AI 编码代理, 为每个代理分配独立的工作环境;
2. 自主任务处理: 代理能够自主修复 CI 故障、处理代码审查评论、自动创建和管理 PR;
3. 监控与协调: 提供仪表盘式监控界面, 协调多个代理之间的工作;
4. 工作流优化: 将复杂任务分解为可管理的子任务, 优化工作流程;
5. 多 Agent 支持: 兼容多种 AI 模型, 根据任务类型选择合适的模型.

[2026/04/12, Tim✨ @timyangnet, 大家经常说的编排(Orchestration)Agent 似乎也不是必须, 看 Anthropic 那个让 16 个 agent 并行两周不打架的案例: ](https://x.com/timyangnet/status/2043086842762014744), [Building a C compiler with a team of parallel Claudes](https://www.anthropic.com/engineering/building-c-compiler)


### 2.2.1 oh-my-zsh 系列
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [oh-my-opencode](https://github.com/code-yeongyu/oh-my-openagent) | 开源的 AI 编码代理编排框架, 提供丰富的技能和工具集成 | OpenCode | ⭐⭐⭐ | 49,716 |
| [Yeachan-Heo/oh-my-claudecode](https://github.com/Yeachan-Heo/oh-my-claudecode) | oh-my-opencode 的 [Claude Code 移植版](https://github.com/Yeachan-Heo/oh-my-claudecode/commit/cd98f12fac986bce4b7246aac3326ed107574fb3)), 之前叫 [oh-my-claude-sisyphus](https://github.com/Yeachan-Heo/oh-my-claudecode/commit/3a02feb187f1185fc51379a84ad001b114ac12af), v3.0.0 之后改名. 官网 [oh-my-claudecode-website](https://yeachan-heo.github.io/oh-my-claudecode-website) | Claude Code | ⭐⭐⭐ | 26,409 |
| [Yeachan-Heo/oh-my-codex](https://github.com/Yeachan-Heo/oh-my-codex) | oh-my-opencode 的 codex 移植版 | Codex | ⭐⭐⭐ | 19,261 |
| [MeroZemory/oh-my-droid](https://github.com/MeroZemory/oh-my-droid) | Factory Droid 的多智能体编排器, 零学习曲线. 基于 oh-my-claudecode 实现. | Factory Droid | ⭐ | 14 |
| [woosikkim/oh-my-claudecode-slim](https://github.com/woosikkim/oh-my-claudecode-slim) | oh-my-claudecode 的精简版. | Claude Code | ⭐ | 1 |
| [alvinunreal/oh-my-opencode-slim](https://github.com/alvinunreal/oh-my-opencode-slim) | oh-my-opencode 的精简版. 其还有很多变种, 比如 [BB-84C/omo-slim-superpowers-patch-kit](https://github.com/BB-84C/omo-slim-superpowers-patch-kit) 对 omos 和 superpowers 进行优化, 使两者可以无冲突的协作. | OpenCode | ⭐ | 3,939 |
| [EremesNG/oh-my-opencode-lite](https://github.com/EremesNG/oh-my-opencode-lite) | 委托优先的 OpenCode 插件, 配备七智能体编队(Orchestrator/Explorer/Librarian/Oracle/Designer/Quick/Deep)、根会话 thoth_mem 持久化、原生任务委托和完整 SDD 工作流(propose→spec→design→tasks→apply→verify→archive). 已归档, 开发迁移至 thoth-agents 多编排生态系统. | OpenCode | ⭐ | 2 |
| [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi) | 终端 AI 编码代理, 基于 badlogic/pi-mono, 提供完整的开发工具链. | Pi | ⭐ | 5,157 |
| [KaimingWan/oh-my-kiro](https://github.com/KaimingWan/oh-my-kiro) | 为 AI 编码代理提供持久内存、确定性工作流和自进化智能的框架, 支持 Kiro CLI, 实现从通用代理到了解代码库的专业代理的演进. | Kiro | ⭐ | 77 |
| [oh-my-agent](https://github.com/first-fluke/oh-my-agent) | 便携式多智能体框架, 用于基于 .agents 的技能、工作流和标准感知智能体团队, 支持 Antigravity、Claude Code、Codex、Cursor、OpenCode 等多种平台 | Claude Code<br>Codex<br>Gemini CLI<br>Cursor<br>OpenCode | ⭐⭐⭐ | 730 |
| [wang-h/oh-my-kimi](https://github.com/wang-h/oh-my-kimi) | 为 Kimi Code CLI 提供工作流协调层(Workflow Orchestration Layer), 提供更好的任务路由 + 更好的工作流 + 更好的运行时体验. 技术栈: TypeScript(91.5%) + Rust(4.7%). 核心模块包括 CLI、Skills(40+ 技能)、Modes(ralph, ralplan, team 等)、Team(多 Agent 协调)、MCP 服务器和 Rust Core(高性能搜索、进程管理、运行时). 内置 30+ Agent 角色和标准化工作流(deep-interview → ralplan → team/ralph). 支持 Native 和 Tmux 两种 Team 执行模式, AGENTS.md 协议和 `.omk/` 状态持久化. 适用于新功能开发、大规模并行工作、Bug 修复和代码审查. 从 oh-my-codex fork, 定位为 Kimi-first 版本. | Kimi Code CLI<br>Codex<br>Claude CLI | ⭐ | 6 |
| [arcsin1/oh-my-ppt](https://github.com/arcsin1/oh-my-ppt) | 纯本地的 AI 幻灯片生成与编辑工具(Electron 桌面应用), 内置 30+ 风格 SKILL. 支持一句话生成 PPT、从文档创建、导入 PPTX 编辑、对话式修改、可视化拖拽编辑、动画演示、数学公式渲染和 PDF/PNG/PPTX 导出. 支持本地 Ollama 模型. | 桌面应用 | ⭐ | 747 |
| [Salomondiei08/oh-my-hermes](https://github.com/Salomondiei08/oh-my-hermes) | Hermes Agent的工作流层, 实现应用的构建、发布和运维自动化, 类似Oh My Zsh对Zsh的增强. 提供自主CTO循环(每小时自动分类GitHub issues并处理)、全生命周期管理(需求澄清到部署运维)、6个专职Agent(CTO/PM/Dev/Security/QA/Ops)、23个技能模块和自动化工作流(GitHub PR管理/安全审查/健康检查). 技术栈: Vercel + Supabase + Uptime Kuma. 支持Slack/Telegram/Discord/WhatsApp多平台通知. | Hermes Agent<br>Claude Code<br>Codex | ⭐ | 381 |
| [worldwonderer/oh-story-claudecode](https://github.com/worldwonderer/oh-story-claudecode) | 网文写作skill包,覆盖长篇与短篇网络小说的扫榜、拆文、写作、去AI味、封面图全流程,包含7个专业Agent和6个自动化Hooks,支持起点、番茄、晋江、知乎盐言等平台 | Claude Code<br>OpenClaw | ⭐ | 1,201 |
| [VOBC/oh-my-coder](https://github.com/VOBC/oh-my-coder) | 国产首个多 Agent 编程框架, 31 个专业 Agent + 12 家国产大模型(DeepSeek/智谱GLM/小米MiMo/Kimi/豆包/百川/Ollama等), 开箱即用零成本起步. 提供 CLI/Web/VSCode 三端, Quest Mode 异步自主编程, 代码审查、Bug调试、测试生成和 Docker 私有部署. 对标 oh-my-claudecode, 聚焦国产模型零成本替代. | 自建CLI<br>Web<br>VSCode | ⭐ | 109 |
| [mortonbaker/oh-my-opencode-pms](https://github.com/mortonbaker/oh-my-opencode-pms) | oh-my-opencode 的 PMS 扩展, 基于 oh-my-opencode-slim fork, 提供 11 个 Agent 全景面板(PM/architect/researcher/synthesizer/builder/judge/qa-reviewer/triage/observer/council/councillor)和内置 HIPAA 级治理 harness(3-strike 循环、烟雾测试门、审计链、预算门控), 流水线: PM → researcher×N → synthesizer → architect → builder → judge → qa-reviewer×N. | OpenCode | ⭐ | 0 |


### 2.2.2 (sub)Agent Orchestrator
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [agents](https://github.com/wshobson/agents) | Claude Code Plugins: Orchestration and Automation, 为 Claude Code 提供全面的生产就绪插件市场, 包含 77 个专注插件、182 个专门代理、149 个代理技能和16 个工作流编排器. 支持智能自动化和多代理编排, 采用三层模型策略(Opus/Sonnet/Haiku)优化性能, 涵盖全栈开发、安全强化、云基础设施、区块链等24个类别. | Claude Code | ⭐⭐⭐⭐ | 33,380 |
| [SuperClaude](https://github.com/SuperClaude-Org/SuperClaude_Framework) | 专为 Claude Code 打造的元编程配置框架, 核心作用是通过丰富的工具集和配置体系, 将 Claude Code 从基础的代码生成工具升级为结构化、专业化的智能开发平台. 包含了 22 个斜杠命令(/sc:), 14 个领域智能代理(Agents), 6 种行为模式, 官网 [superclaude](https://superclaude.netlify.app) | Claude Code | ⭐⭐⭐ | 22,207 |
| [sangrokjung/claude-forge](https://github.com/sangrokjung/claude-forge) | 开源的 Claude Code 开发环境, 提供 11 个专用智能体、40 个斜杠命令、15 个技能工作流程和 15 个自动化钩子. 它被形容为是 Claude Code 的 oh-my-zsh, 它将 Claude 代码从一个基础的 CLI 转变为一个功能齐全的开发环境. 一次安装就能提供代理、命令、技能、钩子和 9 个规则文件——全部预先布线, 随时可用. | Claude Code | ⭐ | 644 |
| [ruvnet/ruflo](https://github.com/ruvnet/ruflo) | Ruflo(Claude-Flow) 是一个全面的人工智能代理编排框架, 将 Claude Code 转变为强大的多代理开发平台. 它使团队能够部署、协调和优化专业的人工智能代理, 协同处理复杂的软件工程任务. 支持多个 Agent 并行执行, 同时提供实时监控面板. | Claude Code | ⭐⭐⭐ | 30,811 |
| [ComposioHQ/agent-orchestrator](https://github.com/ComposioHQ/agent-orchestrator) | 生成并行的 AI 编码代理, 每个代理在自己的 git 工作树中. 代理自主修复 CI 故障, 处理审核评论, 并开放 PR——你只需在一个仪表盘上进行监督.<br>Agent Orchestrator 管理着一系列并行运行在代码库上的 AI 编码代理. 每个代理都有自己的 git 工作树、分支和 PR. 当 CI 失败时, 代理会修复它. 当审核员留下评论时, 代理人会进行回应. 只有当需要人为判断时, 你才会被拉进来. | 多 Agent 支持 | ⭐⭐ | 5,994 |
| [openai/symphony](https://github.com/openai/symphony) | Symphony 将项目工作转化为独立、自主的实现运行, 使团队能够管理工作, 而无需监督编码代理. [An open-source spec for Codex orchestration: Symphony](https://openai.com/index/open-source-codex-orchestration-symphony) | Codex | ⭐⭐⭐ | 14,800 |
| [wozhenbang2004/AgentNexus](https://github.com/wozhenbang2004/AgentNexus) | AgentNexus 不仅仅是一个 AI 应用框架, 它是一个功能完备的智能体 (Agent) 基础设施, 专为解决企业在生产环境中落地复杂 AI 工作流的核心挑战而设计. 摒弃了硬编码的 Agent 逻辑, 通过将模型、工具(MCP)、RAG 知识库、提示词等所有核心组件进行数据库持久化, 并通过 API 驱动的责任链模式在运行时动态构建 Agent, 从而赋予系统强大的动态编排、自主协作与全生命周期管理能力. | 多 Agent 支持 | ⭐ | 113 |
| [cft0808/edict](https://github.com/cft0808/edict) | 三省六部 (Edict), 用 1300 年前的帝国制度, 重新设计了 AI 多 Agent 协作架构. 12 个 AI Agent(11 个业务角色 + 1 个兼容角色) 组成三省六部: 太子分拣、中书省规划、门下省审核封驳、尚书省派发、六部 + 吏部并行执行. 比 CrewAI 多一层制度性审核, 比 AutoGen 多一个实时看板. | 多 Agent 支持 | ⭐⭐⭐ | 14,729 |
| [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | 完整的 AI 编码工作流系统, 提供经过实战验证的工作流模式、自我纠正记忆、并行工作树、结束仪式和 80/20 AI 编码比例, 支持 Claude Code、Cursor 和 32+ 个其他代理 | 多 Agent 支持 | ⭐ | 1,804 |
| [samibs/skillfoundry](https://github.com/samibs/skillfoundry) | AI 工程框架, 提供质量门控、持久记忆和多平台支持, 适用于 Claude Code、Cursor、Copilot、Codex 和 Gemini | 多 Agent 支持 | ⭐ | 6 |
| [agent-sh/agentsys](https://github.com/agent-sh/agentsys) | AI 编码自动化系统, 提供 15 个插件、35 个智能体和 32 个技能, 支持 Claude Code、OpenCode、Codex、Cursor 和 Kiro 等多种编码工具 | 多 Agent 支持 | ⭐ | 861 |
| [claudeforge/orchestrator](https://github.com/claudeforge/orchestrator) | 为 Claude Code 设计的自主开发系统, 提供自动化开发流程和工作流管理. | Claude Code | ⭐ | 37 |
| [shinpr/claude-code-workflows](https://github.com/shinpr/claude-code-workflows) | 为 Claude Code 设计的生产就绪开发工作流, 由专门的 AI 智能体提供支持, 涵盖代码质量、开发工作流和提示工程等多个方面 | Claude Code | ⭐ | 288 |
| [HazAT/pi-interactive-subagents](https://github.com/HazAT/pi-interactive-subagents) | 为 pi 提供交互式子代理功能, 支持在多路复用器面板中生成、编排和管理子代理会话, 内置多种代理角色(planner、scout、worker、reviewer、visual-tester), 实现完整的规划到实现工作流. | Pi | ⭐ | 280 |
| [AI Team OS](https://github.com/CronusL-1141/AI-company) | 将 Claude Code 转变为自动驾驶的 AI 公司, 实现自主运行、学习和进化. 核心功能包括自主操作引擎、自我改进系统、26 个专业 Agent 模板、8 个结构化会议模板、决策透明度和 4 层防御规则系统. 技术架构采用 5 层设计, 包括 Web 仪表板、CLI + REST API、团队编排器、记忆管理器和存储. 适用于自主软件开发、持续集成、团队协作和项目管理等场景. | 多 Agent 支持 | ⭐ | 155 |
| [Citadel](https://github.com/SethGammon/Citadel) | 运行自主编码活动的工具, 根据任务规模路由到合适的工具. 提供 18 个技能(代码审查、测试生成、文档生成等)、3 个自主代理、8 个生命周期钩子、活动持久性和 fleet 协调. 编排阶梯分为四个层次, 从简单技能到复杂舰队协调. 适用于从单行修复到多天并行活动的各种编码任务. | Claude Code | ⭐ | 485 |
| [DeerFlow](https://github.com/bytedance/deer-flow) | 字节跳动开源的超级智能体框架, 基于 LangGraph 和 LangChain 构建, 支持子智能体编排、沙箱执行、持久记忆和技能扩展, 可完成从深度研究到内容生成的多种复杂任务 | 多 Agent 支持 | ⭐⭐ | 59,619 |
| [Code Conductor](https://github.com/ryanmac/code-conductor) | 多 AI 编码代理编排工具, 通过并行运行多个 AI 代理来实现 10 倍速度的功能交付. 支持在隔离的 git worktrees 中工作以避免合并冲突, 与 Claude Code 集成, 代理可自主认领任务、实现和交付. 提供自动 GitHub Actions 工作流和语言无关的设置, 适用于并行处理多个功能开发、加速 backlog 任务处理和自动化代码审查等场景. | 多 Agent 支持 | ⭐ | 92 |
| [Jedward23/Tmux-Orchestrator](https://github.com/Jedward23/Tmux-Orchestrator) | 基于 Tmux 的 AI 代理编排器, 实现 24/7 自主运行. 采用三层架构(Orchestrator → Project Manager → Engineer), 支持自触发调度、多项目管理、自动 Git 备份和实时监控. 通过 Tmux 持久化会话让代理持续运行. | Claude Code | ⭐⭐ | 1,743 |
| [junhoyeo/contrabass](https://github.com/junhoyeo/contrabass) | 面向AI编码代理的项目级编排器,用Go+Charm栈重新实现OpenAI的Symphony. 核心理念是"管理工作,而非管理代理". 终端优先的Issue驱动代理运行器,可选本地Web仪表板. 支持Cobra CLI(TUI/headless/Web模式)、WORKFLOW.md解析器(YAML+Liquid+环境变量)、Issue追踪适配器(Linear/Github/Internal Board)、代理运行器(Codex/OpenCode/oh-my-opencode等)、Git工作树隔离和多代理协调(Team模式,plan→exec→verify流水线). | Codex<br>OpenCode<br>oh-my-opencode<br>oh-my-codex<br>oh-my-claudecode | ⭐ | 166 |
| [duckbugio/flock](https://github.com/duckbugio/flock) | 通过 Telegram 机器人驱动一个 Claude Code AI 开发团队, 自动完成需求规划、编码、测试、审查到提 PR 的完整流程. Go 写的 Telegram 机器人, 背后跑着一整个 Claude Code AI 开发团队. 你在 Telegram 里用自然语言说"实现某某功能", 机器人就通过 5 个角色(planner 规划 → coder 编码 → tester 测试 → reviewer 审查 → arbiter 仲裁)的流水线自动完成需求分析、写代码、跑测试、代码审查, 最后在 Git 仓库上创建 PR. | Claude Code | ⭐ | 747 |


### 2.2.3 Agent Teams Workflow
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [jayminwest/overstory](https://github.com/jayminwest/overstory) | 多智能体编排工具, 将单个编码会话转变为多智能体团队, 通过 tmux 在 git 工作树中生成工作代理, 通过自定义 SQLite 邮件系统协调它们, 并通过分层冲突解决合并它们的工作. 可插拔的 AgentRuntime 接口允许在 Claude Code、Pi、Gemini CLI 或自定义适配器之间切换. | 多 Agent 支持 | ⭐ | 1,196 |
| [Dicklesworthstone/claude_code_agent_farm](https://github.com/Dicklesworthstone/claude_code_agent_farm) | 强大的多智能体编排框架, 可并行运行 20+ 个 Claude Code 代理, 支持 34 种技术栈(Next.js、Python、Rust、Go、Java 等), 提供 bug 修复、最佳实践实现和多代理协作工作流, 具有智能监控、自动恢复、冲突预防和详细的 HTML 运行报告等功能 | Claude Code | ⭐ | 3,802 |
| [cloudshipai/station](https://github.com/cloudshipai/station) | Station 是一个 AI 代理编排平台, 用于构建、测试和部署智能代理团队. 自托管、Git 支持、生产就绪. 主要功能包括: 多代理团队 (协调专业代理在编排器下)、内置评估 (LLM 作为法官自动测试每个代理)、Git 支持的工作流 (像代码一样对代理进行版本控制)、一键部署 (用 stn deploy 推送到生产)、完整可观测性 (每次执行的 Jaeger 跟踪)、自托管 (你的数据, 你的基础设施, 你的控制). 提供 41 个 MCP 工具, 支持多种 AI 提供商 (CloudShip AI、OpenAI、Google Gemini、Anthropic). 代理是简单的 .prompt 文件, 使用 GenKit 的 dotprompt 格式. 支持沙箱隔离代码执行 (Python/Node.js/Bash)、计划任务 (基于 cron 的代理调度)、事件触发执行 (webhook)、捆绑和共享 (打包代理团队以进行分发)、OpenAPI 到 MCP 自动转换. 部署目标包括 Fly.io、Docker、Kubernetes、AWS ECS、Google Cloud Run、Azure 容器实例. | Claude Code<br>OpenCode<br>Cursor<br>Claude Desktop | ⭐ | 418 |
| [AndyMik90/Aperant](https://github.com/AndyMik90/Aperant) | Aperant (前身为 Auto Claude) 是一个自主的多代理编码框架, 可以为你规划、构建和验证软件. 主要功能包括: 自主任务处理 (描述目标, 代理处理规划、实施和验证)、并行执行 (最多12个代理终端同时运行多个构建)、隔离工作区 (所有更改都在 git worktrees 中进行, 主分支保持安全)、自我验证 QA (内置质量保证循环在你审查之前捕获问题)、AI 驱动的合并 (自动冲突解决, 集成回主分支)、记忆层 (代理在会话间保留见解以实现更智能的构建)、GitHub/GitLab 集成 (导入问题, 用 AI 调查, 创建合并请求)、Linear 集成 (与 Linear 同步任务以进行团队进度跟踪). 提供跨平台原生桌面应用 (Windows/macOS/Linux), 具有看板界面、代理终端和路线图功能. 技术栈: Electron (桌面应用)、TypeScript. | Claude Code | ⭐⭐ | 14,101 |
| [backnotprop/plannotator](https://github.com/backnotprop/plannotator) | 交互式计划和代码审查工具, 专为 AI 编码代理设计. 提供可视化 UI 来标记和完善计划或代码差异, 支持团队协作分享, 可无缝集成 Claude Code、Copilot CLI、Gemini CLI、OpenCode、Pi 和 Codex. 核心功能包括可视化计划审查、计划差异自动显示、代码审查、注解任意文件(Markdown/HTML/URL/文件夹)、零知识存储(类似 PrivateBin)、完全开源可自托管. | Claude Code<br>Copilot CLI<br>Gemini CLI<br>OpenCode<br>Pi<br>Codex | ⭐ | 4,957 |
| [amanning3390/deepswarm](https://github.com/amanning3390/deepswarm) | 任务无关的并行工作器编排系统, 自动优化工作器数量和启动间隔实现高达 99.95% 的 API 成功率. 基于 DeepSeek Hermes Reasoning Traces 项目(19,331 条推理轨迹、192K 工具调用、31,000+ 次 API 调用)的实战验证. 技术栈: Python 3 + REST API. 核心特性包括自动优化算法、分层模型委托(V4 Pro 编排 + V4 Flash 执行, 节省 60-70% 成本)、多轮对话支持、故障恢复机制和质量过滤. 支持 5 种任务类型(生成、翻译、摘要、分类、自定义). 提供完整的工作流: 定义任务 → 生成任务种子 → 启动 → 后处理. 适用于批量内容生成、大规模翻译、文档摘要处理和推理轨迹生成. | DeepSeek | ⭐⭐ | 108 |
| [zaxbysauce/opencode-swarm](https://github.com/zaxbysauce/opencode-swarm) | 多专业智能体协作的 AI 编码插件, 通过严格的门控流水线确保代码质量. 采用架构师为中心的协作模式(17+ 智能体), 每个任务必经 13 个步骤的门控流程(编码→审查→测试→安全检查等). 技术栈: TypeScript + Bun + Tree-sitter + Zod. 核心特性包括门控流水线(63+ 工具)、会话恢复(`.swarm/` 持久化)、过程补救模型(PRM)、知识管理(Swarm/Hive 双层记忆)、上下文预算守护和变异测试. 支持三种会话模式(Balanced/Turbo/Full-Auto)和三种项目模式(strict/balanced/fast). | OpenCode | ⭐ | 307 |
| [VRSEN/OpenSwarm](https://github.com/VRSEN/OpenSwarm) | 完全开源的多智能体系统, 从单一 prompt 生成完整交付物(幻灯片、研究报告、数据可视化、文档、图片、视频). 内置 8 个专业代理(Orchestrator、Deep Research、Data Analyst 等), 基于 Agency Swarm 构建. | 多 Agent 支持 | ⭐ | 1,598 |
| [Sakana Fugu]() | [Sakana Fugu: A Multi-Agent Orchestration System as a Foundation Model](https://sakana.ai/fugu-beta) |
| [adamjgmiller/adamsreview](https://github.com/adamjgmiller/adamsreview) | 多阶段代码审查工具, 支持并行子代理检测、验证和自动修复循环. 提供6个核心命令: /adamsreview:review(多视角审查, 最多7个并行子代理)、codex-review(Codex CLI驱动审查)、add(注入外部审查结果)、walkthrough(交互式审查引导)、fix(自动修复循环)、promote(手动提升发现项). | Claude Code<br>Codex CLI | ⭐ | 195 |


### 2.2.4 Agent Dyanmic Workflow
-------


| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [Claude Code Dynamic Workflow](https://claudefa.st/blog/guide/development/dynamic-workflows) | 2026/05/28 Claude Code v2.1.154 同 Claude Opus 4.8 三大核心特性之一(Dynamic Workflows + Effort Controls + Adaptive Thinking), [2026/06/02, 前端哥Liam @jinglian, 很多人看到 Claude Code Dynamic Workflow, 第一反应是:](https://x.com/jinglian/status/2061733037042180485), [2026/06/02, AI少年 @aehyok, 一句话调度了几百个 Agent 干活, Claude Code 这次更新的动态工作流有点猛](https://x.com/aehyok/status/2061698672128348380), [2026/06/08, Mr Panda @PandaTalk8, 为每个任务量身定做: Claude Code 动态工作流完全指南](https://x.com/PandaTalk8/status/2063918562318946740) | Claude Code | ⭐ | 暂未开源 |
| [DannyMac180/skills](https://github.com/DannyMac180/skills) | Dan McAteer创建的AI代理技能集合. 核心技能codex-dynamic-workflows:规划和运行监督式AI代理动态工作流,支持目标模式(goal mode)、子代理(subagents)或模拟工作包(simulated work packets)、审批门(approval gates)、集成(integration)、验证(verification)和可复用工作流制品(reusable workflow artifacts). | Codex(主要) | ⭐ | 330 |
| [Michaelliv/pi-dynamic-workflows](https://github.com/Michaelliv/pi-dynamic-workflows) | 为Pi终端AI编码代理添加Claude Code风格的动态工作流功能. 核心机制:模型写小型JavaScript脚本,将工作扇出到多个隔离子代理并行处理,最后汇总结果. 脚本运行在Node VM沙箱中,提供agent()、parallel()、pipeline()等API. | Pi(主要) | ⭐ | 723 |

### 2.2.5 可编程 Orchestrator
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [bottega](https://github.com/vdaubry/bottega) | 多智能体编排工具, 采用"AI sandwich"理念: 人类在开头和结尾, AI在中间. Ralph Wiggum loop 循环机制(规划→审批→实现⇄审查→达标开PR→人类审查PR), 以规范(spec)+参考实现发布, 支持多 Harness(Claude Code/Codex/OpenCode), 远程优先多人协作, GitHub PR webhook 自动联动. | Claude Code<br>Codex<br>OpenCode | ⭐ | 67 |

## 2.3 (multi)Agent Parallel Workflow(Swarm)
-------

Agent Parallel Workflow 致力于组合多个 Agent 协同工作, 通过 Parallel Workflow 完成多 Agent 并行编排和管理. 最终组合多个 Agent 协同工作, 保障复杂任务的高效完成.

### 2.3.1 (multi)Agent Parallel Orchestrator
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [uluckyXH/OpenMOSS](https://github.com/uluckyXH/OpenMOSS) | 一个 AI 管理 AI 的平台. 多个代理自主协作——规划、执行、审查和检查——而人类只需设定目标并核对结果. OpenMOSS(多代理编排与自我演化系统)是一个基于 OpenClaw 的自组织多代理协作平台. | OpenClaw | ⭐ | 1,177 |
| [fengshao1227/ccg-workflow](https://github.com/fengshao1227/ccg-workflow) | 多模型协作开发工具集. 基于 Claude Code CLI, 整合 Codex/Gemini 后端能力, 提供智能路由、代码审查、Git 工具等 17+ 个命令. | Claude Code/Codex/Gemini | ⭐⭐ | 5,031 |
| [johannesjo/parallel-code](https://github.com/johannesjo/parallel-code) | Parallel Code 为 Claude Code、Codex CLI 和 Gemini CLI 各自自动赋予了自己的 git 分支和工作树. 没有特工互相踩到代码, 没有杂耍终端, 没有精神负担. 只需一个干净的界面, 你就能看到所有内容, 快速导航, 结果准备好时合并——并且从手机上监控. | Claude Code/Codex/Gemini | ⭐ | 588 |
| [EtienneLescot/n8n-as-code](https://github.com/EtienneLescot/n8n-as-code) | 围绕 n8n(开源自动化工作流工具)打造的工具集, 核心目标是为 AI 编码代理赋予 n8n 全量能力, 同时提供 GitOps 流程、TypeScript 工作流开发、多端 (VS Code/CLI/Claude) 操作等能力, 实现 n8n 工作流的高效、可追溯、智能化管理. | 多 Agent 支持 | ⭐ | 737 |
| [eyaltoledano/claude-task-master](https://github.com/eyaltoledano/claude-task-master) | 一个基于 Claude 的 AI 驱动开发任务管理系统, 设计用来与 Cursor AI 无缝协作. Task Master 让 Claude Code 像项目经理一样思考, 自动拆解 PRD(需求文档), 生成任务列表, 并跟踪进度. 通过 MCP 配置, 可以轻松接入 Cursor 和 Windsurf 等开发工具. [官网文档](https://task-master.dev), [@GitHub_Daily 的帖子](https://x.com/GitHub_Daily/status/1915556362139955323), [微信公众号 -- 妙想栈 --26.1k Star！这个 AI 任务管理神器让 Cursor 和 Claude Code 效率翻倍](https://mp.weixin.qq.com/s/3klm_RKTniT0izX1Wn-QDA) | Claude Code | ⭐⭐⭐ | 26,452 |
| [skindhu/AI-TASK-MANAGER](https://github.com/skindhu/AI-TASK-MANAGER) | AI Task Master 是对原始 claude-task-manager 项目的增强和改进版本. 分析了原始项目的设计理念和能力后, 进行了升级. | Claude Code | ⭐ | 190 |
| [stellarlinkco/myclaude](https://github.com/stellarlinkco/myclaude) | 多智能体编排工作流系统, 支持 Claude Code、Codex、Gemini、OpenCode 多后端执行, 提供多种开发工作流程模块 (do、omo、bmad 等) 和可单独安装的技能 | 多 Agent 支持 | ⭐ | 2,575 |
| [axtonliu/ai-pair](https://github.com/axtonliu/ai-pair) | 异构 AI 团队协作工具, 协调多个 AI 模型 (Claude + GPT + Gemini) 作为一个团队工作, 一个创作, 两个审查, 利用不同模型的不同视角, 是一个 Claude Code Skill. [我开源了一个让 Claude、GPT、Gemini 组队的 Skill](https://x.com/AxtonLiu/status/2031732461982416898). | Claude Code/Codex/Gemini | ⭐ | 177 |
| [MistRipple/magi-code](https://github.com/MistRipple/magi-code) | 多智能体工程编排系统, 在 VSCode 中将复杂开发任务自动拆解为可执行合同, 调度异构 Worker 并行协作, 完成从规划、执行、验收到知识沉淀的全流程闭环. | 多 Agent 支持 | ⭐ | 187 |
| [mindfold-ai/Trellis](https://github.com/mindfold-ai/Trellis) | 多平台 AI 编码框架, 用来统一 AI 编程工具的上下文. 提供自动注入规范、任务中心工作流、并行代理执行、项目记忆和团队共享标准等功能<br> 当前多个 AI Coding Agent 并发工作时, 每个工具的规范和历史记录都不互通. Trellis 的做法是在项目中建一个 `.trellis/` 目录, 把代码规范, 任务 PRD, 工作流都存进去. 不管切换到任意 AI 工具, 都能把这些上下文注意进入. 通过 git worktrees 让多个 AI 任务并行执行. 团队里一个人写好规范, 其他人开箱即用. | Claude Code、Cursor、OpenCode、iFlow、Codex、Kilo、Kiro、Gemini CLI、Antigravity 和 Qoder | ⭐ | 7,206 |
| [claude-octopus](https://github.com/nyldn/claude-octopus) | Claude Code 插件, 协调 Codex, Gemini, Claude, Perplexity, OpenRouter, Ollama, Copilot 等 7 家 Agent 以不同角色工作, Octopus 为每个模型分配了独特的角色——Codex 负责实现深度, Gemini 负责生态系统广度, Claude 负责综具有对抗性审查和共识门控. 主要功能包括: 三脑工作流、跨会话持久记忆(深度集成 claude-mem)、从规范到软件的暗黑工厂模式、基于 Double Diamond 框架的方法论、32 个专业角色、39 个命令、50 个技能等. | 多 Agent 支持 | ⭐ | 2,472 |
| [gabrielkoerich/orch](https://github.com/gabrielkoerich/orch) | 一个自主任务编排器, 将工作委托给 AI 编码代理(Claude、Codex、OpenCode、Kimi、MiniMax). 作为后台服务运行, 管理隔离的工作树, 与 GitHub Issues 同步, 并处理从路由到 PR 创建的完整任务生命周期. 支持多项目管理、基于复杂性的路由、代理记忆、实时会话流等功能. | 多 Agent 支持 | ⭐ | 9 |
| [ChesterRa/cccc](https://github.com/ChesterRa/cccc) | 本地优先的多智能体协作内核, 提供轻量级且具有基础设施级别可靠性的多智能体框架. 采用单一写入守护进程设计, 通过只追加账本记录所有消息和事件, 实现可靠的消息传递语义和统一控制平面. 支持 Claude Code、Codex CLI、Gemini CLI 等 8 种一流运行时的协作. | 多 Agent 支持 | ⭐ | 772 |
| [agtx](https://github.com/fynnfluegge/agtx) | 用于管理 agent coding 会话的原生终端看板, 可以接入 Claude Code、Codex、Gemini、OpenCode、Copilot 等任何现有的规范驱动开发框架, 或指定一个具有分阶段技能的自定义插件. 核心功能包括: 1) 编排代理: 自主管理看板、委派任务、推进阶段、检查合并冲突; 2) 多代理任务生命周期: 为每个工作流阶段配置不同代理; 3) 并行执行: 每个任务获得自己的 git worktree 和 tmux 窗口; 4) 规范驱动插件: 支持 GSD、Spec-kit、OpenSpec、BMAD、Superpowers 等; 5) 多项目仪表板: 通过单个 TUI 管理所有项目的代理会话. | Claude Code/Codex/Gemini/OpenCode/Copilot | ⭐ | 823 |
| [swarms](https://github.com/kyegomez/swarms) | 企业级生产就绪的多智能体编排框架, 提供完整的多智能体基础设施平台, 支持生产级部署和与现有系统的无缝集成. 核心功能包括: 层次化智能体集群、并行处理管道、顺序工作流编排、基于图的智能体网络、动态智能体组合、智能体注册表管理等. 支持多种智能体架构如 SequentialWorkflow、ConcurrentWorkflow、AgentRearrange、GraphWorkflow、MixtureOfAgents、GroupChat、HierarchicalSwarm 等, 适用于复杂业务流程自动化、可扩展任务分配、灵活的工作流适应等场景. | 多 Agent 支持 | ⭐⭐ | 6,201 |
| [Compozy](https://github.com/compozy/compozy) | 驱动 AI 辅助开发的完整生命周期, 从想法到代码交付. 提供结构化工作流程(`Idea → PRD → TechSpec → Tasks → Execution → Review`), 支持40+ AI代理, 具有代码库感知增强、多代理执行、工作流记忆等核心特性. | 多 Agent 支持 | ⭐⭐ | 5,49 |
| [swarm-forge](https://github.com/unclebob/swarm-forge) | 基于 tmux 的轻量级代理编排平台, 用于协调多个 AI 代理协作开发. 核心功能包括: 配置驱动的拓扑结构、项目本地角色定义、分层的章程系统、每个角色的后端选择、可观察的 swarm、自托管且轻量级. 支持通过 git worktree 为每个角色创建独立工作环境, 通过 tmux 会话和终端窗口管理多个代理. | Claude<br>Codex | ⭐ | 392 |
| [manaflow](https://github.com/manaflow-ai/manaflow) | 开源的 Claude Code 网页版/Codex Cloud/Devin 替代方案. 核心功能: 1) 并行 Agent 编排: 可同时启动 Claude Code、Codex CLI、Cursor CLI、Gemini CLI、Amp、OpenCode 等多个编码 Agent 并行执行任务; 2) 隔离的 VS Code 工作区: 每个 Agent 运行在独立的云或本地 Docker 容器中的 VS Code 工作区, 确保并行工作的可验证性和高效性; 3) 实时 Web 预览: 在 Agent 开发时可直接预览应用, 嵌入式浏览器显示开发服务器输出; 4) 一键 PR 创建: 从工作区直接审查差异、合并或创建 PR, 无需离开即可查看 CI 状态; 5) 完整工作区监控: 同时查看 VS Code 编辑器、Claude Code TUI 和 VNC 浏览器预览, 监控 Agent 的所有操作; 6) 热图差异查看器: 自动突出显示高风险代码变更, 聚焦关键审查点. 技术特点: 通过 Docker 容器提供隔离环境, 集成 VS Code 作为开发界面. 适用于多 Agent 并行开发、团队协作编码、需要隔离环境的开发任务等场景. | Claude Code/Codex/Cursor/Gemini/Amp/OpenCode | ⭐ | 1,030 |
| [Shannon](https://github.com/Kocoro-lab/Shannon) | 生产级 AI Agent 平台, 提供多策略编排、群体协作、Token 预算控制、人工审批工作流和时间旅行调试等核心功能. 基于 Temporal 工作流引擎实现可靠的执行和回放调试, 支持 OpenAI、Anthropic、Google、DeepSeek 等 10+ LLM 提供商, 采用 WASI 沙箱保障安全执行. 技术栈采用 Go+Rust+Python 多语言架构, 提供 REST API、Python SDK、OpenAI 兼容 API 和桌面应用等多种交互方式, 内置 8 种执行策略(Simple/DAG/ReAct/Research/Exploratory/Browser Use/Domain Analysis/Swarm)满足不同场景需求. 适用于需要可靠、可观测、可调试的生产级 Agent 部署场景. | 多 Agent 支持 | ⭐ | 1,794 |
| [mco-org/mco](https://github.com/mco-org/mco) | MCO (Multi-CLI Orchestrator) - AI 编程 Agent 编排平台, 为 AI 编程助手提供中立的编排层实现多 Agent 并行协作. 技术栈: Python 3.10+ (98.3%) + Shell (1.7%). 核心特性包括并行调度(同时向多个 Agent 发送相同任务)、共识引擎(跨 Agent findings 合并、去重、评分)、辩论模式、分工模式、链式模式、跨会话记忆(evermemos-mcp)和 MCP Server. 支持辩论复核、持久化审查、实时终端流(--stream live)和自定义 Agent 注册. 内置 5 个 Provider(Claude Code, Codex CLI, Gemini CLI, OpenCode, Qwen Code), 通过 `.mco/agents.yaml` 支持扩展 ACP/Shim/Ollama Agent. 适用于多视角验证的代码审查、高风险变更审查、CI/CD 集成和团队协作共识决策. | Claude Code<br>Codex CLI<br>Gemini CLI<br>OpenCode<br>Qwen Code | ⭐ | 333 |
| [dataseeek/MagesticAI](https://github.com/dataseeek/MagesticAI) | 基于 SDD(规范驱动开发)的云端/Web端AI任务管理和代理编排平台. 浏览器端平台,通过协调自主代理管理AI编码任务. 提供看板任务板、多代理(Planner+Coder)、实时终端、Monaco代码编辑器、Git工作树隔离、LLM驱动QA. 核心理念:spec→plan→code→QA全流程在一个自托管浏览器应用中完成. | 自托管Web平台,支持本地和OpenAI兼容LLM | ⭐ | 75 |
| [agent-teams-ai](https://github.com/777genius/agent-teams-ai) | Electron 桌面应用, 编排 AI 智能体团队协作. 支持看板项目管理、Agent 间跨团队实时通信、Hunk 级代码审查、混合 AI teammates(Claude+Codex+OpenCode 同团队)、灵活自主级别(逐动作审批⇔全自主)、Git Worktree 隔离、内置 MCP Server. 免费零配置入门, AGPL-3.0 开源. | Claude Code<br>Codex<br>OpenCode | ⭐ | 1,271 |
| [polynoia](https://github.com/JuneQQQ/polynoia) | IM 风格的多 Agent 协作平台, 将 Claude Code/Codex/OpenCode 统一到类 Slack 即时通讯界面. 支持 1:1 聊天和群聊(Orchestrator 自动分解并行派发), 12+ 种内联 Artifacts(diff/Web预览/Markdown/幻灯片等可直接渲染编辑), per-agent git worktree + 引导式冲突解决, Web/Tauri 桌面/Capacitor 移动三端. | Claude Code<br>Codex<br>OpenCode | ⭐ | 118 |
| [omnigent](https://github.com/omnigent-ai/omnigent) | AI Agent 元编排框架(meta-harness), 为 Claude Code/Codex/Cursor/Pi 及自定义 Agent 提供统一抽象层, 切换或组合不同 Agent 运行环境无需重写代码. 策略治理(审批/限制/预算)三层叠加, 跨设备实时会话同步, 云端沙箱执行(Modal/Daytona), Polly 编排器 + Debby 双头辩论 Agent, 内置 4 类凭证模式(API Key/订阅/Gateway/Databricks). | Claude Code<br>Codex<br>Cursor<br>Pi | ⭐ | 1,421 |


### 2.3.2 (multi)Agent WorkFlow
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [cowork](https://github.com/JonathanRosado/cowork) | 让 Claude 和 Codex 真正协同工作的插件, 实现双 AI 代理协作开发. 核心功能包括: 溯源路由协议(主导思考的代理负责实现)、混合线程(早期独立思考, 后期保持连续性)、用户手动路由覆盖、计划模式感知等. 提供多个命令: /cowork:cowork(设计+实现+解决)、/cowork:question(并行研究+综合)、/cowork:review(实现后双代理审查). 捆绑了无限制的 Codex 运行时, 支持完整的文件系统和网络访问. | Claude Code<br>Codex | ⭐ | 0 |
| [hamelsmu/claude-review-loop](https://github.com/hamelsmu/claude-review-loop) | 一个 Claude Code 插件, 可将自动代码审查循环添加到您的工作流程中. 使用 `/review-loop` 时, 该插件会创建一个两阶段生命周期.<br> 任务阶段: 你描述一项任务, Claude 负责执行<br>2. 审查阶段: 当 Claude 完成后, 会自动运行 Codex 进行独立代码审查, 然后要求 Claude 处理反馈意见<br> 结果: 在您接受更改之前, 每项任务都会得到独立的二次审核意见. | Claude Code/Codex | ⭐ | 638 |
| [joeseesun/qiaomu-heavyskill](https://github.com/joeseesun/qiaomu-heavyskill) | 多AI并行深度推理工具, 让Claude Code实现多视角独立思考, Codex主持批判性讨论, 生成比单一答案更扎实的报告. 提供并行多视角推理(启动3-5个完全独立的AI agent并行思考)、Codex主持讨论(找出盲点综合结论)、两种模式(验证模式-有正确答案问题/讨论模式-无唯一答案问题)和多格式报告输出(traces/原始输出/Markdown/HTML杂志风格/合并PDF). 基于论文arXiv:2605.02396, 证明讨论是生成性的. 技术栈: Claude Code CLI + Codex Plugin + HTML/CSS. | Claude Code<br>OpenAI Codex | ⭐ | 68 |
| [EpicStaff/EpicStaff](https://github.com/EpicStaff/EpicStaff) | 企业级多代理编排平台,提供可视化工作流构建器和Django后端. 核心理念:"我们隐藏复杂性,而非逻辑". 提供Visual+Code混合环境:拖拽式AI工作流编辑器+Python核心逻辑注入、跨流代理上下文(Redis/PostgreSQL持久记忆)、Django多代理后端. 30+贡献者. | 自托管Web平台(Django+Redis+PostgreSQL) | ⭐ | 238 |
| [drivelineresearch/moa-x](https://github.com/drivelineresearch/moa-x) | 让多个模型并行指定计划. 不让一个模型从头想到尾, 让多个模型分层协作. 参考 [2024/06/07, Mixture-of-Agents 论文, Mixture-of-Agents Enhances Large Language Model Capabilities](https://arxiv.org/abs/2406.04692), 指向了不同的任务: 为编 Coding Agent 制定实施计划, 而不是聊天回答. 并行让三位不同的提案者(OpenAI codex、Google gemini、Anthropic claude Sonnet)并行阅读仓库, 自己做网络研究, 然后写一个独立计划. 其中两个计划随后在广播模式下进行细化(每个精炼者都能看到每一个计划). 最后是父级 Claude Opus 会话把整个计划整合成一个你可以付诸行动的计划. 它被设计成在 Claude Code 中运行的技能, 也提供独立的 Python 运行时. | Claude Code/Codex | ⭐ | 16 |


## 2.4  Agent Operating System(One Person, One Software Company)
-------


[2026/06/19, 阿良｜AI 工作流, @RealYDT 这两天, 我用 Codex 搭了一个自己的 AI 个人操作系统: RealYDT OS. ](https://x.com/RealYDT/status/2067809436358373744) 作者借助 Codex 搭建专属 AI 个人操作系统 RealYDT OS, 区别于普通工具合集, 是一套完整规则与实操沉淀体系, 通过 README.md(长期定位), RULES.md(永久规则), LEARNING_SOURCES.md(学习来源), CONTENT_PLAN.md(90 天内容计划), WORKFLOWS.md(真实实操记录), IDEAS.md(长期选题库) 6类文档
1. 每次让 Codex 执行任务前, 它都要先读取 RULES.md(系统设定严格创作准则): 不追热点, 不搬运 AI 新闻, 不写标题党, 未实测的工具必须标注“未实测”, 优先真实实验. 2. 但只有规则还不够, 又建立了 WORKFLOWS.md, 专门记录每次 AI 实操的目标、步骤、Prompt、结果、限制和验证状态. 工作流分为: 草稿, 测试中, 已验证, 可复用, 已停用
3. 只有完成验证的记录, 才会被转化成教程或工具建议. 这套系统目前只验证了文件创建和规则读取流程, 还不能证明它已经提高了长期效率. 作者接下来我会继续用它完成真实项目, 并记录哪些规则有效、哪些流程需要修改.



| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [multica-ai/multica](https://github.com/multica-ai/multica) | 开源平台, 将编码智能体转变为真正的团队成员. 核心功能包括: 智能体作为团队成员(有个人资料、出现在看板、发表评论、创建问题、主动报告障碍)、自主执行(完整任务生命周期管理、WebSocket 实时进度流)、可复用技能(每个解决方案成为团队可复用技能)、统一运行时(一个仪表板管理所有计算资源)、多工作区(跨团队组织工作, 工作区级隔离). | Claude Code<br>Codex | ⭐ | 2,865 |
| [EvolutionAPI/evo-nexus](https://github.com/EvolutionAPI/evo-nexus) | 开源的多智能体操作系统层, 基于 Claude Code CLI 协议构建但不锁定任何单一 LLM 提供商. 默认运行在 Anthropic 的 claude CLI 上, 可透明切换到 OpenAI、Google Gemini、OpenRouter、AWS Bedrock、Google Vertex AI 或 Codex Auth. 将单个 CLI 安装转变为 38 个专业智能体团队, 分为 17 个业务智能体和 21 个工程智能体. 核心功能包括: Markdown 优先的智能体设计、175+ 技能覆盖金融、社区、社交、工程等领域、多提供商支持、MCP 集成(Google Calendar、Gmail、GitHub 等 19 个集成)、斜杠命令、持久化记忆、Web 仪表板、自动化例程(早会简报、邮件分类、社区监控、财务报告等). 适用于企业日常运营管理、软件开发工作流、多智能体协作等场景. 借鉴了 [`yeachan-heo/oh-my-claudecode`](https://github.com/yeachan-heo/oh-my-claudecode), 参见 [`Third-Party Notices`](https://github.com/EvolutionAPI/evo-nexus/blob/main/NOTICE.md). | Claude Code/OpenAI/Gemini/OpenRouter/Bedrock/Vertex AI | ⭐⭐ | 3,542 |
| [AgentsMesh](https://github.com/AgentsMesh/AgentsMesh) | 五个人的团队, 五十个人的产出. AgentPod 远程 AI 工作站、多智能体协作、任务管理、自托管运行器、多智能体支持、多 Git 提供商集成、多租户和企业就绪等. | 多 Agent 支持 | ⭐⭐⭐⭐ | 1,623 |
| [Stanshy/AgentHub](https://github.com/Stanshy/AgentHub) | "一个人,一家软件公司"理念的Electron桌面应用,从单个应用管理47个AI代理. 采用Harness Engineering(Skills+Hooks+FileWatchers)实现有纪律、可追踪的AI工作流. | Claude Code | ⭐ | 182 |
| [revfactory/harness](https://github.com/revfactory/harness) | Claude Code的团队架构工厂(Team-Architecture Factory)元技能. 一句话"build a harness for this project"即可根据领域描述自动生成代理团队定义和技能. 6种架构模式(Pipeline/Fan-out/Fan-in/Expert Pool/Producer-Reviewer/Supervisor/Hierarchical Delegation),配套100个生产就绪的代理团队Harness(10个领域,1,808文件). | Claude Code | ⭐⭐ | 5,167 |
| [nateherkai/AIS-OS](https://github.com/nateherkai/AIS-OS) | AI操作系统(AIOS)入门套件,将Claude Code转变为个人AI操作系统. 3个技能:/onboard(7问题访谈设置向导)、/audit(每周四Cs差距报告)、/level-up(每周三Ms访谈→交付一个产物). 配套两个框架:三Ms(Mindset→Method→Machine)和四Cs. 定位为AI自动化协会(AIS)成员的AIOS入门工具. | Claude Code | ⭐ | 635 |
| [Auto-Company](https://github.com/MaxMiksa/Auto-Company) | 全天候自主运行的 AI 公司, 编排 14 个自主 Agent(模拟世界级领域专家), 实现从产品构思、决策、编码、部署到营销全流程自动化. 双引擎(Claude Code/Codex CLI), consensus.md 极简人类干预(编辑"Next Action"即可转向), 3 周期强制收敛(ideation→validation→execution), 支持 macOS/Windows/WSL2. | Claude Code<br>Codex CLI | ⭐ | 1,230 |
| [crew44](https://github.com/getcrew44/crew44) | 本地优先的 AI 专业智能体编排器, 将已有编码 Agent 转变为协调团队(Go+React+Electron 架构). 核心概念: Runtime→Agent→Skill→Handover→Goal, 每角色绑定最合适模型, SKILL.md 技能累积复用, 独立 git worktree 隔离, 全部运行在 127.0.0.1 无遥测无云端. 支持 11 种 Runtime(Claude/Codex/Cursor/Gemini/OpenCode 等), macOS/Windows/Linux 三端, MIT 开源. | 多 Agent 支持(11种Runtime) | ⭐ | 328 |


# 📝 3 持久化记忆(Persistent Memory)
-------

持久化记忆有多种方式

1. 比如 Qoder内部其实有三套知识系统: ① Memory 负责记用户习惯; ② Repo Wiki 负责项目百科; ③ Knowledge Cards负责技术栈和模块知识;

2. [九原客 @9hills, 尝试了多种 Agent Memory 实现, 只有两种我觉得还有点用.](https://x.com/9hills/status/2059050876921393287) 将记忆划分为 6 类: ① 条目类/向量类; ② 卡片类/知识卡片; ③ 图谱类/关系图谱; ④ 画像类/Profile; ⑤ 记忆块类/Context Block; ⑥ 轨迹摘要类/Memory Stream;


## 3.1 用户习惯记忆
-------

参见[大佬 Leo(@runes_leo) 的帖子](https://x.com/runes_leo/status/2033324111615693168), 让 AI Agent 越用越懂你, 有两条路.

| 路线 | 描述 |
|:---:|:----:|
| Prompt | 对话结束自动沉淀经验到 markdown 文件, 可以按照级别. 下次启动时加载. 改的是 context 而不是权重, 零 GPU, 零成本. |
| Embedding | 走的是权重层——拦截你的对话, 后台异步跑 RL 训练, 模型参数直接更新. 零标注, 边聊边练. |

两条路的终点一样: 用得越久, agent 越像你的分身. 区别在于 prompt 层有天花板(context 窗口), 权重层没有.

[Agent Memory Techniques](https://github.com/NirDiamant/Agent_Memory_Techniques) 学习所有 LLM 代理的记忆技巧.

[2026/06/04, Yanhua @yanhua1010, 这应该是目前最接近正解的 Agent 记忆方案](https://x.com/yanhua1010/status/2062345653079224458)

[2026/06/05, Easycompany @Easycompany333, 小白真正能让Codex提效的使用方法](https://x.com/Easycompany333/status/2062829030131568924) 作者通过 7 个 markdown 文件搭建了一套 Codex 的记忆框架. 如果把整套框架类比公司, AGENTS.md 就是公司的企业制度、企业文化; FOUNDER.md 是个人的偏好、风格; MEMORY.md 通过 global(全局底层规则), founder(Founder 稳定偏好), project:easy-company(Easy一人公司公司级项目记忆), current_session(当前会话上下文), 其他项目默认不读, 除非你明确要求跨项目参考. LOOP.md 的作用就是把如何迭代和优化 Harness 文档的规则写清楚, 因为记忆等内容, 要学会优化和迭代, 智能体才能算的上智能. RULES.md 顾名思义, 这个就是告诉 agents 们哪些事情不能做, 哪些事情就算是做, 也要等我来审批之类的, 类似于企业合同、协议、约束等等; 6. LOG.md 主要是追溯的责任, 日志, 方便与回滚和追责. README.md 是公司的员工手册就行.


### 3.1.1 Prompt 记忆
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [AGI-is-going-to-arrive/Memory-Palace](https://github.com/AGI-is-going-to-arrive/Memory-Palace) | 记忆宫殿为人工智能代理提供了持久上下文和无缝的跨会话连续性. 它为 LLM 提供了持久、可搜索和可审计的历史上下文——所以你的代理在每次对话中都不会 "从零开始", 通过统一的 MCP(模型上下文协议)接口, Memory Palace 为 Codex、Claude Code、Gemini CLI 和 OpenCode 提供了集成路径, 并为光标和反重力提供了文档说明. 目前已验证的范围和已知边界已在 docs/skills/SKILLS_QUICKSTART_EN.md 文献中记录. | Codex/Claude Code/Gemini/OpenCode | ⭐ | 255 |
| [okooo5km/memory-mcp-server](https://github.com/okooo5km/memory-mcp-server) | MCP 知识图谱管理服务器, Swift 实现, 为 LLM 提供持久记忆能力. 知识图谱存储、实体管理、关系跟踪、观察系统、强大搜索. | Claude/Cursor/Chatwise | ⭐ | 104 |
| [coleam00/mcp-mem0](https://github.com/coleam00/mcp-mem0) | 集成 Mem0 的 MCP 服务器, 提供长期记忆和语义搜索能力. 支持 save_memory、get_all_memories、search_memories 三个核心工具. | 多种 MCP 客户端 | ⭐ | 668 |
| [thedotmack/claude-mem](https://github.com/thedotmack/claude-mem) | 为 Claude Code 构建的持久记忆压缩系统, 自动捕获工具使用并生成语义摘要. 提供 5 个生命周期钩子、Web 查看器 UI、mem-search 技能、渐进式披露. | Claude Code | ⭐⭐⭐ | 46,436 |
| [supermemoryai/supermemory](https://github.com/supermemoryai/supermemory) | 高级记忆管理系统, 为 AI 代理提供持久化记忆和上下文管理能力. | 多 Agent 支持 | ⭐⭐⭐ | 22,022 |
| [tickernelz/opencode-mem](https://github.com/tickernelz/opencode-mem) | OpenCode 的记忆管理插件, 提供持久化记忆和上下文管理能力 | OpenCode | ⭐ | 879 |
| [rizal72/true-mem](https://github.com/rizal72/true-mem) | 真实记忆管理系统, 为 AI 代理提供持久化记忆和上下文管理能力 | 多 Agent 支持 | ⭐ | 130 |
| [Alenryuichi/openmemory-plus](https://github.com/Alenryuichi/openmemory-plus) | 增强型记忆管理系统, 为 AI 代理提供持久化记忆和上下文管理能力 | 多 Agent 支持 | ⭐ | 18 |
| [clopca/open-mem](https://github.com/clopca/open-mem) | 开源记忆管理系统, 为 AI 代理提供持久化记忆和上下文管理能力 | 多 Agent 支持 | ⭐ | 13 |
| [varun29ankuS/shodh-memory](https://github.com/varun29ankuS/shodh-memory) | 轻量级、纯离线、超高性能、自学习 / 自衰减的持久化内存系统, 基于神经科学理论设计, 通过算法实现智能的记忆存储、检索、衰减和关联. 实现 "记住重要的、忘记无关的、越用越智能". | 多 Agent 支持 | ⭐ | 189 |
| [topoteretes/cognee](https://github.com/topoteretes/cognee) | 为 AI Agents 提供持久记忆能力的工具, 通过 6 行代码即可实现, 结合向量搜索与图数据库, 将原始数据转化为结构化的知识图谱, 支持多种数据类型和部署方式 | 多 Agent 支持 | ⭐⭐⭐ | 15,045 |
| [peterskoett/self-improving-agent](https://github.com/peterskoett/self-improving-agent) | OpenClaw Skill, 让 Agent 记录犯过的错、学到的东西和用户纠正, 结构化存储到 .learnings 目录, 实现自我进化 | OpenClaw | ⭐ | 479 |
| [loryoncloud/Memory-Like-A-Tree](https://github.com/loryoncloud/Memory-Like-A-Tree) | 为 AI Agent 设计的记忆管理系统, 核心理念是 "Agent 正常工作, 树自动生长". 采用树状结构管理知识, 包括萌芽、绿叶、黄叶、枯叶和土壤等状态, 基于置信度的记忆管理, 支持知识的索引、搜索、衰减和清理, 提供自动化的 Cron 任务, 支持多 Agent 配置和 Obsidian 同步. | 多 Agent 支持 | ⭐ | 123 |
| [MemTensor/MemOS](https://github.com/MemTensor/MemOS) | 为 LLM 和 AI Agent 设计的记忆操作系统, 提供统一的记忆 API、多模态记忆支持、多立方体知识库管理、异步摄取和记忆反馈纠正功能. 支持云服务和本地部署两种方式, 可与 OpenClaw 集成, 实现 72% lower token usage 和多 Agent 记忆共享. | 多 Agent 支持 | ⭐⭐ | 8,220 |
| [gavdalf/total-recall](https://github.com/gavdalf/total-recall) | 为 OpenClaw 自治智能体打造的全自动记忆管理系统, 核心特点是无需人工干预、无数据库 / 向量库依赖, 通过五层观测记忆架构和夜间记忆整合 (Dream Cycle) 实现智能体对话内容的自动压缩、整合、归档与检索, 整体使用成本极低(月均 $0.03-$0.10).<br> 借鉴人类记忆的工作机制: 海马体捕捉即时体验, 睡眠时进行记忆整合(强化重要记忆、剔除无效信息), 对应到系统中:<br>1. 「五层架构」负责即时记忆捕捉与初步整合, 避免记忆遗漏;<br>Observer(观察者)→Reflector(反射器)→Session Recovery(会话恢复)→Reactive Watcher(反应式监控)→Pre-compaction hook(预压缩钩子);<br>2. 「Dream Cycle」负责夜间深度整合, 实现记忆的分类、归档、降冗余, 保持智能体上下文轻量化. 对 observations.md 进行深度处理, 仅归档不删除, 通过语义钩子保证归档内容可检索, 是实现记忆轻量化的核心.<br> 与其他智能体记忆工具的核心区别: 无需人工触发记忆保存 / 整理, 系统自主监控、自动处理, 零维护成本. | Claude Code | ⭐ | 251 |
| [volcengine/OpenViking](https://github.com/volcengine/OpenViking) | 火山引擎(ByteDance Volcengine) Viking 团队开源的专为 AI Agents 设计的上下文数据库, 核心基于文件系统范式统一管理 AI 智能体所需的记忆、资源、技能等上下文, 解决传统 RAG 与 Agent 开发中的上下文碎片化、检索低效、不可观测等核心问题, 目前仓库处于早期开发阶段(2026 年 1 月开源), 整体架构清晰、功能针对性强, 以下从仓库基础信息、核心定位与解决的问题、核心设计与功能、技术架构、使用与部署、社区与开发状态、优势与待完善点七个维度做详细分析. | Claude Code | ⭐⭐⭐ | 21,707 |
| [websitebutlers/codefire-app](https://github.com/websitebutlers/codefire-app) | 为 AI 编码代理提供持久化记忆的跨平台伴侣应用, 支持 Claude Code、Gemini CLI 等主流 AI 编码工具, 通过 MCP 协议提供 63 种工具包括任务跟踪、语义代码搜索、浏览器自动化等功能, 采用 Swift/SwiftUI 和 Electron/React 双架构实现. | Claude Code<br>Gemini CLI | ⭐ | 199 |
| [powermem](https://github.com/oceanbase/powermem) | 与 OpenClaw 集成的智能记忆系统, 为 AI 智能体提供准确、敏捷、经济的记忆能力. 主要特点包括: 48.77% 准确率提升、91.83% 响应速度提升、Token 减少 96.53%. 核心功能: 智能记忆管理(基于艾宾浩斯遗忘曲线)、用户档案支持、多智能体支持(共享 / 隔离记忆)、多模态支持(文本、图像、音频)、深度优化的数据存储(子存储支持、混合检索). | OpenClaw | ⭐ | 617 |
| [runesleo/claude-code-workflow](https://github.com/runesleo/claude-code-workflow) | 为 Claude Code 提供的经过实战测试的工作流模板, 包含记忆管理、上下文工程和任务路由功能. 采用三层架构设计: 自动加载的规则、按需加载的文档和热数据. 核心功能包括: 记忆管理、上下文管理、任务路由、完成前验证和自动保存. | Claude Code | ⭐ | 539 |
| [nhevers/MoltBrain](https://github.com/nhevers/MoltBrain) | 为 OpenClaw、MoltBook 和 Claude Code 提供的长期记忆层, 自动学习和回忆项目上下文. 核心功能包括: 自动捕获发现和决策、语义搜索、Web 查看器、分析跟踪、标签和过滤器、收藏功能、导出功能等. 技术架构基于 SQLite 数据库、ChromaDB 向量搜索和 Web 查看器 UI, 支持多平台集成和 x402 微支付存储服务. | OpenClaw<br>MoltBook<br>Claude Code | ⭐ | 319 |
| [memvid/claude-brain](https://github.com/memvid/claude-brain) | 为 Claude Code 提供持久化记忆的插件, 解决会话间无记忆的问题. 核心目标是让 Claude Code 能够记住之前的对话、决策和解决方案, 实现类似人类的记忆能力. 技术上通过单个文件 (.claude/mind.mv2) 存储记忆, 无需数据库或云服务, 基于 Rust 核心实现亚毫秒级搜索速度. 主要功能包括: 会话上下文自动捕获、记忆搜索、自然语言查询、记忆统计等. 使用场景包括: 跨会话的项目开发、持续的调试过程、团队协作中的知识共享等. 特点是 100% 本地存储、支持版本控制、可轻松传输和共享. | Claude Code | ⭐ | 477 |
| [agentic-box/memora](https://github.com/agentic-box/memora) | 为 AI 智能体提供持久化记忆的轻量级 MCP 服务器, 支持语义记忆存储、知识图谱、会话回忆和跨会话上下文. 核心功能包括: 持久化存储(SQLite + 云同步 S3/R2/D1)、语义搜索(TF-IDF、sentence-transformers、OpenAI)、LLM 去重、记忆链接、知识图谱可视化、实时图表服务器、基于 RAG 的记忆聊天等. 技术架构基于 Python 实现, 支持 Claude Code 和 Codex CLI 集成. | Claude Code<br>Codex CLI | ⭐ | 381 |
| [ContextKeep](https://github.com/mordang7/ContextKeep) | 为 AI 智能体 (Claude、Cursor、Gemini、OpenCode 等) 提供持久化、可搜索的记忆系统, 解决会话间无记忆的问题. 核心功能包括: 无限上下文存储(无过期、无大小限制)、节省 Token 和 API 成本、通用兼容性(支持任何 MCP 合规客户端)、Memory Index Protocol(两步检索系统)、现代化 Web 仪表盘(网格、列表、日历视图)、100% 本地存储(注重隐私)、智能搜索(关键词和语义搜索)、Linux 服务支持. 技术架构基于 SQLite 存储, 支持多种传输方式: Stdio(本地)、SSE(远程 / 家庭实验室)、SSH. 核心 MCP 工具包括: list_all_memories()、retrieve_memory()、store_memory()、search_memories()、list_recent_memories(). 使用场景包括: 跨会话的项目开发、持续的调试过程、团队协作中的知识共享等. | Claude<br>Cursor<br>Gemini<br>OpenCode | ⭐ | 141 |
| [TraceRAG](https://github.com/youngjoey-ai/tracerag) | 一个强调工程化、可观测、可测试、可扩展的 RAG 项目, 目标是把文档导入、切块、向量化、检索、带来源回答、评估与后续 tracing 拆成可独立验证的阶段, 逐步演进成一个可维护、可解释、可复盘的生产级 RAG. 核心功能包括: 文档导入与切块、向量生成与存储、向量检索与混合检索、带来源的回答生成、全链路 tracing、LLM-as-a-judge 评估等. 技术栈基于 FastAPI、PostgreSQL + pgvector、SQLAlchemy + Alembic、LangChain、DashScope、LangGraph、Redis、Langfuse 等. | N/A | ⭐ | 15 |
| [agentmemory](https://github.com/rohitg00/agentmemory) | 为 AI 编码智能体提供持久化记忆系统, 解决会话间无记忆的问题. 核心目标是让智能体能够记住之前的对话、决策和解决方案, 实现跨会话的上下文连续性. 核心功能包括: 自动捕获(工具使用、文件编辑、测试运行、错误)、LLM 压缩(将原始观察压缩为结构化事实、概念和叙述)、上下文注入(在会话开始时注入过去的知识)、语义搜索(混合 BM25 + 向量搜索)、记忆进化(记忆随时间版本化、相互取代、形成关系图)、项目配置文件(每个项目的聚合智能)、自动遗忘(TTL 过期、矛盾检测、基于重要性的驱逐)、隐私优先(存储前剥离 API 密钥、机密)、自我修复(断路器、提供商回退链、自我纠正 LLM 输出、健康监控)、Claude Code 桥接、跨智能体 MCP、知识图谱等. 技术架构基于 iii-engine 的三个原语: HTTP Triggers、KV State + 内存向量索引、Streams (WebSocket), 支持多种 LLM 提供商和嵌入提供商, 混合搜索(BM25 + 向量 + 图), 4 层记忆巩固管道. 使用场景包括: 跨会话的项目开发、持续的调试过程、团队协作中的知识共享等. 支持的平台包括: Claude Code、Claude Code SDK、Cursor、Gemini CLI、OpenCode、Cline / Continue、任何 MCP 客户端、任何通过 REST API 集成的智能体. | Claude Code<br>Cursor<br>Gemini CLI<br>OpenCode<br>Cline / Continue<br>Any MCP client | ⭐ | 3,012 |
| [memvid/memvid](https://github.com/memvid/memvid) | 为 AI Agent 设计的单文件内存层, 替代复杂的 RAG 管道和基于服务器的向量数据库. 核心目标是将数据、嵌入、搜索结构和元数据打包到单个 `.mv2` 文件中, 实现无服务器、便携式的持久化长期记忆. 技术特点包括: 1) 智能帧架构(受视频编码启发, 追加式高效帧序列), 2) 多模态支持(文本嵌入、CLIP 图像搜索、Whisper 音频转录、PDF 提取), 3) 亚毫秒级检索性能(P50: 0.025ms, P99: 0.075ms, 吞吐量比标准方案高 1,372 倍), 4) 时间旅行调试(支持回滚、重放或分支任何内存状态), 5) 模型无关性(支持多种嵌入模型). 性能优势: 在 LoCoMo 基准测试中准确率比任何其他内存系统高 35%, 多跳推理高 76%, 时间推理高 56%. 使用场景包括: 长期运行的 AI Agent、企业知识库、离线优先 AI 系统、代码库理解、客户支持 Agent、工作流自动化等. | 多 Agent 支持 | ⭐⭐⭐ | 15,299 |
| [hermes-lcm](https://github.com/stephenschoettler/hermes-lcm) |  基于 LCM 论文, 为 Hermes Agent 提供无损上下文管理, 确保对话信息永不丢失, 提供分层 DAG 摘要和回溯工具 | 适用于需要长时间保持上下文连贯性、回溯历史对话内容、对准确性要求高的场景 | Hermes Agent | ⭐ | 162 |
| [HKUDS/CatchMe](https://github.com/HKUDS/CatchMe) | 捕获个人完整数字足迹的轻量级工具, 无向量依赖且功能强大. 核心目标是让用户专注于工作, CatchMe 自动捕获其他所有内容, 并存储在本地确保隐私和安全. 技术特点包括: 事件驱动的录制(无计时器延迟, 即时捕获鼠标动作), 智能记忆层次结构(自动组织为 Day→Session→App→Location→Action 五层结构), 基于树的检索(无向量复杂性, 自上而下搜索), 零配置代理集成(单文件设置), 超轻量(~0.2GB 运行内存)和隐私优先, 丰富的 Web 界面. 主要功能包括: 个人编码助手(代码会话回放、编辑文件回忆、输入追踪), 个人深度研究(网页/PDF 浏览记录、搜索查询、阅读信息追踪), 个人文件管理器(文件变更追踪、文档访问、编辑审查), 数字生活概览(应用使用追踪、工作流回放、活动回忆). 使用场景包括: 个人数字活动记录与检索、AI 代理个性化、跨会话的工作记忆、个人知识管理等. 支持与 CLI 代理(OpenClaw、NanoBot、Claude、Cursor 等)集成. | OpenClaw<br>NanoBot<br>Claude<br>Cursor | ⭐ | 383 |
| [MemSkill](https://github.com/ViktorAxelsen/MemSkill) | 为智能体提供学习和进化记忆技能的框架, 用数据驱动的循环替代静态的、手工设计的记忆操作. 核心目标是通过学习可重用的记忆技能并随时间从数据中进化它们, 提高记忆质量和跨任务泛化能力. 技术特点包括: 技能条件记忆构建(为每个跨度组合相关技能, 一次性构建记忆)、从困难案例中进化技能(定期挖掘挑战性例子来完善现有技能并提出新技能)、可重用技能库(维护共享的、不断进化的技能库, 支持跨数据集和基础模型的转移)、高吞吐量评估(多API密钥轮询实现稳定并行调用)、可扩展训练和运行(多线程和多处理用于大规模训练和评估). 支持多种数据集: LoCoMo、LongMemEval、HotpotQA、ALFWorld. 技术栈基于 Python 实现, 提供完整的训练和评估流程. 使用场景包括: 长时程智能体的记忆管理、跨数据集的记忆技能转移、大规模记忆构建和评估等. | 多 Agent 支持 | ⭐ | 440 |
| [seojoonkim/memkraft](https://github.com/seojoonkim/memkraft) | 为 AI 智能体提供的无依赖、本地优先的记忆系统, 使用纯 Markdown 作为存储格式. 核心目标是实现自改进循环、可审计的记忆跟踪和时间旅行功能. 技术特点包括: 1) 零依赖(仅使用 Python 标准库), 2) 双时态事实层(跟踪事实的有效时间和记录时间), 3) 记忆层级(core/recall/archival), 4) 类型感知衰减(不同类型记忆有不同的衰减率), 5) 调试假设跟踪(完整的 OBSERVE→HYPOTHESIZE→EXPERIMENT→CONCLUDE 循环), 6) 记忆快照和时间旅行(可以回溯到过去的记忆状态), 7) 多语言支持(EN/KR/CN/JP). 主要功能包括: 自动提取(从文本中提取实体和事实)、智能搜索(混合搜索)、代理搜索(多跳搜索, 支持上下文感知重新排序)、健康检查、梦想周期(夜间自动维护)、冲突检测和解决、记忆快照和时间旅行、通道上下文记忆、任务连续性注册、代理工作记忆等. 在 LongMemEval 基准测试中达到 98.0% 的准确率, 超过 MemPalace (96.6%) 和 MEMENTO by Microsoft (90.8%). 使用场景包括: 长期运行的 AI 代理、跨会话的项目开发、持续的调试过程、团队协作中的知识共享、个人知识管理、会议准备、调试假设跟踪等. 支持与 Claude Code、OpenClaw、Cursor、OpenAI、MCP、LangChain 等集成. | 多 Agent 支持 | ⭐⭐⭐ | 1,470 |
| [polyxmedia/mnemos](https://github.com/polyxmedia/mnemos) | 为 AI 编码代理提供持久化记忆和技能系统的 MCP 原生工具, 单 Go 二进制文件, 零依赖. 核心目标是构建 AI 编码代理的学习循环, 通过结构化纠正复合成技能, 回顾性重放展示所学内容. 技术特点包括: 1) 纠正日记(tried/wrong_because/fix 作为一等观察类型), 2) 从纠正到技能的自动提升(确定性模式挖掘, 无 LLM), 3) 回顾性重放(生成包含后续所学内容的 Markdown 回顾), 4) 反思(自纠正机制), 5) 提示注入扫描(内存写入边界的安全防护), 6) 压缩恢复(专门的 API 表面), 7) 动态组合预热(会话启动时的上下文注入), 8) 混合检索(BM25 + 向量), 9) 双时态存储, 10) 可移植技能包, 11) Obsidian 保险库导出. 性能优势: 会话启动 <10ms, 搜索亚毫秒级, 无 Python、Docker 或向量数据库依赖. 使用场景包括: 长期运行的 AI 编码代理、跨会话的项目开发、持续的调试过程、团队协作中的知识共享等. 支持与 Claude Code、Cursor、Windsurf、OpenAI Codex CLI 等 MCP 兼容客户端集成. | 多 Agent 支持 | ⭐ | 5 |
| [memodb-io/Acontext](https://github.com/memodb-io/Acontext) | 为 AI 代理提供开源的技能记忆层, 自动捕获代理运行中的学习内容并将其存储为代理技能文件. 核心目标是让代理能够从错误中学习并重用有效的方法, 避免不透明的记忆污染上下文. 技术特点包括: 1) 技能即记忆, 记忆即技能(技能文件采用 Markdown 格式, 可在任何框架中使用), 2) 用户设计结构(通过附加技能定义内存的模式、命名和文件布局), 3) 渐进式披露而非搜索(代理通过工具调用和推理获取所需内容), 4) 可作为 ZIP 下载在任何地方重用, 5) 支持自托管(提供 acontext-cli 快速部署), 6) 提供 Python 和 TypeScript SDK, 7) 包含上下文工程、磁盘、沙箱和代理工具等功能. 主要功能包括: 会话消息存储、任务提取、学习蒸馏、技能代理更新、渐进式技能检索等. 使用场景包括: 改进代理性能、构建能够学习和进化的 AI 代理、跨代理/LLM/框架共享技能、长期运行的 AI 代理、企业知识库、离线优先 AI 系统、代码库理解、客户支持代理、工作流自动化等. | 多 Agent 支持 | ⭐ | 3,346 |
| [kingjulio8238/Memary](https://github.com/kingjulio8238/Memary) | 为自主 AI 代理设计的开源记忆层系统, 模拟人类记忆机制推进智能体发展. 核心功能包括: 自动记忆生成(随代理交互自动更新)、记忆模块(Memory Stream + Entity Knowledge Store, 跟踪用户偏好)、知识图谱存储(支持 FalkorDB 或 Neo4j, 递归检索 + 多跳推理)、多代理支持(多图能力, 不同代理独立记忆)、内置 ReAct 代理(含搜索、视觉、定位、股票等工具)、支持本地模型(Ollama/Llama 3/LLaVA)或云端模型(OpenAI)、Streamlit 仪表盘 UI. 技术架构受 Microsoft K-LaMP 论文启发, 实现时间线分析、主题提取、实体相关性排序、上下文窗口动态组装等功能. 即将推出记忆回溯功能. | 多 Agent 支持 | ⭐ | 2,599 |
| [brobertsaz/claude-os](https://github.com/brobertsaz/claude-os) | 为 Claude Code 提供持久化记忆和上下文连续性的系统,让 Claude 能够记住项目决策、模式和解决方案,支持跨会话学习.核心功能包括:自然语言记忆系统(只需说"remember this")、混合索引系统(tree-sitter 结构索引 + 选择性语义嵌入,10,000 文件 30 秒索引完成)、Session 管理(自动恢复会话状态)、知识生命周期管理(去重、合并、归档、健康报告)、技能库管理(36+ 社区技能,一键安装)、实时看板(Agent-OS 规格跟踪)、Web UI 界面、100% 本地存储.技术栈基于 Python、SQLite + sqlite-vec、Redis、FastAPI、React.使用场景包括:跨会话的项目开发、持续的调试过程、团队协作中的知识共享、AI 编码代理的长期学习等. | Claude Code | ⭐ | 268 |
| [`gastownhall/beads`](https://github.com/gastownhall/beads) | 分布式图形问题跟踪器, 为 AI 代理提供持久化、结构化的记忆. 用依赖感知图替代混乱的 markdown 计划, 让代理能够处理长时任务而不丢失上下文. 基于 Dolt 数据库, 支持版本控制、JSON 输出、依赖跟踪、自动就绪任务检测、语义记忆衰减、知识图谱链接等功能. 提供嵌入式和服务器两种模式, 支持多代理协作和 Git-Free 使用. | Claude Code<br>Cursor<br>OpenCode<br>多 Agent 支持 | ⭐⭐⭐⭐ | 22,765 |
| [matrixorigin/Memoria](https://github.com/matrixorigin/Memoria) | 世界首个 Git 级别的 AI Agent 记忆持久化层, 让记忆的每次变更都可追踪、可审计、可回滚, 就像 Git 管理代码一样管理记忆. 核心目标是让 AI 记忆的修改变得安全可靠. 技术特点包括: 1) Git for Memory - 零拷贝分支、即时快照、时间点回滚, 每个记忆变更都有版本控制; 2) 混合语义检索 - 向量 + 全文混合检索, 按含义而非关键词查找记忆; 3) 自治治理 - 自动检测矛盾、隔离低置信度记忆、维护审计追踪; 4) 隐私优先 - 支持本地嵌入模型, 数据不离开机器; 5) 跨对话持久化 - 偏好、事实和决策在会话间持久保存; 6) 完整审计追踪 - 每个记忆变更都有快照和来源链. 技术架构基于 MatrixOne 的原生写时复制引擎, 支持云模式(Memoria Cloud)和自托管模式(Docker). 主要功能: 记忆存储/检索/搜索/纠正/清理/分支/快照/合并/回滚等, 还提供记忆治理、矛盾检测、洞察合成等维护工具. 支持五种记忆类型: semantic(项目事实)、profile(用户偏好)、procedural(工作流)、working(临时任务上下文)、episodic(会话摘要). 提供完整的 MCP 工具和 CLI, 支持与任何 MCP 兼容的 AI 工具集成. | 多 Agent 支持 | ⭐ | 256 |
| [beolson/ori-mnemos](https://github.com/beolson/ori-mnemos) | Ori Mnemos - 开源的 AI Agent 持久化记忆基础设施, 基于 Recursive Memory Harness (RMH) 框架实现认知架构级别的记忆系统. 技术栈: TypeScript(93.8%) + JavaScript(3.4%) + Python(2.6%). 核心特性包括持久化身份、知识图谱(PageRank + Louvain 社区检测)、三层记忆空间(self/notes/ops 不同衰减率)、认知遗忘机制(ACT-R 理论)、四信号融合检索(语义+BM25+PageRank+温度)、学习检索系统(Q-value 重排序、共现边学习、阶段元学习)和递归记忆探索. 性能基准: Recall@5 90% vs Mem0 29%, F1 0.68 vs Mem0 0.33, 延迟 120ms vs Mem0 1140ms. Token 经济性: 1000 笔记节省 99.6%. 提供 16 个 MCP 工具. 适用于长期对话 Agent、知识管理、研发辅助和研究助手. | Claude Code<br>Hermes Agent<br>Cursor<br>Codex<br>Windsurf<br>多平台(MCP) | ⭐ | 0 |
| [mem9-ai/mem9](https://github.com/mem9-ai/mem9) | AI Coding Agent 的持久化记忆系统, 解决智能体在会话之间遗忘所有信息的问题. 支持跨会话持久化记忆、多智能体共享记忆、混合检索(语义+关键词搜索)、可视化仪表板等功能. 服务端采用 Go 语言 REST API, 支持 TiDB/PostgreSQL/db9 存储后端, 原生向量搜索+全文搜索. 支持 OpenClaw、Hermes Agent、Claude Code、OpenCode、Codex、Dify 等多平台集成. 适用于长期项目开发、多智能体协作、跨设备工作和知识沉淀场景. | OpenClaw<br>Hermes Agent<br>Claude Code<br>OpenCode<br>Codex<br>Dify | ⭐ | 1,073 |
| [ukkit/memcord](https://github.com/ukkit/memcord) | 隐私优先、自托管的 MCP 服务器, 专注于 AI 对话历史的智能管理和检索. 技术栈: Python 3.10+ + MCP SDK 1.27.0+ + uv + Pydantic + NLTK + sumy. 核心架构采用 MCP 服务器、本地 JSON 存储和 TF-IDF 搜索引擎. 提供 28 个 MCP 工具(20 个基础工具 + 8 个高级工具), 分为核心操作、管理、搜索查询、时间导航、项目绑定、合并、状态监控和健康检查等类别. 关键特性包括智能摘要系统(四种后端: sumy/nltk/semantic/transformers)、多格式内容导入(文本/PDF/网页/结构化数据)、智能搜索系统(全文搜索 + 自然语言查询)、记忆槽合并(智能去重)、存储优化(压缩 + 归档)和项目绑定机制(.memcord 文件). 100% 本地存储, 零云端依赖. 符合 MCP 2025-11-25 规范, 支持 Resources/ResourceTemplates/Progress Notifications/Tool Annotations. 适用于软件开发团队、研究和文档工作、商务会议和个人知识库. | Claude Code CLI<br>Claude Desktop<br>VSCode<br>Google Antigravity<br>多平台(MCP) | ⭐ | 67 |
| [CodeAbra/iai-mcp](https://github.com/CodeAbra/iai-mcp) | 开源 AI 编码助手记忆系统(IAI = Independent Autistic Intelligence), 通过 MCP 协议为 Claude 等 AI 助手提供长期记忆, 自动捕获每轮对话. 采用三层记忆架构(Episodic/Semantic/Procedural), 纯本地运行、AES-256-GCM 加密, 99%+ 逐字召回率. | Claude Code<br>多平台(MCP) | ⭐ | 97 |
| [zhangfengcdt/memoir](https://github.com/zhangfengcdt/memoir) | 高性能 AI Agent 语义记忆系统, 为 AI 记忆管理带来 Git 风格版本控制. 支持语义路径(如 `profile.professional.skills.python`)、版本控制(分支/提交/合并/回滚)、O(log n) 分层查找和多 Agent 会话支持. 提供 CLI 和 Claude Code 插件集成. | Claude Code<br>多 Agent 支持 | ⭐ | 338 |
| [omermaksutii/mnemo](https://github.com/omermaksutii/mnemo) | 为 Claude Code 提供持久化记忆的 MCP 工具, 跨会话记住决策、约定和偏好. 基于 ONNX 嵌入模型和 HNSW 向量索引, 亚 100ms 语义搜索. 纯本地优先, 支持项目级和全局两级记忆, 自动捕获配置文件变更. | Claude Code<br>多平台(MCP) | ⭐ | 54 |
| [sdwolf4103/opencode-working-memory](https://github.com/sdwolf4103/opencode-working-memory) | OpenCode代理的自动记忆系统,提供持久化工作空间记忆、热会话上下文和基于压缩的记忆提取,无需额外API调用. 三层记忆架构(工作空间记忆/热会话状态/原生OpenCode状态),自动记忆注入(搭载OpenCode内置压缩请求,零额外LLM/API调用),缓存友好的布局,质量守卫(过滤噪音、脱敏凭证、去重、弱记忆衰减),支持`remember this`命令显式保存,以及`/memory`命令浏览和搜索记忆. | OpenCode | ⭐ | 144 |
| [akitaonrails/ai-memory](https://github.com/akitaonrails/ai-memory) | AI编码代理的长期记忆解决方案,支持跨代理厂商的任务交接. 核心功能包括:①跨代理交接——中途退出Claude Code,在同一目录启动Codex继续,无需重新解释;②Karpathy式LLM Wiki——从观察编译的Markdown页面;③多代理+多机器就绪——支持Claude Code、Codex、OpenCode等;④纯Markdown+Git——wiki可grep、可用Obsidian打开;⑤自动捕获——通过生命周期钩子自动捕获每个提示、工具调用和决策. | Claude Code<br>Codex<br>OpenCode | ⭐ | 470 |
| [mworldorg/markdown-memory](https://github.com/mworldorg/markdown-memory) | 跨平台文件式记忆与提示词桥接工具, 打通 claude.ai(规划) ↔ Claude Code(执行) ↔ Obsidian(长期记忆)的跨会话上下文壁垒. 提供 12 个 Claude Code 技能 + 1 个 claude.ai 技能(mm-web-bridge), 通过共享 Obsidian Vault 存储项目 passport/handoff/session 日志. 提示词桥接将 claude.ai 中的想法转为可粘贴的自含任务, 项目生命周期管理(init/resume/save/handoff/next), git 自动同步到 claude.ai Project Knowledge, 2 个 MCP 工具(secret_scan/health). 技术栈: Python/TypeScript/JavaScript/PowerShell, Node.js(npx 安装), stdio MCP server(TypeScript), Obsidian vault(Markdown). 适用于跨会话持久化项目记忆、跨聊天交接、会话保存与恢复和项目概览仪表盘. | Claude Code<br>claude.ai<br>Antigravity IDE | ⭐ | 26 |


### 3.1.2 Embedding 记忆向量化
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [Gen-Verse/OpenClaw-RL](https://github.com/Gen-Verse/OpenClaw-RL) | 完全异步的强化学习框架, 通过日常对话训练个性化 AI 代理, 支持在终端、GUI、SWE 和工具调用等真实场景中进行大规模 RL 训练, 提供 Binary RL、OPD 和 Combination 三种优化方法. 基于 4 组件异步架构(服务、收集、评估、训练), 支持本地部署和云端 Tinker 部署, 无需手动标注数据, 通过用户反馈自动优化策略. 适用于个人 AI 助手优化和通用代理训练. | 多 Agent 支持 | ⭐ | 4,751 |
| [Martian-Engineering/lossless-claw](https://github.com/Martian-Engineering/lossless-claw) | 基于 Voltropy LCM 论文的无损上下文管理插件, 用 DAG-based 摘要系统替代 OpenClaw 内置的滑动窗口压缩. 通过 SQLite 数据库存储所有消息, 将旧消息分层摘要形成有向无环图, 支持智能上下文组装和精确检索. 提供 lcm_grep、lcm_describe、lcm_expand 等工具实现历史记录搜索和详情召回, 确保对话历史完全无损且可查询. | 上下文管理 | ⭐ | 4,138 |
| [ruvnet/RuVector](https://github.com/ruvnet/RuVector) | 高性能、实时、自学习 AI 向量数据库和 GNN 内存数据库, 定位为完整的 Agentic AI 操作系统. 核心技术包括自学习引擎(GNN 层使搜索结果随时间提升 +12.4% recall)、50+ 注意力机制(FlashAttention-3/MLA/Mamba SSM 等)、混合搜索(RRF)、图 RAG、本地 AI 运行时(ruvllm 支持 GGUF 模型)、完整 Cypher 引擎、PostgreSQL 扩展(230+ SQL 函数)和 RVF 认知容器. 支持 Claude Code/GPT MCP 集成, 适用于企业级多智能体编排、AI 智能体长期记忆、基因组诊断等场景. 获 CES 2026 创新奖. | Claude Code<br>GPT<br>Rust<br>Node.js<br>浏览器(WASM) | ⭐⭐ | 3,964 |

### 3.1.3 DB 记忆
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [cosmicstack-labs/mercury-agent](https://github.com/cosmicstack-labs/mercury-agent) | 灵魂驱动的 AI 代理, 具备权限强化工具、Token 预算管理和多渠道访问能力. 核心特性包括: 1) 权限安全系统 - Shell 命令黑名单、文件夹级读写范围、待批准流程; 2) Second Brain 记忆 - SQLite + FTS5 全文搜索支持, 10 种记忆类型自动提取、冲突解决和自动整合; 3) 灵魂驱动 - 用户可自定义的人格 Markdown 文件(soul.md、persona.md、taste.md、heartbeat.md); 4) Token 感知 - 每日预算强制执行、超 70% 自动简洁化; 5) 24/7 运行 - 后台守护进程、自动重启崩溃恢复、开机自启、定时调度和主动通知; 6) 可扩展 - 单命令安装社区技能. 支持 CLI 和 Telegram 双渠道, 31 个内置工具, 基于 Agent Skills 规范. | 多 Agent 支持 | ⭐ | 1,777 |
| [GabrielMartinMoran/mind](https://github.com/GabrielMartinMoran/mind) | Mind - AI 工作流的自动化记忆层, 解决 AI Agent 在跨会话、跨工具、跨时间维度上丢失上下文的核心痛点. 技术栈: Bun 1.2+ + TypeScript + SQLite + FTS5. 核心特性包括多接口支持(CLI/MCP Server/HTTP API/Web UI)、三层记忆系统(T1 Hot/T2 Warm/T3 Cold, 自动提升+LRU 淘汰)、全文搜索(FTS5 Porter tokenizer)、语义搜索(可选 RAG + OpenAI embeddings)、Checkpoint 会话恢复(目标+待办)、链接与标签系统和 Neural Map 可视化(同心圆层级图谱). 提供 16 个 MCP 工具. 采用 Agent 能力矩阵(L1/L2/L3): L1 MCP 传输(所有 Agent)、L2 指令注入(Claude Code/OpenCode/Codex/Cursor)、L3 Hooks 自动化(Claude Code/OpenCode). 适用于个人 AI 工作流、项目知识管理、会话连续性和团队协作支持. | OpenCode<br>Claude Code<br>Codex<br>Cursor<br>Windsurf<br>Gemini CLI<br>VSCode<br>Antigravity | ⭐ | 100 |
| [Tencent/TencentDB-Agent-Memory](https://github.com/Tencent/TencentDB-Agent-Memory) | 符号化短期记忆+分层长期记忆的AI Agent记忆系统, 通过4层渐进式流水线实现本地化长期记忆, 零外部API依赖. 核心功能包括短期记忆压缩(Mermaid符号化画布+上下文卸载, 降低61% Token消耗)、长期分层记忆(L0对话→L1原子事实→L2场景→L3用户画像语义金字塔)、混合检索(BM25+向量+RRF融合召回)、记忆工具(tdai_memory_search/tdai_conversation_search)和白盒调试(所有中间产物可读). 技术栈: TypeScript 83.6% + Python 8.3% + SQLite + sqlite-vec + Mermaid + BM25. | OpenClaw<br>Hermes Gateway<br>腾讯云DeepSeek | ⭐⭐ | 1,539 |
| [AxDSan/mnemosyne](https://github.com/AxDSan/mnemosyne) | 零依赖、亚毫秒级AI记忆系统,专为Hermes Agent及其他代理设计. 本地优先,无需服务器、Docker或PostgreSQL,只需Python+SQLite. BEAM三层架构(热工作记忆/长期情景记忆/临时草稿本),混合搜索(50%向量+30%FTS5+20%重要性,全部在SQLite内完成),自动整合(通过mnemosyne_sleep()将旧工作记忆摘要迁移到情景记忆),时间三元组(带自动失效的时间感知知识图谱),导出/导入(一份JSON文件迁移整个记忆数据库),跨会话作用域. | Hermes Agent<br>Python代理<br>MCP客户端 | ⭐ | 589 |
| [JSingletonAI/dejavu](https://github.com/JSingletonAI/dejavu) | 跨所有AI工具的本地优先记忆层,无需云存储、无需账号注册. 运行在本地SQLite上,支持Python SDK、CLI、REST API和MCP四种接口方式访问同一记忆库. 统一记忆库——从CLI添加偏好,在Claude Desktop中检索,从Python代理查询;隐私优先——记忆存储在本地~/.dejavu,零遥测、零供应商锁定;Venice推理层——OpenAI兼容、零留存推理用于记忆提取和搜索. | Python SDK<br>CLI<br>REST API<br>MCP(Claude Desktop等) | ⭐ | 100 |
| [410979729/scope-recall-hermes](https://github.com/410979729/scope-recall-hermes) | 为 Hermes agent 提供作用域隔离的持久化记忆系统, 解决 agent 在新窗口/聊天中遗忘一切的问题. 三层架构(Journal 来源层 → SQLite 真值层 → LanceDB 向量检索伴侣层), 当前轮次召回(prefetch), 持久共享记忆 vs 本地临时上下文的作用域隔离, 混合检索(词汇/FTS/BM25 + 向量语义 + RRF 融合排序), 写时治理(确定性去重/近重复保守合并/规则提取/噪音过滤), 夜间对话摘要(批量 LLM/启发式记忆整合), Experience Kernel MVP(playbook + preflight 工具). 技术栈: Python 3.11+, SQLite, LanceDB(可选), sentence-transformers(可选), Hermes Agent 插件体系. 适用于 AI agent 长期记忆持久化、多窗口/多平台记忆隔离与共享、可审计可重建向量索引的记忆系统. | Hermes Agent<br>Python 代理<br>MCP 客户端 | ⭐ | 100 |



### 3.1.3 潜意识
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [letta-ai/claude-subconscious](https://github.com/letta-ai/claude-subconscious) | 为 CLAUDE CODE 构建了一个潜意识. 一个 Letta 代理, 它监视每个会话, 学习你的模式, 并在每次提示前自主注入记忆. 基于 Letta Code SDK 构建的 Claude Code 背景代理, 持续监听会话、读取代码库、建立长期记忆并在每次提示前提供指导. 通过 Read、Grep、Glob 等工具探索代码库, 支持跨会话、跨项目的记忆持久化, 可进行后台研究和模式检测. 提供 whisper、full、off 三种模式, 支持自定义模型和工具访问权限. | 潜意识代理 | ⭐ | 2,679 |
| [neudrive.ai](https://www.neudrive.ai) | AI 身份、记忆与信任的个人中心枢纽. Claude、ChatGPT、Codex、Cursor、Gemini、飞书等 AI 代理可通过此中心共享身份、偏好、记忆、技能、密钥和通信, 无需在每个平台重建上下文. 支持自托管和云端托管, 提供 CLI、浏览器扩展和 OAuth 接入. | 多平台 | ⭐ | 177 |
| [strukto-ai/mirage](https://github.com/strukto-ai/mirage) | AI Agent 的统一虚拟文件系统(UVFS), 将 S3、Google Drive、Slack、Gmail、GitHub 等服务挂载为单一文件树. AI 代理使用熟悉的 Unix 命令即可访问所有后端, 提供 Python 和 TypeScript SDK, 支持 OpenAI Agents SDK、Vercel AI SDK 等主流框架. | Claude Code<br>Codex<br>多平台 | ⭐ | 1,515 |
| [adelinamart/robrain](https://github.com/adelinamart/robrain) | 开源 AI Agent 团队共享记忆系统, 捕捉架构决策和被拒绝方案, 标记决策矛盾, 防止团队重复讨论已决定问题, 采用 PostgreSQL+pgvector 和 MCP 协议. | Claude Code<br>Cursor<br>Copilot | ⭐ | 54 |
| [EverMind-AI/EverOS](https://github.com/EverMind-AI/EverOS) | 统一长期记忆操作系统,用于自进化Agent应用、构建和评估,包含EverCore自组织记忆操作系统、HyperMem超图分层记忆和评估基准 | Claude Code<br>OpenClaw<br>Cursor<br>Ten Framework | ⭐⭐⭐ | 5,206 |

## 3.2 知识图谱
-------

### 3.2.1 记忆共享
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [mem0ai/mem0-mcp](https://github.com/mem0ai/mem0-mcp) | Mem0 MCP 服务器, 将 Mem0 Memory API 包装为 Model Context Protocol (MCP) 服务器, 支持添加、搜索、更新和删除长期记忆, 适用于 MCP 兼容客户端(Claude Desktop、Cursor、自定义代理) | 多 Agent 支持 | ⭐ | 642 |
| [cctrace](https://github.com/jimmc414/cctrace) | Claude Code 会话导出和导入工具, 支持将会话提取为可移植格式用于归档、分析或共享. 提供两种导出模式: 经典导出 (到 `~/claude_sessions/exports/`) 和可移植导出(到仓库内的 `.claude-sessions/`), 支持导入会话继续工作, 包含文件历史、待办事项、计划和配置的完整迁移 | Claude Code | ⭐ | 176 |
| [arisvas4/codified-context-infrastructure](https://github.com/arisvas4/codified-context-infrastructure) | 为 AI 编码代理提供结构化的上下文基础设施, 解决大型代码库中 AI 代理缺乏持久记忆的问题. 实现三层上下文架构: 热内存 (Constitution)、专业代理(Specialized Agents) 和冷内存(Knowledge Base + MCP), 支持按需加载上下文, 提高 token 使用效率, 适用于复杂代码库的 AI 辅助开发 | 多 Agent 支持 | ⭐ | 110 |
| [agentic-stack](https://github.com/codejunkie99/agentic-stack) | 可移植的 AI 大脑系统, 提供跨不同 AI 编码工具的知识和技能迁移能力. 四层内存结构(working/episodic/semantic/personal)、审查协议、渐进式技能系统、FTS5 内存搜索、内容聚类 | 跨工具知识迁移、项目持久 AI 记忆库、持续知识体系改进、一致的工作流和技能集. Agentic-Stack 把 AI 代理的记忆、技能和协议打包成一个可复用的 `.agent/` 目录. 目前适配八种主流编码工具, 换工具时不用重新配置. 记忆系统分四层, 夜间自动把重复出现的模式聚类成候选经验, 你审核后才会归档. 附带 CLI 工具链, 方便管理技能、搜索记忆和审核经验教训. | 多 Agent 支持 | ⭐ | 110 |

### 3.2.2 LLM WIKI/RAG
-------

[2026/04/07, @disksing, 也是跟风 vibe 了一个基于 db9 的 LLM Wiki.](https://x.com/disksing/status/2041508629904548184)

[2026/04/06, X@elliotchen100, Karpathy 的 LLM Wiki: 为什么这条推文炸了, 以及它真正在说什么](https://x.com/elliotchen100/status/2040981753490477403)

[2026/04/05, X@laozhang2579, Karpathy 最新分享: 用 LLM 搭建个人知识库, 告别 RAG 的低效循环](https://x.com/laozhang2579/status/2040732229035585615)

[2026/04/06, 范凯说 AI | Kai on AI @fankaishuoai, Karpathy 的 LLM Wiki 火了, 我改造了一下, 比原版更好用](https://x.com/fankaishuoai/status/2041171980494479679)

[2026/04/03, Yanhua @yanhua1010, 用 LLM + Obsidian 构建个人知识库: 基于 Karpathy 的"LLM Knowledge Bases"工作流](https://x.com/yanhua1010/status/2039966047378583815)

[2026/04/12, 撸毛吃猪脚饭 @mnmn94253156337, 看到D哥的一篇Obsidian+AI的教程, 感觉很有用, 分享一下《Obsidian : 主人, 我想思考》](https://x.com/mnmn94253156337/status/2043347445917331957)

[LLM Wiki v2](https://gist.github.com/rohitg00/2067ab416f7bbe447c1977edaaa681e2)
[2026/04/12, Nav Toor @heynavtoor, llm wiki V2, Extends Karpathy's original](https://x.com/heynavtoor/status/2043321909971202403)
[2026/04/12, Berryxia.AI @berryxia, Karpathy 的 LLM Wiki 48 小时冲到 5000 stars 后, v2 直接进化成"活的记忆系统"了！](https://x.com/berryxia/status/2043471951134646282)

[2026/05/17, 豆本豆 @Potatoloogs, 如何构建一个在你睡觉时也能运行整个业务的 Obsidian 知识库(完整课程)](https://x.com/Potatoloogs/status/2055535284419432860)

[2026/06/13, Introducing the Open Knowledge Format](https://cloud.google.com/blog/products/data-analytics/how-the-open-knowledge-format-can-improve-data-sharing) Google 提议了一个提案, [GoogleCloudPlatform/knowledge-catalog](https://github.com/GoogleCloudPlatform/knowledge-catalog). 随后有人汇总了 [2026/06/18, Y11 @seclink, 按照 Google Open Knowledge Format (OKF) 规范](https://x.com/seclink/status/2067506020318916661)

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [Karpathy LLM Wiki](https://github.com/Astro-Han/karpathy-llm-wiki) | 构建和维护Karpathy风格的LLM知识库, 支持摄取源、查询和维护 | Claude Code, Cursor, Codex等 | ⭐ | 176 |
| [llm-wiki-skill](https://github.com/sdyckjq-lab/llm-wiki-skill) | 基于 Karpathy 的 llm-wiki 方法论, 为 Claude Code、Codex、OpenClaw 等 agent 提供统一的个人知识库构建系统 | Claude Code, Codex, OpenClaw | ⭐ | 377 |
| [gnekt/My-Brain-Is-Full-Crew](https://github.com/gnekt/My-Brain-Is-Full-Crew) | 一个由 8+ AI 代理和 13 个专业技能组成的团队, 管理 Obsidian vault, 帮助用户组织、归档、连接、搜索、转录和分类电子邮件. 支持多语言, 通过聊天界面操作, 不需要手动管理文件. 适用于 PhD 学生、研究人员、有脑雾或工作记忆超负荷的人、非英语母语者等. | Claude Code | ⭐ | 2,473 |
| [llm_wiki](https://github.com/nashsu/llm_wiki) | 基于 Karpathy 的 LLM Wiki 模式, 构建了一个跨平台桌面应用, 自动将文档转换为结构化、互联的知识库. 核心功能包括两步链式思考摄取、4信号知识图谱、Louvain社区检测、图谱洞察、4阶段查询检索、深度研究、异步审查系统和 Chrome 网页裁剪器. 支持多格式文档、知识图谱可视化、多语言界面等. | 通用 LLM 应用 | ⭐ | 319 |
| [safishamsi/graphify](https://github.com/safishamsi/graphify) | 借助 Karpathy 的 LLM Wiki 思想实现的一款多模态 AI 编码助手知识图谱工具, 支持 19 种编程语言, 可处理代码、PDF、Markdown、截图等多种格式, 通过 AST 提取和 Claude 子代理并行处理构建知识图谱, 大幅减少 token 消耗(71.5x), 提供交互式图谱、查询功能和 Git 钩子集成, 支持 Claude Code、Codex、OpenCode、OpenClaw、Factory Droid 等多个平台. | 多平台 | ⭐⭐⭐ | 18,150 |
| [Hypatia](https://github.com/MarchLiu/hypatia) | 一个面向AI的记忆管理系统, 以古代亚历山大图书馆馆长希帕提娅命名, 构建结构化的知识图谱存储. 采用双数据库架构(DuckDB + SQLite FTS5), 支持知识条目和陈述三元组, 提供自定义JSE查询语言, 零外部模型依赖, 实现10-100倍于向量检索的性能和100%召回率. 适用于AI代理长期记忆、个人知识库和企业知识管理. | 多平台(Claude Code技能, 通用CLI) | ⭐⭐ | 129 |
| [GBrain](https://github.com/garrytan/gbrain) | 为 AI 代理构建的长期记忆和知识管理系统, 实现 Vannevar Bush 设想的"记忆扩展器". 采用"编译真理+时间线"知识模型, 支持混合搜索(关键词+向量+RRF融合), 实体检测和丰富管道. 基于 PostgreSQL + pgvector + Supabase, 提供 CLI/MCP 服务器/远程 API 三种访问方式. 核心特性: 知识复合增长, 零重复工作, 人类可读的 Markdown 格式, 生产就绪的技能包. 适用于个人知识管理, AI代理增强, 团队协作和企业知识库. | 多平台(OpenClaw, Hermes Agent, Claude Code, Cursor等). 相关扩展插件 [durang/gbrain-http-wrapper](https://github.com/durang/gbrain-http-wrapper) 和 [durang/gbrain-claude-connect](https://github.com/durang/gbrain-claude-connect) | ⭐⭐ | 3,391 |
| [MemPalace](https://github.com/milla-jovovich/mempalace) | 最高评分的 AI 记忆系统, 通过"宫殿"结构(wings/rooms/closets/drawers)组织记忆, 使用 ChromaDB 存储原始对话内容, 提供 96.6% 的 LongMemEval R@5 分数. 完全本地运行, 无外部 API 依赖, 支持知识图谱和 AAAK 压缩方言. 适用于个人开发者和团队的记忆管理, 可与 Claude、ChatGPT、Gemini、Llama 等多种AI系统集成. | 多平台(Claude Code, ChatGPT, Gemini, Llama, Mistral 等). | ⭐⭐⭐ | 40777 |
| [Wikiwise](https://github.com/TristanH/wikiwise) | 原生 macOS 应用, 将任何 markdown 文件文件夹转变为可浏览、可发布的 wiki, 由编码代理维护. 基于 Andrej Karpathy 的 llm-wiki 模式, LLM 增量构建和维护持久、互联的 wiki. | macOS | ⭐⭐ | 58
| [mempal](https://github.com/ZhangHanDong/mempal) | Coding Agent 的项目记忆工具, 单二进制, 混合检索, 10秒内带出处找回历史决策. 核心特性包括混合检索(BM25 + 向量语义搜索)、知识图谱(三元组 + 时态验证)、跨项目隧道、自描述协议、多语言嵌入、单文件存储(SQLite + sqlite-vec)、7个MCP工具、Agent日记和安全操作. [官网](https://zhanghandong.github.io/mempal) | 多平台(支持MCP协议的Agent) | ⭐ | 106 |
| [llm-wiki-compiler](https://github.com/atomicmemory/llm-wiki-compiler) | 知识编译器, 将原始源文件编译成相互链接的markdown wiki. 受 Karpathy 的 LLM Wiki 模式启发, 采用两阶段管道处理, 支持增量编译和复合查询, 提供 MCP 服务器供 AI 代理集成. | 多平台(支持MCP协议的Agent) | ⭐ | 536 |
| [nvk/llm-wiki](https://github.com/nvk/llm-wiki) | LLM Wiki - 为任何 AI agent 提供 LLM 编译的知识库系统, 实现自动化知识生命周期管理(研究→摄取→编译→查询→输出). 技术栈: Shell(94.1%) + JavaScript(5.9%). 核心架构采用 Hub-and-Topic Wiki 结构(hub 注册表 + 主题隔离)、零依赖设计(纯 Markdown + YAML frontmatter)和 LLM-as-Compiler 隐喻. 提供 10 大核心操作: Ingest/Ingest-Collection/Inventory/Dataset/Compile/Query/Research/Audit/Output/Lessons Learned. 高级特性包括并行多智能体研究(5/8/10 agents)、论题驱动研究(反确认偏差)、问题模式自动检测、置信度评分系统、双向链接双格式(Obsidian wikilink + markdown link)、结构守护者和活动日志. 支持 Claude Code(22K tokens)、OpenAI Codex(3K tokens)、OpenCode、Pi(1K tokens)等平台. 适用于学术文献综述、技术标准调研、知识管理、仓库差距分析和内容创作. | Claude Code<br>Codex<br>OpenCode<br>Pi<br>多平台 | ⭐ | 369 |
| [yifanfeng97/Hyper-Extract](https://github.com/yifanfeng97/Hyper-Extract) | 智能、LLM 驱动的知识提取与演进框架, 将高度非结构化的文本转化为持久化、可预测、强类型的知识摘要. 技术栈: Python 3.11+ + LangChain + FAISS + Pydantic + OpenAI API. 三层架构设计: Templates(80+ 预设模板覆盖 6 大领域) + Methods(KG-Gen, GraphRAG, LightRAG 等 10+ 提取引擎) + Auto-Types(8 种强类型知识结构). 支持 AutoModel/AutoList/AutoSet/AutoGraph/AutoHypergraph/AutoTemporalGraph/AutoSpatialGraph/AutoSpatioTemporalGraph 8 种知识结构. CLI 命令: parse/search/show/feed. 默认支持 OpenAI(gpt-4o-mini), 可扩展支持 Anthropic Claude 和 Google Gemini. 适用于传记信息提取、文献综述、法律案例分析、医疗病历分析、历史事件重建、知识库构建和关系网络分析. 是唯一支持空间图谱和超图的开源方案. | OpenAI<br>Anthropic Claude<br>Google Gemini | ⭐ | 842 |
| [atomicstrata/llm-wiki-compiler](https://github.com/atomicstrata/llm-wiki-compiler) | 基于 Karpathy LLM Wiki 模式的 wiki 编译器, 将原始源文件编译为相互链接的 Markdown wiki. 支持增量编译(SHA-256 变更检测)、双阶段处理(概念提取→页面生成)、多 Provider(Anthropic/OpenAI/Ollama/Copilot)、MCP 服务器和 Obsidian 兼容. | 多平台(支持MCP协议的Agent) | ⭐ | 1,090 |
| [szw321127/llm-wiki-for-code](https://github.com/szw321127/llm-wiki-for-code) | 面向 Codex 与 Claude Code 的持久代码库 Wiki(简称 pk). 把长期项目的代码实践、推荐方案、任务决策和证据关系保存到 `.project-knowledge/` 中. 支持任务前预检、任务后自动沉淀、知识治理、图谱可视化和 Obsidian 兼容. | Codex<br>Claude Code | ⭐ | 20 |
| [mnemo](https://github.com/zaydmulani09/mnemo) | 本地优先的 LLM 记忆层, 为自定义 LLM 管道提供持久化知识图谱和语义检索, 无需云端. 核心功能: 自动从对话提取实体、构建知识图谱(Rust+petgraph)、检索排序上下文并注入后续 prompt. 技术栈: Rust(79.4%)核心 + Python SDK(15.8%), SQLite(WAL)存储, Axum REST API, 支持 Ollama/OpenAI/Anthropic 多后端. 122 Rust测试 + 21 Python测试. 适用于为自定义 LLM 管道添加跨会话持久记忆. | 多平台(REST API + Python SDK + CLI) | ⭐ | 204 |
| [memanto](https://github.com/moorcheh-ai/memanto) | AI 编码助手的持久记忆代理(Claude Code/Cursor/Codex 等), 提供跨会话的长期可查询记忆. 核心三原语: remember/recall/answer, 支持13种记忆类型(指令/事实/决策/目标/偏好/关系等). 零索引延迟, 即写即搜. 支持时间查询、冲突检测、文件上传和每日摘要. 基于 Moorcheh 语义引擎(信息论检索, 非向量DB). 基准: 89.8% LongMemEval, 87.1% LoCoMo(超越 Mem0/Zep/Letta). 一键集成: memanto connect <tool-id>. | Claude Code<br>Cursor<br>Codex<br>Windsurf<br>Cline 等17+平台 | ⭐ | 742 |


### 3.2.3 Second Brain
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [Second-Brain](https://github.com/KasperZutterman/Second-Brain) | 收集整理公开 Zettelkastens/Second Brains/Digital Gardens 的 Awesome List, 当前收录 130+ 个公开知识库实例, 列出维护者、笔记站点 URL 及社交媒体链接. 附有额外资源链接(Maggie Appleton compilation、Nikita compilation、Best-of Digital Gardens 等). 涵盖 Obsidian Publish、Roam Research、GitHub wikis、个人站点、Notion 等多种知识库平台. 适用于寻找知识管理灵感、学习他人笔记结构和发现优质公开知识库. | 通用(参考资源) | ⭐ | 1,796 |

### 3.2.4 知识库插件
-------

#### 3.2.4.1 Obsidian
-------


[2026/06/20, 云析 @yunxi0623, Obsidian 的 10 大 AI Skill, 第 1 名安装量居然 37 万！](https://x.com/yunxi0623/status/2068195785993515404)

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [obsidian-ai-second-brain](https://github.com/helloianneo/obsidian-ai-second-brain) | [2026/04/13, Ian (伊恩) @ianneo_ai, 基于 Karpathy 的 LLM Wiki 方法把 Obsidian 和 Claude Code 接起来之后, 写东西的方式彻底变了！！](https://x.com/ianneo_ai/status/2043618182636961812) | 基于 Karpathy LLM Wiki 方法论的 AI 知识库方案, 通过 Obsidian + Claudian 插件 + Claude Code 构建个人知识管理系统, 支持素材自动整理、智能查询和知识库体检, 实现知识的复合增长. | ⭐ | 4 |
| [claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) | Claude + Obsidian知识伴侣, 基于Karpathy的LLM Wiki模式构建持久、复合的wiki库. 支持自动摄取源、智能查询、知识库体检和热缓存等功能, 提供10个技能和多智能体支持. | Claude Code | ⭐⭐⭐⭐ | 5,048 |
| [Obsidian-OpenCode-Knowledge](https://github.com/zxfccmm4/Obsidian-OpenCode-Knowledge) | 面向非技术用户的本地 AI 知识管理方案, 无需编程, 一键部署, 开箱即用. 支持多种 AI 服务提供商, 实现素材自动整理、智能查询和知识库体检, 以及社交媒体内容采集(小红书、抖音、Twitter/X、微博、B站、微信公众号等). | Obsidian + OpenCode + 多种 AI 服务 | ⭐⭐⭐⭐ | 120 |
| [Claudian](https://github.com/YishenTu/claudian) | 将 AI 编码代理(Claude Code、Codex、Opencode)嵌入到 Obsidian 库的插件, 库成为代理的工作目录. 支持侧边栏聊天、行内编辑、Slash 命令和技能、@提及文件/子代理/MCP 服务器、计划模式、指令模式、MCP 服务器连接、多标签对话等功能. 基于 TypeScript 开发, 支持多语言(i18n), 适用于 Obsidian 中的 AI 辅助文档编辑、代码编写和知识管理. | Obsidian | ⭐⭐⭐ | 9,565 |
| [obsidian-agent-client](https://github.com/RAIT-09/obsidian-agent-client) | 将 AI 代理(Claude Code、Codex、Gemini CLI)直接集成到 Obsidian 的插件, 基于 Zed 的 Agent Client Protocol (ACP) 构建. 支持 @notename 语法引用笔记、图片附件、斜杠命令、多代理切换、多会话并行、浮动聊天、模式与模型切换、会话历史恢复/分叉、聊天导出为 Markdown、终端集成、MCP 服务器支持等功能. 适用于在 Obsidian 中与 AI 代理协作进行文档编辑、知识管理和开发任务. | Obsidian | ⭐ | 1,848 |
| [Ar9av/obsidian-wiki](https://github.com/Ar9av/obsidian-wiki) | 基于 Andrej Karpathy 提出的 LLM Wiki 模式的知识管理框架, 将知识编译一次并保持更新而不是每次都重新检索(RAG). 技术栈: Python(57.6%) + HTML(33.5%) + Shell(8.9%). 核心架构采用三层设计(Raw Sources/Wiki/Schema)和 Delta Tracking 系统(SHA-256 哈希 + 时间戳). 提供 28 个技能覆盖设置、知识摄入(支持 PDF/Markdown/图片和多 Agent 历史)、查询检索、维护审计、导出可视化等功能. 关键特性包括增量摄入、来源可信度标记(提取/推断/争议)、置信度与生命周期管理、分层检索策略(index→summary→grep→full-page)和可选 QMD 语义搜索. 支持 15+ AI Agent 平台(Claude Code、Cursor、Windsurf、Codex、Gemini CLI、Antigravity、Kiro、Hermes、OpenClaw、OpenCode、Aider、Factory Droid、Trae、Copilot CLI、Kilocode). 适用于个人知识管理、跨项目知识复用、AI Agent 会话历史挖掘、团队知识库维护和研究探索. | 多平台(15+ Agent) | ⭐ | 988 |
| [jsgrrchg/NeverWrite](https://github.com/jsgrrchg/NeverWrite) | 本地优先的知识工作空间, Cursor 和 Obsidian 的混合体, 为多智能体并行工作流打造. 技术栈: Electron 41 + React 19 + TypeScript + Vite 8 + CodeMirror 6 + Rust 后端. Monorepo 结构: apps/desktop(主应用) + apps/web-clipper(浏览器扩展) + crates/(Rust 核心模块: ai/diff/index/types/vault). 核心特性包括 Vault 和工作区管理、Markdown 编辑(CodeMirror 6 + wikilink 补全)、实时预览、多格式支持(CSV/PDF/图片)、知识导航(反向链接/图谱视图/概念图)、AI 和变更控制(ACP 运行时集成 + 内联审查 + 累积操作日志)、Web Clipper(整页/选择/URL 剪藏). 伦理优先: 无黑盒、无混淆、无隐藏写入, 所有变更用户可见可审. 支持 Codex/Claude/Gemini/Kilo 四种 ACP 运行时. 适用于知识工作者、多智能体协作、透明度需求和本地优先倡导者. 当前 Pre-1.0, Apache-2.0 许可. | Codex<br>Claude<br>Gemini<br>Kilo | ⭐ | 459 |
| [breferrari/obsidian-mind](https://github.com/breferrari/obsidian-mind) | 为 AI 编码代理提供持久化记忆的 Obsidian 知识库模板. 通过 18 个斜杠命令、9 个子代理和 5 个生命周期钩子, 让代理自动记录决策、会议、事件、工作进展和绩效证据. 基于 QMD 语义搜索实现跨会话上下文检索. | Claude Code<br>Codex CLI<br>Gemini CLI | ⭐⭐⭐ | 2,386 |
| [SIXIANGGUO/cc-note-ops](https://github.com/SIXIANGGUO/cc-note-ops) | 基于Claude Code的Obsidian笔记操作面板,让用户通过按钮一键触发Claude Code执行Obsidian笔记操作. 核心功能是将Obsidian笔记库与Claude Code结合,提供操作面板界面,用户可以点击按钮让Claude Code自动完成笔记相关任务,例如将Obsidian笔记转化为公众号文章等. 参见[2026/05/20, 不滑锅 @buhuaguo1, 我给 Obsidian 做了个AI 创作台: 打开笔记, 就能让 Claude Code 直接改它](https://x.com/buhuaguo1/status/2057083421869080740) | Claude Code<br>Obsidian | ⭐ | 184 |
| [Kwipu](https://github.com/benmaster82/Kwipu) | 本地 Graph RAG 系统, 将 Markdown 笔记转化为可查询的知识图谱, 支持自然语言提问和跨文件关联回答. 专为 Obsidian vault 构建, 也兼容任意 Markdown 文件夹. 核心特性: 属性图谱索引(LLM提取实体关系三元组)、Obsidian 原生支持(wikilinks+YAML frontmatter)、混合检索(同义词扩展+向量搜索+BM25+时间匹配)、增量更新、多语言(6种)、反幻觉提示(引用来源)、全本地运行. 技术栈: Python+Ollama+LlamaIndex+nomic-embed-text. 提供 MCP 服务器. | Obsidian<br>多平台(MCP) | ⭐ | 195 |
| [YishenTu/claudian](https://github.com/YishenTu/claudian) | 将 AI 编码代理(Claude Code、Codex、Opencode)嵌入到 Obsidian 库的插件, 库成为代理的工作目录. 支持侧边栏聊天、行内编辑、Slash 命令和技能、@提及文件/子代理/MCP 服务器、计划模式、指令模式、MCP 服务器连接、多标签对话等功能. 基于 TypeScript 开发, 支持多语言(i18n), 适用于 Obsidian 中的 AI 辅助文档编辑、代码编写和知识管理. | Obsidian | ⭐⭐⭐ | 13,059 |

#### 3.2.4.2 notebooklm
-------


| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [notebooklm-py](https://github.com/teng-lin/notebooklm-py) | Google NotebookLM 的非官方 Python API 和 Agent Skill, 实现完整编程访问 NotebookLM 所有功能(notebook/source/chat/notes/sharing/research). 超越 Web UI 的能力: 批量下载、Quiz/Flashcard 结构化导出、PPTX 导出、Mind Map JSON 提取、Source fulltext 访问. 内容生成: Audio Overview(podcast)、Video、Slide Deck、Quiz、Flashcard、Report、Mind Map 等. 多接入方式: Python API、CLI、MCP Server、REST Server、AI Agent(Claude Code/Codex). 适用于自动化 NotebookLM 工作流和批量内容生成. | Claude Code<br>Codex<br>OpenClaw | ⭐⭐⭐ | 16,559 |

## 3.3 自我进化
-------

### 3.3.1 self-evolution
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [BayramAnnakov/claude-reflect](https://github.com/BayramAnnakov/claude-reflect) | 一个为 Claude Code 设计的自学习系统, 能够捕获用户的纠正并发现工作流模式, 将它们转化为永久记忆和可重用技能. 核心功能包括从纠正中学习、发现工作流模式、多语言支持和技能改进. 通过两阶段流程 (自动捕获和手动处理) 实现, 使用混合检测方法 (正则表达式和语义 AI 验证) 确保准确性. 支持将学习内容同步到多个目标文件, 并能从会话历史中发现重复模式生成可重用技能. 适用于提高 Claude Code 的准确性和自动化程度. | Claude Code | ⭐ | 886 |
| [primeline-ai/evolving-lite](https://github.com/primeline-ai/evolving-lite) | 一个为 Claude Code 设计的自学习系统, 能够从用户的纠正中学习, 记住有效的解决方案, 并在后续会话中自动应用这些知识. 采用四层反馈循环 (学习、上下文、自我修复、进化) 和分层激活机制, 从安全监控到深度记忆逐步提升. | Claude Code | ⭐ | 40 |
| [HKUDS/OpenSpace](https://github.com/HKUDS/OpenSpace) | 一个为 AI 代理设计的自进化引擎, 能够让所有 AI 代理 (如 OpenClaw、nanobot、Claude Code、Codex、Cursor 等) 从实际经验中学习、适应和进化, 并相互分享知识. 核心功能包括: 自我进化(技能自动修复、改进和学习)、集体代理智能(一个代理的改进成为所有代理的升级)、令牌效率(重复使用成功解决方案, 减少 46% 的令牌消耗). 支持通过 MCP 服务器与任何支持技能的代理集成, 提供本地仪表板跟踪技能进化, 并拥有云技能社区用于共享进化后的技能. 在 GDPVal 基准测试中, 使用相同的 LLM 基础模型, OpenSpace 代理的收入是基线代理的 4.2 倍, 同时减少 46% 的令牌消耗. 适用于构建复杂系统、处理合规工作、工程项目、文档生成等多种专业任务. | 多平台支持 | ⭐ | 4,760 |
| [rohitg00/pro-workflow](https://github.com/rohitg00/pro-workflow) | 一个为 Claude Code 等 AI 代理设计的自我纠正系统, 通过 SQLite 数据库捕获用户的纠正并转化为规则, 在后续会话中自动应用这些规则, 减少重复纠正的需要. 核心功能包括: 自我纠正循环(自动从纠正中学习)、LLM 门控(AI 驱动的提交验证和秘密检测)、权限调优(分析拒绝模式, 生成优化的允许/拒绝规则)、上下文优化(令牌管理和压缩保护)、成本跟踪(会话成本意识和预算基准)、MCP 审计(分析 MCP 服务器令牌开销)等. 提供 24 个技能、8 个代理、21 个命令和 29 个钩子脚本(覆盖 24 个事件), 支持 Claude Code、Cursor 和 32+ 其他代理(通过 SkillKit). 适用于提高 AI 代理的准确性和自动化程度, 减少重复纠正, 优化开发工作流. | 多平台支持 | ⭐ | 1,804 |
| [NousResearch/hermes-agent-self-evolution](https://github.com/NousResearch/hermes-agent-self-evolution) | 一个为 Hermes Agent 设计的进化式自我改进系统, 使用 DSPy + GEPA (遗传-帕累托提示进化) 自动优化 Hermes Agent 的技能、工具描述、系统提示和代码, 通过反思式进化搜索产生可测量的更好版本. 无需 GPU 训练, 一切通过 API 调用操作 — 变异文本、评估结果并选择最佳变体. 每次优化运行成本约 2-10 美元. 核心功能包括: 技能文件优化 (已实现)、工具描述优化 (计划中)、系统提示部分优化 (计划中)、工具实现代码优化 (计划中)、持续改进循环 (计划中). 采用 DSPy + GEPA (反思式提示进化) 和达尔文进化器 (基于 Git 的代码进化) 作为引擎. 所有进化变体必须通过完整测试套件、大小限制、缓存兼容性、语义保留和 PR 审查等护栏. 适用于提高 Hermes Agent 的性能和自动化程度, 实现持续的自我改进. | Hermes Agent | ⭐ | 1554 |
| [Goldentrii/AgentRecall](https://github.com/Goldentrii/AgentRecall) | 一个为 AI 代理设计的记忆和学习系统, 通过五层记忆金字塔模型(工作记忆→情景记忆→记忆宫殿→感知系统→洞察索引)实现跨会话记忆和智能距离协议. 核心功能包括: `/arsave` 和 `/arstart` 命令实现会话间记忆传递, 跨项目洞察召回, 复合感知系统(200行上限强制质量优先), 自动交叉引用通过 [[wikilinks]], Obsidian 兼容. 提供 MCP 服务器(支持 Claude Code、Cursor、VS Code、Windsurf、Codex)、SDK(支持 JS/TS 框架)和 CLI 三种使用方式. 所有数据本地存储为 Markdown, 零云端依赖. 适用于长期项目开发、团队协作、知识积累和跨项目经验传递等场景. | 多平台支持 | ⭐ | 149 |
| [BayramAnnakov/claude-reflect](https://github.com/BayramAnnakov/claude-reflect) | 一个为 Claude Code 设计的自我学习系统, 捕获用户的纠正并转化为永久记忆和可重用技能. 核心功能包括: 从纠正中学习(自动捕获用户纠正并添加到 CLAUDE.md)、发现工作流模式(分析会话历史寻找重复任务并生成可重用命令)、永久记忆(纠正同步到 CLAUDE.md, 跨会话保持)、技能发现(从重复模式中生成技能)、多语言支持(AI 理解任何语言的纠正)、技能改进(使用技能时的纠正可路由回技能文件本身). 采用两阶段处理(自动捕获 + 手动处理)、混合检测方法(正则表达式 + 语义 AI 验证)和多目标同步(全局和项目特定 CLAUDE.md). 适用于提高 Claude Code 的准确性和一致性, 减少重复纠正, 发现和自动化重复工作流, 持续改进技能. | 多平台支持 | ⭐ | 997 |
| [ViktorAxelsen/MemSkill](https://github.com/ViktorAxelsen/MemSkill) | MemSkill 是一个用于长时限智能体的记忆技能学习和进化框架. 它用数据驱动的循环代替了静态、手工设计的记忆操作, 从任务反馈中学习、优化和重用技能, 实现更具适应性的记忆构建. 核心特点包括技能条件记忆构建、从困难案例中进化技能、可重用技能库、高吞吐量评估和可扩展训练. 其进化的技能是元记忆形式, 关注提取什么记忆、如何记忆、关注什么以及保留或遗忘什么, 而非记忆内容本身. 支持 LoCoMo、LongMemEval、HotpotQA、ALFWorld 等多个数据集, 提供中断训练恢复、并行记忆提取等实用功能. | 通用 AI Agent | ⭐⭐⭐⭐ | 452 |
| [future-agi/future-agi](https://github.com/future-agi/future-agi) | 一个开源平台, 用于构建自改进的 AI 代理, 将评估、追踪、模拟、防护栏、网关、优化等功能整合到一个平台和一个反馈循环中. 核心功能包括: 模拟(数千个多轮对话、真实角色、对抗性输入)、评估(50+ 指标: 真实性、幻觉、工具使用正确性等)、保护(18 个内置扫描器 + 15 个供应商适配器)、监控(OpenTelemetry 原生追踪, 50+ 框架支持)、代理指挥中心(OpenAI 兼容网关, 100+ 供应商)、优化(6 种提示优化算法). 技术栈: Go(网关, ~29k req/s, P99 ≤ 21ms)、Python 3.11+(Django 4.2)、React 18 + Vite、PostgreSQL、ClickHouse、Redis、RabbitMQ + Temporal. 支持 Docker Compose、Kubernetes、云平台部署. 适用于客户支持、语音代理、内部工具、RAG 和搜索、自主代理、计算机使用代理、编码代理等多种场景. | 多平台支持 | ⭐ | 839 |
| [AMAP-ML/SkillClaw](https://github.com/AMAP-ML/SkillClaw) | AI Agent 技能集体进化框架, 通过"Agentic Evolver"技术使技能从每次真实交互中自动演进. 采用客户端代理(Client Proxy)+进化服务器(Evolve Server)双组件架构, 客户端拦截 Agent 请求并记录会话数据, 服务器端支持 workflow(固定3阶段 LLM 管道)和 agent(OpenClaw 驱动)两种进化引擎. 具备自动去重、自动改进、自动验证技能功能. 支持 Hermes、OpenClaw、Codex、Claude Code、QwenPaw 等多平台, 适用于单用户技能进化、多 Agent 共享技能库、多设备同步、团队共享进化场景. | Hermes<br>OpenClaw<br>Codex<br>Claude Code<br>QwenPaw | ⭐ | 1,201 |
| [Cranot/super-hermes](https://github.com/Cranot/super-hermes) | 教Hermes Agent编写自己的分析思考指令的技能集,核心理念是"知道自己做不到什么的代理". Super Hermes在执行复杂任务前会先编写针对特定问题的认知棱镜(cognitive prism),不同问题获得不同棱镜,然后执行棱镜并报告发现和未发现的约束. 核心技能包括:/prism-scan(生成最优棱镜并执行分析)、/prism-full(多通道管线带强制对抗性自我纠正)、/prism-3way(WHERE/WHEN/WHY三正交操作加交叉综合)、/prism-discover(映射所有可能分析域)、/prism-reflect(自我觉察分析). 7个经过验证的棱镜来自1000+实验. 约束历史机制让代理从自身盲点学习. | Hermes Agent(棱镜可独立用于任何支持system-prompt的工具) | ⭐ | 190 |
| [autocontext](https://github.com/greyhaven-ai/autocontext) | 递归自我改进的 Harness 框架, 用自然语言描述目标, 通过多角色协作循环(competitor→analyst→coach→architect→curator)迭代执行真实评估, 保留有效策略、淘汰无效策略, 产出结构化 trace+artifacts(playbook/datasets/distilled model)供下一次运行继承. 11种 Scenario Family(game/agent_task/simulation/artifact_editing/investigation/workflow/negotiation 等). 支持从生产 trace 构建数据集并蒸馏为本地模型(MLX/CUDA). 多接入面: Python CLI/TypeScript SDK/Claude Code MCP/Pi 扩展. 支持 Anthropic/OpenAI/Gemini/Mistral/Groq 等多 Provider. 适用于 Agent 技能自动进化、任务驱动优化和模型蒸馏. | Claude Code<br>Codex<br>多平台(MCP/CLI/SDK) | ⭐ | 1,197 |


### 3.3.2 Auto Research
-------

[2026/06/19, DeepSeek 研究员 Deli Chen 把他的 AutoResearch 协议开源了](https://x.com/AYi_AInotes/status/2067819352926150953), 同时[扔出 4 篇关于 AutoResearch 的论文](https://victorchen96.github.io/auto_research/paper.html), 其中包括 [Self-play 的综述(第四篇)](https://victorchen96.github.io/blog_self_play_story.html). AYi @AYi_AInotes 反馈看到的最值得深入研究的一次 skills 开源和工程脚手架, 最后总结的 5 个工程思路大家可以直接拿去用.

Deli Chen 认为: [AutoResearch Framework](https://victorchen96.github.io/auto_research/framework.html) AutoResearch 的核心其实是一份 SKILL.md, 不是 Python 代码. 每次迭代开全新 session, 只注入精选状态文件; 状态全用文件系统持久化; 三层心跳看门狗, 挂了能自动拉起; 连续没新发现就强制结构化 pivot, 不是让你多调几个参数, 而是换假设、换框架; 执行和验证严格分离, 别让同一个 agent 既干活又自己吹自己. 核心哲学一句话: 代理失败不是模型不够聪明, 而是缺少可靠的脚手架. 这点反直觉, 也非常实用. 很多人做 agent 项目, 拼命堆 prompt、换模型, 结果一跑几天就各种 silent stall、认知循环、状态丢失. Deli 的做法是反过来——先把生产线、质检、应急机制建好, 再让模型在里面跑.

[Self-play 的综述(第四篇)](https://victorchen96.github.io/blog_self_play_story.html) 的论文里还有两个洞察, 比开源本身更值钱.
1. 第一: 先验知识有时是天花板, 不是地板. 受 AlphaZero 启发, 核心观点观点是: 人类给的「最佳实践」和「专家经验」, 经常把系统锚定在局部最优里. Self-play 的力量在于, 它可以自己和自己对练, 探索出人类都没想到的路径. 大量专业知识有时候反而是枷锁, 不是翅膀.
2. 第二: 验证信号质量比模型大小更重要. 他们在 285B 上做了真实实验, 不同 verifier noise 条件下效果差异巨大. 噪声一大, 训练分布上的提升就崩, 而且伤害 held-out 泛化, 模型开始过拟合到自己生成的数据. 再大的模型加再多的 self-play, 如果判断「好坏」的机制是 noisy 的, 最终结果也废. 就像你健身, 反馈系统比努力程度更决定上限.

以前做研究, 人类是操作员, 一步步盯着. 现在代理能把「实验-运行-debug-总结」这个循环自己跑通, 人类的角色在变成导演: 定大方向、设边界条件、定义什么叫成功、设计评价标准. Deli 认为这是他们 Continual Learning 旅程的开始. 未来真正厉害的, 不是会用 AI 的人, 而是能设计出稳定自主闭环的人——不管是研究、内容, 还是产品.

可以直接用的工程思路:
1. 状态别全靠对话历史, 用文件系统持久化, 新迭代只注入必要状态;
2. 建 stall 检测 + 强制 pivot 机制, 连续没进步就换框架, 不是加参数;
3. 执行和验证分离, 重要任务别让同一个系统既干又评;
4. 多层 watchdog, 核心 agent 挂了外部脚本还能拉起来;
5. Fresh session 思维, 长期项目定期重置上下文 + 只保留精华;
那个 SKILL.md 本身值得认真读, 里面那些约束, 很多是真实跑了几十上百小时血泪经验总结出来的, 不是纸上谈兵;

[2026/06/19, nash_su @nash_su, 在 arvix 论文地址前面加个 auto, 直接基于论文内容构建 autoresearch 代码, 这产品思路绝了, 这不就是那些 YouTube downloader 的产品思路么, 还能这么用, 我还是得学习啊...](https://x.com/nash_su/status/2067790423935135843)

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [davebcn87/pi-autoresearch](https://github.com/davebcn87/pi-autoresearch) | 为pi(终端AI编码代理)提供的自主实验循环扩展, 实现尝试想法、测量结果、保留有效改进的自动化流程 | 提供/autoresearch命令、UI小部件、技能等完整工具集 | Claude Code | ⭐ | 4400 |
| [karpathy/autoresearch](https://github.com/karpathy/autoresearch) | AI代理在单GPU上自动运行nanochat训练的研究, 通过修改代码、训练评估、保留或丢弃结果实现自主实验, 包含prepare.py、train.py和program.md三个核心文件 | Claude Code | ⭐⭐⭐⭐ | 73,059 |
| [smallnest/autoresearch](https://github.com/smallnest/autoresearch) | 全自动化软件开发工具, 基于 GitHub Issue 管理的全自动化开发工具, 支持多 Agent 轮转审核、质量门禁和自动 PR 流程, 适用于任意 Git + GitHub 项目(Go、Node.js、Python、Rust、Java 等) | Claude Code |  ⭐ | 354 |
| [uditgoenka/autoresearch](https://github.com/uditgoenka/autoresearch) | Claude Autoresearch Skill, 为 Claude Code 提供自主目标导向迭代, 基于 Karpathy 的 autoresearch 思想, 实现修改→验证→保留/丢弃→无限重复的循环流程 | Claude Code | ⭐ | 3943 |
| [alvinreal/awesome-autoresearch](https://github.com/alvinreal/awesome-autoresearch) | 精选的自主改进循环、研究代理和受karpathy/autoresearch启发的衍生项目索引, 包含通用衍生项目、研究代理系统、平台移植、特定领域适配、评估基准、用例和相关资源 | NA | ⭐ | 1,754 |
| [TheGreenCedar/codex-autoresearch](https://github.com/TheGreenCedar/codex-autoresearch) | 为 Codex 提供可测量的改进循环插件, 帮助 AI 代理将"使这个更好"转化为有度量的迭代流程. 核心功能包括定义目标和基准契约、安全编辑范围、运行小实验包、基于证据保留/丢弃更改、跨上下文丢失保留 ASI(累积结构化智能)和指标、打包有用工作以供审查. 提供实时仪表板展示基线、最新、最佳指标, 支持质量差距循环, 生成可审查的分支. 工作流程: 目标识别→会话管理→基准验证→运行实验→日志决策→继续或定稿. 适用于目标可测量、基准可重复、存在正确性检查、编辑范围可审查的场景. | Codex | ⭐ | 252 |
| [wanshuiyin/Auto-claude-code-research-in-sleep](https://github.com/wanshuiyin/Auto-claude-code-research-in-sleep) | 让Claude Code在你睡觉时做研究,醒来发现论文已评分、弱点已识别、实验已运行、叙事已重写,包含65+捆绑skills和Research Wiki持久化 | Claude Code<br>Codex CLI<br>Cursor<br>Trae<br>Antigravity<br>Copilot CLI<br>OpenClaw<br>Windsurf | ⭐⭐⭐ | 9,728 |
| [yibie/awesome-autoresearch](https://github.com/yibie/awesome-autoresearch) | 精选跨行业公开autoresearch使用案例列表,回答"autoresearch已在哪些真实工作流中使用",包含科学研究、软件优化、金融交易等分类 | 纯文档列表 | ⭐ | 372 |


## 3.4 上下文工程
-------

[2026/04/28, VerySmallWoods @verysmallwoods, Agent 框架的上下文管理: 四种实现, 殊途同归](https://x.com/verysmallwoods/status/2048891335701090339)

### 3.4.1 Token Efficient
-------

[2026/04/06, 小八 @IceBearMiner, Claude Code 省钱大法: Token 消耗直降 80%](https://x.com/IceBearMiner/status/2041152419032101247)

#### 3.4.1.1 输出裁剪和过滤
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [rtk-ai/rtk](https://github.com/rtk-ai/rtk) | RTK 会在命令输出到达你的 LLM 上下文之前过滤和压缩它们. 单一 Rust 二进制, 零依赖, 开销 <10 ms. | 多 Agent 支持 | ⭐⭐⭐ | 20,956 |
| [Narwhal-Lab/MagicSkills](https://github.com/Narwhal-Lab/MagicSkills) | 北京大学开源的 AI Agent 技能管理系统, 类似 npm 的角色, 实现 Skill 的统一管理、安装、组合和同步, 支持 "写一次、到处用" 的能力复用. 核心功能包括: 统一共享 skill 池、为不同 Agent 创建技能集合、同步到 AGENTS.md 或暴露为 tool/function. 支持 26+ 平台, 可从 Anthropic 官方仓库安装 Skill. 适用于多 Agent 项目、Agent Engineering、可复用 Skill 库等场景. | 多 Agent 支持 | ⭐ | 274 |
| [drona23/claude-token-efficient](https://github.com/drona23/claude-token-efficient) | 专注于优化 Claude 模型的 Token 使用效率, 通过实现 Token 高效的工具调用、提供节省 Token 的最佳实践和工具, 帮助开发者减少 Claude API 的 Token 消耗, 降低使用成本. 支持通过配置优化、工具调用策略调整等方式, 平均节省 14% 的输出 Token, 最高可达 70%, 同时减少 API 调用延迟. 适用于使用 Claude Code 进行日常开发、代码生成和调试的场景, 特别适合需要控制 API 成本的团队和个人开发者. [微信公众号 --AI 工程化 --8 行代码让 Claude Code 闭嘴: 输出 token 直降 63%, 废话全砍](https://mp.weixin.qq.com/s/DrPUykwCwIEryUDwYBxucQ) | 多 Agent 支持 | ⭐ | 3,622 |
| [mpecan/tokf](https://github.com/mpecan/tokf) | Token 优化工具, 专注于提高 AI 代理的 Token 使用效率, 通过智能上下文管理和 Token 消耗优化, 帮助开发者减少 API 成本. 核心功能可能包括上下文压缩、Token 使用分析、智能提示词优化等. | 多 Agent 支持 | ⭐ | 143 |
| `.claudeignore` | 用于指定 Claude 应忽略的文件和目录, 减少不必要的上下文加载, 优化 Token 使用. | 多 Agent 支持 | ⭐ | 0 |
| [CompactMode]() | 上下文压缩模式, 通过智能压缩算法减少上下文大小, 提高 Token 使用效率. | 多 Agent 支持 | ⭐ | 0 |
| [PTC]() | 可能是 Prompt Token Control 的缩写, 用于控制提示词的 Token 使用, 优化提示词结构. | 多 Agent 支持 | ⭐ | 0 |
| [JuliusBrussee/caveman](https://github.com/JuliusBrussee/caveman) | 通过 caveman 式简洁表达减少约 75% 的输出 token, 同时保持完整技术准确性. 装上之后, Claude 的回复风格从 "写小作文" 变成 "发电报". 冠词砍了, 寒暄砍了, 铺垫砍了, 但代码和技术术语一个字不动. 实测下来平均省 65% 的 token, 解释类任务最狠能省 87%. 还包含 Caveman Compress 工具, 可压缩记忆文件减少约 45% 的输入 token. 支持 Lite/Full/Ultra 三种强度级别, 保留技术术语和代码块, 移除冗余填充词. 平均节省 65% token, 响应速度提升约 3 倍, 适用于减少 token 使用和成本、获得更快响应、更易读的答案. [X@sitinme, 2026/04/07, 一个叫 Caveman 的 Claude Code 技能, 原理特别简单但效果很好——就是让 Claude 说话别废话.](https://x.com/sitinme/status/2041436315133374853), [X@0xLaughing, 2026/04/07, 中文输出精简规则(Caveman 中文化变体)](https://x.com/0xLaughing/status/2041438001931448589) | Claude Code | ⭐⭐ |7,630 |
| [hexiecs/talk-normal](https://github.com/hexiecs/talk-normal) | 让任何 LLM 像正常人一样说话, 避免冗余和废话, 只提供直接的答案. 通过单个系统提示词将冗长的 LLM 输出转换为简洁、信息丰富的响应. 适用于任何模型(GPT、Gemini、LLaMA等), 在 GPT-4o-mini 上平均减少 73% 的字符数, 在 GPT-5.4 上平均减少 72% 的字符数, 同时保留所有有用信息. 支持多种使用方式, 包括 OpenClaw、ChatGPT 自定义指令和 OpenAI API 工具. | Claude Code | ⭐ | 1,023 |
| [vincentkoc/tokenjuice](https://github.com/vincentkoc/tokenjuice) | 🧃Token 减重工具, 专为终端密集型代理工作流程设计的精益输出压缩器. 可作为原生 CLI 工具或流行编码和代理框架的扩展使用. 核心功能包括终端输出压缩、多种框架集成(Claude Code、Codex CLI、pi)、保留原始命令执行、提供原始输出选项、基于规则的压缩系统和 JSON 格式输出. 技术栈主要为 TypeScript (90.5%) 和 JavaScript (9.5%). 目标是实现库优先设计、JSON 规则解析、明确的减少和包装模式、易于调试的文件支持工件、无静默命令重写, 以及优先考虑速度和可靠性. 适用于需要减少 Token 使用的 LLM 应用、终端密集型代理工作流程, 以及与各种编码框架的集成场景. | 多框架集成 | ⭐ | 102 |
| [batish52/codecontext](https://github.com/batish52/codecontext) | 自动减少 LLM 成本 40-70% 的网关工具, 位于代码和 LLM API 之间. 通过智能路由简单提示到本地模型、压缩上下文、跟踪实际节省成本来优化 LLM 使用. 核心功能包括项目扫描和索引(提取符号, 构建 BM25 索引和语义嵌入)、提示分类(决定是否需要外部推理)、上下文打包(组装最相关的代码块到 token 预算中)、多模型支持(OpenAI、Anthropic、Ollama 等)以及成本跟踪(写入实际 token 计数和美元成本到本地 SQLite 分类账). 支持 TypeScript/JavaScript AST 解析, 适用于工程师开发 AI 辅助工具的场景. | 多模型支持 | ⭐ | 13 |
| [chopratejas/headroom](https://github.com/chopratejas/headroom) | AI Agent 上下文压缩层, 在工具输出、日志、文件和 RAG 内容到达 LLM 前进行压缩, 减少 60-95% 的 Token, 答案不变. 提供库(Python/TypeScript)、代理(proxy)、Agent 包装器(Claude/Codex/Cursor)、MCP 服务器和跨 Agent 记忆. 支持 6 种压缩算法(SmartCrusher/CodeCompressor/Kompress 等), 可逆压缩(CCR)允许按需检索原始内容, headroom learn 从失败会话中挖掘修正写入 CLAUDE.md/AGENTS.md. | 多 Agent 支持<br>Claude Code<br>Codex<br>Cursor | ⭐⭐⭐ | 21,290 |


#### 3.4.1.2 上下文压缩
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [mksglu/context-mode](https://github.com/mksglu/context-mode) | 上下文模式管理工具, 帮助优化和管理 AI 代理的上下文使用, 减少 Token 消耗. | 多 Agent 支持 | ⭐⭐ | 10,986 |
| [open-compress/claw-compactor](https://github.com/open-compress/claw-compactor) | **OpenClaw 上下文压缩优化工具** - 专为 OpenClaw 设计的 Token 消耗优化解决方案, 通过智能上下文压缩算法减少 45% 的 Token 使用量. 核心功能包括:<br>1). 激进式上下文修剪: 将 TTL 从默认 1 小时缩短至 5 分钟, 配合 0.5 的 hardClearRatio 及时清理过期工具结果;<br>2). 智能缓存保活: 针对 Anthropic Claude 系列模型, 通过 55 分钟心跳机制保持缓存温热状态, 避免昂贵的重写成本;<br>3). 本地化记忆搜索: 集成本地 Embedding 模型替代云端 API 调用, 将 Embedding 成本降至零;<br>4). 多层压缩策略: 结合 micro-compact、auto-compact 和 manual compact 三层压缩机制, 实现上下文的无损压缩与持久化存储.<br> 实测数据显示: 平均上下文长度从 128k 降至 70k, 缓存写入频率降低 90%, 特别适用于长对话场景和复杂任务处理. | OpenClaw | ⭐ | 2,172 |
| [SocratiCode](https://github.com/giancarloerra/SocratiCode) | 为 AI 助手提供整个代码库的深度语义理解, 零配置、完全私有、免费, 支持大规模代码库(超过 4000 万行代码). 核心功能包括混合搜索(语义搜索 + BM25 词汇搜索)、AST 感知的代码分块、多语言代码依赖图、可搜索的上下文工件等. 基于 Qdrant 向量数据库, 支持多种嵌入提供商(Ollama、OpenAI、Google Gemini), 实现了增量索引、批处理、实时文件监控和多代理支持. 适用于代码库探索、架构分析、跨文件和跨语言推理等场景. | 多 Agent 支持 | ⭐ | 788 |
| [ooples/token-optimizer-mcp](https://github.com/ooples/token-optimizer-mcp) | 智能 Token 优化工具, 专为 Claude Code 设计, 通过缓存、压缩和智能工具智能实现 95%+ 的 Token 减少. 核心功能包括 MCP 压缩技术、智能缓存机制、工具调用优化和 Token 消耗监控. 通过减少无效的 Schema 开销和优化上下文管理, 显著降低 API 成本和提高响应速度. 适用于使用 MCP 服务器的企业级集成和分布式系统, 特别适合需要控制 Token 消耗的大型项目. | 多 Agent 支持 | ⭐ | 162 |
| [sting8k/pi-vcc](https://github.com/sting8k/pi-vcc) | 为 Pi 编码代理提供的智能、快速、无损会话压缩工具, 纯算法实现无需 LLM 调用. 核心功能包括: 算法提取压缩(将对话转化为结构化摘要, 35-99% Token 减少)、确定性输出(相同输入=相同输出, 无幻觉风险)、5 个语义分区(session goal/files & changes/commits/outstanding context/user preferences)、简短转录(每个工具调用折叠为单行)、有界合并(滚动分区在合并后重新截断而非无限增长)、无损回溯(vcc_recall 工具通过读取原始 JSONL 实现跨压缩搜索, 支持 scope:"all" 全量搜索)、30-470ms 压缩延迟(零 API 调用). 技术栈: TypeScript. 提供 /pi-vcc 手动压缩命令和 /pi-vcc-recall 搜索历史命令. | Pi | ⭐ | 190 |


#### 3.4.1.3 智能 Cache
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [zenobi-us/opencode-skillful](https://github.com/zenobi-us/opencode-skillful) | (注意: 该仓库已 archived, 不再更新)提供懒惰加载的技能发现和注入.<br>AI 有时会因为加载了太多的 "系统提示词" 或 "操作指南" 而浪费大量初始 Token.<br> 核心功能是将复杂的 Prompt 碎片化为 "技能"<br> 默认情况下上下文是空的, 只有当 AI 识别到任务(比如" 现在需要进行 Docker 部署 "), 时, 它才会动态" 注入 "相关的专业知识和规则. 这能节省约 20%-40% 的静态上下文空间.<br>1. 在对话中, 智能体使用 skill_find 来发现技能.<br>2. 使用 skill_use "skill_name"<br>3. 代理可以用来 skill_resource skill_relative/resource/path 读取参考资料. | OpenCode | ⭐ | 266 |
| [yvgude/lean-ctx](https://github.com/yvgude/lean-ctx) | AI 编码代理的上下文运行时, 通过智能缓存和压缩将 Token 消耗减少 60-95%. 单一 Rust 二进制, 提供文件读取缓存(10 种读取模式)、Shell 输出压缩(95+ 模式)、属性图分析和会话记忆. 支持 25+ 种 AI 工具和 IDE. | 多 Agent 支持 | ⭐ | 1,177 |
| [learningCatHD/telos-sdk](https://github.com/learningCatHD/telos-sdk) | 缓存感知的提示协议和网关, 用于可移植的 Agent 上下文. 位于 Agent 和模型之间, 通过重构请求段将共享前缀从缓存读取提供服务, 避免每轮重复计费, 6 轮实测节省 92.3% Token 费用. 核心特性: Agent 行为不变(SWE-bench A/B 测试无回归)、缓存命中加速推理、本地运行无遥测、跨模型兼容(Anthropic/OpenAI/DeepSeek/vLLM/SGLang). 三大组件: 三色带协议(PIN/FOLD/DROP)、本地代理网关、CLI(telos init/dashboard). 来自清华大学 LEAP Lab. | 多 Agent 支持 | ⭐ | 300 |


#### 3.4.1.4 专家模式
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [DietrichGebert/ponytail](https://github.com/DietrichGebert/ponytail) | **Ponytail 解决的问题不是"代码太多", 而是"Agent 默认想写太多"**. 它给了 Agent 一套本能: 在碰键盘之前, 先问六个问题. 往往问到第二个就停了. 它让你想起公司里那个最老的程序员. 他什么都不说. 他写一行. 它能跑. [2026/06/14, yibie @yibie, # Ponytail: 让 AI Agent 写出 1 行而不是 50 行的 skill](https://x.com/yibie/status/2066155762678977017) | Claude Code<br>OpenCode | ⭐ | 10,614 |
| [lokikill123/codex-token-skills](https://github.com/lokikill123/codex-token-skills) | 用 Codex 总是额度不够, 天才程序员陨落？这个工具能帮你省下近50% 的 Token. 它做成了两个自动化 Skill<br>1. token-saver(精简大师): 极致压缩输出, 自动跳过废话、不重复读取文件, 让 AI 零废话直奔主题. <br>2. memory(全局记忆): 统一前缀结构并优化上下文压缩, 哪怕长对话也不会丢失关键信息. <br>它还专门针对 DeepSeek V4 Pro 做到了 KV Cache 复用最大化, 大幅提升了缓存命中率.  | Claude Code<br>OpenCode | ⭐ | 78 |

### 3.4.2 Prompt Optimizer
-------

#### 3.4.2.1 Prompt Optimizer
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [DannyMac180/ace-platform](https://github.com/DannyMac180/ace-platform) | 一款开源的自进化 AI Agent 平台, 由 Dan McAteer 基于 ace-agent/ace 复刻并深度开发, 核心价值是将一次性的 AI 提示词转化为可持续进化的工作手册(Playbooks), 让 AI 工作流在实际使用中持续优化, 减少提示词漂移、降低重复错误, 提升 AI 输出的稳定性. | NA | ⭐ | 143 |
| [linshenkx/prompt-optimizer](https://github.com/linshenkx/prompt-optimizer) | 一个强大的 AI 提示词优化工具, 帮助用户编写更好的 AI 提示词, 提升 AI 输出质量. 支持 Web 应用、桌面应用、Chrome 插件和 Docker 部署四种使用方式. 核心特性包括智能优化、双模式优化(系统提示词和用户提示词)、对比测试、多模型集成、图像生成、高级测试模式、安全架构、多端支持、访问控制和 MCP 协议支持. 适用于角色扮演对话、知识图谱提取、诗歌写作等场景, 可帮助激发小模型潜力、保障生产环境稳定性、辅助创意探索与需求定制. | 多平台 | ⭐⭐⭐ | 26,149 |
| [annotated-autoresearch](https://github.com/delip/mini-apps/tree/main/annotated-autoresearch) | 一个实验性项目, 旨在让 LLM 进行自主研究. 核心功能是通过固定时间预算 (5 分钟) 的训练循环, 让 LLM 自动修改 train.py 文件, 尝试不同的模型架构、优化器和超参数, 以达到最低的 val_bpb 指标. 包含完整的实验设置、运行流程、结果记录和评估标准. 适用于 AI 自主研究和模型优化场景. 参见 [mini-apps/annotated-autoresearch](https://delip.github.io/mini-apps/annotated-autoresearch). | NA | ⭐ | 2 |
| [hellowind777/hello2cc](https://github.com/hellowind777/hello2cc) | 一个专为第三方模型设计的 Claude Code 插件, 旨在让第三方模型在 Claude Code 中表现得尽可能接近 Opus. 核心功能包括优化工具和代理选择、改进团队 / 任务工作流程使用、增强失败恢复能力、统一输出风格, 以及推动第三方模型采用 Claude Code 原生能力优先级. 适用于已通过 CCSwitch 或其他映射层连接第三方模型到 Claude Code 的用户, 帮助这些模型更可靠地使用已安装的技能、工作流、MCP 服务器或插件. | Claude Code | ⭐ | 489 |
| [linexjlin/GPTs](https://github.com/linexjlin/GPTs) | 一个收集泄露的 GPT 提示词 (Prompts) 的 GitHub 仓库, 包含各种 GPT 模型的提示词模板和配置. 旨在为开发者和研究者提供参考和学习资源, 帮助他们更好地理解和构建自己的 GPT 应用. 核心价值包括丰富的提示词收集、完全开源免费、多来源收集、社区驱动贡献和学习友好. | NA | ⭐⭐⭐ | 31,980 |
| [songtianlun/awesome-prompts](https://github.com/songtianlun/awesome-prompts) | 一个精选的提示词库, 收录了面向大语言模型和多模态模型的各类提示词, 并按模态与任务类型分类, 包括文本生成、文生图、文生视频等情境. 核心功能包括多模态分类(文本-文本、文本-图像、文本-视频)、OpenClaw101 翻译用例、双语支持(英文/中文), 以及通过 prmbr.com 提供更好的阅读体验. 适用于开发者、研究者和 AI 爱好者, 帮助他们快速找到和使用高质量的提示词, 提升 AI 模型的输出效果. | NA | ⭐ | 467 |
| [agents-md](https://github.com/TheRealSeanDonahoe/agents-md) | 一个可直接使用的 AGENTS.md 文件, 使每个编码代理表现得像高级工程师而不是急切的实习生. 它可以消除奉承, 阻止随意重构, 强制验证循环. 综合了 Karpathy 的四个原则和 Boris Cherny 的 Claude Code 工作流程. | Claude Code、Codex、Gemini CLI、Cursor | ⭐ | 237 |
| [anothervibecoder-s/claudecode-harness](https://github.com/anothervibecoder-s/claudecode-harness) | 提供一套 Claude Code 工程化使用规范, 通过上下文纪律、子代理委派和多模型共识, 实现长时间高强度 SaaS 开发的零配额超限和零幻觉修复. 这是一套 Claude Code 的日常使用规范, 核心是把主会话的上下文压到最轻, 搜索、测试之类的事丢给便宜的子代理跑, 重要改动让多个模型并行审查. 配套的模板文件覆盖了职责分工、代码行数上限、部署流程、安全规则、记忆连续性等方面, 目标是长时间用 AI 写代码不出错也不超配额. | NA | ⭐ | 98 |
| [agent-style](https://github.com/yzhao062/agent-style) | 为 AI 编码和写作代理提供 21 条写作规则, 让生成的内容读起来更像专业技术人员的作品. 包含 12 条经典写作规则和 9 条实地观察规则, 支持软执行(生成时加载)和技能(事后审查)两种使用方式. 支持 Claude Code、Codex、GitHub Copilot、Cursor、Aider 等多种 AI 代理. | Claude Code、Codex、GitHub Copilot、Cursor、Aider 等 | ⭐⭐⭐⭐ | 12,500+
| [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts) | 一个包含 Claude Code 所有系统提示词的仓库, 包括 24 个内置工具描述、子代理提示词(Plan/Explore/Task)、实用提示词(CLAUDE.md, compact, statusline, magic docs, WebFetch, Bash cmd, security review, agent creation)等. 仓库会在每个 Claude Code 版本发布后几分钟内更新, 并提供系统提示词的变更日志, 记录了从 v2.0.14 以来 161 个版本的变更. 核心价值在于提供了 Claude Code 系统提示词的完整、准确、及时的参考, 帮助开发者理解和定制 Claude Code 的行为. | Claude Code | ⭐⭐⭐ | 9,416 |
| [prompts.chat](https://github.com/f/prompts.chat) | 世界上最大的开源AI提示库, 适用于 ChatGPT、Claude、Gemini、Llama、Mistral 等 AI 模型 |  NA | ⭐ | 161,120 |
| [robzolkos/pi-nocchio](https://github.com/robzolkos/pi-nocchio) | 一个小巧的 Pi 包, 添加了 `--dump-system-prompt` CLI 标志, 用于打印 Pi 组装好的系统提示词到标准输出. 核心功能是在不调用模型的情况下, 实时导出完整的系统提示词, 包括加载的工具、上下文文件、技能、自定义系统提示词、追加的系统提示词、当前日期和工作目录等信息. 支持保存到文件, 也可以提供自己的初始提示文本. 当不使用该标志时, 扩展对性能的影响可以忽略不计. 适用于调试 Pi 的系统提示词、了解 Pi 的提示组装机制、分析其他扩展对系统提示词的修改等场景. | Pi | ⭐ | 20 |
| [nidhinjs/prompt-master](https://github.com/nidhinjs/prompt-master) | 一个 Claude 技能, 用于为任何 AI 工具编写精准提示词. 支持 30+ AI 工具(Claude、ChatGPT、Gemini、Cursor、Claude Code、GitHub Copilot、Midjourney、DALL-E、Stable Diffusion 等). 核心特性包括: 结构化管道(检测目标工具→提取9个意图维度→提出澄清问题→路由到正确框架→应用安全技术→令牌效率审计→交付提示词)、12种自动选择的提示词模板、5种安全技术、检测35种浪费积分的模式、记忆块系统. 目标是零浪费令牌, 无需反复提示即可获得正确答案, 让每个词都有实际作用. | Claude 技能、多平台 | ⭐⭐ | 7,195 |
| [tweakcc](https://github.com/Piebald-AI/tweakcc) | CLI 工具, 用于升级 Claude Code 体验, 支持自定义系统提示、主题、工具集和 UI, 提供 API 接口和自定义补丁功能, 支持多种安装方式(npm、原生二进制)<br>Claude Code 原生版本在开发者使用中存在系统提示词不可修改、工具集全量加载占用上下文以及终端交互体验单一等限制. 开源工具 tweakcc 通 过切入底层 cli.js, 提供了重写系统提示词、按需动态加载工具集、实现 Opus 混合模式处理超大项目以及优化终端视觉与性能的能力. 该工具核心代码不到 500 行, 旨在帮助开发者夺回对 AI 助手的控制权. | Claude Code | ⭐ | 1,612 |
| [b-nnett/codex-plusplus](https://github.com/b-nnett/codex-plusplus) | Codex++ 是 Codex 桌面应用的 tweak 系统, 无需重新构建应用即可注入自定义功能、修复 UI 问题、添加 tweak 管理器. 它通过注入 loader 到 app.asar 中, 在启动时拉取 runtime, 然后发现和加载 tweaks(带有 manifest 和 start/stop 生命周期的小型 ESM 模块), 并在 Codex 的设置 UI 中注入 "Tweaks" 标签页, 支持在应用内启用、禁用和配置 tweaks. 默认提供自定义快捷键和 UI 改进等 tweaks, 支持 macOS 和 Windows. | Codex | ⭐ | 1,304 |
| [yao-open-prompts](https://github.com/yaojingang/yao-open-prompts) | 中文 AI 提示词开源库, 收录 116 个高质量提示词, 覆盖内容创作、营销推广、学习方法、工作效率等 9 大场景. 采用 RTF 框架结构化设计, 支持版本控制与持续更新, 提供网页逆向、文章/图片反编译等特色工具, 配套自动化脚本生成目录与文档站点. | 多 Agent 支持 | ⭐ | 1,433 |
| [brandonhimpfen/awesome-prompt-engineering](https://github.com/brandonhimpfen/awesome-prompt-engineering) | 大语言模型(LLM)和生成式AI提示工程的精选资源列表, 包含指南、工具、论文和平台. 收录提示工程学习资源(指南/课程/教程)、提示库和提示管理工具、研究论文和社区资源、应用案例和相关Awesome列表. 支持OpenAI GPT、Claude、LangChain、PromptLayer、Promptfoo、Chainlit、FlowGPT、PromptBase、AgentGPT、Auto-GPT等工具和平台. 为提示工程师提供全面的参考资料. | 通用 | ⭐ | 234 |
| [kingbootoshi/directional-prompting)](https://github.com/kingbootoshi/directional-prompting) | 提供双层提示词编写框架, 用目标导向和正向指令让 LLM 精准执行, 避免否定式指令带来的歧义. 一个双层提示词写法, Claude Code 和 Codex CLI 都能用. 第一层写清楚目标、成功标准、什么时候停; 第二层用正向动词告诉模型该怎么走, 别写"不要 xxx". Claude 4.7 和 GPT-5.5 的指南都说了, 正面指令比否定指令好用. 这个技能会帮你把提示词里的否定表达改成正向说法, 适合写系统提示词、技能描述、IDE 规则集. | Claude Code<br>Codex | ⭐ | 98 |
| [SK-DEV-AI/opencode-slim-system](https://github.com/SK-DEV-AI/opencode-slim-system) | 减少OpenCode每次请求的Token开销,通过用紧凑版本替换OpenCode的捆绑系统提示和内置工具描述. 每次请求节省约1,400 Token(系统提示)+约8,300 Token(工具描述)=约9,700 Token总节省. 核心机制:①tool.definition钩子——每个session每个工具触发一次,如果有精简版本则替换原始描述,覆盖所有17个内置OpenCode工具;②experimental.chat.system.transform钩子——构建系统提示时触发,检测到默认提示后替换为精简版本. | OpenCode | ⭐ | 1 |
| [severity1/claude-code-prompt-improver](https://github.com/severity1/claude-code-prompt-improver) | Claude Code的智能提示改进钩子插件,核心理念是"输入想法,输出精确". 通过UserPromptSubmit钩子拦截用户提示并评估其清晰度,模糊提示会自动触发prompt-improver技能进行研究和澄清. 4阶段流程(Research → Questions → Clarify → Execute),使用AskUserQuestion工具生成1-6个定向澄清问题,旁路前缀支持(`*`跳过评估、`/`斜杠命令、`#`记忆化). | Claude Code | ⭐ | 1,574 |
| [modaic-ai/gepa-viz](https://github.com/modaic-ai/gepa-viz) | GEPA 提示词优化运行的可交互实时可视化工具, 将候选提示词树渲染为力导向图, 观察 Prompt 在 Pareto 前沿上的实时演化. 甜甜圈节点按验证集逐例得分显示正确/错误, 点击节点查看候选提示词与父提示词差异、反思反馈、Pareto 前沿像素网格. 三种使用模式: 嵌入式(默认, 自动启动浏览器)、远程模式(适合跨机器优化)、静态模式(仅输出 run.json). 技术栈: TypeScript + Python, 前端 Vite + React + d3 + Tailwind. | GEPA<br>多 LLM | ⭐ | 405 |


#### 3.4.2.2 Prompt 收录
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [2026/05/19, omega.欧米茄.AI @PierceZhang34, 如何让 Claude Code 彻底"闭嘴", 自己做决定、自主执行](https://x.com/PierceZhang34/status/2056669815511867682). | NA | 多 Agent | ⭐ | 博文不涉及开源 |
| [2026/05/18, 老金 @freeman1266, 让 Codex 在你睡觉时自己写代码](https://x.com/freeman1266/status/2056351092804297028) | NA | 多 Agent | ⭐ | 博文不涉及开源 |
| [2026/05/19, 泊舟 @bozhou_ai, 这个提示词能够很好的将AI coding过程中的施工计划给你保留到文件里面, 能显著降低 AI 写代码后的不可控感. ](https://x.com/bozhou_ai/status/2056550516558274920) | 这个方法本质上是把AI的"思考过程"转成可审计的文档. 对 Prompt Engineering 来说, 迭代几次后, 你会发现 notes 里的 tradeoff 记录能反过来优化你的 SPEC 写法, 形成闭环. 提示词如下所示: "请根据 <SPEC> 完成功能实现. 在实现过程中, 请持续维护一个 implementation-notes.html 文件, 记录所有 SPEC 中没有明确说明但你必须做出的决策、你对原需求做出的调整、实现中的技术取舍、临时假设、潜在风险, 以及我后续维护这个功能时需要知道的信息." | 多 Agent | ⭐ | 博文不涉及开源 |
| [2026/05/18, AYi @AYi_AInotes, 为什么Claude内部放弃了Markdown, 因为HTML才是AI时代的唯一标准(完整实战指南・附全套提示词)](https://x.com/AYi_AInotes/status/2056377322542944690) | NA | 多 Agent | ⭐ | 博文不涉及开源 |
| [2026/05/18, 码良 @cxjwin, 一个大厂 leader 的面试 SKILL, 和给同学的 3 条建议](https://x.com/cxjwin/status/2056231835408191665) | NA | 多 Agent | ⭐ | 博文不涉及开源 |
| [2026/05/29, Serena @369Serena, 别再伺候 AI 了: 5 个方法狠狠压榨 Codex](https://x.com/369Serena/status/2060330862223515816) | Codex | ⭐ | 博文不涉及开源 |
| [2026/05/18, 达芬七｜Seven @SuisPasDaVinci, Claude Code 进阶: 14 个让 AI 处理脏活累活的高级技巧](https://x.com/SuisPasDaVinci/status/2056222280665923793) | Claude Code | ⭐ | 博文不涉及开源 |
| [2026/05/21, AYi @AYi_AInotes, 用我的神级Prompt测试了Gemini 3.5 Flash, 确认了一件事: Google直接宣告AI 大模型纯聊天时代彻底终结了！ ](https://x.com/AYi_AInotes/status/2057318390138609911) | Gemini CLI | ⭐ | 博文不涉及开源 |
| [2026/06/02, serein @you1873118, 最近翻到一个中文 Prompt 网站](https://x.com/you1873118/status/2061672493153464804) | [完全免费的中文 AI 提示词](https://prompt123.cn), 发现并使用高质量的 AI 提示词, 释放人工智能的无限潜能. | 多 Agent | ⭐ | 博文不涉及开源 |
| [2026/06/02, 泊舟 @bozhou_ai, 一个能带你学习的skill, 中文内容如下, 可以参考一下](https://x.com/bozhou_ai/status/2061623947112960502) | 参见 [@ThariqS ThariqS/SKILL.MD](https://gist.github.com/ThariqS/1389dcdff9eba4789887a2211370f06b)
| [2026/06/02, 金尘马 @jinchenma_ai, 3分钟教你如何把 Codex、Claude Code 的 skills 统一管理(内附提示词)](https://x.com/jinchenma_ai/status/2061477349582139767)
| [2026/06/03, Leo｜一个人 + AI, @runes_leo, 我最近在 Codex App 里跑通了跨对话协作: 一个主 thread 推进任务. 发现某一步该交给另一条业务线, 就写一份 handoff 文件, 再用短期定时任务把目标 thread 唤醒.](https://x.com/runes_leo/status/2062034028568420851) | handoff 提示词 |
| [2026/06/02, 爆裂队长NEXT @thinkszyg, 复杂需求先别让 AI 写代码: 多 Agent 并行 Plan 实操](https://x.com/thinkszyg/status/2061761272199479511) | 复杂任务先别让 AI 写代码, 先让 3 个 AI 同时出 Plan. Claude Code/Codex/Cursor/Gemini/Composer 2.5 等分别出一版. 最终, 三个方案放在一起看, 再决定用哪个. 方案重点看如下几个点: ① 它是不是乱动文件. ② 它有没有复用现有代码. ③ 它有没有提到边界情况. ④ 步骤是不是能执行. 看起来折腾, 但实际用下来, 反而省时间. 因为把这件事, 变成了「让几个 AI 先把路线放开, 我们来做选择题」. |
| [2026/06/02, 逸尘 @gengdaJ, 让 Codex 不再失忆——外接 Obsidian 大脑 Token 优化, 重要记忆全部记住](https://x.com/gengdaJ/status/2061756699170807819) |
| [2026/06/09, YanXbt @IBuzovskyi, 5 HERMES AGENT SOUL.md TEMPLATES YOU CAN COPY RIGHT NOW.](https://x.com/IBuzovskyi/status/2064032745672876199) | 5 HERMES SOUL.md 模板: 研究员(RESEARCHER), 内容创作者(CONTENT CREATOR), 运营经理(OPS MANAGER), 代码检视专家(CODE REVIEWER), 销售开发(SDR/SALES DEVELOPMENT) |
| [2026/06/04, Aomyying @AomyYing, 如何靠 Claude Skills 做被动收入](https://x.com/AomyYing/status/2062414031244398791) | 掌握一套把个人经验, 打包成可规模化、可被动变现的数字产品的能力. |
| [2026/06/12, 向阳乔木 @vista8, 现在都是 AI Agent做开发, 人喜欢的 PRD 和 AI 喜欢的是不一样的.](https://x.com/vista8/status/2065264509170876417) | 为了精准高效开发, 写了个专门服务于 AI 的 PRD 文档生成Prompt. 先有这个文档, 再给 AI 开发, 功能完整度和丰富性会远远比自己想的全面、好用. [Prompt地址](https://xiangyangqiaomu.feishu.cn/wiki/EUM7wPW7XiWTJHk2kM9ciBQantb), [开源地址](https://github.com/joeseesun/qiaomu-ai-prd) |
| [2026/06/18, Wey Gu 古思为 @wey_gu, 分享下我现在的典型 handoff 方式](https://x.com/wey_gu/status/2067473320753475932) | 请继续 xxx 的工作, 了解一下之前的进展. 此外[评论区 Menci 💖 @lcMenci 指出他现在的 handoff](https://x.com/lcMenci/status/20674771318826313040) 是有 `/reading-claude-session <uuid>` 和 `/reading-codex-session <uuid>` 两个 skill, 可以继续未完成的工作、重新根据最早的讨论来 review、或是单纯找前一个 agent 的茬


| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [WEIFENG2333/phistory](https://github.com/WEIFENG2333/phistory) | 自动归档主流编码 Agent CLI 的版本化系统提示词快照, 每小时检测新版本并捕获完整系统提示词. 支持 Claude Code(343 快照)、Codex CLI(55)、OpenClaw(64)、opencode(73) 等 7 种 Agent. 核心价值: 追踪厂商如何迭代系统提示词、发现新增工具/权限检查/模型默认值、对比不同 CLI 的 Agent 行为设计差异、提供稳定快照用于审计调试. 提供 Web 查看器(phistory.cc)进行跨版本对比. | 多 Agent CLI | ⭐ | 142 |
| [elder-plinius/CL4R1T4S](https://github.com/elder-plinius/CL4R1T4S) | AI 系统透明性与可观测性项目, 全面提取主流 AI 模型/Agent 的系统提示词、行为准则和工具定义. 覆盖 OpenAI、Google、Anthropic、xAI、Cursor、Windsurf、Devin、Manus、Replit、Lovable、Bolt、Cline 等几乎所有主流 AI 系统. 核心理念: 如果不了解 AI 的输入(系统提示词), 就无法信任其输出. 仓库按 AI 公司分目录, 欢迎 PR 贡献新提取的提示词(需附模型名称/版本、提取日期和上下文说明). | 通用 | ⭐⭐⭐ | 38,070 |
| [YouMind Prompts](https://youmind.com/zh-CN/prompts) | AI 提示词资料库. 全球最大的免费 AI 提示词库, 覆盖图像、视频和网页提示词. 持续追踪最新模型, 每日上新. | 通用 | ⭐ | NA |
| [asgeirtj/system_prompts_leaks](https://github.com/asgeirtj/system_prompts_leaks) | AI 系统提示词泄露收集仓库, 被《华盛顿邮报》报道. 系统性收录各大 AI 产品背后隐藏的系统提示词指令, 涵盖 Anthropic(Claude Fable 5/Opus 4.8 等)、OpenAI(GPT-5.5/o4-mini/Codex CLI 等)、Google(Gemini 3.5 Flash/CLI 等)、xAI(Grok 4.3 等)、VS Code Copilot Agent、Cursor、Perplexity 等数十个模型版本. 提供原始提示词、可视化版本、新旧版本对比, 社区驱动持续更新. | 通用 | ⭐⭐⭐ | 42,694 |


#### 3.4.2.3 Prompt 网页插件
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [zhu1090093659/deepseek-pp](https://github.com/zhu1090093659/deepseek-pp) | DeepSeek++ 浏览器扩展, 把 DeepSeek 网页版扩展成支持中英文体验、记忆、项目、Skill、MCP、浏览器控制、保存项、产物下载、对话导出和自动化的 AI Agent 工作台. 核心功能: 侧边栏对话、类原生工具调用(自动识别执行)、内置网络搜索/网页获取、Agent 式持续执行(多步续跑)、MCP 工具系统集成、OfficeCLI 文档工具(.docx/.xlsx/.pptx)、四种记忆系统、Skill 技能系统(内置/自定义/GitHub 导入)、自动化任务(手动/定时触发). 支持 Chrome、Edge、Firefox. | DeepSeek<br>Chrome<br>MCP | ⭐ | 697 |
| [乔木快捷提示词](https://chromewebstore.google.com/detail/乔木快捷提示词/ndfmbdiaclladmoeifbhlkacllmfhjej) |


### 3.4.3 Map&Graph
-------

[2026/04/05, 实践哥MinLi @MinLiBuilds, Cmd+Click 直达代码: Claude Code告别路径复制粘贴](https://x.com/MinLiBuilds/status/2040580427916919180)

#### 3.4.3.1 Code Mode
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [code-mode](https://github.com/universal-tool-calling-protocol/code-mode) | 将 AI 代理从笨拙的工具调用者转变为高效的代码执行器, 只需 3 行代码. 通过让 LLM 执行 TypeScript 代码来访问整个工具包, 支持多协议集成(MCP、HTTP、File、CLI), 提供安全的 VM 沙箱、超时保护、完整的可观测性和零外部依赖, 大幅提高复杂工作流的执行效率. | 多平台 | ⭐ | 1,420 |
| [mcpc](https://github.com/apify/mcpc) | 通用 MCP(Model Context Protocol)CLI 客户端, 支持持久会话、stdio/HTTP、OAuth 2.1、任务、代码模式的 JSON 输出、AI 沙箱的代理、x402 等功能. 提供完整的 MCP 协议支持, 包括工具调用、资源管理、提示模板、异步任务等核心功能, 是连接和管理 MCP 服务器的强大工具. | 多平台 | ⭐ | 420 |
| [nekocode/filetree-skill](https://github.com/nekocode/filetree-skill) | Claude Code插件,用于维护仓库中的FILETREE.md文件索引. 核心功能是为每个文件写一行用途说明并附上内容hash,让AI进入项目时先读一个轻量索引,而不是每次都从ls、grep、打开文件开始摸索. filetree把代码库结构化成一个可维护的Markdown文件,团队共享. | Claude Code | ⭐ | 130 |
| [Kappaemme-git/codex-complexity-optimizer](https://github.com/Kappaemme-git/codex-complexity-optimizer) | OpenAI Codex的代码库复杂度分析技能,提供安全的代码库复杂度审计和性能优化报告. 核心功能是将Codex会话转化为全仓库复杂度审计,标记热点、排列风险等级,并告诉你生产代码修改前该改什么. 每个发现提供6项具体输出:文件、行号、当前复杂度、推荐变更、预期变更后复杂度和风险级别. 工作流程保守安全:默认只读取仓库、摘要最差热点、停止而不修改文件. | OpenAI Codex | ⭐ | 869 |


#### 3.4.3.2 Code Graph
-------


从目前业界开源项目以及论文来看, Code Graph 主要形成两个流派:
1. Agent Optimization 派: 代表 CodeGraph, code-review-graph, graphify, graperoot, Repowise; 核心通过生成代码索引等减少 Agent 分析仓库的的 Token 数量
2. Repository Understanding 派, 代表 Understand-Anything, Sourcegraph Code Graph, DeepWiki, RepoPrompt, LogicLens Semantic Layer; 核心是为了让人更好的理解仓库.

而通过 Code Graph 让 Agent 理解仓库, 目前社区已形成三代方案
1. 第一代: 纯 Ventor RAG, 代表 RepoGPT, RepoMix
2. 第二代: Graph + Vector, 代表 graperoot, Repowise
3. 第三代: Graph First: 代表 CodeGraph, code-review-graph

[How code-review-graph Cuts Claude Code Token Usage by 49x (And Whether It's Actually Worth It)](https://www.innovatrixinfotech.com/blog/code-review-graph-claude-code-token-usage-reduction) 分析了 code-review-graph 的原理

[2026/06/01, 掘金--Yue的 AI 工坊--35K Star 一夜爆火: CodeGraph 把 AI 编码 Agent 的 Token 砍掉 57%, 工具调用减少 62%](https://juejin.cn/post/7645917873245585454) 则分析了 Code Graph 的实现, 并对比 CodeGraph, Serena, CodeGraphContext, code-graph-rag-mcp 几个工具.

code-review-graph 和 CodeGraph 的原理极其相似:
Layer 1: Parse — Building the AST with Tree-sitter, 基于 Tree-sitter 解析代码 AST;
Layer 2: Store — SQLite Graph Database 在本地构建持久化代码知识图谱, 记录函数、类、导入、调用、继承等代码依赖关系;
Layer 3: Trace — Blast Radius Analysis: code-review-graph 通过文件变更时自动做影响范围(爆炸半径)分析, 精准定位仅和当前修改相关的代码、测试文件; 实现增量更新图谱, 文件改动 2 秒内完成刷新; Code Graph 则通过原生 OS 文件事件(FSEvents / inotify / ReadDirectoryChangesW)监听变更, 2 秒 debounce 后增量同步;
Layer 4: Serve — MCP Integration, 通过 MCP 仅向 Claude 推送最小必要上下文, 替代全量文件读取.

一个合理的工作流推荐:  CodeGraph + RTK + Repowise
1. Code Graph 负责代码关系图, 告诉 Agent 谁和谁有调用/依赖关系;
2. RTK 负责输出压缩
3. Repowise 则作为仓库的知识层

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [tirth8205/code-review-graph](https://github.com/tirth8205/code-review-graph) | 一款为 Claude Code 打造的本地代码知识图谱工具, 核心解决 Claude Code 在代码审查时重复读取整个代码库、token 消耗过高、审查效率低的问题, 通过构建代码结构化图谱实现增量更新和精准的上下文提取, 大幅降低 token 消耗同时提升审查质量. | Claude Code | ⭐⭐ | 7,378 |
| [ix-infrastructure/Ix](https://github.com/ix-infrastructure/Ix) | 一个系统映射工具, 为开发者和 AI 提供系统级理解能力. 通过构建代码库的结构化地图, 捕获系统关系和流程, 实现持久化的系统记忆. 支持 TypeScript/JavaScript、Python、Go、Java 等多种语言, 可大幅减少开发任务中的 token 消耗(30-99.7%), 提高 LLM 使用效率(至少 43%). 提供 Claude、Codex、OpenClaw 等插件集成, 核心功能包括系统映射、流程追踪、影响分析和 AI 辅助推理. | 通用 | ⭐ | 113 |
| [1st1/lat.md](https://github.com/1st1/lat.md) | 为代码库创建知识图谱的工具, 通过 Markdown 文件组织知识, 支持 wiki 链接、代码引用和反向链接, 提供 CLI 工具验证一致性和语义搜索功能, 解决大型代码库知识管理问题 | 多 Agent 支持 | ⭐ | 919 |
| [Hyper-Extract](https://github.com/yifanfeng97/Hyper-Extract) | 智能、基于 LLM 的知识提取和演化框架, 将非结构化文本转换为结构化知识抽象, 支持多种格式从简单集合到复杂知识图谱、超图和时空图. 提供 8 种 Auto-Types、10+ 提取引擎、80+ 领域模板和增量演化能力, 可通过 CLI 或 Python API 使用. | 通用 | ⭐ | 275 |
| [SoulForge](https://github.com/ProxySoul/soulforge) | 一个智能 AI 编码工具, 通过构建实时依赖图来理解代码库, 支持 33 种语言, 提供多代理调度、外科式代码读取和即时上下文压缩等功能, 大幅提高编码效率并降低成本 | 核心技术包括 SQLite 支持的 Soul Map(包含 PageRank 排名、git 共变历史、影响范围评分等)、4 层智能系统(LSP、ts-morph、tree-sitter、regex)、多代理并行处理、嵌入式 Neovim 等 | 适用于需要深入理解大型代码库的开发团队, 希望降低 AI 编码成本的用户, 以及需要高效代码分析和重构的场景 | ⭐ | 255 |
| [Codex-CLI-Compact (GrapeRoot)](https://github.com/kunal12203/Codex-CLI-Compact) | 一个为 AI 编码助手提供复合上下文的工具, 使 Claude Code、Codex CLI、Gemini CLI、Cursor、OpenCode 和 GitHub Copilot 在不牺牲质量的情况下节省 30-45% 的成本. 通过构建代码库的语义图, 预加载相关上下文, 并在会话间记忆文件交互, 实现成本的持续降低. 支持多种编程语言, 所有处理均在本地进行, 确保代码安全. | 适用于任何规模的项目, 支持 macOS、Linux 和 Windows, 适合希望降低 AI 编码成本同时保持高质量输出的开发团队. | ⭐ | 619 |
| [GitNexus](https://github.com/abhigyanpatwari/GitNexus) | GitNexus: The Zero-Server Code Intelligence Engine - 一个客户端知识图谱创建器, 完全在浏览器中运行, 拖放GitHub仓库或ZIP文件, 获取带有内置Graph RAG Agent的交互式知识图谱 | Claude Code、Cursor、Codex、Windsurf、OpenCode | ⭐⭐⭐ | 27158 |
| [Token Savior](https://github.com/Mibayy/token-savior) | 为 Claude Code 提供的 MCP 服务器, 实现 97% 的代码导航令牌节省和跨会话记忆上下文的持久化记忆引擎. 提供 78 个工具, 零外部依赖, 支持 17+ 种语言包括 Python、TypeScript/JS、Go、Rust、C#、Java、C/C++、GLSL 等, 以及各种配置格式. | 核心技术包括符号级内容哈希(19x 重索引加速)、程序切片(92% 令牌减少)、背包上下文打包、依赖图上的 PageRank/RWR、Markov 预测预取、语义哈希、编辑验证等, 适用于大型代码库导航、AI 编码助手成本降低、跨会话上下文保留、代码变更影响分析、代码质量分析、多语言项目等场景 | Claude Code | ⭐ | 300 |
| [cocoindex-code](https://github.com/cocoindex-io/cocoindex-code) | 基于AST的轻量级嵌入式代码搜索引擎CLI, 为AI编码Agent节省70%的Token消耗并提高速度. 支持28+种语言, 提供语义搜索、零配置安装、增量索引和本地嵌入模型等功能. | Claude Code、Cursor、Codex、OpenCode | ⭐⭐⭐ | 1,361 |
| [Claude Context](https://github.com/zilliztech/claude-context) | 为 Claude Code 和其他 AI 编码代理添加语义代码搜索功能, 让整个代码库成为 AI 代理的上下文 | 语义代码搜索、向量数据库集成、增量索引、智能代码分块 | 大型代码库理解、AI 编码辅助、跨文件代码搜索 | Claude Code | ⭐⭐⭐ | 6,756 |
| [Entroly](https://github.com/juyterman1000/entroly) | 一个为 AI 编码工具提供全代码库上下文的工具, 通过压缩技术减少 70-95% 的令牌成本, 同时确保 AI 能够看到完整的代码库. 核心功能包括代码库索引、信息密度评分、数学优化的文件选择、分层压缩、自学习循环和联邦群体学习. | 适用于与 Claude、Cursor、Copilot、Codex、MiniMax 等 AI 编码工具集成, 任何规模的项目, 特别适合希望降低 AI API 成本、提高 AI 回答准确性、减少开发者修复 AI 错误时间的团队. | ⭐ | 319 |
| [OpenWolf](https://github.com/cytostack/openwolf) | 为 Claude Code 提供"第二大脑"的开源中间件, 通过 6 个不可见的生命周期钩子脚本实现项目智能、Token 追踪和隐形执行. 它核心功能包括: ① 项目文件索引(anatomy.md), 让 Claude 在读取前了解文件内容和 Token 估算, 它会自动生成项目文件地图, 标注每个文件的内容摘要和大小, Claude 不用打开文件就能知道里面有什么, 大幅减少无效扫描; ② 学习记忆(cerebrum.md)累积用户偏好和历史错误, 读过的文件会被记录, 重复读取直接拦截. 你纠正过的错误和编码偏好也会被记住, 下次遇到同类情况不再走弯路; 还内置 bug 记忆库, 修过的问题自动归档, 下次遇到相似报错能直接调出历史方案, 省去重复排查的时间; ③ Token 账本(token-ledger.json)追踪每次会话的 Token 消耗; Bug 记忆(buglog.json)防止重复发现已知问题. 实测可节省约 65-80% 的 Token 消耗, 并拦截 71% 的重复文件读取. 额外提供 Design QC(全页截图设计评估)、Reframe(UI 框架迁移辅助)和后台任务调度等功能. | Claude Code | ⭐ | 966 |
| [codewiki.google](https://codewiki.google) | Google 推出的 AI 原生代码文档平台, 通过 Gemini 大模型为代码仓库自动生成结构化 Wiki 文档并提供实时对话式查询功能. 核心功能: AI 自动解析代码生成系统概览与模块说明、每次代码变更后自动同步更新文档、集成 Gemini 智能对话助手支持自然语言问答、自动生成架构图/类关系图/序列图等可视化图表、文档与代码双向链接实现无缝跳转. 使用场景: 理解开源项目、新人入职快速上手、团队协作文档管理、调试与故障排查. 目前支持公共仓库免费在线预览, 私有仓库可通过 Gemini CLI 扩展在本地或内网环境运行(即将推出). | Gemini<br>Web<br>CLI | NA | 暂不开源 |
| [colbymchenry/codegraph](https://github.com/colbymchenry/codegraph) | 为 Claude Code 增强语义代码智能的开源工具, 通过构建预索引知识图谱实现代码快速智能探索. 核心目标: 减少 Claude Code 工具调用次数(平均减少94%)和加速代码探索(平均提升77%). 技术实现: tree-sitter 将源代码解析为 AST, 提取函数/类/方法节点及调用/导入/继承边关系, 存储于本地 SQLite + FTS5 全文搜索, MCP 服务器通过原生 OS 文件事件(FSEvents/inotify)实现自动同步. 主要功能: 智能上下文构建、全文符号搜索、调用链追踪(callers/callees)、影响范围分析、框架感知路由识别(支持 Django/Flask/FastAPI/Express/Laravel/Spring 等13个框架). 支持 19+ 编程语言: TypeScript/JavaScript/Python/Go/Rust/Java/C#/PHP/Ruby/C++/Swift/Kotlin/Dart/Svelte/Vue 等. 使用场景: 代码理解与探索、调用链追踪、修改前影响分析、全代码库符号搜索. MIT 许可. | Claude Code<br>Windows<br>macOS<br>Linux | ⭐ | 53,901 |
| [JordanCoin/codemap](https://github.com/JordanCoin/codemap) | 为 AI 提供"项目大脑"的上下文工具, 让 LLM 即时获取项目架构上下文无需消耗大量 tokens. 技术栈: Go 1.24.0(98.8%) + MCP SDK + bubbletea + fsnotify. 核心特性包括多种可视化模式(树状视图/Diff模式/依赖流图/Skyline模式/影响分析)、Claude Code Hooks自动上下文注入(session-start/pre-edit/post-edit/prompt-submit/session-stop)、MCP Server(17个工具: get_structure/get_dependencies/get_diff/get_hubs/get_file_context/start_watch/stop_watch/list_skills/get_skill/get_handoff等)、技能框架(5个内置技能: hub-safety/refactor/test-first/explore/handoff)、智能路由(意图分类+Hub风险分析+技能匹配)、多智能体协作(分层 Handoff: prefix+delta缓存优化+智能体历史追踪)、HTTP API和上下文协议. 支持 Claude Code(核心目标)、OpenAI Codex、MCP客户端和通用平台(Cursor/Windsurf等通过HTTP). 适用于重构分析、代码审查、多智能体切换、远程仓库探索和持续上下文维护. | Claude Code<br>Codex<br>多平台(MCP) | ⭐ | 555 |
| [AirswitchAsa/dog](https://github.com/AirswitchAsa/dog) | DOG (Documentation Oriented Grammar) - 将 AI 编程代理的计划转化为持久化的项目知识图谱, 用类型化的、可 lint 检查的 Markdown 文档替代一次性规格说明. 技术栈: Python 3.13(98.4%) + marko + pydantic + rapidfuzz + typer + fastapi + uvicorn + watchfiles. 核心概念采用四种原语(Actor@/Behavior!/Component#/Data&)和 Project 顶层概览. 主要功能包括文档索引与查询(dog list/get/search)、引用分析与影响评估(dog refs)、质量检查(dog lint/format)、可视化与导出(dog graph/export)、实时浏览(dog serve). 支持 Claude Code/Cursor/Codex 通过技能系统集成. 实测效果: 概念召回率+3.5%、文件召回率+32%、工具调用次数-35%. 适用于长期维护项目、AI辅助开发、微服务架构和团队协作. | Claude Code<br>Cursor<br>Codex | ⭐ | 10 |
| [Octocode](https://github.com/Muvon/octocode) | AI Agent 的代码库结构化智能工具, 基于 Rust + Tree-sitter 构建结构化代码索引, 通过 GraphRAG 知识图谱和混合语义搜索, 让 AI 能够真正理解、搜索和导航项目架构. 本地优先(隐私安全), 开源 Apache 2.0, 深度集成 MCP 协议, 支持 Claude/Cursor 等主流 AI 工具. | 多 Agent 支持 | ⭐⭐ | 371 |
| [Jakedismo/codegraph-rust](https://github.com/Jakedismo/codegraph-rust) | 将整个代码库转换为可搜索的知识图谱, 让 AI 智能体真正理解代码结构和依赖关系. 采用图数据库+向量嵌入+LSP解析, 提供4个智能体工具(上下文收集、影响分析、架构理解、质量评估)、混合搜索(70%向量+30%词汇)、分层索引、上下文溢出防护和守护模式. 支持Claude Code、Cursor、Gemini CLI等MCP兼容智能体. 技术栈: Rust 98.2% + SurrealDB + Tree-sitter + MCP协议. | Claude Code<br>Cursor<br>Gemini CLI<br>MCP兼容智能体 | ⭐ | 699 |
| [xnuinside/codegraph](https://github.com/xnuinside/codegraph) | 静态 Python 代码分析器, 生成交互式可视化图表, 无需执行即可展示代码结构和依赖关系. 提供交互式可视化(缩放、拖拽、节点重排)、节点搜索与高亮连接、节点信息提示、按连接数过滤节点、检测未链接模块、巨型对象检测和CSV导出功能. 技术栈: Python 56.8% + JavaScript 27.4% + CSS 9.6%. | 通用 | ⭐ | 471 |
| [repowise-dev/repowise](https://github.com/repowise-dev/repowise) | AI编码代理的代码库智能层, 提供四层智能架构(图智能-Git智能-文档智能-决策智能)和七个MCP工具(get_overview、get_answer、get_context、search_risk、get_why、get_dead_code). 支持多仓库工作区、跨仓库共变检测、API契约提取、联邦MCP查询和自动同步(Git钩子、文件监视器、Webhooks). 技术栈: Python 70.8% + TypeScript 27% + Tree-sitter. | Claude Code<br>MCP兼容智能体 | ⭐ | 1,590 |
| [raushankcode/ripple](https://github.com/raushankcode/ripple) | TypeScript 项目的实时架构上下文视图. AI coding agent 在写代码时经常因为"不知道影响范围"而改出问题. Ripple 专门给 AI agent 提供实时的架构上下文, Impact Lens: 选中文件后能看到它被哪些文件引用、它又依赖了哪些文件(本地 blast radius 可视化); CodeLens: 直接显示函数/组件的 caller 数量; 修改前做 Safety Check, 提示可能影响未测试的文件; 一键生成适合喂给 Claude Code / Cursor 的架构感知 prompt; 自动维护 `.ripple/WORKFLOW.md`, 让 agent 在编辑前先理解项目结构; 核心解决的问题是 Context Rot —— 静态的 `CLAUDE.md/.cursorrules` 随着代码演进会逐渐失效, 而 Ripple 提供的是实时的、本地的依赖关系信息. | 多 Agent 支持 | ⭐ | 1 |
| [DeusData/codebase-memory-mcp](https://github.com/DeusData/codebase-memory-mcp) | 用 AI 辅助编程时, 简单问个问题要逐个文件去翻找读取, 既费 token 又容易找错上下文. 把整个代码库解析成一张知识图谱, 让 AI 直接「看懂」项目结构. 用纯 C 写的单个可执行文件, 零依赖, 下载后一条命令就能装好. 索引速度很猛, Linux 内核两千八百万行代码, 3 分钟跑完. 支持 158 种编程语言的语法解析, 能跨文件追踪函数调用链、识别接口路由、发现死代码. 还自带 3D 图谱可视化界面. 如果我们经常用 AI 写代码, 又觉得它对项目全局缺乏理解, 这个工具值得一试. | 兼容 Claude Code、Gemini CLI、Codex 等 11 款 Agent 编程工具 | ⭐ | 10,663 |
| [Egonex-AI/Understand-Anything](https://github.com/Egonex-AI/Understand-Anything) | ⭐ | 67,052 |
| [](https://github.com/kunal12203/graperoot-plugin) | 13 |


#### 3.4.3.3 Context
-------


| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [upstash/context7](https://github.com/upstash/context7) | 一个为 AI 编码助手提供最新代码文档的平台, 能够从源代码中提取最新的、特定版本的文档和代码示例并直接放入提示中. 支持 CLI + Skills 和 MCP 两种工作模式, 可通过 `npx ctx7 setup` 快速安装. 核心功能包括库文档检索、版本匹配、API 参考等, 解决 LLM 依赖过时信息的问题. | 通用 | ⭐⭐⭐⭐ | 52,050 |
| [ForLoopCodes/contextplus](https://github.com/ForLoopCodes/contextplus) | 一个为开发者设计的 MCP 服务器, 要求 99% 准确性. 通过结合 RAG、Tree-sitter AST、谱聚类和 Obsidian 风格链接, 将大型代码库转变为可搜索的分层特征图. 提供 17 个 MCP 工具, 包括结构分析、语义搜索、代码操作、版本控制和记忆图等功能. 支持多种 IDE 和编码助手, 可通过 `npx contextplus init` 快速配置. | 通用 | ⭐ | 1,745 |
| [piercelamb/deep-project](https://github.com/piercelamb/deep-project) | 一个将模糊的软件项目需求转化为可规划组件的 Claude Code 插件, 通过 AI 辅助的访谈和分解过程, 将大型项目分解为可管理的规划单元. 作为 Deep Trilogy 的第一步, 它确保你已经考虑了软件构建的每个主要组件, 并为后续的 `/deep-plan` 做好了准备. 核心功能包括自适应访谈、拆分分析、依赖映射和规范生成等. | 通用 | ⭐ | 111 |
| [Context Hub](https://github.com/andrewyng/context-hub) | 一个为编码代理提供策划、版本化文档的平台, 解决编码代理幻觉 API 和忘记会话中学习内容的问题. 支持 CLI 工具 (chub 命令), 提供增量获取、注释和反馈系统, 使代理能够通过每个任务变得更智能. 所有内容都是开放和可维护的. | 通用 | ⭐⭐⭐⭐ | 12,984 |
| [QuinnAho/claudemap](https://github.com/QuinnAho/claudemap) | 为 AI 编码者设计的代码可视化工具, 被称为 "Google Maps for vibecoders". 不同于传统可视化工具, ClaudeMap 通过 AI 分析你的项目并按照实际功能组织代码, 以你思考项目的方式将代码分组为概念. 支持全局概览和细节放大, 颜色区分健康和问题代码, 提供 /explain 和 /show 命令进行交互式代码探索, 支持多地图和迭代细化, 兼容 Claude Code 和 OpenAI Codex. | Claude Code / Codex | ⭐⭐⭐ | 1,532 |
| [championswimmer/pi-context-prune](https://github.com/championswimmer/pi-context-prune) | Pi 编码代理上下文剪枝扩展, 总结已完成的工具调用批次, 从未来 LLM 上下文中剪枝原始工具输出, 并提供 context_tree_query 安全门按需恢复任何原始输出. 支持五种触发模式(every-turn、on-context-tag、on-demand、agent-message、agentic-auto), 提供 /pruner 命令行工具配置, 支持多种摘要模型和缓存友好设计, 有效减少长会话的 Token 消耗. [2026/05/14, 九原客 @9hills, 我最近在用 pi-context-prune 这个插件, 今天腾讯新出的 agent memory 也用了类似的思路](https://x.com/9hills/status/2054837782384959796) | Pi | ⭐ | 63 |
| [yamadashy/repomix](https://github.com/yamadashy/repomix) | 将整个代码仓库打包成单个AI友好格式文件, 适用于将代码库提供给LLM或其他AI工具. 支持多种输出格式(XML/Markdown/JSON/Plain)、Token计数、Git感知(自动遵循.gitignore)、安全检查(检测敏感信息)、Tree-sitter智能压缩、远程仓库支持、MCP服务器集成和Claude Agent Skills生成. 技术栈: TypeScript 93% + Vue 4.7%. 支持Claude、ChatGPT、DeepSeek等多种LLM平台. | Claude<br>ChatGPT<br>DeepSeek<br>多LLM平台 | ⭐⭐⭐ | 24,908 |
| [yusufkaraaslan/Skill_Seekers](https://github.com/yusufkaraaslan/Skill_Seekers) | AI系统的数据预处理层, 将18种来源(文档网站、GitHub仓库、PDF、Word、视频、Jupyter Notebook等)转化为结构化知识资产, 支持20+平台导出. 核心功能包括智能发现(sitemap/llms.txt/无头浏览器)、GitHub深度分析(AST解析/API提取)、视频提取(字幕/OCR)、20+LLM平台支持、RAG框架集成、异步抓取(2-3x提升)和MCP服务器(14个工具). 技术栈: Python 98% + FastMCP. 支持Claude、Cursor、OpenAI等19种AI编程助手. | Claude<br>Cursor<br>Codex<br>OpenAI<br>多平台支持 | ⭐⭐⭐ | 13,575 |
| [hoangnb24/repository-harness](https://github.com/hoangnb24/repository-harness) | 将任意软件仓库转变为 Agent-ready 工作空间, 为 Claude Code、Codex、Cursor 等编码 Agent 提供仓库级操作框架, 补齐 Agent 在改代码前缺失的项目上下文. 核心理念: 编码 Agent 不仅需要更好的 Prompt, 更需要更好的仓库结构. 核心组件: Agent 操作指南(AGENTS.md)、人-Agent 协作模型(HARNESS.md)、功能分级(FEATURE_INTAKE.md)、架构发现与边界规则(ARCHITECTURE.md)、行为-验证矩阵(TEST_MATRIX.md)、故事包与 backlog、决策记录、模板库、工具注册机制、Harness CLI(Rust 实现). | Claude Code<br>Codex<br>Cursor | ⭐ | 507 |


#### 3.4.3.4 LSP
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [Claude Code LSP Enforcement Kit](https://github.com/nesaminua/claude-code-lsp-enforcement-kit) | 强制 Claude Code 使用 LSP 而非 Grep 进行代码导航的钩子工具集, 可节省约 80% 的 tokens. | Claude Code | ⭐ | 241 |
| [blvp/cc-lspctl](https://github.com/blvp/cc-lspctl) | Mason 风格的 LSP 服务器管理器, 使用 Neovim 兼容的 Lua 配置定义 LSP 服务器并自动生成 Claude Code LSP 插件 | Claude Code | ⭐ | 4 |
| [zircote/lsp-tools](https://github.com/zircote/lsp-tools) | LSP 优先的代码智能工具, 强制执行语义代码导航, 提供 IDE 级精度的代码操作 | Claude Code | ⭐ | 3 |
| [Piebald-AI/claude-code-lsps](https://github.com/Piebald-AI/claude-code-lsps) | Claude Code LSP插件市场, 提供TypeScript、Rust、Python等多种编程语言的LSP服务器支持, 实现代码导航、符号查找等IDE级功能 | Claude Code | ⭐ | 410 |
| [ktnyt/cclsp](https://github.com/ktnyt/cclsp) | MCP 服务器, 将 LLM 编码代理与 LSP 服务器无缝集成, 解决 LLM 提供准确行/列号的问题, 支持 go to definition、find references 等功能. | 多平台支持 | ⭐ | 614 |
| [boostvolt/claude-code-lsps](https://github.com/boostvolt/claude-code-lsps) | Claude Code 的 LSP 插件集合, 支持多种编程语言, 提供LSP工具和自动诊断功能 | Claude Code | ⭐ | 148 |
| [agent-sh/agnix](https://github.com/agent-sh/agnix) | 代理配置 lint 工具, 支持 399 条规则, 覆盖 Claude Code、Codex CLI 等多种 AI 工具, 提供自动修复功能 | 多平台支持 | ⭐ | 177 |
| [MinishLab/semble](https://github.com/MinishLab/semble) | 为 AI Agent 提供快速准确的代码搜索,比 grep+read 减少 98% token 消耗,使用 tree-sitter 分块 + Model2Vec 嵌入 + BM25 混合检索,支持 MCP Server 模式. | Claude Code<br>Cursor<br>Codex<br>OpenCode<br>VS Code<br>GitHub Copilot CLI<br>Windsurf<br>Gemini CLI<br>Kiro<br>Zed | ⭐⭐⭐ | 1,785 |

### 3.4.4 Context 处理
-------

#### 3.4.4.1 Thinking
-------


| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [fluxgear/pi-thinking-steps](https://github.com/fluxgear/pi-thinking-steps) | 结构化的终端原生思考步骤渲染器, 为 Pi 提供折叠、摘要和展开三种视图模式, 提升模型推理的可读性. | Pi | ⭐⭐⭐ | 53 |
| [0xsakura666/opus-style-output](https://github.com/0xsakura666/opus-style-output) | 专为 Codex/GPT 模型设计的全局 Skill, 让输出风格更接近 Claude Opus 的优点(清晰、结构化、温和、易读、简洁). 技术栈: YAML + Markdown(纯提示工程, 无代码实现). 核心能力包括全局输出优化、Opus 风格表达、表格优先、Emoji 分区、前端文案约束和用户视角 copy. 输出格式规范采用五区结构(✅已完成/📁涉及文件/🧪验证/⚠️说明/💡后续建议). 前端文案重写规则: 标题/导航/按钮优先短名词短语、描述文本面向用户价值、避免技术感强的表达. 对比示例覆盖加载状态/设置页/工作台/表单校验/按钮文案等场景. 通过 Codex skills 目录安装, 支持自动触发和手动触发. 适用于代码任务总结、前端文案优化、方案对比、Code Review 和产品文档. | Codex<br>GPT系列 | ⭐ | 40 |
| [tjboudreaux/cc-thinking-skills](https://github.com/tjboudreaux/cc-thinking-skills) | 39个心智模型与框架的批判性思维技能集,专为Claude Code设计,增强AI辅助问题解决、决策制定和战略分析能力. 涵盖六大类别:①决策与分析(第一性原理、二阶思维、逆向思维等8个);②认知与行为(贝叶斯推理、去偏差、苏格拉底法等7个);③系统与策略(系统思维、OODA循环、约束理论等7个);④问题解决与创新(奥卡姆剃刀、TRIZ、科学方法等7个);⑤估计与风险(费米估算、安全边际等5个);⑥产品与创新(JTBD等);⑦元技能(模型路由、选择、组合3个). | Claude Code | ⭐ | 294 |


#### 3.4.4.2 Rules
-------

[2026/05/13, Vince 聊开发 @vincemask, 从 0 开始: 用 Hooks 打造自动化 Claude Code 工作流](https://x.com/vincemask/status/2054457804057100405)

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [ciembor/agent-rules-books](https://github.com/ciembor/agent-rules-books) | AI 编程助手(Codex/Cursor/Claude Code)的 AGENTS.md 规则集, 从14本经典软件工程著作(《重构》《代码整洁之道》《领域驱动设计》《架构整洁之道》《数据密集型应用设计》等)中提炼结构化规则. 提供 full/mini/nano 三级版本适配不同上下文预算, 采用 MUST/SHOULD/MUST NOT 语义表达确保强制性与指导性区分. 覆盖日常代码质量、架构边界、领域建模、重构实践、遗留代码改造及生产系统设计等场景. MIT 许可, 社区活跃. | Codex<br>Cursor<br>Claude Code | ⭐ | 1,098 |
| [revfactory/harness-100](https://github.com/revfactory/harness-100) | 面向 Claude Code 的生产级 AI Agent 团队协作系统集合(200个Harness + 978个Agent定义 + 630个技能模块). 技术栈: Markdown + YAML配置文件. 每个Harness采用三层技能系统(Orchestrator编排层 + Agent-Extending扩展层 + External外部工具层). 核心特性包括Agent Team Mode(SendMessage直接通信+交叉验证)、依赖DAG编排、文件驱动通信(_workspace目录)、错误处理策略(重试/跳过/降级)和规模自适应. 十大领域覆盖: 内容创作、软件开发、数据AI、商业战略、教育培训、法律合规、健康生活、沟通文档、运营流程、专业领域. 每个领域内嵌真实业务框架(AIDA/SOLID/DDD/OWASP/BMC/Bloom分类法/IRAC等). 典型案例: YouTube Production Harness(5个专业角色+完整工作流+2个技能扩展). 适用于内容创作、软件开发、数据科学、企业运营、咨询顾问、教育工作和法律专业. | Claude Code | ⭐ | 714 |


#### 3.4.4.3 输入格式
-------


| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [curl.md](https://curl.md) | 专门把网页转成 Markdown 格式喂给 AI, token 消耗直接砍一大截. CLI、浏览器插件、API 三种用法随你选 | Cursor、Claude | ⭐ | 210 |

#### 3.4.4.4 输出格式
-------

[2026/05/10, AYi @AYi_AInotes, HTML 是 AI 时代的沟通语言](https://x.com/AYi_AInotes/status/2052842474687680678) 分析了 [2026/05/09, Thariq
@trq212, Using Claude Code: The Unreasonable Effectiveness of HTML](https://x.com/trq212/status/2052809885763747935)
[2026/05/18, AYi @AYi_AInotes, 为什么Claude内部放弃了Markdown, 因为HTML才是AI时代的唯一标准(完整实战指南・附全套提示词)](https://x.com/AYi_AInotes/status/2056377322542944690) 则回答了"到底哪些活该用 HTML,哪些活该用 Markdown?"

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [nicobailon/visual-explainer](https://github.com/nicobailon/visual-explainer) | 将复杂终端输出转换为美观HTML页面或幻灯片,替代ASCII表格和流程图,支持Mermaid图表、Chart.js数据可视化,自包含HTML无需构建步骤 | Claude Code<br>Pi<br>Codex CLI<br>OpenCode<br>Cursor<br>OpenClaw | ⭐⭐⭐ | 8,180 |
| [nexu-io/html-anything](https://github.com/nexu-io/html-anything) | 智能时代的HTML编辑器, 本地AI Agent编写HTML, 一键导出到微信/X/知乎. 零API密钥, 支持8种编码Agent CLI(Claude/Cursor/Codex/Gemini/OpenCode/Qwen/Aider)×75技能模板×9种交付场景(文章、演示文稿、简历、小红书卡片、Web原型、数据可视化、Hyperframes视频). 提供流式渲染、实时预览、沙箱化iframe隔离. 技术栈: Next.js 16 + React 18 + Tailwind v4. | Claude Code<br>Cursor<br>Codex<br>Gemini CLI<br>OpenCode<br>Qwen Code<br>Aider | ⭐ | 1,682 |
| [curl.md](https://curl.md) | curl.md —— Markdown时代的curl, 让LLM直接获取网页内容为结构化Markdown, 专为AI Agent设计的信息摄取工具. | 通用(LLM工具) | ⭐ | NA |
| [vercel-labs/mdxg](https://github.com/vercel-labs/mdxg) | 一个标准, 定义界面如何呈现和导航Markdown文档, 将单文件转化为多页面导航体验. 核心功能包括虚拟页面(H1/H2自动分割)、页面导航、页面大纲(H3-H6标题导航)、顺序阅读、搜索功能、代码块渲染(语法高亮+复制按钮)、任务列表、预览/源码模式切换和文档链接. 技术栈: TypeScript 94% + CSS 5%. 提供VS Code扩展和Web实现作为参考. | 通用(Markdown渲染界面) | ⭐ | 297 |
| [markdown-viewer](https://github.com/markdown-viewer) | Markdown文档查看器, 提供简洁的文档浏览和导航功能. 支持多种Markdown格式渲染, 适用于技术文档、博客文章等场景的快速预览和阅读. | 通用 | ⭐ | 12 |
| [alchaincyf/huashu-md-html](https://github.com/alchaincyf/huashu-md-html) | md/html/docx多向流水线, 四种能力一站式: 万物→md(PDF/DOCX/PPT/XLSX/EPUB/音频/YouTube/网页URL转换为markdown) → md→精美html(4套反AI slop主题) → html→md(反向归档) → md→出版社级docx(封面、目录、页眉页脚). 技术栈: Python 47.5% + CSS 52%. 支持Claude Code、Cursor、Codex、OpenClaw、Hermes等跨Agent通用. | Claude Code<br>Cursor<br>Codex<br>OpenClaw<br>Hermes | ⭐ | 549 |
| [ysm-dev/cpdown](https://github.com/ysm-dev/cpdown) | 一键复制网页内容或YouTube字幕为干净Markdown格式,浏览器扩展基于WXT+React+Shadcn UI,使用Defuddle或Mozilla Readability提取主要内容 | 独立浏览器扩展(配合任何LLM) | ⭐ | 545 |
| [crimx/agentic-markdown](https://github.com/crimx/agentic-markdown) | 轻量级Markdown-first模板引擎,支持变量替换和条件内容渲染. 通过HTML注释指令在Markdown文档中嵌入变量(agentic:var)和条件逻辑(agentic:if/elseif/else/endif),实现按不同AI Agent(如codex、claude、gemini)或项目变量动态渲染Markdown内容. 支持精确匹配、多值匹配(分隔)、变量非空检查. 不支持嵌套条件块. | NA | ⭐ | 12 |
| [kovamd/kova](https://github.com/kovamd/kova) | 将 Markdown 原生转换为带实时预览、多布局、主题系统和 PPTX 导出的幻灯片. 用 Markdown 直接生成演示幻灯片. 它自动识别 16 种布局(标题、分栏、代码、公式等), 支持 KaTeX 数学公式、Mermaid 图表和代码高亮. 内置 11 套主题, 也可以装社区主题或自己写 YAML 主题. 全屏演示带演讲者备注, 还能导出成 PPTX 格式. | Claude Code | ⭐ | 52 |

#### 3.4.4.5 AGENT.MD
-------


[2026/05/29, 爆裂队长NEXT @thinkszyg, AGENTS.md 完全指南 2026: 规范、工具、示例](https://x.com/thinkszyg/status/2060295182864814569) [AGENTS.md](https://agents.md) 是 Linux 基金会维护采用的跨 AI 编程助手通用标准, 仓库地址 [agentsmd/agents.md](https://github.com/agentsmd/agents.md) 根目录纯 Markdown 文件, 供 Cursor、Copilot 等二十余种工具读取, 统一存放项目构建、测试、代码规范、操作边界, 解决多工具规则碎片化、AI 丢失项目约定的痛点. 无强制语法, 推荐划分项目环境、测试、目录、PR、三级行为约束章节; 单体仓库支持嵌套文件, 就近规则优先级更高. 它与 Claude 专用 CLAUDE.md、复用能力 SKILL.md、工具协议 MCP 互补. 写作需指令清晰、标注版本与完整命令, 控制单文件 300 行内, 禁止存放密钥; 开源项目配置后可大幅减少 AI 提交代码返工.

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [SOUL.md](https://github.com/madhvantyagi/SOUL.md) | AI Agent 人格定义文件集合库, 每个 SOUL.md 定义 Agent 的身份、语气、信念和边界, 让 Agent 拥有可辨识的性格而非千篇一律的默认人设, 兼容 OpenClaw、Hermes、OpenCode、Claude 等 | OpenClaw、Hermes、OpenCode | ⭐ | 283 |
| [agents.md](https://github.com/zeke/agents.md) | AI 编码代理全局指令文件(Claude Code、OpenCode、Codex 等), 加载到每次编码会话中作为系统级指南, 规范代理行为: 验证什么、跳过什么、如何编写提交和 PR | OpenCode、Claude Code、Codex | ⭐ | 140 |
| [awesome-claude-md](https://github.com/josix/awesome-claude-md) | 精选公开 GitHub 项目中的优秀 claude.md 文件和 onboard 模式集合, 提供分析、最佳实践和模板, 帮助开发者创建有效的 AI 入门文档 | Claude Code | ⭐⭐ | 390 |


# 🎨 4 状态管理
-------

## 4.1 通知
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [opencode-notifier](https://github.com/mohak34/opencode-notifier) | OpenCode 桌面通知插件 (仓库可能已下线) | OpenCode | ⭐ | 428 |
| [opencode-terminal-notifier](https://github.com/mathew-cf/opencode-terminal-notifier) | OpenCode 终端通知插件, 通过终端本身发送通知, 点击通知可跳回正确的终端会话. 支持 Ghostty/iTerm2/Kitty/WezTerm 桌面通知, 其他终端声音 + dock bounce | OpenCode | ⭐ | 2 |
| [opencode-smart-voice-notify](https://github.com/MasuRii/opencode-smart-voice-notify) | OpenCode 智能语音通知插件 (仓库可能已下线) | OpenCode | ⭐ | 52 |
| [claude-code-sound-notification](https://github.com/EryouHao/claude-code-sound-notification) | Claude Code 声音通知插件, 使用 SND01 "sine" 声音套件, 在等待用户确认和 Claude 完成响应时提供声音提示 | Claude Code | ⭐ | 28 |
| [peon-ping](https://github.com/PeonPing/peon-ping) | 为 AI 编码代理提供游戏角色语音和视觉覆盖通知, 支持 Claude Code、Amp、GitHub Copilot、Cursor、OpenCode 等多种工具, 当代理完成任务或需要权限时通过声音和视觉提示提醒用户 | 多平台支持 | ⭐ | 4,374 |


## 4.2 会话管理
-------

[总结多会话管理编排的帖子](https://x.com/juristr/status/2031820737745682520)


### 4.2.1 会话监控
-------

#### 4.2.1.1 TUI 监控工具
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [asheshgoplani/agent-deck](https://github.com/asheshgoplani/agent-deck) | AI 代理命令中心, 支持多平台, 提供会话管理、MCP 池化等功能, 适用于 Claude Code、OpenCode 等多种 AI 编程工具 | 多 Agent 支持 | ⭐ | 1,955 |
| [Frayo44/agent-view](https://github.com/Frayo44/agent-view) | 轻量级基于终端的代理编排器, 用于管理多个 AI 编码助手, 支持实时状态监控、智能通知、会话管理、Git Worktree 集成和远程会话管理, 适用于 Claude Code、Gemini CLI、OpenCode、Codex CLI 等多种 AI 编程工具 | Claude Code/Gemini/OpenCode/Codex | ⭐ | 344 |
| [hallucinogen/agent-viewer](https://github.com/hallucinogen/agent-viewer) | OpenCode 状态栏插件, 显示当前会话信息 | OpenCode | ⭐ | 356 |
| [fynnfluegge/agtx](https://github.com/fynnfluegge/agtx) | 用于管理 agent coding 会话的原生终端看板, 可以接入 Claude Code、Codex、Gemini、OpenCode、Copilot 等任何现有的规范驱动开发框架, 或指定一个具有分阶段技能的自定义插件. | Claude Code/Codex/Gemini/OpenCode/Copilot | ⭐ | 823 |
| [batrachianai/toad](https://github.com/batrachianai/toad) | TUI 界面的终端 AI 智能体管理器. | 多 Agent 支持 | ⭐ | 2,809 |
| [Dimillian/CodexMonitor](https://github.com/Dimillian/CodexMonitor) | Tauri 应用, 用于在本地工作区中编排多个 Codex 代理, 提供侧边栏管理项目, 主屏幕用于快速操作, 以及由 Codex app-server 协议支持的对话视图. | Codex | ⭐ | 3,490 |
| [agentastic.dev](https://www.agentastic.dev) | Agentic 开发环境, 支持运行 30 + 并行编码代理(Claude Code、Codex、Gemini、Cursor 等), 使用 Git worktrees 或 Docker 容器进行完全隔离, 每个代理都有自己的内置 IDE、Ghostty 终端和浏览器. | 多 Agent 支持 | ⭐⭐⭐⭐⭐ | NA |
| [agent-sessions](https://github.com/jazzyalex/agent-sessions) | 统一会话浏览器, 支持 Codex CLI、Claude Code、Gemini CLI、GitHub Copilot CLI、Droid (Factory CLI)和 OpenCode, 提供搜索、浏览和恢复过去的 AI 编码会话的本地优先 macOS 应用 | macOS 14+ | ⭐ | 450 |
| [claudex](https://github.com/kunwar-shah/claudex) | 专业的 Claude Code 会话查看器和分析工具, 是一个全栈 web 应用, 为开发人员、QA 工程师和研究人员提供检查、搜索和分析 Claude Code 对话历史的能力. 主要功能包括: MCP 服务器(为 Claude Code 提供跨会话持久记忆)、结构化记忆系统、自动项目发现、全文搜索(SQLite FTS5)、通用模板支持、智能内容渲染、会话分析、导出选项、现代 UI 等. 技术栈: React、Fastify、SQLite、Docker. 适用于 Claude Code 对话分析、搜索、记忆管理等场景 | Claude Code | ⭐ | 75 |
| [illegalstudio/lazyagent](https://github.com/illegalstudio/lazyagent) | 一个单一界面监控所有编码代理 (Claude Code、Cursor、pi、OpenCode) 的工具, 提供终端 UI、macOS 菜单栏应用和 HTTP API, 无锁定、无服务器、纯观察性. 支持活动状态检测、Git worktree 检测、令牌使用和成本估算、实时活动火花图等功能. | 多 Agent 支持 | ⭐ | 131 |
| [Markus](https://www.markus.global) | 开源平台, 用于设计、部署和管理自主 AI 代理和团队, 具有任务治理、知识系统和多渠道通信能力. 主要特点包括: 自主代理(带角色、技能、记忆和心跳驱动的主动工作)、多代理团队(角色分配和治理策略)、任务治理(看板、审批工作流、交付审查)、技能和工具(符合 Agent Skills 开放标准)、外部代理集成(通过 A2A 协议)、通信中心(Web UI 聊天和多渠道集成)、知识系统(三层记忆)、信任和治理(渐进式信任级别)、项目管理、代理构建器、GUI 自动化和社区中心. 技术栈: TypeScript、React、SQLite/PostgreSQL、本地优先、LLM 无关. 许可证: AGPL-3.0. 适用于构建、管理和扩展 AI 工作队伍、多代理协作项目、任务治理和审批工作流、跨渠道 AI 通信等场景 | 多 Agent 支持 | ⭐⭐ |
| [kincoy/cc9s](https://github.com/kincoy/cc9s) | 受 k9s 启发的 TUI 和 CLI 工具, 用于高效管理 Claude Code 会话、技能和代理. 提供会话浏览、搜索、检查、恢复、批量删除、项目概览、技能和代理资源浏览器等功能. 支持 CLI 模式用于脚本自动化, JSON 输出用于 AI 代理集成. 技术栈: Go + Bubble Tea/Lip Gloss TUI 框架. 适用于管理大量 Claude Code 会话、快速查找恢复历史会话、分析使用情况、管理本地技能和代理等场景 | Claude Code | ⭐ | 64 |
| [ldegio/agtop](https://github.com/ldegio/agtop) | 类似于 htop 的终端用户界面(TUI)工具, 专门用于监控 AI 编码代理会话(Claude Code 和 Codex). 提供实时监控成本、令牌使用情况、上下文压力、CPU 负载、工具调用等关键指标. 主要功能包括: 自动会话发现、成本跟踪(按会话细分和计费计划支持)、上下文压力监控(CTX%)、实时性能监控(CPU/内存)、进程树查看、工具活动跟踪、配置浏览(CLAUDE.md/AGENTS.md、记忆、技能、MCP服务器)、会话管理、多种输出模式(交互式TUI、表格、JSON). 技术栈: Node.js (>=18), 无外部依赖, 单文件发布. 工作原理: 读取 JSONL 转录文件, 从 LiteLLM 获取模型定价, 使用 ps/lsof 收集系统指标. 适用于成本监控、性能调优、会话管理、工具使用分析、上下文管理、自动化集成等场景 | Claude Code/Codex | ⭐ | 46 |
| [abtop](https://github.com/graykode/abtop) | 类似于 btop 的 AI 编码代理监控工具, 用于实时查看 Claude Code 和 Codex CLI 会话的令牌使用情况、上下文窗口百分比、速率限制、子进程和开放端口等信息. 主要功能包括: 自动发现会话、令牌跟踪、上下文窗口监控、状态检测、当前任务查看、速率限制监控、Git状态显示、子进程/端口监控、子代理支持(仅Claude Code)、内存状态(仅Claude Code)、10个内置主题(包括4个色盲友好选项)、tmux会话跳转支持等. | Claude Code/Codex | ⭐ | 895 |
| [patoles/agent-flow](https://github.com/patoles/agent-flow) | Claude Code 和 Codex 代理编排的实时可视化工具, 通过交互式节点图实时展示代理执行过程, 支持多会话监控、时间线和消息面板, 帮助理解代理行为、调试工具调用链、查看时间消耗. 提供三种使用方式: npx agent-flow-app(独立Web应用)、VS Code扩展、从源码构建. 核心功能包括: 实时代理可视化、Claude Code钩子、Codex rollout文件读取、多会话支持、交互式画布、时间线和消息面板、JSONL日志文件支持 | Claude Code/Codex | ⭐ | 1,508 |
| [Spool](https://github.com/spool-lab/spool) | 本地 AI 会话管理工具, 收集 Claude Code、Codex CLI、Gemini CLI 会话并提供侧边栏浏览、固定和 ⌘K 全文搜索功能, 采用 Electron + React + SQLite 技术栈, 数据完全本地存储, 隐私优先. | Claude Code<br>Codex<br>Gemini CLI | ⭐ | 483 |
| [CTOP](https://github.com/aakashadesara/ctop) | AI 编程代理的终端监控面板, 实时追踪 Claude Code 和 Codex CLI 的 CPU、内存、Token 消耗、上下文窗口及 API 成本, 提供列表/窗格双视图、日志尾随、24小时历史图表和会话管理功能, 支持插件扩展和 5 种主题, 零依赖、跨平台运行. | Claude Code<br>Codex | ⭐ | 41 |
| [Lanes](https://github.com/lanes-sh/app) | macOS 原生 AI 编程工作空间, 将多个 AI 代理会话集成在 Issue Board 面板中, 支持实时终端和任务状态追踪, 实现并行编码的高效管理. 支持 Apple Silicon 和 Intel 芯片, macOS Ventura (13.0) 或更高版本. | macOS | ⭐ | 132 |
| [joewinke/jat](https://github.com/joewinke/jat) | "世界首个Agentic IDE"——自主代理开发环境JAT(Just Agentic Tasks),支持监督式或自主运行. 核心理念是"Supervise the Swarm",可管理20+代理的手动监督或让代理自主运行. 集成任务管理、代理编排、代码编辑器(Monaco Editor)、Git集成和终端访问的统一IDE. 可连接RSS、Slack、Telegram、Gmail,事件自动创建任务并生成代理. 支持Epic Swarm模式(同时运行20+代理)、Cron调度器、语音命令操作(Ctrl+Space)、技能市场、Supabase集成. 100%本地运行. | Linux<br>macOS<br>本地自托管<br>远程VPS | ⭐ | 237 |
| [SakuraByteCore/codexmate](https://github.com/SakuraByteCore/codexmate) | 本地AI编码代理的统一控制面板"Codex Mate",提供Provider管理、会话浏览、用量分析、技能市场、任务队列等一站式管理功能. 核心定位"Zero cloud, local-first control plane",支持在Codex、Claude Code、OpenClaw、Gemini CLI等多个Agent之间切换Provider/模型,实时监控配置与状态,跨工具统一列出/过滤/导出会话,可视化消息趋势和Top项目. 还提供DAG基础任务队列、OpenAI Bridge、Prompt模板、MCP集成等. 38个Releases. | macOS<br>Linux<br>Windows | ⭐ | 186 |
| [paulrobello/claude-office](https://github.com/paulrobello/claude-office) | 实时像素艺术办公室模拟Claude Office Visualizer,将Claude Code操作可视化. 一个"老板"角色(主Claude Agent)管理工作、派遣"员工"Agent(子代理)、在动画办公室环境中编排任务. 提供12种白板模式(Todo列表、远程工作者、工具使用饼图、组织架构图等),多楼层建筑导航,后台任务追踪,上下文窗口追踪,城市天际线(实时昼夜循环),Git状态面板等. | Linux<br>macOS<br>Windows | ⭐ | 398 |
| [AgentSight](https://github.com/eunomia-bpf/agentsight) | 基于 eBPF 的零 SDK 系统级 AI Agent 追踪与监控工具, 无需代码修改即可从外部观察任意 Agent CLI, 捕获进程树、文件操作、网络活动、LLM 流量(prompt/response/model/token), 提供实时 top 模式和 Web 可视化 | Linux<br>macOS | ⭐⭐ | 455 |
| [Agentinel](https://github.com/0x0funky/Agentinel) | 本地资源哨兵, 监控 AI Agent CLI(Claude Code、Codex、MCP servers)的 RAM、进程与磁盘使用, 标记泄漏/僵尸/失控缓存, 提出需用户确认的 AI 清理方案 | Windows<br>macOS | ⭐ | 35 |


#### 4.2.1.2 仪表盘
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [FlorianBruniaux/ccboard](https://github.com/FlorianBruniaux/ccboard) | 一个开源的 TUI/Web 仪表盘, 用于 Claude Code 会话监控、成本跟踪和配置管理. 核心功能包括 11 个交互式标签页(仪表盘、会话、配置、钩子、代理、成本、历史、MCP、分析、活动、搜索)、实时监控、SQLite 缓存(89x 启动速度提升)、跨平台支持和零配置. 技术栈: Rust、Ratatui、Axum、Leptos WASM. | Claude Code | ⭐ | 50 |
| [Arindam200/cc-lens](https://github.com/Arindam200/cc-lens) | 实时监控仪表盘, 用于 Claude Code 分析. 直接从 ~/.claude/ 读取数据, 无云服务, 无遥测, 仅使用本地数据. 提供令牌使用情况、项目活动分布、成本分析、会话回放等功能. 可通过 npx cc-lens 快速启动. 使用场景: 监控 Claude Code 使用情况、分析成本、查看项目活动模式、管理会话历史和内存文件. | Claude Code | ⭐ | 290 |
| [joeynyc/hermes-hudui](https://github.com/joeynyc/hermes-hudui) | 基于浏览器的 Hermes Agent 监控仪表盘, 提供实时认知状态可视化. 核心功能包括: 身份监控(标识、运行时间、脑容量)、知识统计(对话、消息、行动、技能)、记忆系统(容量条形图、用户档案)、服务健康(API密钥、服务状态)、学习进度(最近技能)、工作状态(活跃项目)、定时任务、思维模式(工具使用梯度图)、活动节奏(每日火花图)、成长变化(快照差异)、成本估算(按模型USD). 技术栈: React + Vite + TypeScript + SWR (前端), FastAPI + WebSocket (后端). 特点: 实时WebSocket更新、智能缓存、4种主题、键盘快捷键、独立运行. 适用于 Hermes Agent 用户监控、AI代理调试、成本跟踪、团队协作等场景 | Hermes Agent | ⭐ | 463 |
| [xaspx/hermes-control-interface](https://github.com/xaspx/hermes-control-interface) | 自托管的Web仪表盘, 用于Hermes AI代理堆栈. 提供基于浏览器的终端、文件浏览器、会话概览、cron管理、系统指标和代理状态面板——所有这些都在单一密码门后面. 核心功能包括7个页面(主页、代理管理、代理详情、使用分析、技能市场、维护、文件浏览器)、实时终端、通知系统、深色/浅色主题和多用户认证. | Hermes Agent | ⭐⭐ | 235 |
| [hesamsheikh/octogent](https://github.com/hesamsheikh/octogent) | 大神 Hesam Sheikh, 改造 Claude Code 成多 Agent 系统八爪鱼, 专为 Claude Code 打造的多 Agent 协作框架, 通过多 Agent 架构 + 可视化监控的组合, 提供一个 Claude Code 的编排仪表板, 用于管理上下文、自动化和开发者思维空间. 核心功能包括创建 tentacles (上下文层)、使用 todo.md 作为执行表面、运行多个 Claude Code 终端、生成子代理、支持代理间消息传递、将上下文保存在文件中, 以及提供本地 API 和 UI. 技术栈: TypeScript 86.7%, CSS 12.4%. 要求: Node.js 22+, claude, git, gh, curl. | Claude Code | ⭐ | 604 |
| [EKKOLearnAI/hermes-web-ui](https://github.com/EKKOLearnAI/hermes-web-ui) | 一个全功能的 Web 仪表盘, 用于 Hermes Agent, 管理 AI 聊天会话、监控使用情况和成本、配置平台渠道、调度定时任务、浏览技能等. 核心功能包括: AI 聊天(实时流式传输、多会话管理、Markdown 渲染、工具调用详情展开、文件上传支持、全局模型选择器)、平台渠道(8 个平台的统一配置、凭证管理、频道行为设置)、使用分析(总令牌使用情况细分、会话计数、估计成本跟踪、模型使用分布图表、30 天每日趋势)、定时任务(创建、编辑、暂停、恢复、删除 cron 作业)、模型管理(从凭证池自动发现模型、添加自定义 OpenAI 兼容提供商)、技能和内存(浏览和搜索已安装的技能、查看技能详情)、日志(查看代理/网关/错误日志、按日志级别过滤)、设置(显示、代理、内存、会话重置、隐私、API 服务器配置)、Web 终端(集成终端、多会话支持、实时键盘输入和 PTY 输出流). | Hermes Agent | ⭐⭐ | 5,217 |
| [ai-genius-automations/octoally](https://github.com/ai-genius-automations/octoally) | 为 Claude Code 提供的本地优先编排仪表盘, 支持多智能体蜂巢思维会话、单智能体工作流和交互式终端, 提供实时流式输出的美观 Web UI. 主要功能包括: 活动会话网格、蜂巢思维会话、智能体会话、交互式终端、内置 Web 浏览器、Git 源代码控制、文件浏览器、会话持久性、实时流式传输、多项目支持、语音听写和桌面应用. 技术栈: 前端(React 19, Vite, Tailwind CSS 4)、后端(Fastify, TypeScript, SQLite)、桌面应用(Electron)、会话管理(tmux, Claude Code + RuFlo). 适用于多智能体并行开发、AI 编码会话管理、项目管理、Git 操作等场景. | Claude Code/RuFlo | ⭐ | 80 |
| [f/agentlytics](https://github.com/f/agentlytics) | 为 AI 编码代理提供的综合分析仪表盘, 支持 Cursor、Windsurf、Claude Code、VS Code Copilot、Zed、Antigravity、OpenCode、Command Code 等 16 种编辑器. 核心功能包括: 统一仪表盘(KPI、活动热图、编辑器分解、编码 streak、令牌经济)、会话管理(搜索、过滤、语法高亮)、成本估算(按模型、编辑器、项目、月份分解)、项目级分析、深度分析(工具频率热图、模型分布)、编辑器比较、订阅管理、团队协作(Relay 功能). 技术栈: JavaScript 95.3%、TypeScript 4.2%, 支持 Node.js 和 Deno(沙箱模式). 特点: 本地优先, 数据不离开本地机器, 支持团队会话共享. | 多 Agent 支持 | ⭐⭐ | 478 |
| [tugcantopaloglu/openclaw-dashboard](https://github.com/tugcantopaloglu/openclaw-dashboard) | 为 OpenClaw AI 代理提供的安全、实时监控仪表盘, 支持身份验证、TOTP 双因素认证、成本跟踪、实时消息流、内存文件浏览器等功能. 核心功能包括: 会话管理、速率限制监控、成本分析、实时消息流、内存文件查看器、文件管理器、系统健康监控、服务控制、日志查看器、Cron管理、Tailscale集成、活动热图、主题切换、键盘快捷键、移动响应式、浏览器通知、时间线视图、Git活动跟踪、Claude和Gemini使用跟踪、系统安全仪表板、配置编辑器、Docker管理、通知中心. | OpenClaw | ⭐⭐ | 655 |
| [opsrobot-ai/opsrobot](https://github.com/opsrobot-ai/opsrobot) | OpenClaw 可观测性平台 - 专为 AI Agent(数字员工)设计的企业级可观测性管理平台. 技术栈: React 18 + Node.js + Apache Doris(OLAP) + Vector + OpenTelemetry(OTel) + Docker Compose. 双服务器架构(认证服务器8000端口 + ADK服务器8001端口). 核心能力矩阵包括全天候观测(会话溯源/实时监控/实例监控/日志搜索)、风险感知(安全审计/权限管控/风暴拦截)、可管理成本(Token消耗看板/成本分析/ROI报表/数字员工画像). 数据采集通过Vector监听sessions.json/*.jsonl日志文件, OTel协议采集Traces/Metrics/Logs. 支持OTel标准化、eBPF增强、OLAP架构和轻量化设计. 适用于IT运维、CIO安全团队、CEO/CFO成本核算和开发团队性能调优. 需配置OpenClaw diagnostics-otel插件启用数据采集. 在线Demo: https://opsrobot-demo.aishu.cn:3000/. | OpenClaw | ⭐ | 129 |
| [antiv/mate](https://github.com/antiv/mate) | MATE (Multi-Agent Tree Engine) - AI Agent 的指挥中心, 生产级多智能体编排引擎构建在 Google ADK 之上. 技术栈: Python 3.8+ + FastAPI + Google ADK + LiteLLM(50+ LLM提供商) + SQLAlchemy + OAuth 2.0 + MCP协议 + Prometheus + OpenTelemetry + React Flow + Docker. 双服务器架构(认证服务器 + ADK服务器). 核心功能包括 The Studio(无代码构建器/即时配置/自构建Agent)、The Control Room(RBAC per Agent/成本透明化/防护栏机制)、The Lab(回归测试/评估框架)、Work Room(内置聊天界面)、嵌入式聊天组件(一行代码部署)和 MCP 集成. 支持多云切换(Gemini/GPT-4o/Ollama等)、A2A协议、审计日志(EU AI Act合规). 适用于企业级多Agent系统、快速原型迭代、多团队协作、客服支持、AI产品化. | Google ADK<br>多平台(LiteLLM支持50+) | ⭐ | 58 |
| [komal-SkyNET/claude-skill-homeassistant](https://github.com/komal-SkyNET/claude-skill-homeassistant) | 为 Claude Code 提供专业的 Home Assistant 配置管理能力的技能. 技术栈: Claude Code Skills Framework + SSH + hass-cli + Git工作流 + SCP快速部署. 核心功能包括配置管理核心能力(部署工作流/智能重载策略/配置验证/远程CLI访问)、自动化开发工作流(完整的验证协议/日志分析/迭代修复)、Lovelace 仪表板开发(平板优化/卡片类型/模板模式/陷阱解决). 部署决策树: Git工作流(最终版本) vs SCP工作流(快速迭代). 智能Reload vs Restart判断: automations/scripts/scenes/templates可重载(快速), Min/Max传感器/新集成配置/核心配置需要重启. 提供 Jinja2 模板库和常用命令速查. 适用于 DevOps配置管理、仪表板开发、模板开发和故障排查. | Claude Code | ⭐ | 403 |
| [BradGroux/veritas-kanban](https://github.com/BradGroux/veritas-kanban) | Veritas Kanban - 本地优先的任务管理和 AI 智能体编排平台, "AI 智能体工作的可视化指挥中心". 技术栈: React 19 + Vite 7.3 + Express 5.2 + TypeScript 6.0(严格模式) + Markdown文件存储 + YAML工作流 + pnpm monorepo + Playwright + Vitest. pnpm monorepo结构: web/ + server/ + shared/ + cli/ + mcp/ + tasks/ + .veritas-kanban/. 核心功能包括 AI智能体编排(智能体管理/Squad Chat/智能体治理v4.0:策略引擎/决策审计/行为漂移检测)、工作流引擎(YAML定义多步骤管道/顺序/并行/门控审批)、任务智能管理(依赖图/崩溃恢复/观察记忆/时间跟踪)、Git原生开发(工作树管理/代码审查/PR管理/Issues同步)、MCP服务器(33+工具/7类工具)、CLI工具(vk begin/done/list/show/create/update等)、可定制仪表盘(v4.0新增)和Prompt模板注册表(v4.0新增). 零基础设施设计: 无数据库/Redis/Docker(本地), Markdown存储, git备份. 支持 OpenClaw原生编排、MCP客户端(Claude Desktop/Cursor/Cline)、OpenAI Codex和平台无关REST API. 适用于开发者日常工作、团队协作、AI智能体研发. | OpenClaw<br>Claude Desktop<br>Cursor<br>Codex<br>多平台(REST API) | ⭐ | 694 |
| [Claude Code Agent View](https://code.claude.com/docs/en/agent-view) | 参见 [Agent view in Claude Code](https://claude.com/blog/agent-view-in-claude-code) | Claude Code | ⭐ | 暂未开源 |
| [icebear0828/token-ray](https://github.com/icebear0828/token-ray) | 本地AI Token、成本、设备用量仪表盘,监控Claude Code、Gemini CLI、Codex等工具使用,Go+React+Wails桌面应用,支持LAN多设备同步 | Claude Code<br>Gemini CLI<br>Codex<br>Antigravity CLI | ⭐ | 21 |
| [8bit64k/cronalytics](https://github.com/8bit64k/cronalytics) | Hermes Agent的Cron任务成本可观测性插件,将自动化任务支出可视化,基于on_session_end hook+SQLite fact DB+FastAPI REST API+React Dashboard | Hermes Agent | ⭐ | 69 |
| [microsoft/AI-Engineering-Coach](https://github.com/microsoft/AI-Engineering-Coach) | 分析AI编码助手使用习惯提供改进建议和学习路径,VS Code扩展本地解析session logs,包含45条反模式规则和练习评分系统 | VS Code Extension | ⭐ | 118 |
| [juliantanx/aiusage](https://github.com/juliantanx/aiusage) | 本地AI编码助手使用追踪仪表盘,统一追踪22种AI编码工具的Token使用量、费用和会话数据. 核心定位"No accounts. No telemetry. No cloud required.",数据默认保存在本地. 覆盖Claude Code、Codex、OpenCode、Cursor、Hermes等22种工具. 支持多机器同步(通过GitHub、S3或R2,完全可选). | 跨平台(支持22种AI编码工具) | ⭐ | 9 |
| [hereww/codextools](https://github.com/hereww/codextools) | Codex的独立桌面管理工具(Go+React),提供设置、启动、连接模式切换、UI增强、脚本管理、诊断和修复工作流. 核心定位为Codex的全生命周期管理面板,功能包括:①简单启动面——仅暴露普通用户需要的操作;②中继与API管理——支持官方登录、兼容API模式、协议切换;③UI增强控制;④脚本中心——安装/启用/禁用/更新/移除用户脚本;⑤恢复与诊断——内置日志、诊断输出、路径修复;⑥历史对话修复. 21个Releases. | Windows<br>macOS | ⭐ | 74 |
| [relaydeck/relaydeck](https://github.com/relaydeck/relaydeck) | 本地优先的CLI编码Agent集群操作系统("Orchestrate agents. Plug the world in."),提供多Agent并行编排、Agent间通信、远程控制和实时观测能力. 支持7种Harness(Claude Code、Codex、Cursor、OpenCode等),8种Model Provider,30+内置Plugin(vault、github、telegram等). 核心功能包括:durable peer-to-peer messaging、Telegram远程控制、Live PTY终端、HITL升级通道、Token/cost管控、文件事件监控. | Linux<br>macOS<br>Telegram远程控制 | ⭐ | 42 |


### 4.2.2 会话 Terminal(TUI/GUI)
-------

#### 4.2.2.1 Ghostty 系列
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [manaflow-ai/cmux](https://github.com/manaflow-ai/cmux) | 基于 Ghostty 的 macOS 终端, 具有垂直标签和 AI 编码代理通知, 支持通知环、通知面板、应用内浏览器、垂直 + 水平标签等功能, 原生 macOS 应用, 使用 Swift 和 AppKit 构建. | 多 Agent 支持 | ⭐⭐⭐ | 13,257 |
| [vaayne/mori](https://github.com/vaayne/mori) | 一款原生 macOS 工作区终端, 围绕项目和工作树组织, 由 tmux 和 libghostty 驱动. 类似于 cmux, 方便同时管理多个 worktree. superset 太慢, conductor 不是 macos 原生, cmux 太丑. | 多 Agent 支持 | ⭐ | 190 |
| [ghostty-org/ghostty](https://github.com/ghostty-org/ghostty) | 快速、原生、功能丰富的终端模拟器, 提供速度、功能和原生 UI 的平衡. 主要特点包括: 标准合规的终端模拟、竞争性性能(多渲染器架构, Linux 使用 OpenGL, macOS 使用 Metal)、基本可定制性(字体、背景颜色等)、丰富的窗口功能(多窗口、标签、窗格)、原生平台体验、跨平台 libghostty 库用于嵌入式终端. 技术栈: Zig(核心)、SwiftUI(macOS)、GTK(Linux)、Metal/OpenGL(渲染). 适用于作为现有终端模拟器的替代品、嵌入到其他应用程序中、需要高性能终端的开发环境、需要现代终端功能的 CLI 工具开发等场景 | 多平台支持 | ⭐ | 56,938 |
| [everettjf/liney](https://github.com/everettjf/liney) | 原生 macOS 终端工作区应用, 专为跨仓库、工作树、分支和分割窗格工作的开发者设计. 主要特点包括: 在侧边栏中管理多个仓库和工作树、重新打开相同的窗格布局、混合本地 shell、SSH 和代理支持的终端会话、基于键盘的工作流. 技术栈: AppKit、SwiftUI、Ghostty. 适用于需要管理多个代码库、频繁切换工作树、保持终端布局的 macOS 开发者. | macOS 原生 | ⭐ | 100 |
| [leeronzhang/termura](https://github.com/leeronzhang/termura) | 一款为 AI 编程工具(Claude Code、Codex、Aider、OpenCode、Gemini、Pi 等)深度用户打造的原生 macOS 终端. 主要特点包括: GPU 加速终端渲染(libghostty + Metal)、多会话管理与会话分支、AI Agent 集成(自动检测、状态追踪、Token 计数、风险检测)、编辑器级输入组件、双面板模式、Markdown 笔记集成、项目集成(Git 状态、文件树、语法高亮)、全文搜索、Visor 模式. 技术栈: SwiftUI + AppKit(UI)、libghostty(终端渲染)、GRDB(SQLite + FTS5 数据库)、Highlightr(语法高亮). 适用于需要与 AI 编程工具深度集成的 macOS 开发者、多会话管理需求、终端输出捕获为笔记、项目文件编辑与预览等场景. | macOS 原生 | ⭐ | 4 |
| [zxcvbnmzsedr/devhaven](https://github.com/zxcvbnmzsedr/devhaven) | 专为长期在终端工作的 macOS 开发者打造的一体化工作区应用. 主要特点包括: 智能项目管理(目录扫描自动发现 Git 项目、持久化导入、灵活过滤)、Git 可视化(提交热图、统计仪表板、分支和工作树视图)、原生终端工作区(多项目支持、标签和分割窗格、GhosttyKit 引擎驱动、会话持久化)、内置浏览器 Pane、拖拽功能(文件夹导入、文件路径拖入终端). 适用于需要管理多个 Git 项目、集成终端与 Git 可视化、持久化工作区会话的 macOS 开发者. | macOS 原生 | ⭐ | 61 |
| [muxy-app/muxy](https://github.com/muxy-app/muxy) | 一款 macOS 终端多路复用器, 使用 SwiftUI 和 libghostty 构建. 主要特点包括: 基于项目的工作流程(按项目组织终端, 持久工作区状态)、垂直标签(侧边栏标签条, 支持拖放重新排序、固定、重命名和中键关闭)、分割窗格(水平和垂直分割, 支持键盘导航和可调整大小的分隔符)、内置 VCS(简单轻量级的基本 git diff 和操作)、200+ 主题(内置主题选择器, 可浏览和搜索 Ghostty 主题)、可定制快捷键(40+ 可配置键盘快捷键, 带有冲突检测)、工作区持久性(每个项目的标签、分割和焦点状态都被保存和恢复)、终端内搜索(在终端输出中查找文本, 支持匹配导航)、拖放(重新排序标签和项目, 在窗格之间拖动标签以创建分割)、自动更新(通过 Sparkle 内置更新检查)、文本编辑器(原生轻量级文本编辑器, 支持大多数编程语言的代码高亮). | macOS 原生 | ⭐ | 120 |
| [thdxg/macterm](https://github.com/thdxg/macterm) | 一款基于 SwiftUI 和 libghostty 构建的 macOS 终端多路复用器. 主要特点包括: 无限多路复用与持久化、原生侧边栏与动态标签标题、可配置主题、字体和键盘映射(支持热重载)、快速终端、支持多个同步实例、CLI 交互(打开、删除和列出项目). | macOS 原生 | ⭐ | 55 |
| [ZimengXiong/winmux](https://github.com/ZimengXiong/winmux) | 基于 Aerospace 构建的 macOS 窗口管理器, 提供直观的窗口管理体验. 主要特点包括: 管理(平铺)模式和非管理模式、6个意图(悬停提示)区域方便移动窗口、标签组功能、侧边栏、Exposé功能、设置界面、应用程序启动快捷键. 技术栈: 基于 Aerospace, 最终目标是基于 Yabai. 适用于需要高效窗口组织的 macOS 用户, 特别是开发者. | macOS 原生 | ⭐ | 100+ |
| [Aniket-508/termcn](https://github.com/Aniket-508/termcn) | 为 React 开发的终端 UI 组件库, 零配置, 开箱即用. 主要特点包括: 主题感知(自动适应终端主题)、与 shadcn/ui 兼容、基于 Ink 提供强大的终端渲染、可组合性、包含图表和数据组件、AI 组件、导航组件. 技术栈: React, Ink, shadcn/ui. 适用于构建终端 UI 的 React 开发者, 特别是需要构建复杂终端应用的场景. | 多平台支持 | ⭐ | 50+ |
| [Franvy/gtab](https://github.com/Franvy/gtab) | 一个为 macOS 上的 Ghostty 终端设计的轻量级工作区管理器. 主要特点包括: 保存当前 Ghostty 窗口布局为命名工作区、通过快捷键快速重新打开、支持标签页、工作目录、标题和拆分窗格的保存与恢复、通过键盘优先的 TUI 或命令行直接启动工作区、新窗口自动对齐到当前 Ghostty 窗口位置和大小、支持重命名、删除和搜索工作区. 技术栈: Rust, AppleScript. 适用于需要在 Ghostty 中快速切换不同工作环境的 macOS 用户, 特别是开发者. | macOS 原生 | ⭐ | 100 |
| [10xChengTu/MUX0](https://github.com/10xChengTu/MUX0) | 基于libghostty构建的原生macOS终端, 提供工作区、标签和分割窗格管理, 以及实时AI代理状态显示. 主要特点包括: 工作区→标签→分割的层级组织、实时AI代理状态(Claude Code、OpenCode、Codex)、工作区侧边栏元数据(git分支、PR状态、通知)、美观主题、双语UI(英文/简体中文)、布局持久化、自动更新. 基于 libghostty 引擎和 Metal GPU 渲染. 适用于需要按项目组织终端会话、监控 AI 代理状态、多窗格并行工作的 macOS 开发者. | macOS 原生 | ⭐⭐⭐ | 148 |
| [sanghun0724/cmux-claude-skills](https://github.com/sanghun0724/cmux-claude-skills) | cmux 终端自动化技能, 为 Claude Code 提供工作区布局设置、表面自动分类、会话快照/恢复和 Markdown 实时预览功能 | macOS 原生 | ⭐ | 20 |
| [headless-terminal](https://github.com/montanaflynn/headless-terminal) | 一个无头终端工具(Puppeteer for terminal UIs), 用于驱动 vim、emacs、htop、nethack 等交互式 TUI 应用. 主要功能包括: 在后台会话中启动程序、发送按键、快照屏幕、从另一个 shell 实时观看.适用于 AI 代理编码、TUI 的 CI 测试、演示和文档生成、跟随调试等场景 | 多平台支持 | ⭐ | 70 |
| [nowledge-co/con-terminal](https://github.com/nowledge-co/con-terminal) | Nowledge 公司推出的原生终端模拟器, 定位为"带有内置 AI 功能的终端模拟器"(Native Terminal Emulator with a builtin AI Harness). 面向传统终端用户, 强调终端优先、AI 作为辅助, 保持 PTY 真实、shell 可见、agent 可问责. 核心功能: 原生 macOS 终端窗口/标签页/分屏、内置 AI harness 读取上下文并请求确认后执行操作、支持 SSH/tmux/编码 agent CLI 终端原生工作流、GPU 加速、开源免费. 使用场景: 远程服务器连接、会话管理、自动化脚本执行、需要在终端中集成轻量 AI 辅助的开发者工作流. 目前最佳支持 macOS, 可通过 Homebrew 或安装脚本在 Linux 等平台安装, Windows 支持开发中. 官网 [con.nowledge.co](https://con.nowledge.co). | macOS<br>Linux<br>SSH<br>tmux | ⭐ | 391 |
| [montanaflynn/headless-terminal](https://github.com/montanaflynn/headless-terminal) | headless-terminal(ht) - "Puppeteer for terminal UIs", 终端界面自动化控制工具. 技术栈: Go 1.26+(99.5%) + libghostty-vt(Zig 0.15.2静态链接) + CMake + cgo. 守护进程架构(CLI + Unix Socket + JSON协议). 核心命令: run/send/view/wait/watch/record/list/stop/kill/remove. Vim风格按键表示法(<CR>/<Esc>/<C-x>/<M-x>/<F1>-<F12>). 同步策略(Pacing/Duration/Text/Idle/Cursor/Change). 多格式输出. Agent Skill支持(Claude Code/Skills CLI/Codex/Cursor/Gemini). 渐进式披露(SKILL.md常驻 + 参考文档按需加载). 决策树指导防止Agent常见错误(在send后立即view). 适用于AI Agent编码自动化、CI/CD中TUI测试、演示和文档生成、实时调试监控. 支持macOS(Apple Silicon)和Linux(x86_64/arm64). | Claude Code<br>Codex<br>Cursor<br>Gemini<br>多平台(Skills) | ⭐ | 93 |
| [Ghostty Config](https://github.com/zerebos/ghostty-config) | Web 端 Ghostty 终端配置生成器, 通过可视化界面调整字体、颜色、光标等设置, 实时预览效果并一键导出配置文件, 适合希望快速定制终端又不熟悉配置文件语法的开发者使用. 基于 Bun/Svelte/TypeScript 构建, 3.7k Stars. | Ghostty 终端 | ⭐⭐⭐ | 3,670 |
| [Rig](https://github.com/backnotprop/rig) | macOS 平台的 Ghostty 终端辅助工具, 通过 AppleScript 和 Accessibility API 实现会话管理、窗口切换与自动布局, 支持本地服务器 URL 检测与一键跳转, 适合多项目开发者高效管理终端工作区. | macOS | ⭐ | 228 |
| [Prowl](https://github.com/onevcat/Prowl) | 原生 macOS AI 编程代理终端, 基于 libghostty 和 TCA 架构构建, 支持 Canvas 鸟瞰视图、Git Worktree 书架式管理、自定义快捷操作及程序化 CLI 控制, macOS 26.0+ 可用, 专为并行 AI Agent 工作流设计. | macOS | ⭐⭐ | 304 |
| [iAmCorey/kooky](https://github.com/iAmCorey/kooky) | AI编码体验极简现代终端,集成多种AI Agent于统一界面,Swift+SwiftUI+libghostty GPU加速,支持一键启动AI Agent和Agent活动状态实时指示 | Claude Code<br>Codex<br>Gemini CLI<br>OpenCode<br>Amp<br>Cursor CLI<br>Copilot CLI | ⭐ | 163 |
| [sanvibyfish/openowl-app](https://github.com/sanvibyfish/openowl-app) | macOS原生Git GUI+GPU加速终端+文件编辑器集成开发环境,Swift+SwiftUI+libghostty Metal渲染,支持Git变更管理和多标签代码编辑器 | 任何CLI工具(Claude Code/OpenCode/Codex等) | ⭐ | 55 |
| [scarce/axel](https://github.com/scarce/axel) | macOS原生多Agent编排应用(SwiftUI),核心架构基于tmux面板和Ghostty终端编排多Agent并行工作,配合git worktree实现每个Agent对应独立分支避免冲突. 提供实时权限审批Inbox、可复用Skills/Context加载、Automerge CRDT+Supabase跨设备同步. 技术栈:Swift 71.5%+Rust 14%+TypeScript 8.2%. Beta阶段. | macOS 14+ | ⭐ | 202 |
| [Franvy/gtab](https://github.com/Franvy/gtab) | Ghostty终端标签页布局保存与恢复工具(macOS专用),一键保存当前窗口布局(标签页、工作目录、分割面板)为命名工作区,后续一键恢复. 通过TUI(Cmd+G)键盘优先快速搜索/启动工作区,13个Releases(v1.7.0). | macOS only(依赖Ghostty) | ⭐ | 99 |
| [Conductor](https://github.com/zhengzizhe/conductor) | macOS 多 Agent 终端工作台, 同时跑 Codex、Claude Code 和普通 shell, 真实终端 pane(libghostty)、工作区侧栏、会话续聊、任务队列、待处理状态、Token 用量统计、工具面板、CLI/Socket 自动化控制 | macOS(依赖Ghostty) | ⭐ | 140 |
| [Boo](https://github.com/coder/boo) | 基于 libghostty VT 核心的 GNU screen 风格终端复用器(Zig), 会话断开后存活可重新连接, 全屏会话管理器, 基于 libghostty 的精确重绘保留样式/光标/滚动区域, 自动化/AI 友好: send/peek/wait 无需 TTY | macOS<br>Linux | ⭐⭐ | 646 |


#### 4.2.2.2 TMUX 系列
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [AnganSamadder/opentmux](https://github.com/AnganSamadder/opentmux) | OpenCode 插件, 提供智能 tmux 集成, 用于实时查看代理执行情况. 自动生成窗格、流式传输输出、管理终端工作区. 主要特点包括: 自动 tmux 窗格生成、实时流式传输、自动清理、可配置布局、多端口支持、智能包装器(自动检测是否在 tmux 中). 适用于实时查看多个代理执行情况、管理多个代理会话、自动管理 tmux 窗格等场景. | 多平台支持 | ⭐⭐ | 71 |
| [ataraxy-labs/opensessions](https://github.com/ataraxy-labs/opensessions) | 一个 tumux 插件, 基于 tmux 的侧边栏终端工具, 用于管理会话、代理和本地主机标签. 它集成到现有的 tmux 工作流中, 而不是替换它: 一个小面板用于会话切换、代理状态、仓库面包屑和快速跳回到正确的终端. 主要功能包括: 实时代理状态(支持 Amp、Claude Code、Codex 和 OpenCode)、每个线程的未读标记、会话上下文(分支、工作目录、线程名称和检测到的本地端口)、程序化元数据 API、快速会话切换、各种快捷键和主题切换. 技术栈: 后端(Bun)、前端(Solid)、集成(tmux 插件). 适用于管理多个 tmux 会话、监控 AI 代理状态、快速在不同会话间切换、查看会话上下文信息、通过 API 推送自定义状态和日志等场景. | Amp, Claude Code, Codex, OpenCode | ⭐ | 831 |
| [liamvinberg/opencode-tmux](https://github.com/liamvinberg/opencode-tmux) | OpenCode 的 tmux 集成插件, 自动注入 tmux 会话上下文并提供与 tmux 窗格交互的工具. 主要功能包括: 自动注入上下文(会话启动和压缩时注入当前 tmux 会话信息)、服务器检测(自动识别运行中的开发服务器)、错误高亮(读取日志时标记错误模式)、交互工具(读取日志、重启服务器、发送命令、列出会话). 支持多种服务器进程检测(JS/TS, Python, Container, Rust, Go, Ruby, Java 等)和错误模式检测. 技术上实现了优雅降级, 当 tmux 未安装时插件会静默禁用, 当不在 tmux 会话中时自动上下文会被禁用但工具仍然可用. 适用于在 tmux 环境中使用 OpenCode 进行开发、监控服务器状态、管理多个终端窗格等场景. | OpenCode | ⭐ | 0 |
| [pedropombeiro/opencode-plugins/tmux-indicator](https://github.com/pedropombeiro/opencode-plugins/tree/main/packages/tmux-indicator) | OpenCode 插件, 在代理等待用户输入(权限提示或问题)时设置 tmux 窗口选项(@opencode-waiting), 代理恢复时清除该选项. 工作原理: 当代理询问权限或提出问题时在当前 tmux 窗口设置 @opencode-waiting 1, 代理恢复工作或空闲时取消设置; 3秒启动宽限期防止插件初始化期间的误激活; 向窗格 TTY 写入 BEL 字符使 tmux 设置 window_bell_flag, 可使用 Prefix + M-n 跳转到下一个等待窗口; 在 tmux 状态行中使用该选项显示视觉指示器. 当 $TMUX 或 $TMUX_PANE 未设置时插件无操作. 推荐 tmux 设置: set -gw window-status-bell-style default、set -g bell-action none. 技术上实现了在代理状态变化时与 tmux 窗口状态的同步, 提供了直观的视觉指示和快速导航功能. 适用于在 tmux 环境中使用 OpenCode 时快速识别需要用户交互的会话、通过状态栏监控代理状态、使用快捷键快速切换到等待用户输入的窗口等场景. | OpenCode | ⭐ | 0 |
| [opencode-tmux.nvim](https://github.com/simonwinther/opencode-tmux.nvim) | Neovim 插件, 通过 tmux 面板与 OpenCode 交互, 替代嵌入式终端, 支持多种快捷键操作和上下文发送. | OpenCode | ⭐ | 2 |
| [tmux-team](https://github.com/wkh237/tmux-team) | 协调在 tmux 窗格中运行的 AI 代理(Claude、Codex、Gemini), 支持发送消息、等待响应、广播到所有代理等功能. | OpenCode | ⭐ | 3 |
| [claude-code-plus-plus](https://github.com/BlitzJB/claude-code-plus-plus) | 多窗格终端界面, 用于运行并行 Claude Code 代理, 支持 git worktree 隔离, 具有多会话管理、终端管理等功能. | Claude Code | ⭐ | 3 |
| [tmux-claude-status](https://github.com/xsmyile/tmux-claude-status) | 零依赖 shell 插件, 在 tmux 状态栏显示 Claude Code 实时活动, 支持查看所有窗格的工作状态. | Claude Code | ⭐ | 3 |
| [tmux-claude-usage](https://github.com/eljulians/tmux-claude-usage) | 在 tmux 状态栏显示 Claude Code 使用限制, 支持本地和精确模式, 具有多种显示格式和颜色编码功能. | Claude Code | ⭐ | 0 |
| [coders](https://github.com/jayphen/coders) | 在隔离的 tmux 会话中生成 AI 编码助手(Claude、Gemini、Codex、OpenCode), 支持可选的 git worktrees, 具有多工具支持、交互式会话等功能. | Claude Code | ⭐ | 1 |
| [tmux-claude-code](https://github.com/MaxGhenis/tmux-claude-code) | 管理 tmux 中的 Claude Code 会话, 支持通过关键字搜索过去的对话、在正确的目录中恢复会话、交互式浏览会话等功能. | Claude Code | ⭐ | 1 |
| [claude-tmux](https://github.com/nielsgroen/claude-tmux) | 终端用户界面, 用于管理 tmux 中的多个 Claude Code 会话, 提供会话概览、状态检测、快速切换、实时预览等功能. | Claude Code | ⭐ | 135 |
| [claude-session-manager](https://github.com/pablobfonseca/claude-session-manager) |监控和管理跨 tmux 的 Claude Code 会话, 检测运行 claude 二进制文件的窗格, 分析终端输出以确定状态, 并提供基于弹出窗口的 UI 进行快速导航. |  Claude Code | ⭐ | 0 |
| [termcn](https://github.com/Aniket-508/termcn) | 基于 Ink 的美观终端 UI 组件, 100% 免费, 零配置, 一键设置, 支持主题感知、shadcn/ui 兼容、可组合组件、图表数据、AI 组件和导航功能. | 终端 UI | ⭐ | 220 |
| [aque](https://github.com/can-can/aque) | 基于 tmux 的代理队列管理器, 让你坐在一个 "desk" 前, AI 代理会来找你, 支持多代理管理、统一仪表板、自动附加、空闲检测等功能. | Claude Code, aider, Code | ⭐ | 2 |
| [standardagents/dmux](https://github.com/standardagents/dmux) | 开发代理多路复用器, 用于在隔离的 git worktrees 中管理多个 AI 编码代理, 支持并行分支、开发和合并, 兼容多种代理(Claude Code、Codex、OpenCode、Gemini 等), 官网 [dmux.ai](https://dmux.ai) | 多 Agent 支持 | ⭐ | 1,337 |
| [wavyrai/tmux-ide](https://github.com/wavyrai/tmux-ide) | 将任意项目转换为基于 tmux 的终端 IDE, 通过简单的 ide.yml 配置文件实现开发环境自动化布局管理. 技术栈: TypeScript(99.2%) + Node.js/Bun + tmux >=3.0 + Hono + WebSocket/SSE + OpenTUI/Solid.js. Monorepo结构(cli/lib/daemon/orchestrator/command-center/widgets/schemas/templates/skill/dashboard). 核心功能包括智能检测、多窗格布局、会话管理、Command Center(REST API+SSE+WebSocket)、配置编辑器(交互式TUI). Agent Team协作功能: 5种角色、任务编排(Mission→Goal→Task层级)、自动分配、Git Worktree隔离、PR自动化、知识库和技能注入. Widget系统: explorer/tasks/warroom/costs/changes/preview/config. 5大预设模板: default/nextjs/vite/agent-team/agent-team-nextjs/python/go/convex/missions. 适用于单Agent开发、多Agent协作、Monorepo管理、Python/Go项目、任务驱动开发. 官网: tmux-ide.com. | Claude Code<br>Codex<br>多平台(AI CLI) | ⭐ | 456 |
| [Herdr](https://herdr.dev) | 在一个终端中监督多个编码代理的工具, 允许用户同时管理和监控多个 AI 编码代理的执行. 支持 moshi + herdr 组合, 实现代理的并行调度和状态追踪. 参见 [2026/05/17, 「herdr」终端里的 Agent 版 tmux: 让 Claude Code、Codex 等任务持续运行、随时接回](https://wefound.cc/p/2464.html). | 多 Agent 支持 | ⭐ | NA |
| [Worktrunk](https://github.com/max-sixty/worktrunk) | Rust 编写的 Git worktree 管理 CLI, 专为并行 AI Agent(Claude Code/Codex)工作流优化. 提供 switch/list/merge/remove 核心命令, 支持 Hooks 自动化、LLM 提交信息生成、构建缓存共享等高级功能, 让多 agent 并行开发像操作分支一样简单. 5k+ Stars, 跨平台支持. | 多 Agent 支持 | ⭐⭐⭐⭐ | 5,011 |


#### 4.2.2.3 聚合终端
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [supacode.sh](https://supacode.sh) | AI 编码代理管理工具, 提供多代理并行执行和监控能力. | 多 Agent 支持 | ⭐⭐⭐ | NA |
| [thisguymartin/grove](https://github.com/thisguymartin/grove) | AI 原生终端工作区, 为同时在多个 git 分支上工作的开发人员设计, 运行一个命令即可获得完全连接的 Zellij 会话, 每个 worktree 一个彩色编码的标签, 每个标签预加载 LazyGit、AI 代理和 shell. | Claude Code/Gemini/OpenCode | ⭐ | 61 |
| [thecommander.app](https://thecommander.app) | AI 编码代理管理工具, 提供多代理并行执行和监控能力. | 多 Agent 支持 | ⭐⭐⭐ | NA |
| [mux.coder.com](https://mux.coder.com) | 开发代理多路复用器, 用于管理多个 AI 编码代理. | 多 Agent 支持 | ⭐⭐⭐ | NA |
| [smithers.sh](https://smithers.sh/introduction) | TypeScript 框架, 用于使用 JSX 构建确定性、可恢复的 AI 工作流, 处理执行顺序、持久状态持久化、结构化输出验证和崩溃恢复. | 多 Agent 支持 | ⭐⭐⭐⭐ | NA |
| [zellij-org/zellij](https://github.com/zellij-org/zellij) | 面向开发人员、运维人员和终端爱好者的工作区, 是一个终端多路复用器. 主要特点包括: 开箱即用的良好体验、深度可定制性、通过布局实现个人自动化、真正的多人协作、独特的 UX 功能(如浮动和堆叠窗格)、插件系统(支持任何编译为 WebAssembly 的语言)、内置 Web 客户端(使终端成为可选). 技术栈: Rust. 适用于终端工作区管理、多路复用终端会话、多人协作开发、定制化终端环境等场景 | 多平台支持 | ⭐⭐⭐ | 31,197 |
| [batiai/batipanel](https://github.com/batiai/batipanel) | AI 驱动的终端工作区管理器, 一键设置完整开发环境, 包括 Claude Code、lazygit、btop、yazi 等工具, 支持 8 种布局和 8 种主题, 提供会话持久化和跨平台支持. 主要功能: 全功能安装、会话管理、多种布局选择、多主题支持、智能回退机制、跨平台兼容. 技术栈: tmux、Claude Code、lazygit、btop、yazi. 适用于开发环境快速搭建、多面板终端管理、AI 编码会话管理等场景 | 多平台支持 | ⭐ | 28 |
| [smux](https://github.com/ShawnPana/smux) | 一个一键式 tmux 设置工具, 提供终端自动化功能, 专为 AI 代理设计. 主要特点包括: Option 键绑定、鼠标支持、窗格标签、tmux-bridge CLI 用于跨窗格代理通信, 支持代理到代理的交互(如 Claude Code 可以与 Codex 交互). 技术栈: tmux. 适用于 AI 代理终端管理、多窗格终端操作、代理间通信等场景 | 多平台支持 | ⭐ | 1,220 |
| [GabrielTecuceanu/tsman](https://github.com/GabrielTecuceanu/tsman) | 一个用 Rust 构建的功能丰富的 tmux 会话管理器. 主要功能: 快速保存 / 恢复 / 删除 / 编辑 / 重新加载 tmux 会话, 支持可重用的窗口 / 窗格布局模板, 提供交互式 TUI 菜单管理会话和布局, 支持模糊查找, 提供 bash、zsh 和 fish 的 shell 补全. 技术栈: Rust、CLI、TUI、fuzzy-finding. 适用于开发者使用 tmux 管理多个终端会话, 需要快速保存和恢复会话状态, 或者在不同项目间切换时保持一致的窗口布局等场景 | 多平台支持 | ⭐ | 52 |
| [nyanko3141592/tmuxcc](https://github.com/nyanko3141592/tmuxcc) | AI Agent Dashboard for tmux - 监控和管理多个 AI 编码代理的 TUI 应用, 支持 Claude Code、OpenCode、Codex CLI 和 Gemini CLI. 主要功能包括: 多代理监控、实时状态显示、审批管理、批量操作、层次视图、子代理跟踪、上下文感知、窗格预览、焦点集成和可定制性. 适用于在 tmux 环境中管理多个 AI 编码代理、实时监控代理状态、快速处理审批请求等场景 | 多 Agent 支持 | ⭐ | 56 |
| [NekoApocalypse/Vibe99](https://github.com/NekoApocalypse/Vibe99) | 焦点优先的桌面终端工作区, 专为 AI 代理编码设计(专为一个终端需要全神贯注而其他几个终端只需外围可见的情况设计), 采用"焦点+周边感知"的不对称布局: 一个主窗格全尺寸显示, 其他窗格压缩为窄预览(界面保持一个面板可读, 其余部分压缩成狭窄的可见预览), 支持快速空间记忆和导航模式切换. 主要特点包括: 不对称终端布局、标签颜色编码、实时显示设置、捕获模式生成原型图、跨平台打包支持. 适用于同时监控多个 AI 编码代理、管理多终端开发任务、在活跃工作与上下文监控间快速切换等场景. Vibe99 这个名字是对 Tetris 99(俄罗斯方块 99)的致敬: 你专注于自己的棋盘, 同时还要跟踪周围的许多其他人. | 多平台支持 | ⭐ | 28 |
| [wterm](https://wterm.dev) | 网页终端模拟器, 核心使用 Zig 语言编写并编译为 WASM, 提供接近原生的性能. 主要特点包括: VT100/VT220/xterm 转义序列解析、DOM 渲染(支持本地文本选择、剪贴板、浏览器查找、屏幕阅读器)、脏行跟踪(仅重渲染被触摸的行)、主题支持、备用屏幕缓冲区、回滚历史、24位颜色、自动调整大小、WebSocket 传输等. 适用于网页终端应用、在线开发环境、浏览器中的终端体验等场景 | 多平台支持 | ⭐ | NA |
| [herdr](https://github.com/ogulcancelik/herdr) | 在一个终端中监督多个编码代理的工具, 允许用户同时管理和监控多个 AI 编码代理的执行. 适用于需要并行运行多个编码代理、统一管理代理输出和状态的场景. | 多 Agent 支持 | ⭐ | 369 |
| [OpenCompanyApp/kosmokrator](https://github.com/OpenCompanyApp/kosmokrator) | 神话主题的 AI 编码代理, 在终端中运行, 支持读取、写入、编辑文件, 搜索代码库, 执行 shell 命令, 生成并行子代理 | 多 Agent 支持 | ⭐⭐⭐ | 18 |
| [tw93/Kaku](https://github.com/tw93/Kaku) | 一个专为 AI 编程设计的快速、开箱即用的终端, 基于 WezTerm 深度定制. 特点: 零配置(JetBrains Mono 字体、macOS 字体渲染)、主题感知(跟随系统深色/浅色模式)、内置 zsh 插件生态、快速轻量(二进制体积小 40%、启动瞬间)、完整 WezTerm Lua API 兼容. 内置 AI 助手: 命令失败自动建议修复(Cmd+Shift+E 应用)、自然语言转命令(# &lt;描述&gt; + Enter)、AI 工具配置面板(支持 Claude Code、Codex、Gemini CLI、Copilot CLI、Kimi Code 等). 是三部曲之一(Kaku 写代码, Waza 练习惯, Kami 发文档). 技术栈: Rust、Lua. 适用于 macOS 终端 AI 编程工作流、快速开发环境等场景. | macOS 支持 | ⭐⭐⭐⭐ | 4,771 |
| [CoderLuii/HolyClaude](https://github.com/CoderLuii/HolyClaude) | 一个 Docker 容器, 一键配置完整的 AI 开发工作站. 包含: Claude Code、CloudCLI Web UI、无头浏览器(Chromium + Xvfb + Playwright)、7 个 AI CLI(Claude Code、Gemini CLI、OpenAI Codex、Cursor、TaskMaster AI、Junie、OpenCode)、50+ 开发工具(Node.js、Python、Git、数据库客户端等). 支持 Claude Max/Pro 订阅和 API 密钥, 无需额外付费. 核心功能: 容器化部署、数据持久化、权限管理(UID/GID 映射)、通知系统(Apprise 支持 100+ 服务)、s6-overlay 进程管理、多架构支持(AMD64 + ARM64). 提供 full 和 slim 两种镜像变体. 技术栈: Docker、s6-overlay、CloudCLI. 适用于快速搭建 AI 编码环境、NAS 部署、远程开发等场景. | Docker 容器支持 | ⭐⭐⭐⭐ | 2,121 |
| [NeuralNomadsAI/CodeNomad](https://github.com/NeuralNomadsAI/CodeNomad) | AI 编程驾驶舱, 将 OpenCode 从终端工具转化为高端桌面工作区. 提供多实例工作区、远程访问(SSH/VPN)、会话管理、语音输入、Git Worktree、侧边栏工具集成、命令面板、文件系统浏览器、认证安全、主题切换和国际化等功能. 技术栈采用 TypeScript(88.5%)+CSS+Rust, SolidJS 前端, Electron/Tauri 桌面壳, Monorepo 架构. 支持 macOS/Windows/Linux 桌面端及浏览器 Server 模式, 适用于长时间 AI 编程会话、远程开发、多项目并行管理场景. | OpenCode<br>macOS<br>Windows<br>Linux | ⭐⭐ | 1,441 |
| [ModernProgrammer/Termini](https://github.com/ModernProgrammer/Termini) | macOS菜单栏极简终端即开即用不打断工作流,Swift+SwiftUI+SwiftTerm,支持多标签会话和6种内置主题 | 任何CLI工具 | ⭐ | 33 |
| [thisguymartin/grove](https://github.com/thisguymartin/grove) | AI原生终端工作空间,一键为每个git worktree生成Zellij布局(LazyGit+AI Agent+工作台),Shell脚本+Zellij+LazyGit,三栏布局设计 | Claude Code<br>Gemini CLI<br>OpenCode<br>Codex CLI | ⭐ | 70 |
| [leodavinci1/kanbots](https://github.com/leodavinci1/kanbots) | 看板驱动的多Agent并行调度器,可同时运行11种Agent CLI(Claude Code、Codex、Gemini、Cursor等). 核心理念"Drop a folder. Get a board. Dispatch agents on every card",每个Agent在独立worktree中运行. 提供五列看板(Backlog→Done)+Inbox、拖拽管理、Autopilot模式(feature-dev多角色并行+qa自动检查修复)、决策交互、Sentry错误导入、MCP集成、分支预览/Promote. | macOS<br>Linux<br>Windows(Electron) | ⭐ | 480 |
| [ansxuman/Clauge](https://github.com/ansxuman/Clauge) | "One window. Every dev tool."——集成所有开发工具的单窗口应用,每个模式配备专属AI,数据本地存储. 基于Tauri v2(Rust)+SvelteKit,提供7个模式:①Agent模式——并行运行coding agents;②Workspace模式——看板+笔记;③REST模式——API客户端;④SQL模式——多引擎SQL编辑器;⑤NoSQL模式——MongoDB+Redis;⑥SSH模式——带AI的终端;⑦Explorer模式——统一文件浏览器. 内置45+ MCP工具. | Windows<br>macOS<br>Linux(Tauri v2) | ⭐ | 703 |
| [NazzarenoGiannelli/tuiboard](https://github.com/NazzarenoGiannelli/tuiboard) | 终端纯Markdown看板,可选Today/Tomorrow日计划、24小时议程+日历、以及实时Claude Code Agent视图. 四大Zone:①board(kanban看板);②planner(日计划);③agenda(24小时时间线+日历叠加);④agents(实时查看Claude Code会话状态). 支持Obsidian vault集成、vim风格hjkl导航. | Linux<br>macOS<br>Windows | ⭐ | 63 |
| [XuYa Terminal](https://github.com/xuya-dev/XuYa-Terminal) | 面向 AI Agent 工程师的原生终端工作台(Tauri v2+React 19+Rust), 内置30+模型智能体、CodeMirror 代码编辑器、Git集成面板、Claude Code/Codex/OpenCode 快捷启动、AI 配置中心、额度查询、多标签分屏、10+主题 | Windows<br>macOS<br>Linux | ⭐ | 26 |
| [Warp](https://github.com/warpdotdev/warp) | 内置编码 Agent(Oz)的 Agentic 开发环境, 支持 Issue→Spec→PR 自动化工作流, 也支持接入外部 CLI Agent(Claude Code、Codex、Gemini CLI), Rust 高性能终端, Wasm 扩展 | macOS<br>Linux<br>Windows | ⭐⭐⭐⭐⭐ | 61,907 |
| [Otty](https://otty.sh) | [2026/06/20, 老鬼 @laogui, Typora 团队新作 Otty: 我终于找到心仪的轻量终端了！](https://x.com/laogui/status/2068166479330332925) | Linux | ⭐ | 暂不开源 |


### 4.2.3 聚合桌面(客户端)
-------

#### 4.2.3.1 桌面 GUI
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [Superconductor](https://super.engineering) | Agent 聚合软件, 管理和运行多个 AI 编程代理. 定位为 "Parallel by default. Custom by design." 的下一代开发工具. 支持在一个软件里面启动比如 Claude Code、Codex、Gemini CLI 等其他编码 Agent CLI 工具. 完全用 Rust 写的, 目前只有 MacOS 版本. 并行运行无限数量 AI 代理(Claude Code/Codex/Gemini CLI/OpenCode/Cursor Agent 等)、隔离 git worktrees、多布局面板、画中画窗口、主题自定义、内置终端复用器、Git 工作流集成(提交/推送/创建 PR). 使用场景: 并行运行多个 AI 编程代理开发任务、跨仓库协调工作区、管理分支代码审查和 PR 状态、自定义命令自动化脚本、高性能原生开发环境. | Claude Code、Codex、Gemini CLI、OpenCode | 未开源 |
| [desktop-cc-gui](https://github.com/zhukunpenglinyutong/desktop-cc-gui) | 为专业开发者设计的 Cursor 替代方案, 专注于开发者体验, 目标是构建 100% 开源和透明的下一代 VibeCoding 编辑器, 基于 CodexMonitor 构建. [官网](https://www.mossx.ai) | Claude Code、Codex CLI、OpenCode CLI、Gemini CLI | ⭐ | 2,511 |
| [collaborator-ai/collab-public](https://github.com/collaborator-ai/collab-public) | 协作者是一个端到端的代理开发环境. 终端、上下文文件和运行中的代码——全部集中在无限画布上. 没有上下文切换, 没有找标签. 只有你的经纪人和你的工作, 并肩而立. | 多 Agent 支持 | ⭐ | 2,301 |
| [superset-sh/superset](https://github.com/superset-sh/superset) | 涡轮终端, 允许运行任何 CLI 编码代理, 同时运行多个代理而不会有上下文切换开销, 每个任务在自己的 git worktree 中隔离, 内置差异查看器和编辑器. | 多 Agent 支持 | ⭐⭐ | 9,108 |
| [conductor.build](https://conductor.build) | 用于创建并行 Codex 和 Claude Code 智能体的工具, 在隔离的工作区中运行. 主要功能包括: 添加仓库(Conductor 克隆并在 Mac 上工作)、部署智能体(每个 Claude Code 获得隔离工作区)、管理(查看谁在工作、需要注意什么、审查代码). 技术栈: 基于 git worktree, 支持 Claude Code 和 Codex. 适用于多智能体并行开发、代码审查、团队协作等场景 | Codex<br>Claude Code | ⭐⭐ | NA |
| [paperclipai/paperclip](https://github.com/paperclipai/paperclip) | Node.js 服务器和 React UI, 编排一组 AI 代理来运行业务, 具有组织结构图、预算、治理、目标对齐和代理协调功能. 通过 [paperclipai/companies](https://github.com/paperclipai/companies) 可以组合公司. | 多 Agent 支持 | ⭐⭐⭐ | 50,123 |
| [stablyai/orca](https://github.com/stablyai/orca) | 面向 100 倍构建者的 AI 编排器, 支持在多个仓库中并行运行 Claude Code、Codex 或 OpenCode, 每个代理在独立的 git worktree 中运行, 所有状态集中跟踪. 主要特点包括: 工作树原生(每个功能有自己的 worktree, 无需 stash 或分支切换)、多代理终端(在标签页和窗格中并行运行多个 AI 代理)、内置源代码控制(查看 AI 生成的差异、快速编辑和提交)、GitHub 集成(PR、问题和 Actions 检查自动链接到每个 worktree)、通知系统(代理完成或需要关注时通知). 新增功能: 每个工作树的浏览器和设计模式(内置浏览器预览应用, 点击 UI 元素直接放入 AI 聊天上下文)、Orca CLI(从终端进行代理编排). 官网 [onorca](https://www.onorca.dev) | Claude Code/Codex/OpenCode | ⭐⭐⭐ | 624 |
| [OpenChamber](https://github.com/openchamber/openchamber) | 为 OpenCode AI 代理提供跨设备的桌面和 Web 界面, 支持分支化聊天时间线、多代理运行、Git 工作流集成、语音模式等功能, 可在桌面、浏览器和 VS Code 中使用. | OpenCode | ⭐ | 3169 |
| [hanshuaikang/nezha](https://github.com/hanshuaikang/nezha) | 一个面向 Vibe Coding 的 Agent-First 桌面应用, 支持在多个项目间并行运行 Claude Code 和 Codex 代理, 具有多项目工作区、任务生命周期可视化、原生 Git 集成、轻量级代码编辑器、使用分析等功能. | Claude Code/Codex | ⭐⭐ | 1,039 |
| [ItsWendell/palot](https://github.com/ItsWendell/palot) | 为 OpenCode 提供多代理桌面 GUI, 支持管理编码会话、可视化差异和实时流. | OpenCode | ⭐ | 63 |
| [kcosr/assistant](https://github.com/kcosr/assistant) | 基于面板的个人AI助手, 具有插件架构, 支持多代理CLI集成(Claude Code、Codex、Pi)和文本/语音界面. AI代理与用户共享包含笔记、列表和其他面板的工作区. 主要特点: 文本聊天与流式响应、语音输入/输出、CLI代理集成、面板插件系统、MCP工具集成、会话管理、多客户端支持、主题偏好设置. 技术栈: TypeScript 87.3%、CSS 6.0%、Java 4.1%、JavaScript 1.5%、HTML 0.8%、Rust 0.3%. | Claude Code/Codex/Pi | ⭐⭐ | 54 |
| [milisp/codexia](https://github.com/milisp/codexia) | 基于 Tauri v2 的应用, 结合 Codex CLI + Claude Code, 提供代理工作流、IDE 风格编辑器、无头 Web 服务器和提示记事本. 技术栈: 前端使用 React + TypeScript + Zustand + shadcn/ui, 后端使用 Tauri v2 + Rust, 包含 Axum Web 服务器用于远程控制. | Codex/Claude Code | ⭐⭐⭐ | 620 |
| [SoloTerm](https://soloterm.com) | 一个为AI代理和开发栈提供统一终端工作区的工具, 支持运行多个CLI代理(Claude Code、Codex、Gemini等), 与开发栈一起运行, 自动重启崩溃的进程, 提供MCP集成让AI代理能够查看日志和进程状态. 轻量级设计(25MB), 基于Tauri, 支持团队共享配置. | Claude Code/Codex/Gemini | ⭐ | 不开源 |
| [different-ai-studio/teamclaw](https://github.com/different-ai-studio/teamclaw) | 基于 OpenCode 的本地 AI 代理桌面应用, 提供多角色 AI 助手, 支持三栏布局、多渠道集成(Discord、飞书、邮件等)、团队协作(P2P和S3/OSS模式)、自动化任务、MCP支持和技能扩展系统. 技术栈: Tauri 2.0 (Rust)、React 19 + TypeScript、Tailwind CSS 4、Zustand、OpenCode. | 多AI代理 | ⭐ | 104 |
| [outworked/outworked](https://github.com/outworked/outworked) | Outworked 是一个桌面应用, 将 Claude 变成一个 AI 员工团队. 可以雇佣代理、赋予角色, 让它们写代码、浏览网页、发送消息、运行定时任务, 一切都在像素风格的办公室中可视化进行. 主要特点: 像素办公室(Phaser渲染)、多代理协作、自动编排、Claude Code完整工具访问、MCP服务器支持、消息通道(iMessage/Slack)、内置浏览器、隧道功能、技能系统、SQLite存储、资源包自定义. | Claude Code | ⭐ | 277 |
| [delibae/claude-prism](https://github.com/delibae/claude-prism) | ClaudePrism 是一个离线优先的科学写作工作区, 由 Claude 驱动. 它是 OpenAI Prism 的本地替代方案, 支持 LaTeX + Python + 100+ 科学技能, 在桌面本地运行. 主要特点: 本地存储和编译、Tauri 2 + Rust 构建、内置 uv Python 包管理、100+ 领域特定技能(生物信息学、化学信息学、ML 等)、模板库和项目向导、Git 历史版本控制、实时 PDF 预览(SyncTeX)、Zotero 集成. | Claude | ⭐⭐ | 1,308 |
| [minghinmatthewlam/pi-gui](https://github.com/minghinmatthewlam/pi-gui) | pi 会话的 Electron 桌面外壳, 为本地代理工作流构建. 该仓库为 @mariozechner/pi-coding-agent 提供桌面 UI 包装, 不是独立的编码代理运行时, 依赖上游 pi 包进行会话管理、模型/认证设置和代理执行. 主要功能包括: 在桌面外壳中打开本地工作区、列出和恢复与每个工作区关联的 pi 会话、创建新会话并通过 pi 运行时发送提示、持久化桌面 UI 状态(如选中的工作区、选中的会话和编辑器草稿). 技术栈: Electron、pnpm、TypeScript. 仓库结构: apps/desktop(Electron 应用和渲染器 UI)、packages/session-driver(共享会话驱动类型)、packages/catalogs(轻量级工作区/会话目录状态)、packages/pi-sdk-driver(从桌面应用到 @mariozechner/pi-coding-agent 的适配器). 适用于使用 pi 编码代理进行本地开发的场景. | Pi | ⭐ | 297 |
| [am-will/codex-app](https://github.com/am-will/codex-app) | Codex 桌面应用 Linux 打包和发布仓库. 该仓库跟踪 Codex 的 Linux 打包流程并发布可安装的发布工件. 使用 Electron Forge 工作区构建 Linux 发布包, 支持 .AppImage / .deb / .rpm 格式. 还包含 Arch Linux / Yay 的 AUR 元数据. | Codex | ⭐ | 100 |
| [0xranx/OpenContext](https://github.com/0xranx/OpenContext) | 为 AI 助手提供持久化记忆的轻量级个人上下文/知识库. 复用现有的编码代理 CLI (Codex/Claude/OpenCode), 添加 GUI + 内置技能/工具. 主要功能包括: oc CLI 管理全局上下文库、MCP Server 供代理调用、技能+斜杠命令、桌面应用和 Web UI. 解决了 AI 上下文在跨天/仓库/聊天时丢失的问题. 技术栈: TypeScript, Tauri, React. 适用于使用 AI 助手进行构建时需要持久化上下文和知识的开发者. | Codex/Claude/OpenCode | ⭐ | 557 |
| [daxaur/openpaw](https://github.com/daxaur/openpaw) | 将 Claude Code 转变为完整个人助手的工具. 安装 38 个技能覆盖邮件、日历、Spotify、智能家居、Slack、GitHub、Obsidian 等 8 个类别. 主要功能: 一键安装技能和所需 CLI 工具、给 Claude 赋予身份和持久化记忆、设置权限和安全钩子、Telegram 桥接、任务看板、智能调度、主题定制. 技术栈: CLI 工具集成. 适用于希望 Claude Code 能处理更多日常任务的用户. | Claude Code | ⭐ | 125 |
| [penso/arbor](https://github.com/penso/arbor) | Arbor 是一个基于 Rust + GPUI 构建的全原生智能编码桌面应用. 提供统一界面管理仓库、issue 驱动的工作树、嵌入式终端、进程管理、代码差异对比、PR 上下文、AI 编码代理活动, 以及一个共享守护进程同时支撑 Arbor 的 Web UI、CLI 和 MCP 服务器. 核心能力: 1) 多仓库工作树管理, 支持从 GitHub/GitLab issue 直接创建工作树; 2) 内置 PTY 终端, 支持 Procfile/arbor.toml 管理进程, 可调度任务并支持 Claude/Codex 触发; 3) 代码差异对比与 PR 评论功能; 4) ACP 代理聊天 (Claude、Codex、Pi、Gemini、OpenAI 兼容); 5) AI 代理状态实时可见; 6) 远程守护进程支持, 通过 arbor-httpd、arbor-cli、arbor-mcp 提供 API/CLI/MCP 接口; 7) 支持 SSH/Mosh 远程 outpost. 技术栈: Rust (GPUI 框架)、TypeScript (Web UI). 适用于需要并行编码会话、多仓库管理、AI 编码代理集成的开发者. | Claude/Codex/Pi/Gemini | ⭐ | 721 |
| [chencore/AionUi](https://github.com/chencore/AionUi) | 免费开源的 AI 代理 Cowork 平台, 提供内置 AI 代理(零配置即用)、多代理模式(支持 Claude Code、Codex、Qwen Code、Kiro、Hermes Agent 等 16+ CLI 代理自动检测与统一界面)、团队模式(多代理协作)、WebUI 远程访问、多平台集成(Telegram、飞书、钉钉、微信、企业微信)、定时任务(24/7 无人值守)、Office 文档生成(PPT 含 Morph 动画、Word、Excel)、20+ AI 平台支持(Gemini、OpenAI、Anthropic、AWS Bedrock、Ollama、本地模型等)、技能系统与自定义助手、10+ 格式预览面板、智能文件管理等功能. 技术栈: Electron、Vite、React、Bun. 是 Claude Cowork 的全模型、跨平台增强版. | 多AI代理(内置/Claude Code/Codex/Qwen Code/Gemini等) | ⭐⭐⭐ | 47 |
| [fathah/hermes-desktop](https://github.com/fathah/hermes-desktop) | Hermes Agent 原生桌面应用, 提供一站式 GUI 涵盖聊天、会话管理、Profile 切换、14 个工具集、内存系统、16 个消息网关(Telegram/Discord/Slack/WhatsApp 等)、定时任务调度等功能, 集成 Hermes Office(Claw3d) 视觉界面. 技术栈: Electron 39 + React 19 + TypeScript 5.9 + Tailwind CSS 4 + Vite 7 + better-sqlite3(FTS5 全文搜索) + i18next 国际化. 支持 OpenRouter/Anthropic/OpenAI/Google/xAI/Qwen/MiniMax/Hugging Face/Groq 等多提供商, 以及 LM Studio/Ollama/vLLM/llama.cpp 本地模型. | Hermes Agent<br>Electron<br>多模型提供商 | ⭐⭐ | 1,174 |
| [jyy1529/claude-desktop_win-zh_cn](https://github.com/jyy1529/claude-desktop_win-zh_cn) | Claude Desktop 中文资源与 Windows 补丁, 为 Windows 版 Claude Desktop 提供完整中文界面. 技术栈: Python 3(84.0%) + PowerShell(15.7%) + BAT(0.3%) + JSON翻译资源. 12727+条翻译键(桌面355 + 前端12326 + Statsig 46). 实现方式: 导出副本补丁(不修改官方安装目录) + 配置共享 + 备份机制 + 权限友好. 核心功能包括界面汉化(100%覆盖率)、字体自定义(预设字体/系统字体/本地ttf导入)、第三方推理支持(Gateway/cc-switch/newapi)、虚拟化支持(Cowork/VM)、解压版支持、卸载恢复. 补丁范围覆盖桌面壳层/前端界面/JS Chunk UI标签. 第三方推理配置通过Gateway接入cc-switch本地代理. 适用于日常中文用户、第三方推理接入、字体个性化、虚拟化开发. LINUX DO社区支持. | Claude Desktop<br>第三方推理(Gateway/cc-switch) | ⭐ | 256 |
| [lukilabs/craft-agents-oss](https://github.com/lukilabs/craft-agents-oss) | Craft Docs 开发的开源桌面应用, 采用"Agent Native"软件设计理念, 基于 Claude Agent SDK 和 Pi SDK 构建. 支持多会话管理、权限控制(Explore/Ask to Edit/Auto 三级模式)、技能系统、MCP 服务器集成、REST API(Google/Slack/Microsoft)连接、本地文件系统访问、自动化工作流(定时任务/事件触发)和远程服务器部署. 技术栈: Bun + Electron + React + shadcn/ui. 支持 Anthropic Claude、Google AI Studio、ChatGPT Plus(Codex OAuth)、GitHub Copilot、OpenAI API、OpenRouter、Ollama 等多 LLM 提供商, 覆盖 macOS/Linux/Windows 桌面及 Docker 部署. [官网](https://agents.craft.do) | Claude Agent SDK<br>Pi SDK<br>Electron<br>多模型提供商 | ⭐⭐⭐ | 5,841 |
| [qqqqqf-q/Arkloop](https://github.com/qqqqqf-q/Arkloop) | Arkloop - 干净、强大、属于你的 AI Agent 平台. 技术栈: Go(API/Gateway/Worker/Sandbox/Bridge/CLI) + React/TypeScript(Web/Console/Console-lite/Desktop + Electron) + PostgreSQL + Redis + SeaweedFS + OpenViking + pnpm/Turbo + Docker Compose. 多服务架构(API认证+Gateway代理+Worker执行+Sandbox隔离+Bridge桥接). 核心功能包括多模型路由(OpenAI/Anthropic/DeepSeek/OpenAI兼容API + 优先级路由 + 速率限制处理)、沙箱执行、持久记忆(系统约束/长期事实/会话上下文/向量记忆)、Prompt注入防护(语义级扫描)、渠道接入(Telegram集成)、自定义Persona(独立系统提示词/工具集定制/Lua脚本)、协议支持(MCP/ACP)、技能生态(ClawHub/OpenClaw兼容). 部署模式: 桌面应用(开箱即用)/CLI工具/Homebrew/自托管. MIT修改版Apache 2.0协议(禁止多租户SaaS + 品牌保护). 官网: arkloop.io. 适用于个人开发者、小团队、企业用户. | OpenAI<br>Anthropic<br>DeepSeek<br>多平台(OpenAI兼容) | ⭐ | 297 |
| [Howcode](https://github.com/IgorWarzocha/howcode) | 专为 Pi AI 设计的桌面编程应用, 集成工作区、终端、Git、Diff 审阅, 使用 React+Electron+Bun 构建, 支持语音输入和 Skills 管理, 强调 UX 而非文件编辑器, 提供卡片式项目管理和持久化终端历史. | Pi | ⭐ | 152 |
| [49Agents](https://github.com/49Agents/49Agents) | 开源 2D 智能体 IDE, 通过无限画布统一管理多个 AI agents 的原生 CLI、终端、Git 及文件, 支持跨机器编排和实时终端广播输入, 提供自托管架构和跨设备访问能力, 适合需要同时管理多个 AI 编程助手和分布式开发场景的开发者. | 多 Agent 支持 | ⭐ | 242 |
| [Codeg](https://github.com/xintaofei/codeg) | 企业级多智能体编码工作空间, 统一聚合 Claude Code、Codex、OpenCode 等本地 AI 代理会话, 支持可视化项目脚手架、并行 git worktree 开发、MCP/Skills 管理及 Telegram/飞书/微信聊天渠道集成, 可作为桌面应用、独立服务器或 Docker 容器部署. | 多 Agent 支持 | ⭐⭐ | 1,136 |
| [enz1m/enzim-coder](https://github.com/enz1m/enzim-coder) | Linux桌面应用整合AI编码线程、工作空间、Git上下文、文件浏览和Agent会话,Rust+GTK4+libadwaita+SQLite本地存储,支持持久化线程和多Profile会话 | Codex CLI<br>OpenCode CLI | ⭐ | 60 |
| [tonisives/clawtab](https://github.com/tonisives/clawtab) | Agent控制中心,创建和管理来自任何提供商的Agent组并通过Web/移动端远程监控控制,Rust+Tauri+TypeScript+xterm.js+tmux,支持定时任务和通知系统 | Claude Code<br>Codex<br>OpenCode | ⭐ | 31 |
| [RunMaestro/Maestro](https://github.com/RunMaestro/Maestro) | 跨平台桌面应用用于编排和管理AI agents队列实现多项目并行开发,TypeScript+Vite+Vitest,支持Git Worktrees并行开发、Auto Run自动化、Group Chat协调和远程控制 | Claude Code<br>OpenAI Codex<br>OpenCode<br>Factory Droid | ⭐⭐⭐ | 2,919 |
| [Core-Mate/OpenGUI](https://github.com/Core-Mate/OpenGUI) | 开源AI移动操作器让AI自动化操作真实Android手机,Kotlin Android客户端+TypeScript/NestJS后端,支持最长12小时任务运行和远程调度飞书/Telegram/Discord | Claude(Opus全角色)<br>Codex<br>Qwen 3.6 Plus<br>Doubao Pro | ⭐ | 131 |
| [OpenSource03/harnss](https://github.com/OpenSource03/harnss) | 跨平台桌面应用,为AI编码代理(Claude Code、Codex、ACP兼容代理)提供统一管理界面. 核心目标是在一个窗口中同时运行、管理和切换多个AI编码代理,不丢失上下文、会话或工具状态. 主要功能包括:多引擎并行会话、丰富的工具调用可视化(文件编辑词级diff、bash输出内联)、MCP服务器管理、Git集成(暂存、提交、推送、分支浏览、worktree管理)、内置终端与浏览器、项目工作空间、Agent Store、计划模式与三级权限控制、后台任务代理、图像附件与标注工具、语音输入、会话搜索与历史. 基于Agent Client Protocol(ACP)构建. | macOS<br>Windows<br>Linux(Electron) | ⭐ | 277 |
| [Razz19/Exort](https://github.com/Razz19/Exort) | 基于OpenCode的嵌入式开发桌面应用,为微控制器编程提供本地工作空间. 核心目标是让AI编码代理专门服务于嵌入式开发,提供从编写代码到编译上传再到串口监控的一体化工作流. AI编码代理(基于OpenCode)、项目管理器、板卡管理器(安装管理Arduino CLI板平台和核心)、编译与上传(自动和手动)、串口监视器、串口绘图器、Provider连接、本地历史. 支持Arduino/ESP32/RP2040/STM32等. | macOS<br>Windows<br>Linux(Electron) | ⭐ | 195 |
| [Hermes Desktop](hermes-agent.nousresearch.com/desktop) | Hermes Agent 的桌面版本, 提供本地 GUI 界面运行 Hermes AI 编码代理, 支持多会话管理、MCP集成和可视化工作流编排. | macOS<br>Windows<br>Linux | ⭐ | NA |
| [Wayland](https://github.com/FerroxLabs/wayland) | 本地优先桌面 AI 代理指挥中心, 一个面板驱动 Claude Code、Codex、Gemini、Qwen 等16种 CLI Agent, Cowork 协作+177个工作流+自组装多Agent团队+认知记忆系统(5分区×3层级)+MCP集成+25个远程渠道+Constitution规则治理+Rust核心引擎 | macOS<br>Windows<br>Linux | ⭐⭐ | 439 |
| [Hermes-CN Desktop](https://github.com/Eynzof/Hermes-CN-Desktop) | Hermes Agent 中文社区桌面客户端(Tauri v2+Rust+React), 一键安装, 内置 Hermes-CN-Core 中文社区修改版内核, 完整 Agent UI(聊天/MCP/Skills/Memory/Profiles/定时任务/LaTeX渲染), 覆盖主流中国云端模型+本地部署, 非商业免费 | Windows<br>macOS | ⭐⭐ | 477 |
| [Munder Difflin](https://github.com/chaitanyagiri/munder-difflin) | 本地多 Agent 蜂巢编排器, 真实终端运行 Claude Code/Antigravity/Codex, GOD 编排器自动路由裁决任务, 基于Git的身份/记忆/邮箱/黑板蜂巢层, Pixi.js 办公楼层可视化(角色走动/信封飞递), 任务看板+熔断器+成本遥测+Git Worktree隔离 | macOS<br>Linux<br>Windows | ⭐⭐ | 533 |
| [Ordinus](https://github.com/muratgur/ordinus) | 本地优先桌面应用, 组合 Codex/Claude/Gemini CLI 为 AI Agent 并编排成 DAG 调度工作流, 可视化 Workflow Designer, Workboard 实时观察, 连接 Google/WhatsApp/X/Linear 等账号(凭据本地加密), Telegram 远程访问, SQLite 存储无遥测 | macOS<br>Windows<br>Linux | ⭐ | 79 |
| [WeSight](https://github.com/freestylefly/wesight) | 桌面 AI Agent 工作台, 一键安装 Claude Code/Codex/OpenClaw/Hermes 等 Agent CLI, 可视化聊天/工具/文件/IM通道/技能, 飞书路由, AI Runtime Dashboard(引擎/模型/Token/TTFT/TPS), SkillHub技能市场, 桌面宠物+像素工作室 | macOS<br>Windows | ⭐⭐ | 676 |
| [Alma](https://alma.now) | 一款赏心悦目的桌面应用, 为您整合 AI 体验. 在 OpenAI、Anthropic、Google Gemini 及自定义服务之间无缝切换. 智能记忆跨会话保持上下文和偏好, 解决不同模型切换时记忆丢失问题. Markdown渲染+代码高亮+流式响应+Web搜索+工具调用 | macOS<br>Windows<br>Linux | ⭐ | 暂未开源 |
| [Pi Studio](https://github.com/shixin-guo/pi-studio) | Pi 编码代理的本地桌面 GUI, 完整 Markdown 渲染+流式响应+代码 diff 内联, 多 Agent 多会话并行, 项目工作区+Git分支显示, LAN QR码移动访问+PWA, 包管理器, 成本追踪仪表盘+模型趋势, 6套主题+毛玻璃效果 | macOS<br>Windows<br>Linux | ⭐ | 127 |
| [TOKENICODE](https://github.com/yiliqi78/TOKENICODE) | Claude Code 桌面客户端(Tauri 2+React 19+Tailwind CSS 4), 6个预设API提供商(Anthropic/DeepSeek/智谱/Qwen/Kimi/MiniMax)+自定义端点, 中国友好(Gitee镜像/代理/中文UI), SDK权限审批(4工作模式), 流式三阶段对话, Checkpoints回滚, Skills&MCP UI管理, 多主题×亮暗模式 | Windows<br>macOS<br>Linux | ⭐⭐ | 336 |
| [yorgai/ORG2](https://github.com/yorgai/ORG2) | 开源的 Cursor 风格 Agent IDE, 但专为可审查性、可追溯性和控制而构建, 而非仅仅是更快的编码. 核心理念是将 Agent 视为持久、可观察的组织内同事, 而非无状态、难以审查的助手. 关键特性包括: 可重放的执行轨迹(长期运行会话审计、审查和调试)、基于 Rust 的 Agent 运行时(使用现有 API 密钥和订阅)、跨会话记忆与跨 Agent 知识共享、资源感知执行(根据 CPU/RAM/人类注意力可用性调整)、Agent 驱动 GUI 端到端测试(监督式自我进化)、调度和自动启动会话(Agent 可过夜运行)、组织级对齐表面(问题/项目管理协调人类、Agent、目标和问责, WIP)和会话协作(自托管 Supabase, WIP). 技术栈: Rust + Tauri, 本地优先执行(磁盘占用 <100MB), 支持 10+ CLI. 适用于需要可审查、可追踪的 AI 编码工作流、团队协作和长期 Agent 运行的场景. | 多 Agent 支持 | ⭐ | 878 |


#### 4.2.3.2 Web GUI
-------

[2026/04/26, DeFi狙击手 | Bird🕊️, @bi_9527zx, Hermes Web UI我推荐用这个](https://x.com/bi_9527zx/status/2048374724590436565)

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [pingdotgg/t3code](https://github.com/pingdotgg/t3code) | 一个为编码代理(目前支持 Codex 和 Claude)提供的最小化 Web GUI, 支持通过命令行运行 (`npx t3`) 和桌面应用安装. | Codex/Claude | ⭐⭐⭐ | 10,097 |
| [dpcode](https://github.com/Emanuele-web04/dpcode) | 一个用于编码代理的最小化Web GUI, 目前支持Codex和Claude, 未来将支持更多AI模型 | TypeScript (98.1%) | 基于T3Code克隆定制, 提供简洁界面与AI编码代理交互, 支持命令行运行和桌面应用安装, 适用于开发者使用AI辅助编程的场景 | ⭐ | 215 |
| [maria-rcks/t1code](https://github.com/maria-rcks/t1code) | T1Code 是 T3Code 的终端版本, 为编码代理(Codex 和 Claude)提供界面. 主要功能包括: 终端 UI(TUI)、Web UI(React/Vite)、桌面应用(Electron)、Git 集成、终端访问、检查点和会话恢复、项目脚本管理、图片支持. | Codex/Claude | ⭐ | 463 |
| [opactorai/Claudable](https://github.com/opactorai/Claudable) | 开源 Web 应用构建器, 结合 Claude Code AI Agent 能力和 Lovable 简洁构建体验. 用户用自然语言描述需求, Claudable 实时生成代码并展示可工作的应用预览. 技术栈: Next.js + TypeScript + Tailwind CSS + shadcn/ui + Prisma + SQLite/Supabase + Vercel + Electron. 核心功能包括自然语言转代码、实时热重载预览、一键 Vercel 部署、Supabase 数据库集成、GitHub 版本控制、跨平台桌面应用. 支持 Claude Code、Codex CLI、Cursor CLI、Qwen Code、Z.AI GLM-4.6 等多 AI 编码 Agent. 适用于快速原型开发、产品迭代和跨平台应用构建. | Claude Code<br>Codex CLI<br>Cursor CLI<br>Qwen Code<br>Next.js | ⭐⭐⭐ | 3,944 |
| [outsourc-e/hermes-workspace](https://github.com/outsourc-e/hermes-workspace) | AI Agent 命令中心, 完整的 workspace 而非简单聊天界面, 集成 chat、files、memory、skills、terminal 等功能. v2 版本采用零分支策略直接基于 NousResearch/hermes-agent 构建. 技术栈: Node.js 22+ + TypeScript + Docker/Docker Compose, 支持 Hermes Agent 网关(:8642)和 Dashboard(:9119). 支持 Anthropic/OpenAI/OpenRouter/Google Gemini/Ollama/LM Studio/vLLM 等 LLM 提供商, 采用 PWA 跨平台安装, 支持 Tailscale 远程访问. Swarm 模式支持多 Agent 协作, 适用于本地 AI Agent 开发、家庭实验室、Docker 和远程服务器部署. | Hermes Agent<br>PWA<br>Docker<br>多模型提供商 | ⭐⭐ | 3,462 |
| [siteboon/claudecodeui](https://github.com/siteboon/claudecodeui) | CloudCLI(原名 Claude Code UI)开源 Web 界面/GUI, 为 Claude Code、Cursor CLI、Codex、Gemini CLI 提供跨设备(桌面/平板/手机)图形化操作体验. 前端 React + Vite + Tailwind CSS + TypeScript + CodeMirror 代码编辑, 支持 Docker 沙箱隔离、PM2 进程管理、MCP 服务器配置同步. 核心功能: 响应式 UI、交互式聊天、内置 Shell 终端、文件浏览器(语法高亮/实时编辑)、Git 可视化、多会话管理、可选 TaskMaster AI 任务规划. 支持 Claude/GPT/Gemini 多模型家族, 提供 npm 自托管、Docker 沙箱、CloudCLI Cloud 云托管三种部署方式. | Claude Code<br>Cursor CLI<br>Codex<br>Gemini CLI | ⭐⭐⭐ | 10,632 |
| [Emanuele-web04/dpcode](https://github.com/Emanuele-web04/dpcode) | DP Code - 为 AI 编码代理提供最小化 Web GUI, 统一管理多个 AI 编码助手. 技术栈: Bun/Node.js 24.10+ + TypeScript + Turbo(Monorepo) + React 19 + Vite 8 + Tailwind CSS 4 + Zustand + TanStack Router/Query + Base UI + xterm.js + react-markdown + Lexical 0.41 + @dnd-kit + Electron 40.6 + Flask + Supabase(PostgreSQL + 认证 + RLS) + PyGithub + Docker. Monorepo结构: apps/server + apps/web + apps/desktop + packages/contracts + packages/shared + packages/effect-acp. 核心功能包括多AI提供商支持、Web GUI界面(实时流式输出/会话管理/多项目支持)、桌面应用(跨平台/自动更新)、容器化执行环境(每个任务独立Docker容器). Git工作流自动化: 自动克隆/创建分支/生成diff和patch/提交代码/创建PR. 项目处于早期阶段, 不接受外部贡献. 适用于AI辅助编码、多模型对比、会话管理、项目隔离. 官网: dpcode.cc. | Codex<br>Claude Code<br>Gemini<br>OpenCode | ⭐ | 479 |
| [joeynyc/hermes-hudui](https://github.com/joeynyc/hermes-hudui) | 基于浏览器的 AI Agent 意识监控仪表盘, 专为 Hermes Agent(具有持久记忆的 AI Agent)设计. 以 Web UI 形式呈现, 提供与 TUI 版本相同数据和灵魂, 支持 macOS/Linux/WSL. 技术栈: Python + Node.js + WebSocket 实时数据更新. 提供 18 个功能标签页: 执行仪表盘、身份、记忆、技能、会话、Cron 任务、项目、健康诊断、成本分析、模型分析、模式校正、Sudo 治理、实时聊天、OAuth 提供商、Gateway 控制、插件管理等. 支持中英文双语切换, 内置 5 款主题(Neural Awakening/Hermes Teal/Blade Runner/fsociety/Anime)及可选 CRT 扫描线效果. 特色: Gateway 可视化(web search/图像生成/TTS/浏览器自动化路由状态)、成本分析(按模型统计 Token 和费用)、插件管理、键盘快捷键(1-9/0 切换标签/t 切换主题/Ctrl+K 命令面板). 与 hermes-hud(TUI 版本)共享同一数据目录(`~/.hermes/`), 可同时或独立使用. MIT 许可. | Hermes Agent<br>Python<br>Node.js<br>WebSocket | ⭐⭐ | 1,383 |
| [pi-kanban](https://github.com/NikiforovAll/pi-kanban) | Pi 编码代理的看板工作空间, 提供任务管理、状态追踪和可视化界面. 详见博客文章 [pi-kanban: A Workspace for the Pi Coding Agent](https://nikiforovall.blog/ai/productivity/2026/05/09/pi-kanban). | Pi | ⭐ | NA |
| [nesquena/hermes-webui](https://github.com/nesquena/hermes-webui) | Hermes Agent轻量级Web界面三面板布局,无框架无构建步骤,Python+JavaScript+原生HTML/CSS,支持多模型、语音输入、工作空间文件管理和会话管理 | Hermes Agent<br>多模型提供商(OpenAI/Anthropic/Google/DeepSeek等) | ⭐⭐⭐ | 7,811 |
| [tt-a1i/hive](https://github.com/tt-a1i/hive) | 浏览器内的本机多Agent协作工作台,让一群CLI编码代理(Claude Code、Codex、OpenCode、Gemini)在本地各自开工,通过Orchestrator编排器派活、归总进展,Worker各司其职. Hive不替换任何CLI,Agent仍是本机真实PTY进程,Hive只是它们外面的"团队shell". 主要功能:Orchestrator+Worker的真实PTY进程管理、基于Markdown的任务图(.hive/tasks.md)作为协调协议、team命令注入实现代理间通信、PTY后台保留与CLI原生session恢复. | macOS<br>Linux<br>Windows(Node.js 22+) | ⭐ | 273 |
| [pewdiepie-archdaemon/odysseus](https://github.com/pewdiepie-archdaemon/odysseus) | 自托管的AI工作空间,定位为ChatGPT和Claude UI体验的自托管版本,本地优先、隐私优先. 核心功能包括:Chat(与本地模型或API对话)、Agent(基于opencode的自主代理,支持MCP/Web/文件/Shell/Skills/记忆)、Cookbook(扫描硬件推荐模型)、Deep Research(多步研究)、Compare(多模型并排盲测)、Documents(AI辅助编辑)、Memory/Skills(ChromaDB+fastembed)、Email(IMAP/SMTP)、Notes & Tasks、Calendar(CalDAV)、移动端(PWA). | macOS<br>Linux<br>Windows(Docker或原生),移动端(PWA) | ⭐⭐⭐ | 34,041 |


#### 4.2.3.3 IDE 插件
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [VSmux](https://github.com/maddada/vsmux) | T3code & Agent CLIs 管理器 | 允许在不离开 IDE 的情况下管理所有 CLI 编码代理会话 | 远程访问、分割视图、通用搜索、会话组织、恢复会话、快速启动、会话分叉、睡眠模式、自定义 AI 配置文件、代理交接、自定义操作按钮、固定提示、集成浏览器、自动化 Git、变更监控、高级设置 | 适用于喜欢并行使用多个代理 CLI 进行编码的开发者, 不想被锁定到特定工具中的用户, 以及喜欢在自己喜欢的编辑器中查看更改的人 | ⭐ | 12 |

### 4.2.4 会话管理与迁移
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [lyston11/codex-session-toolkit](https://github.com/lyston11/codex-session-toolkit) | TUI 优先的 Codex 会话工具箱, 用于管理、迁移和同步 Codex AI 编程助手的会话数据. 技术栈: Python >=3.8(97.3%) + Shell(1.2%) + PowerShell(1.1%) + 无第三方运行时依赖. 分层架构: 入口层/编排层/业务层/存储层/表现层/界面层(TUI). 严格依赖方向控制(Store→Service→Application→Entrypoint). 核心功能包括 Session/Browse(会话浏览/搜索/导出/按项目筛选/批量导出)、Bundle/Transfer(Bundle传输/校验/导入/批量导入/项目路径映射)、Skills/Transfer(Skills迁移/导出/导入/删除/智能识别)、Repair/Maintenance(Desktop可见性修复/Provider迁移/归档会话管理/备份管理/清理旧副本/Dry-run支持)、GitHub/Sync(GitHub同步/代理配置/状态检查/Pull/Push). Bundle结构化存储(按machine/sessions/skills分类). Skills智能搬运(best-effort/strict/skip/overwrite四种模式). TUI交互设计(快捷键支持). 适用于跨设备迁移项目会话、同步自定义Skills、修复Desktop可见性、清理归档会话、找回导入覆盖前的会话. | Codex Desktop<br>Codex CLI | ⭐ | 37 |

### 4.2.5 会话画布
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [DeadWaveWave/opencove](https://github.com/DeadWaveWave/opencove) | 空间开发工作区, 将 AI 代理、终端、任务和笔记放在同一个无限 2D 画布上, 使工作的完整状态保持可见. 主要特点包括: 无限空间画布、为 CLI 代理构建、上下文保持可见、持久工作区、空间存档、丰富的媒体和智能布局、全局搜索和控制中心、工作区隔离等. 技术栈: Electron + React + TypeScript、@xyflow/react、xterm.js 和 node-pty、Vitest 和 Playwright. 适用于运行多个 Claude Code 或 Codex 会话、在一个共享工作区中保持任务计划、笔记和终端输出、切换项目而不丢失布局、上下文或执行历史等场景. 参见 [2026/04/06, 老鬼 @laogui, OpenCove 是另一个「无限画布 + AI Agent + 终端」产品](https://x.com/laogui/status/2041155253668831418) | 多 Agent 支持 | ⭐ | 1,046 |
| [hridaya423/conductor-tasks](https://github.com/hridaya423/conductor-tasks) | 一个智能任务管理助手, 将需求转化为可操作的任务, 生成实施计划, 跟踪进度并加速开发. 支持通过 MCP 集成到编辑器或作为独立 CLI 工具使用, 利用多个 LLM 来简化从规划到执行的开发过程. | 多 Agent 支持 | ⭐ | 75 |
| [dcosson/h2](https://github.com/dcosson/h2) | 一个代理运行器、消息传递和编排层, 用于 AI 编码代理. 它是一个三层系统: 1) 代理运行器: 启动、监控和管理 AI 编码代理, 支持后台运行、状态跟踪和权限管理; 2) 消息传递: 代理可以相互发现和通信, 用户可以通过 Telegram 机器人与它们通信; 3) 编排: 定义具有角色和指令的代理团队, 然后一起启动它们处理项目. 支持 Claude Max 和 ChatGPT Pro 计划, 无需 API 密钥. | 多 Agent 支持 | ⭐ | 114 |
| [conductor.build](https://www.conductor.build) | 创建并行的 Codex + Claude Code 代理, 在隔离的工作区中, 一目了然地查看它们正在做什么, 然后审查和合并更改. | Claude Code/Codex | ⭐⭐⭐⭐ | 暂未开源 |
| [AlexPeppas/agentplex](https://github.com/AlexPeppas/agentplex) | 具有图形可视化的多会话 Claude Code/Codex/GitHub 编排器. 主要功能包括: 多会话管理(并行运行多个 Claude Code/Codex/GH CLI 会话)、图形画布(在可视化画布上拖放和连接会话节点)、HITL 通知(当 CLI 会话需要人工输入时通知)、跨会话消息传递(会话间发送消息, 支持Haiku驱动的摘要)、子代理跟踪(通过 JSONL 转录跟踪可视化生成的子代理)、计划和任务可视化(在图形中呈现计划和任务列表)、会话恢复(使用 claude --resume 恢复之前的 Claude 会话). 技术栈: Electron(桌面外壳)、React(UI 框架)、React Flow(图形画布)、xterm.js(终端)、Zustand(状态管理)、node-pty(PTY 后端)、Anthropic SDK(可选摘要). 适用于多会话 AI 代理管理、复杂任务分解、团队协作、项目可视化等场景. | Claude Code/Codex/GitHub CLI | ⭐⭐ | 49 |
| [Zodex](https://zodex.dev) | Zodex 是一个基于 Rust 构建的 AI 集成开发环境, 将 AI 聊天、原生终端和 Git 集成到一个轻量级应用中. 支持多种 AI 模型(OpenAI、Claude、Gemini 等), 提供 AI 驱动的设计生成、无缝 Git 集成、内置终端和状态回滚等功能. 基于 Tauri v2 构建, 本地优先设计, 启动速度快, 占用资源少. 适用于需要 AI 辅助编码、多模型协作和高效开发环境的开发者. | Claude Code<br>Codex | ⭐ | NA |
| [agentflow](https://github.com/berabuddies/agentflow#agentflow) | 智能体编排框架, 支持在依赖图中编排 Codex、Claude 和 Kimi 智能体, 实现并行扇出、迭代循环和在 SSH/EC2/ECS 上的远程执行. 核心功能包括: 并行扇出(fanout)、迭代循环(on_failure)、远程执行(EC2/ECS/SSH)、共享实例、共享内存(scratchboard)、智能体调优(evolve)等. 支持 94 节点的复杂流水线, 适用于大规模智能体协作场景. | Codex<br>Claude<br>Kimi | ⭐ | 1,046 |
| [MeisnerDan/mission-control](https://github.com/MeisnerDan/mission-control) | 为将工作委托给 AI 代理的独立创业者提供的开源指挥中心. 核心理念是 "驯服 swarm. 交付重要的东西". 主要功能包括: Eisenhower 矩阵 (按重要性和紧急性优先排序, 在象限之间拖放)、看板 (跟踪从未开始、进行中到完成列的工作)、目标层次结构 (长期目标与里程碑跟踪、进度条和关联任务)、头脑转储 (即时捕获想法, 稍后分类到任务)、代理团队 (6个内置代理 + 创建具有唯一指令的无限自定义代理)、技能库 (定义可重用的知识模块并注入到代理提示中)、多代理任务 (分配主导代理 + 协作者以进行基于团队的工作)、编排器 (运行 /orchestrate 以同时为待处理工作生成所有代理)、自主守护进程 (后台进程, 自动轮询任务, 生成 Claude Code 会话, 强制执行并发, 并提供实时仪表板)、一键执行 (按任何任务卡片上的播放生成 Claude Code 会话; 实时状态指示器、成功/失败提示和自动完成)、会话弹性 (超时或达到最大步数的代理会自动重新生成继续会话, 在任务注释和子任务中保留进度). Field Ops (外部操作执行) 提供 64 服务目录、加密保险库、财务安全控制、3个自治级别、审批工作流、试运行测试、任务系统和紧急停止按钮. | Claude Code | ⭐ | 397 |
| [pierrecomputer/pierre](https://github.com/pierrecomputer/pierre) | Pierre Computer Company 开源代码仓库, 面向 AI Agent 的开发者工具库. 采用 TypeScript Monorepo 架构(91%), Bun 运行时和包管理器, workspace catalog 模式管理依赖. 核心 packages: diffs(差异比较引擎)、trees(树形数据结构处理)、truncate(文本截断工具)、storage-elements(存储元素组件)、path-store(路径存储方案). 采用严格 TypeScript 编译配置, 支持项目引用跨包类型检查. 专为 AI Agent 设计, 支持 agent-browser 浏览器自动化, worktree 机制支持并行开发, 适用于构建开发者效率工具和 AI 自动化工作流. | AI Agent 环境<br>Bun<br>TypeScript<br>agent-browser | ⭐ | 3,843 |
| [ObservedObserver/async-code](https://github.com/ObservedObserver/async-code) | AI 代码 Agent 并行任务管理系统, 使用 Claude Code 和 CodeX CLI 执行多任务并行处理, 提供 Codex 风格 Web UI. 技术栈: Next.js 15.3.3 + React 19.0 + TypeScript + TailwindCSS 4 + Radix UI + shadcn/ui + CodeMirror 6 + Supabase Auth UI + Sonner + Next Themes + Python Flask + Flask-CORS + Supabase(PostgreSQL + 认证 + RLS) + PyGithub + Docker + Docker Compose. 三层架构: 前端(任务管理UI/Agent对比界面/GitHub集成配置) + 后端(任务调度系统/Docker容器编排/GitHub API集成) + AI Agent执行容器(Claude Code CLI/CodeX CLI/Git工作流自动化). 核心功能包括多Agent并行执行(独立Docker容器隔离)、Git工作流自动化(自动克隆/创建分支/生成diff和patch/提交代码/创建PR)、项目管理系统、任务对比与评估、用户认证与权限(RLS行级安全). 容器化执行环境基于Node.js 20.9.0 Alpine. 数据库设计: users/projects/tasks表全部启用RLS. API端点: start-task/task-status/tasks/create-pr/validate-token/git-diff. Patch智能应用(解析git patch + GitHub Tree API批量提交). 适用于团队协作开发、AI Agent对比研究、自动化代码重构、个人项目开发、教育与学习. Apache 2.0许可. | Claude Code<br>CodeX<br>多平台(可扩展) | ⭐⭐⭐ | 526 |
| [kdlbs/kandev](https://github.com/kdlbs/kandev) | Kandev - AI 看板与开发环境, 并行管理多个 AI Agent、编排任务流、审查变更、交付价值. 技术栈: Go 1.21+(统一二进制架构) + SQLite/PostgreSQL + NATS(规划) + Docker SDK + WebSocket + Next.js + TypeScript + Shadcn/UI + Monaco Editor + xterm.js + dockview + Zustand + Mermaid/Recharts. 单体二进制运行所有服务. ACP协议(JSON-RPC 2.0 over stdin/stdout). 16+ AI平台支持: Claude Code/Codex/GitHub Copilot/Gemini CLI/Amp/Auggie/OpenCode/Cursor/Qwen/Factory Droid/iFlow/Kilocode/Pi/Kimi/AWS Kiro/Qoder/Trae. 核心功能包括多Agent支持、并行任务执行、集成工作区(终端/代码编辑器/git更改面板/嵌入式VS Code/聊天界面)、看板管理(拖拽式面板/列/自动化工作流)、工作流自动化(5大预设: Kanban/Plan & Build/Architecture/Feature Dev/PR Review)、子任务系统、CLI直通(PTY终端)、工作区隔离(Git worktree)、多仓库任务、灵活执行器(本地/Docker/远程sprites.dev)、会话管理、统计追踪. 设计哲学: 定向优于控制/密度但不杂乱/状态可见但平静/熟悉度保持信任. AGPL-3.0许可(无遥测/可自托管). Discord社区支持. 适用于多Agent协作开发、大型特性开发、架构设计与评估、自动化代码审查、多仓库协调、远程Agent执行. | 多Agent(16+平台ACP协议) | ⭐ | 161 |
| [0-AI-UG/cate](https://github.com/0-AI-UG/cate) | 空间化桌面IDE提供无限画布来组织代码、终端、浏览器和Git工具,Electron 41+React 18+Zustand+Monaco Editor+xterm.js+node-pty,支持多工作区会话和分离窗口 | Claude Code<br>OpenAI Codex<br>Gemini<br>Cursor<br>OpenCode<br>MCP Servers | ⭐ | 155 |
| [shannhk/hermes-agent-control-room](https://github.com/shannhk/hermes-agent-control-room) | Agent控制室模板从单Hermes agent扩展到专家团队和自动化工作流,Shell脚本+Node.js+Docker容器化,Task Bus模式支持VPS部署 | Claude Code<br>Codex CLI<br>Hermes Agent | ⭐ | 384 |
| [triggerdotdev/trigger.dev](https://github.com/triggerdotdev/trigger.dev) | 开源的AI工作流和代理构建平台,用TypeScript编写,专注于长时间运行任务、重试、队列、可观测性和弹性扩展. 核心功能包括:无超时的长时间运行任务、持久性与重试、真正的运行时自由(可自定义系统包,运行浏览器/Python等)、Human-in-the-loop(暂停等待人类审批)、实时应用与流式响应、可观测性与监控、批量触发、结构化输入输出、并发与队列控制、Checkpointing检查点恢复、自托管(Docker/Kubernetes). Apache 2.0许可证. | 云端<br>自托管(Docker/Kubernetes) | ⭐⭐⭐ | 15,091 |
| [yofine/mexus-agent-team](https://github.com/yofine/mexus-agent-team) | 纯Markdown的Agent Team工作流插件,为Claude Code和Codex提供基于文件的团队协作能力. 核心目标是通过Markdown文件作为唯一协调协议,让Squad Lead(编排者)分解任务、命名小队、发布kanban,Background Agent认领任务、完成工作、写回结果. 提供/mexus-team:mission(创建新Mission)、/mexus-team:continue(恢复Mission)、/mexus-team:roundtable(圆桌讨论)、/mexus-team:board(本地Web看板)、/mexus-team:status(终端状态)等命令. | Claude Code<br>Codex | ⭐ | 10 |
| [voidcraft-dev/memory-forge-rs](https://github.com/voidcraft-dev/memory-forge-rs) | 本地桌面应用,让用户浏览、编辑和管理AI编码助手的会话记录. 核心目标是解决"AI做出错误假设后持续跑偏"的痛点:直接编辑对话历史中的错误消息,AI在下次--resume时从修正后的记忆继续. 主要功能:记忆操控(编辑/擦除/注入AI对话历史中的任意消息)、修改追溯(前后diff对比)、多平台统一管理(Claude Code/Codex CLI/OpenCode/Kiro/Gemini CLI)、仪表盘、收藏与归档、会话别名、5套主题、双语界面(中文/英文)、提示词库、系统托盘、纯本地运行(零网络请求). 基于Tauri v2构建. | macOS<br>Windows<br>Linux(Tauri v2) | ⭐ | 344 |


## 4.3 状态管理
-------

### 4.3.1 状态栏增强
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [ccstatusline](https://github.com/sirmalloc/ccstatusline) | Claude Code 状态栏插件, 显示当前会话信息 | Claude Code | ⭐⭐ | 6,937 |
| [jarrodwatts/claude-hud](https://github.com/jarrodwatts/claude-hud) | Claude Code 的 HUD 界面, 提供实时状态监控和交互能力 | Claude Code | ⭐⭐⭐ | 17,788 |
| [Link-Start/my-claude-hud](https://github.com/Link-Start/my-claude-hud) | Claude Code 的自定义 HUD 界面, 提供实时状态监控和交互能力 | Claude Code | ⭐ | 3 |
| [AwesomeJun/awesome-claude-plugins](https://github.com/AwesomeJun/awesome-claude-plugins) | 一个为 Claude Code 打造的插件市场, 核心提供 Awesome Statusline 插件, 具有美观的 Catppuccin 主题状态栏、实时 API 监控、多显示模式等功能 | Claude Code | ⭐ | 55 |
| [NoobyGains/claude-pulse](https://github.com/NoobyGains/claude-pulse) | 一个为 Claude Code 打造的实时使用监控工具, 提供彩色编码进度条、10 种内置主题、彩虹动画、自动更新通知等功能, 实时显示会话使用情况、剩余时间、每周使用情况等 | Claude Code | ⭐ | 309 |
| [claude-esp](https://github.com/phiat/claude-esp) | 实时监控 Claude Code 的隐藏输出 (思考、工具调用、子代理) 到单独终端, 支持多会话、层次树视图、实时流、子代理跟踪、令牌使用跟踪等功能. | Claude Code | ⭐ | 112 |
| [hermes-hud](https://github.com/joeynyc/hermes-hud) | AI 代理的意识监控器, 终端仪表板, 用于观察代理的思考过程、记忆、错误和随时间的成长, 具有交互式 TUI、成长跟踪、项目跟踪、健康检查等功能 | Hermes | ⭐ | 183 |
| [Claude Code Status Line](https://github.com/daniel3303/ClaudeCodeStatusLine) | 为 Claude Code 提供自定义状态栏, 显示模型信息、令牌使用情况、速率限制、重置时间和 Git 分支信息, 支持颜色编码使用百分比、缓存机制和更新通知 | Claude Code | ⭐⭐ | 415 |
| [pi-powerbar](https://github.com/juanibiapina/pi-powerbar) | pi 扩展, 渲染持久化的 powerline 风格状态栏, 支持左右对齐分段显示, 内置 git-branch、tokens、context-usage、provider、model、sub-hourly、sub-weekly 等分段, 其他扩展可通过事件更新分段 | pi | ⭐⭐ | 21 |
| [headroom](https://github.com/henchmarketing-rgb/headroom) | Claude Code 上下文使用监控工具, 提供实时状态栏显示, 读取实际会话 JSONL 文件追踪模型和上下文使用情况, 支持 Sonnet 4.6 的 200k/1M 上下文自动调整, 每个目录独立避免窗口干扰 | Claude Code | ⭐⭐ | 66 |
| [claude-code-statusline](https://github.com/jsubroto/claude-code-statusline) | Claude Code 状态行交互式配置工具, 基于 Python 标准库实现 TUI 界面, 支持自定义显示模型、目录、上下文用量、Token 成本、Git 分支和执行时长等字段, 提供 5 种主题样式, 适用于需要个性化 Claude Code 工作区显示的开发者. | Claude Code | ⭐ | 12 |
| [stormzhang/token-tracker](https://github.com/stormzhang/token-tracker) | 本地AI Agent Token消耗追踪和分析工具, 支持Claude Code和Codex. 提供自定义StatusLine状态栏+CLI Dashboard, 实时查看token用量、等效成本、限额状态. 核心功能包括多Agent追踪、限额监控(5h/7d配额)、成本分析(按会话/日/周/月)、会话洞察(项目/模型/时长)、零配置自动检测、隐私安全(纯本地存储). 技术栈: Python 3.11+ + Rich + Shell. | Claude Code<br>Codex | ⭐ | 328 |


### 4.3.2 Token 统计
-------

[Simon Willison 做了一个 Token Counter 来计算 Claude 不同模型的 Token 消耗](https://tools.simonwillison.net/claude-token-counter)


| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [junhoyeo/tokscale](https://github.com/junhoyeo/tokscale) | 一个高性能的 CLI 工具和可视化仪表板, 用于跟踪多个 AI 编码代理的令牌使用情况和成本, 支持 OpenCode、Claude Code、Codex CLI、Cursor IDE 等多种平台, 提供交互式 TUI、实时定价计算、详细的令牌使用分解、原生 Rust 核心(10 倍更快处理)、Web 可视化和社交平台等功能 | 多平台 | ⭐ | 1,701 |
| [yaojingang/tokkit](https://github.com/yaojingang/tokkit) | 一个轻量级、本地优先的 AI 编码工具使用记录器, 帮助开发者跨 Codex、Claude Code、Warp、Kaku、Cursor、CodeBuddy、Augment、ChatGPT 导出、GitHub Copilot 指标导出、Trae 任务历史等工具跟踪令牌使用、成本、模型、终端和客户端, 提供精确 / 部分 / 估计三种精度级别的统计, 支持自动扫描、每日报告、预算跟踪、本地价格覆盖等功能, 核心 CLI 为 tokkit, 快捷方式为 tok | 多平台 | ⭐ | 10 |
| [guard22/opencode-tps-meter](https://github.com/guard22/opencode-tps-meter) | 为 OpenCode TUI 底部添加实时 TPS (Tokens Per Second) 计数器, 显示响应流式传输时过去 15 秒的实时滚动 TPS 和响应完成后的精确输出 TPS. | OpenCode | ⭐ | 69 |
| [MrQianjinsi/agentic-metric](https://github.com/MrQianjinsi/agentic-metric) | 一个本地监控工具, 用于 AI 编码代理, 类似于 top 命令, 用于监控编码代理. 它可以跟踪 Claude Code、Codex、OpenCode、Qwen Code、VS Code (Copilot Chat) 等平台的令牌使用情况和成本, 并提供 TUI 仪表板和 CLI 界面. 支持实时监控、成本估算、今日概览、历史趋势等功能, 所有数据均存储在本地, 无网络请求. 主要特性包括: 实时监控运行中的代理进程、增量 JSONL 会话解析、每模型定价表与 CLI 管理、今日使用概览、30 天历史趋势、TUI 仪表板(1秒实时刷新)、多代理插件架构. 支持 Linux 和 macOS 平台. | 多平台 | ⭐ | 172 |
| [williamcr01/opencode-tps](https://github.com/williamcr01/opencode-tps) | 为 OpenCode TUI 界面添加实时 TPS (Tokens Per Second) 计数器, 显示 AI 模型生成令牌的速度, 位于 TUI 右下角并动态更新. 通过钩子到 OpenCode 的消息流事件, 使用 5 秒滚动窗口计算 TPS, 无令牌生成时显示 "-", 流结束或错误时自动清除. 支持通过 OpenCode CLI 或 npm 安装, 要求 OpenCode >= 1.3.14, 仅支持 TUI 界面. | OpenCode | ⭐ | 21 |
| [codeburn](https://github.com/AgentSeal/codeburn) | 一个用于跟踪 AI 编码令牌使用情况的工具, 通过任务类型、工具、模型、MCP 服务器和项目进行分类, 跟踪每种活动类型的一次性成功率, 提供交互式 TUI 仪表板、macOS 菜单栏小部件、CSV/JSON 导出等功能. 通过直接读取 Claude Code 会话记录, 无需包装器、代理或 API 密钥. 支持 13 个任务类别分类, 包括编码、调试、功能开发、重构、测试等, 提供每日成本图表、按项目/模型/活动的细分、核心工具和 MCP 服务器分析. | Claude Code | ⭐ | 361 |
| [opencode-quota](https://github.com/slkiser/opencode-quota) | 为 OpenCode 添加使用配额和令牌可见性, 无上下文窗口污染. 提供 TUI 侧边栏面板、弹出配额提示和手动命令, 支持多个提供商(Anthropic、GitHub Copilot、OpenAI、Cursor、Qwen Code、Alibaba Coding Plan、MiniMax Coding Plan、Kimi Code、Chutes AI、Synthetic、Google Antigravity、Z.ai Coding Plan、NanoGPT、OpenCode Go)的配额管理和令牌报告. | OpenCode | ⭐ | 232 |
| [token-dashboard](https://github.com/nateherkai/token-dashboard) | 一个本地仪表板, 读取 Claude Code 写入到 ~/.claude/projects/ 的 JSONL 转录文件, 转换为每个提示的成本分析、工具/文件热图、子代理归因、缓存分析等. 所有数据均在本地运行, 无数据离开机器, 无遥测, 无 API 调用, 无需登录. 主要功能包括: 查看哪些提示成本高昂、比较不同项目的令牌使用情况、发现浪费模式、了解"缓存命中"实际节省的成本、确认 Pro 或 Max 计划的价值. 技术栈: Python 3 (仅标准库)、SQLite、纯 JavaScript + ECharts. 提供 7 个标签页: Overview、Prompts、Sessions、Projects、Skills、Tips、Settings. 支持实时更新, 每 30 秒重新扫描并推送更新. | Claude Code | ⭐ | 238 |
| [Claude-Code-Usage-Monitor](https://github.com/Maciek-roboblog/Claude-Code-Usage-Monitor) | 一个实时终端监控工具, 用于跟踪 Claude AI 令牌使用情况, 具有高级分析、基于机器学习的预测和 Rich UI 界面. 主要功能包括: ML 基于预测(P90 百分位计算和智能会话限制检测)、实时监控(可配置刷新率)、高级 Rich UI(颜色编码进度条、表格和布局)、智能自动检测(自动计划切换和自定义限制发现)、增强的计划支持(Pro、Max5、Max20、Custom)、高级警告系统、模块化设计、智能主题、成本分析等. 支持多种安装方式(uv、pip、pipx), 要求 Python 3.9+. | Claude Code | ⭐ | 7,837 |
| [mag123c/toktrack](https://github.com/mag123c/toktrack) | 一个在统一仪表板中跟踪所有 AI 编码 CLI(Claude Code、Codex CLI、Gemini CLI、OpenCode、PI Agent)令牌使用和成本的工具. 使用 Rust 构建, 采用 simd-json 超快速解析和 rayon 并行处理, 性能比现有工具快 1000 倍(冷启动约 1s, 缓存查询约 0.04s). 提供持久化缓存机制, 解决 Claude Code 等工具默认 30 天后删除数据导致历史记录丢失的问题. 功能包括: TUI 仪表板(3 个标签页: 概览、统计、模型)、CLI 命令(日/周/月统计, 支持 JSON 输出)、可分享的使用报告(文本和 SVG). | Claude Code | ⭐ | 120 |
| [wesm/agentsview](https://github.com/wesm/agentsview) | 本地优先的 AI 编程助手会话智能分析工具, 提供统一的会话管理平台.  支持自动发现15+个主流AI编程助手(Claude Code/Codex/GitHub Copilot/Gemini CLI/OpenCode/Cursor/Amp等). 核心功能包括会话浏览器(Web界面+SSE实时更新+全文搜索+键盘导航)、Token使用和成本追踪(每日成本摘要+模型细分+日期过滤+代理过滤)、会话统计(持续时长分布+峰值上下文+工具使用+缓存经济学+原型分类+Git/GitHub指标可选)、Web UI仪表板、PostgreSQL团队同步. 性能比实时解析工具快100倍(预索引SQLite查询), 零遥测零账号完全本地化. MIT许可, 官网agentsview.io. 适用于个人开发者统一管理、团队协作集中监控、企业环境合规审计、研究分析交互模式. | 多平台(15+ AI助手自动发现) | ⭐ | 857 |
| [foyzulkarim/claude-lens](https://github.com/foyzulkarim/claude-lens) | Claude Code 本地可视化仪表板, 提供零配置本地工具监控和分析使用情况. 技术栈: Node.js ≥18 + Express + 原生HTML+JS + Bootstrap 5.3 + dotenv + nodemon. 架构: Frontend(统计卡片+图表+表格) + Backend(HTTP API: stats/history/sessions/tool-calls/projects/daily-costs) + Claude Code数据源(`stats-cache.json/history.jsonl/sessions/*.json/projects/*/`). 核心功能包括今日vs全时段统计、缓存性能分析(命中率+成本节约)、每日成本明细表(含模型使用统计)、工具调用分析(使用排名+跨项目统计+详情查看)、项目活动统计(按项目分组+会话数+使用时间). 价格配置支持AWS Bedrock和Anthropic API(可自定义Token价格). 成本计算覆盖input/output/cache_read/cache_create四类token. 一键启动(npx github:foyzulkarim/claude-lens), 适用于成本控制、性能优化、工作流分析、项目追踪. | Claude Code<br>AWS Bedrock<br>Anthropic API | ⭐ | 190 |
| [kenn-io/agentsview](https://github.com/kenn-io/agentsview) | 本地优先的 AI 编程助手会话浏览器与成本追踪工具, 一个二进制文件无需账号, 所有数据本地存储. 支持搜索、分析和统计超过 20 种 AI 编码助手(Claude Code、Codex 等)的 Token 使用和会话数据. 技术栈: Go 76.6% + TypeScript 12.9% + Svelte 8.1%. | 多平台(20+ AI助手) | ⭐⭐ | 2,647 |
| [Nanako0129/coralline](https://github.com/Nanako0129/coralline) | Powerlevel10k 风格的 Claude Code 状态栏脚本, 显示目录、Git 分支、模型、上下文窗口用量、速率限制、费用、时钟等信息段, 支持主题切换和响应式布局. 技术栈: Shell 82.7% + Python 17.3%. | Claude Code | ⭐⭐ | 332 |
| [ratelworks/token-horse](https://github.com/ratelworks/token-horse) | Claude Code 和 Codex CLI 的终端像素小马宠物, 小马奔跑速度随会话 Token 消耗速率加快, 受韩国出租车计费器上奔腾小马启发. 技术栈: JavaScript 100%, Node.js/npm. | Claude Code<br>Codex CLI | ⭐⭐ | 14 |

### 4.3.3 Bar 状态
-------


| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [cordwainersmith/Claudoscope](https://github.com/cordwainersmith/Claudoscope) | 一个原生 macOS 菜单 bar 应用, 用于探索、分析和管理 Claude Code 会话, 提供实时仪表板、分析功能、会话历史记录和项目洞察, 支持令牌使用和成本估算、会话浏览、工具调用分析、配置健康检查等功能, 仅支持 Apple Silicon Mac (M1 或更高版本) | macOS | ⭐ | 121 |
| [Four-JJJJ/AI-Plan-Monitoring](https://github.com/Four-JJJJ/AI-Plan-Monitoring) | 一个 macOS 菜单栏应用, 用于监控多个 AI 服务的额度和余额, 支持多账号管理和切换. 核心功能包括: 多账号自动记录与一键切换、独立额度重置倒计时、第三方网站用量监控、官方服务和第三方中转统一监控、第三方站点配置模板化、低额度提醒和鉴权失效提醒、菜单栏实时查看剩余额度和重置时间. 支持的官方服务包括 Codex、Claude、Gemini、GitHub Copilot、Cursor、Windsurf、Kimi、Amp、Z.ai、JetBrains AI、Kiro 等, 支持的第三方站点模板包括 open.ailinyu.de、platform.moonshot.cn、platform.xiaomimimo.com 等. 技术栈基于 Swift 6, 要求 macOS 14+. | macOS | ⭐ | 68 |
| [Lcharvol/Claude-God](https://github.com/Lcharvol/Claude-God) | 一个 macOS 菜单 bar 应用, 用于实时监控 Claude AI 使用情况, 提供配额跟踪、峰值/非峰值指示器、会话成本、消耗率预测、使用热图、ROI 分析、桌面小部件和多账户支持等功能. 核心功能包括: 实时配额监控、动态图标(根据配额状态变色)、实时倒计时、消耗率预测、模型顾问、成本跟踪、项目细分、会话历史、火花线图表、模型细分、每日预算、CSV 导出、活动会话检测、自动凭证管理、重置通知、自动刷新、菜单 bar 模式、紧凑模式、通知、登录时启动、插件市场等. 技术栈基于 Swift, 无外部依赖. | macOS | ⭐ | 21 |
| [sylearn/AIUsage](https://github.com/sylearn/AIUsage) | 一个 macOS 应用, 提供一站式仪表盘用于管理所有 AI 订阅, 包括配额、成本、账户和 Claude Code 代理. 核心功能包括仪表盘监控、提供商监控、Claude Code 统计、账户详情、代理管理和配置、代理统计以及菜单栏显示. 技术栈基于 Swift (98.0%) 开发. | macOS | ⭐ | 159 |
| [Artzainnn/ClaudeUsageBar](https://github.com/Artzainnn/ClaudeUsageBar) | 一个 macOS 菜单栏应用, 用于实时跟踪 Claude.ai 的使用情况. 核心功能包括实时使用跟踪(会话和每周限制)、颜色编码的菜单栏图标、智能通知、键盘快捷键、自动刷新、隐私优先(数据存储在本地)、Pro 计划支持以及仅菜单栏显示(无 Dock 图标). 技术栈基于 SwiftUI、AppKit、Carbon 等. | macOS | ⭐ | 157 |
| [steipete/CodexBar](https://github.com/steipete/CodexBar) | 一个轻量级 macOS 14+ 菜单栏应用,实时监控 Codex、Claude、Cursor、Gemini、Antigravity、Copilot、z.ai、Kimi、Kiro、Vertex AI、Augment、Amp、JetBrains AI、OpenRouter、Perplexity、Abacus AI、DeepSeek 等多平台 AI 服务的配额使用情况,显示会话/周度使用量和重置倒计时. 支持每个提供商独立状态栏或合并图标模式、提供成本扫描 CLI、WidgetKit 小部件、隐私优先设计(数据全在本地处理) | macOS | ⭐ | 229 |
| [steipete/RepoBar](https://github.com/steipete/RepoBar) | macOS 菜单栏应用, 让开发者不打开浏览器即可随时掌握 GitHub 工作动态. 紧凑菜单显示 issue/PR 数量、star/fork 数、最新活动、CI 状态、本地 checkout 状态、GitHub API rate-limit 健康状况. 技术栈: Swift/SwiftPM, 集成 GitHub REST API 和 GraphQL, 支持本地项目扫描(当前分支、上游分支、ahead/behind 状态、dirty files), 可选自动同步功能. 支持读取 gitcrawl 格式 GitHub 备份归档, 离线或 rate-limit 时仍可查看 issue/PR 列表. 附带 CLI 工具便于自动化调试, 支持 GitHub.com 及 GitHub Enterprise 认证. 适用于多仓库频繁切换的开发者快速查看动态. | macOS<br>GitHub API<br>Swift | ⭐ | 2,001 |
| [Blimp-Labs/claude-usage-bar](https://github.com/Blimp-Labs/claude-usage-bar) | macOS 菜单栏应用, 实时跟踪 Claude.ai 使用情况. 核心功能: 实时使用跟踪(会话和每周限制)、颜色编码菜单栏图标、智能通知、键盘快捷键、自动刷新、隐私优先(数据存储在本地)、Pro 计划支持、仅菜单栏显示(无 Dock 图标). 技术栈: SwiftUI、AppKit、Carbon 等. 适用于 Claude Pro 用户实时监控配额使用, 避免额度耗尽中断工作. | macOS<br>Claude.ai<br>SwiftUI | ⭐ | 437 |
| [AThevon/TokenEater](https://github.com/AThevon/TokenEater) | macOS 原生菜单栏应用+桌面小组件+浮动覆盖层, 实时监控 Claude AI 使用限制. 技术栈: Swift 5.9(99.7%) + SwiftUI + WidgetKit + macOS 14+. MV Pattern + Repository Pattern + Protocol-Oriented Design. 禁用@Observable避免Release构建CPU freeze. 应用/Widget分离架构(主应用非沙盒读Keychain+调用API, Widget沙盒只读本地JSON). 核心功能包括菜单栏监控(实时百分比显示+三种布局+弹出仪表板)、桌面小组件系统(WidgetKit原生+三种小组件+15分钟刷新)、Agent Watchers(浮动覆盖层+Dock悬停+终端跳转+JSONL实时监控)、历史记录浏览器(JSONL解析+模型筛选+时间范围+每日分解)、智能颜色系统(风险感知配色+三种气质模式+早期置信度抑制)、智能配速分析(四个区域+配速vs平衡图)、主题与通知(4预设+自定义+细粒度通知). Keychain静默读取OAuth Token, 安全边界Token不离开本机. 适用于Claude Pro/Max/Team计划用户避免用量额度耗尽、实时监控、会话管理、历史分析、配速规划. | Claude Pro<br>Claude Max<br>Claude Team | ⭐⭐⭐ | 270 |
| [tddworks/ClaudeBar](https://github.com/tddworks/ClaudeBar) | macOS 菜单栏应用, 实时监控主流 AI 编码助手配额使用情况. 聚合展示 Claude、Codex、Gemini、GitHub Copilot 等多平台剩余额度. 技术栈: Swift 6.2+ + SwiftUI + Tuist 项目管理, 采用分层架构(Domain/Infrastructure/App). 核心功能: 多平台实时配额追踪、会话/周度/模型级使用百分比、多种主题模式(浅色/深色/CLI/圣诞)、iTerm2 配色导入、红黄绿三色状态指示条、配额告警通知、自动刷新. 支持监控 Claude CLI、Codex CLI、Gemini CLI、GitHub Copilot、Antigravity、Z.ai、Kimi、Kiro、Amp 等平台. | macOS<br>Claude CLI<br>Codex<br>Gemini<br>Copilot | ⭐ | 1,106 |
| [UsageBoard](https://github.com/marsmay/UsageBoard) | 原生 macOS 菜单栏应用, 通过 Python 插件聚合展示 API/模型服务用量, 支持智谱 Claude Codex MiniMax DeepSeek Tavily 等平台, 以进度条和统计图可视化配额消耗, 支持定时刷新、参数配置、中英文切换. | macOS | ⭐ | 93 |
| [Muxbar](https://github.com/1989v/muxbar) | macOS 原生菜单栏工具, 集成 tmux 会话管理、caffeinate 休眠控制、Closed-lid 合盖运行模式, 支持多终端和会话模板, 适合需要在后台持续运行构建/CI/远程会话的开发者. | macOS | ⭐ | 12 |
| [geebos/agent-battery](https://github.com/geebos/agent-battery) | 轻量级macOS菜单栏应用以电池百分比形式显示Claude Code和Codex剩余使用配额,Swift+SwiftUI+MenuBarExtra,双数据源自动刷新和颜色预警 | Claude Code<br>Codex | ⭐ | 31 |
| [robinebers/openusage](https://github.com/robinebers/openusage) | 菜单栏应用一站式追踪所有AI编码订阅使用量和配额,Tauri+Vite+React+TypeScript+Rust,支持16+提供商实时进度条和badge提示,本地HTTP API供第三方应用读取数据 | Claude<br>Cursor<br>Codex<br>Copilot<br>Gemini<br>Windsurf<br>Kimi Code<br>OpenCode Go等 | ⭐⭐⭐ | 2,492 |
| [otoha1119/token-checker](https://github.com/otoha1119/token-checker) | macOS菜单栏应用,实时显示Claude Code和Codex的使用率(速率限制信息). 核心目标是让开发者无需切换窗口即可监控AI编码代理的token使用情况. 菜单栏两个甜甜圈图表显示Claude和Codex使用率、点击展开弹出窗口显示5小时窗口和周窗口使用率详情、重置倒计时、更新间隔选择、登录时自动启动. Claude通过Keychain获取OAuth token后请求Anthropic用量API;Codex通过子进程JSON-RPC调用. Swift 92.9%原生应用. | macOS 14 Sonoma及以上 | ⭐ | 65 |
| [Javis603/token-monitor](https://github.com/Javis603/token-monitor) | AI 工具即时 Token、成本与限额监控桌面组件, 支持多设备同步. 覆盖 Claude Code、Codex、OpenCode、Hermes、OpenClaw、Cursor、Antigravity 等多种平台. 技术栈: JavaScript 83.2% + CSS + HTML, Node.js 18.17+ / Electron 桌面应用. | 多平台(15+ AI工具) | ⭐⭐ | 158 |
| [ntd4996/agentpet](https://github.com/ntd4996/agentpet) | macOS 和 Windows 桌面宠物应用, 实时监控 AI 编码代理(Claude Code、Codex、Cursor、Gemini CLI 等)的工作状态, 通过桌面宠物提供可视化反馈, 宠物随代码工作成长、升级、攀升排行榜. 技术栈: Swift/SwiftUI + Unix-socket daemon, Windows 版使用 Tauri + Rust. | Claude Code<br>Codex<br>Cursor<br>Gemini CLI 等 | ⭐⭐ | 191 |
| [Joyi-code/DeepSeekMonitorWindows](https://github.com/Joyi-code/DeepSeekMonitorWindows) | Windows 桌面端 DeepSeek API 用量监控应用, 查看账户余额、当月消费、模型 Token 用量和最近用量趋势. 技术栈: Tauri 2 + React 18 + Rust. | DeepSeek<br>Windows | ⭐⭐ | 195 |
| [mm7894215/TokenTracker](https://github.com/mm7894215/TokenTracker) | 跨 22 种 AI 编码工具(Claude Code、Codex、Cursor、Gemini、Roo Code、Zed Agent、Goose 等)的 Token 用量追踪器, 本地优先零配置, 提供美观仪表板、macOS 菜单栏应用和 4 个桌面小组件. 技术栈: JavaScript 71.8% + Swift 11.2% + TypeScript 10.8%. | 多平台(22+ AI工具) | ⭐⭐ | 726 |


### 4.3.4 状态管理
-------


| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [matt1398/claude-devtools](https://github.com/matt1398/claude-devtools) | Claude Code 的开发工具集, 提供调试、监控和优化能力 | Claude Code | ⭐ | 2,992 |
| [blader/taskmaster](https://github.com/blader/taskmaster) | 编码代理的完成保护工具, 解决代理在完成用户目标之前就停止的问题, 要求代理发出明确的完成令牌, 支持 Codex 和 Claude 两种代理. | Codex/Claude Code | ⭐ | 491 |
| [nicobailon/pi-design-deck](https://github.com/nicobailon/pi-design-deck) | 一个用于 Pi 编码代理的工具, 提供多页视觉决策卡. 在 macOS 上, 使用 Glimpse 在原生 WKWebView 窗口中渲染; 在其他平台上, 它会回到浏览器标签页. 每张幻灯片会展示 2 到 4 个高保真预览——代码差异、架构图、界面模型——你可以每张幻灯片选择一个. 代理会获得干净的选择映射, 然后进入实现阶段. | OpenClaw<br>Pi | ⭐ | 173 |
| [automazeio/ccpm](https://github.com/automazeio/ccpm) | 使用 Claude Code 工作流程, 利用基于规格的开发、GitHub issue、Git 工作树以及多个并行运行的 AI 代理, 实现更快的发布. 防止上下文丢失, 防止任务阻塞, 保障质量. 这个经过实战验证的系统将 PRD 变成史诗级. | Claude Code |
| [hridaya423/conductor-tasks](https://github.com/hridaya423/conductor-tasks) | 智能助手, 用于将需求转化为可操作的任务, 生成实施计划, 跟踪进度, 并加速开发过程. 主要功能包括: AI 驱动的任务生成、智能任务扩展和规划、强大的 CLI 自动化、多功能任务模板、可视化任务管理(看板、依赖树、摘要仪表板)、多提供商 LLM 灵活性(支持 OpenAI、Anthropic、Groq、Mistral、Google Gemini、Perplexity、xAI、Azure OpenAI 等). 技术栈: JavaScript/TypeScript (Node.js), 支持 MCP 集成和独立 CLI 使用. 适用于开发项目规划和任务管理、PRD 解析和任务生成、开发流程自动化、项目可视化和进度跟踪等场景 | 多 Agent 支持 | ⭐ | 75 |
| [cc-enhanced](https://github.com/melonicecream/cc-enhanced) | 非官方的 Claude Code 项目管理 TUI 仪表盘, 支持实时项目监控、使用分析、智能待办系统和现代 UI 主题, 基于 Rust 开发, 提供性能优化的用户体验. | Claude Code | ⭐ | 19 |
| [777genius/claude_agent_teams_ui](https://github.com/777genius/claude_agent_teams_ui) | AI 代理团队任务管理工具, 让代理自主工作、相互通信、互相审查, 用户只需查看看板. 支持跨团队通信、代理间消息传递、任务附件、代码审查、实时进程监控等功能, 100% 免费开源, 完全本地运行 | Claude Code | ⭐ | 550 |
| [OrbitDock](https://github.com/Robdel12/OrbitDock) | 一个用于管理和协调 AI 编码代理的工具, 允许从任何地方运行、审查和编排 AI 编码代理. 核心是一个 Rust 服务器, 连接到 macOS 和 iOS 应用, 支持 Claude Code 和 Codex. 主要功能包括: Mission Control(指向 Linear 项目, 代理自动处理问题)、双向控制 (发送消息、指导、分叉对话等)、代码审查(magit 风格的差异视图, 支持内联评论)、多服务器支持(可以连接多个设备上的服务器) 等. | Claude Code<br>Codex | ⭐ | 90 |
| [linsheng9731/clawsync](https://github.com/linsheng9731/clawsync) | OpenClaw 状态跨机器同步 CLI 工具, 采用纯 Git 原生工作流实现安全备份与恢复. 核心技术: 细粒度备份范围控制(支持 include/exclude/ignore-paths)、内置敏感数据清理管道(默认启用自动替换 secrets 为占位符)、丰富恢复策略(overwrite/skip/merge 三种模式)、本地优先合并机制、定时同步支持(通过 cron job). 技术栈: TypeScript, 基于 Git 的备份工作流(git init/push/pull/merge). 使用场景: OpenClaw 配置跨设备同步、开发环境状态备份与恢复、灾难恢复(disaster-recovery)、团队配置共享、定时自动备份. 支持 GitHub Releases 一键安装或 npm 本地开发安装. | OpenClaw<br>CLI<br>Git | ⭐ | 4 |
| [tracknotch](https://github.com/manojacharix/tracknotch) | 原生 macOS 应用, 在 Notch/菜单栏实时监控 LLM 使用情况. 支持 Claude Code、OpenAI、Cursor、Codex 等多提供商, 本地优先架构, API 密钥存储于 Keychain, 提供上下文可视化与预算追踪功能. | macOS | ⭐ | 11 |
| [cclank/tokei](https://github.com/cclank/tokei) | [Tokei 時計](https://tokei.lanshuagent.com) — macOS 菜单栏应用, 实时追踪 9 款 AI 编程工具(Claude Code、Codex CLI、Gemini CLI、Grok CLI、Hermes、OpenClaw、Pi、OpenCode、Qoder)的用量、成本和性能, 基于本地日志零网络流量. 技术栈: C++ 41.9% + C 32.9% + Swift 12.7% + Python 7.2%. | macOS | ⭐⭐ | 61 |


### 4.3.5 会话分析
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [token-optimizer](https://github.com/alexgreensh/token-optimizer) | 查找并修复幽灵令牌, 在压缩中生存, 避免上下文质量衰减, 提供智能压缩、质量跟踪、使用分析和成本节省功能. 安装完成之后, 可以通过 `/token-optimizer` 生成 Token 分析的 Dashboard, 实时追踪每一个 API 调用的 token 分解, 输入多少、输出多少、缓存命中多少、缓存写入多少, 一笔一笔给你算清楚. 你的钱花在哪了, 哪些skill你装了但从没用过, 哪些 MCP 服务器一直在白吃你的预算, 一目了然. 而且这个 Dashboard 不消耗你哪怕一个 token. 它跑在外部进程里, 不注入指令到你的上下文, 不加 MCP 开销. 参见 [微信公众号--智声工坊--Token Optimizer: 你的AI在变笨, 而你看不到](https://mp.weixin.qq.com/s/yUIePLzDVVswPPCFrKRDUA) | Claude Code、VS Code 扩展、OpenClaw 插件 | ⭐⭐⭐⭐⭐ | 539 |
| [RubyRose2001/claudeInsight](https://github.com/RubyRose2001/claudeInsight) | 完全本地化的 Claude AI 对话历史管理和分析工具, 帮助开发者管理和回顾与 Claude 的对话历史. 主要功能包括: 历史记录扫描与管理、项目管理、会话查看与搜索、模型配置管理、技能管理、工作区管理. 技术栈: 后端(Fastify, TypeScript)、前端(Vue 3, TypeScript, Vite, Radix Vue, Tailwind CSS, Pinia, Monaco Editor, Chart.js)、包管理(pnpm). 适用于 Claude AI 对话历史管理、多项目对话记录管理、会话搜索与分析、模型和技能管理等场景. | Claude Code | ⭐ | 25 |
| [claude-doctor](https://github.com/millionco/claude-doctor) | 分析 Claude Code 会话中的行为反模式, 从历史记录生成 CLAUDE.md/AGENTS.md 规则, 支持结构、行为和词汇信号检测, 包括 AFINN-165 情感评分. | Claude Code | ⭐ | 497 |
| [Langfuse](https://github.com/langfuse/langfuse) | 开源 LLM 工程平台 | 帮助团队协作开发、监控、评估和调试 AI 应用, 支持自托管部署, 提供可观测性、提示管理、评估、数据集管理和 LLM Playground 等核心功能, 集成多种 LLM 框架和工具 | 适用于需要构建、监控和优化 LLM 应用的团队和开发者 | ⭐⭐⭐ | 25,895 |
| [claude-conversation-extractor](https://github.com/ZeroSumQuant/claude-conversation-extractor) | 导出 Claude Code 对话记录到 Markdown 的专用工具, 自动扫描 `~/.claude/projects` 下的 JSONL 日志文件, 支持批量导出、实时全文搜索、多格式转换(Markdown/JSON/HTML)和详细模式(含 Tool Use/MCP 响应/终端输出). 纯 Python 实现, 零外部依赖, 跨平台支持(Windows/macOS/Linux), 测试覆盖率 97%. 可选 spaCy 语义搜索增强. 适用于备份 Claude Code 会话、归档编程对话、搜索历史解决方案等场景. | Claude Code | ⭐⭐⭐⭐ | 525 |
| [sentrux](https://github.com/sentrux/sentrux) | AI Agent 代码架构质量传感器与治理工具, 用于闭环 AI 辅助编程中的架构退化问题. 核心功能包括: 实时可视化(交互式树状图展示项目结构与依赖关系, 文件被修改时高亮 glow)、质量度量(5 大根因指标——模块化 modularity、无环性 acyclicity、深度 depth、均衡性 equality、冗余度 redundancy, 综合评分 0–10000)、质量门禁(`quality gate`, 支持保存基线并对比会话前后的架构退化)、规则引擎(通过 `.sentrux/rules.toml` 定义架构约束, 如最大循环依赖数、最大耦合度、禁止 God File、分层依赖方向等, 支持 CI 集成)、MCP 集成(提供 9 个 MCP 工具: `scan/health/session_start/session_end/rescan/check_rules/evolution/dsm/test_gaps`, 让 Agent 实时感知架构健康度). | Claude Code(MCP 插件), Cursor, Windsurf, OpenCode, OpenClaw 等任意 MCP 客户端 | ⭐ | 1,186 |
| [claude-tap](https://github.com/liaohch3/claude-tap) | 拦截和检查 Claude Code 或 Codex CLI 的所有 API 流量的专业工具. 通过反向代理架构记录完整的请求-响应对, 提供美观的追踪查看器. 核心功能包括: 实时查看 API 调用、结构化差异对比、Token 使用分解(输入/输出/缓存读/缓存写)、工具检查器、全文搜索、深色模式、多语言支持(中文、英文、日文等). 技术栈: Python 实现, 自包含 HTML 查看器, 零外部依赖, SSE 实时流式转发. 支持多种使用模式: 基础追踪、实时浏览器查看、仅代理模式、最大追踪会话数控制等. 适用于学习 Claude Code/Codex 工作原理、调试代理行为、分析 Token 使用、优化提示词工程等场景. 参见 [2026/04/29, AI少年 @aehyok, 你好不好奇在Claude Code中输入"你好"后, API发出的请求到底是什么样的](https://x.com/aehyok/status/2049386268786839616) | Claude Code、Codex CLI | ⭐ | 93 |
| [vibeforge1111/keep-codex-fast](https://github.com/vibeforge1111/keep-codex-fast) | Codex 本地状态维护工具, 解决长期使用后性能下降问题, 核心"先移交再归档不删除". 技术栈: Python 100% + SQLite操作state_5.sqlite. 三种工作模式: Inspect(只读报告)、Maintain(备份→归档→移动→清理→规范化)、Repair(修复SQLite显示元数据膨胀). 核心功能包括会话管理(归档>10天非固定会话+生成manifest和恢复脚本)、Worktree清理(移动>7天过期worktrees)、日志轮转(归档>64MB logs_2.sqlite)、配置清理(清理不存在路径+移除Windows扩展路径格式)、元数据修复(可选修复threads.title/first_user_message膨胀+不删除JSONL transcript)、进程监控(报告重型进程+检测Codex运行)、Handoff文档系统(交接文档含仓库/目标/完成项/关键文件/命令/错误/下一步/约束). 安全原则: 不永久删除、备份优先(~/.codex/archived_sessions)、隐私安全、恢复脚本可撤销. 推荐使用频率: 重度用户每周/轻度用户每两周. 适用于重度Codex用户性能下降症状(启动慢/线程导航sluggish/UI加载慢/本地状态文件过大). MIT许可. | Codex Desktop<br>Codex CLI | ⭐⭐⭐⭐ | 796 |
| [moazbuilds/CodeMachine-CLI](https://github.com/moazbuilds/CodeMachine-CLI) | AI 编码代理编排工具, 将人工维护的"工作流知识"自动化. 解决每次使用 AI 编码代理需重复引导、解释过程、管理上下文的痛点, 让复杂工作流可捕获、复用和自动化执行. 技术栈: TypeScript(98%) + Bun 运行时, 通过 headless 脚本模式驱动多种 AI 编码引擎. 核心功能: 工作流编排与复用、多代理协调与通信、并行任务执行、长时运行持久化、上下文工程与动态管理. 支持 Claude Code、Codex、Cursor 等主流 AI 编码引擎. 适用于复杂项目自动化开发、重复性编码任务、多模块同步开发、团队共享最佳实践工作流. Apache-2.0 许可, v0.8.0 Nova BETA. | Claude Code<br>Codex<br>Cursor | ⭐⭐ | 2,475 |
| [0xSero/ai-data-extraction](https://github.com/0xSero/ai-data-extraction) | AI编程助手训练数据提取工具包, 从AI编程助手中提取完整对话、Agent推理和代码上下文数据. 支持自动提取完整对话历史、用户消息与AI响应、代码上下文(文件路径/行号/代码片段)、代码diff和编辑、工具使用和执行结果、时间戳和元数据. 输出格式JSONL, 可直接用于机器学习训练数据. 技术栈: Python 3.6+ 标准库(无外部依赖). 支持Claude Code、Codex、Cursor、Trae、Windsurf、Gemini等10+平台. | Claude Code<br>Codex<br>Cursor<br>Windsurf<br>Gemini<br>多平台支持 | ⭐ | 680 |
| [nvwalj/ai-memory-reader](https://github.com/nvwalj/ai-memory-reader) | 原生macOS/iOS应用浏览和管理AI代理内存文件(CLAUDE.md、AGENTS.md、JSONL会话记录),Swift+SwiftUI+MarkdownUI 3MB通用二进制,自动发现8个AI代理目录 | Claude Code<br>Codex<br>Cursor<br>Gemini<br>Continue<br>GitHub Copilot<br>Aider<br>OpenClaw | ⭐ | 17 |
| [raindrop-ai/workshop](https://github.com/raindrop-ai/workshop) | 本地调试器实时流式追踪AI代理每个token、工具调用和决策过程,TypeScript+Bun+SQLite+React+Vite,自愈评估循环支持25+ SDK集成 | Claude Code<br>Codex<br>Devin<br>Cursor<br>OpenCode | ⭐⭐⭐ | 603 |
| [DevonPeroutky/agent-profiler](https://github.com/DevonPeroutky/agent-profiler) | 本地追踪查看器专门分析编码代理会话性能和上下文膨胀问题,Node.js+TypeScript+React+HTML零依赖,三种视图分析上下文膨胀和优化模式 | Codex<br>Claude Code | ⭐ | 6 |
| [haidang1810/md2html](https://github.com/haidang1810/md2html) | 便携技能将AI生成Markdown文档转换为可读性强单页HTML,纯HTML+CSS+Markdown零安装无依赖,智能分析流程转Mermaid图、讨论转对比卡片、步骤转时间线 | Claude Code<br>Codex CLI<br>Antigravity<br>Cursor<br>Continue.dev | ⭐ | 214 |
| [Hyperion-GPU/ProofFlow-v0.1](https://github.com/Hyperion-GPU/ProofFlow-v0.1) | AI编码工作账本系统让AI生成工作可审核可追踪可撤销,Python+FastAPI+SQLite+React+MCP Server 23个工具,工作账本流程和证据图谱 | Claude Code<br>Codex | ⭐ | 110 |
| [regent-vcs/re_gent](https://github.com/regent-vcs/re_gent) | AI编码代理的版本控制系统,跟踪代理执行了哪些操作、哪个Prompt写了哪行代码,并在出错时回滚. 提供三大核心命令:rgt log(查看会话做了什么)、rgt blame(哪个prompt写了这行代码)、rgt show(检查任意Step的完整上下文). BLAKE3内容寻址存储与自动去重、SQLite索引实现亚10毫秒查询、Per-Session DAG并发会话跟踪、Hook驱动自动集成(Claude Code/Codex/OpenCode)、零配置、并发安全、VSCode扩展(内联blame注释). | Claude Code<br>Codex<br>OpenCode | ⭐ | 584 |
| [jianshuo/ccglass](https://github.com/jianshuo/ccglass) | 轻量级本地日志反向代理+Web仪表盘,用于查看AI编码代理(Claude Code/Codex/OpenCode/DeepSeek-TUI等)发送给模型的全部请求内容. 核心目标:解决"这些CLI忽略HTTP_PROXY/HTTPS_PROXY,Charles/mitmproxy无法看到流量"的问题. ccglass通过让客户端在本地HTTP层与代理交互(客户端自己做HTTPS到真实API),无需CA证书或TLS pinning. 实时请求流、对话流(自上而下序列图)、Turn-to-turn diff、Token/cache/cost(精确估算USD)、响应重组与导出(raw/Markdown/JSON/HAR)、会话汇总、每模型过滤、Copy as cURL、自检MCP. | macOS<br>Linux<br>Windows(Node.js ≥ 18) | ⭐ | 297 |
| [regent-vcs/re_gent](https://github.com/regent-vcs/re_gent) | AI编码代理的版本控制系统(同上行248),跟踪代理执行了哪些操作、哪个Prompt写了哪行代码,并在出错时回滚. 提供rgt log、rgt blame、rgt show三大核心命令,基于BLAKE3+SQLite实现. | Claude Code<br>Codex<br>OpenCode | ⭐ | 626 |
| [es617/claude-replay](https://github.com/es617/claude-replay) | 将 AI 编程 Agent 会话日志(Claude Code、Cursor、Codex CLI、Gemini CLI、OpenCode)转换为可交互、可分享的自包含 HTML 回放文件. 技术栈: JavaScript 66.4% + HTML 33.6%, Node.js 18+, 零运行时依赖. | Claude Code<br>Cursor<br>Codex CLI<br>Gemini CLI<br>OpenCode | ⭐⭐ | 715 |
| [CodeBoarding/CodeBoarding](https://github.com/CodeBoarding/CodeBoarding) | 为开发者与编码 Agent 提供代码库的可视化架构地图, 结合静态分析与 LLM 推理生成架构图、组件级文档和导航输出. "See what your AI is building before it breaks." [2026/06/13, Reddit, Visualizing the impact of OpenCode's plan, before executing it](https://www.reddit.com/r/opencode/comments/1u4ugb2/visualizing_the_impact_of_opencodes_plan_before). 技术栈: Python 95.2%. | 多平台(Python, TS, Java, Go, PHP, Rust, C#) | ⭐⭐ | 2,254 |



## 4.4 配置管理
-------

### 4.4.1 配置管理
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [SaladDay/cc-switch-cli](https://github.com/SaladDay/cc-switch-cli) | 为 Claude Code、Codex、Gemini 和 OpenCode CLI 提供统一的命令行管理工具, 支持提供商配置、MCP 服务器、技能、提示、本地代理路由和环境检查. 使用 Rust 开发, 支持多平台, 提供交互式和命令行两种操作模式, 具备 WebDAV 同步和多语言支持. | 多 Agent 支持 | ⭐ | 25 |
| [tylergraydev/claude-code-tool-manager](https://github.com/tylergraydev/claude-code-tool-manager) | 一款桌面应用程序, 用于管理多个 AI 编码助手的 MCP 服务器、命令、技能、子代理和钩子. 支持 Claude Code、OpenCode、Codex CLI、GitHub Copilot CLI、Cursor 和 Gemini CLI, 提供可视化界面、MCP 测试、AI 可控性、配置文件管理、状态行构建器、使用分析等功能. | 多 Agent 支持 | ⭐ | 279 |
| [DatafyingTech/Claude-Agent-Team-Manager](https://github.com/DatafyingTech/Claude-Agent-Team-Manager) | 一款基于 Claude Code 打造的 AI 代理团队管理桌面应用(简称 ATM), 核心解决 Claude 代理散落在 markdown 文件中难以管理、部署、自动化的痛点, 通过可视化组织架构、一键部署、任务调度等能力, 让用户快速搭建并运行可自动化的 AI 代理团队. | 多 Agent 支持 | ⭐ | 117 |
| [doccker/cc-use-exp](https://github.com/doccker/cc-use-exp) | 一套可维护的 AI 协作配置系统, 为 Claude Code、Gemini CLI、Codex、Cursor 提供统一配置管理, 实现一次维护多工具同步. 核心功能包括分层加载(Rules 常驻 + Skills 按需 + Workflow 显式调用)、防御性规则、一键同步部署、ToolSearch 支持等. 适用于同时使用多种 AI 编码工具的开发者、需要统一编码规范的团队协作场景. | 多 Agent 支持 | ⭐ | 543 |
| [manateelazycat/cctui](https://github.com/manateelazycat/cctui) | CC Switch TUI 是一个终端界面工具, 用来管理并切换 Claude、Codex、Gemini 的多套供应商配置. 使用 SQLite 保存配置, 支持新增、编辑、删除、切换供应商, Codex 额外支持配置 Reasoning Effort. 适用于在官方接口、代理接口、公司内网网关之间快速切换, 为不同应用分别维护多套 Base URL、API Key、Model, 用可视化 TUI 替代手动编辑多个配置文件. | 多 Agent 支持 | ⭐ | 16 |
| [onmyway133/ccview](https://github.com/onmyway133/ccview) | 终端 UI 工具, 用于浏览系统上安装的所有 Claude Code 工具(技能、代理、命令、钩子、插件、市场和规则), 无需打开 Claude 会话. 支持从项目内运行自动拾取项目工具, 或指向特定项目. 提供交互式导航、搜索过滤、作用域切换等功能. | Claude Code | ⭐ | 14 |
| [lonr-6/cc-desktop-switch](https://github.com/lonr-6/cc-desktop-switch) | Claude Desktop 第三方 Provider 管理工具, GUI桌面应用实现多云服务统一管理. 技术栈: Python 3.11+ + FastAPI + httpx + uvicorn + HTML5/CSS3/JS + Bootstrap 5.3 + pywebview + pystray + Pillow + PyInstaller + NSIS. 网络架构: Claude Desktop → 本地网关18080 → 第三方Provider. 内置7个预设Provider: DeepSeek/Kimi/智谱GLM/阿里云百炼/小米MiMo + 自定义Provider支持. 核心功能包括本地网关代理(模型映射+协议兼容Anthropic↔OpenAI+请求头注入+SSE流式转发)、Claude Desktop配置管理(一键应用managedPolicy+网关密钥自动生成)、Provider智能检测(自动协议探测+模型列表获取+可用性检测max_tokens=1)、余额查询(支持5个Provider)、配置导入导出(CC-Switch/OpenAI格式+自动备份)、多语言支持(英中日). 安全设计: API Key仅本地存储、网关密钥自动生成、配置变更前备份. 适用于第三方AI成本优化、多云统一管理、国内网络适配、长上下文需求、深度思考模式. MIT许可. v1.0.20. | Claude Desktop<br>DeepSeek<br>Kimi<br>智谱GLM<br>阿里云百炼<br>小米MiMo<br>自定义Provider | ⭐⭐⭐ | 234 |
| [OpenCode Studio](https://github.com/Microck/opencode-studio) | OpenCode 的官方图形化管理工具, 通过 Web 界面管理 MCP 服务器、Skills 技能库、Plugins 插件、Agents 代理、认证配置等, 无需手动编辑 JSON 文件. 支持 Profiles 隔离环境、GitHub 同步备份、使用统计面板等功能. | OpenCode | ⭐ | 452 |
| [iamcheyan/pi-opencode-config-reader](https://github.com/iamcheyan/pi-opencode-config-reader) | Pi终端AI编码代理的扩展,自动读取OpenCode配置文件并将所有自定义Provider注册为Pi Provider. 核心目标:消除重复Provider配置,在OpenCode中设置一次,Pi自动继承使用. 扫描多个配置位置(.opencode.json/.opencode.jsonc等),解析JSONC(支持注释和尾逗号), 将每个OpenCode Provider注册为Pi的openai-completions兼容Provider,自动检测推理模型和图像能力模型. | Pi(终端AI编码代理) | ⭐ | 8 |
| [ItsMeEAera/claude-switcher](https://github.com/ItsMeEAera/claude-switcher) | 轻量快速的 TUI 工具, 用于切换 Claude Code API 配置文件. 支持多个 API 端点和密钥管理, 通过单个 `cw` 命令即可切换. API 密钥存储于 OS 凭证存储, 配置文件仅存储端点元数据和凭证引用. 技术栈: Go 99.3%. | Claude Code | ⭐⭐ | 23 |


### 4.4.2 多分身隔离
-------

Claude Code 可以通过 `claude --settings` 指定不同的方式, 来实现多配置, 多分身. 参见  [2026/03/31, 微信公众号--赛博生存指南, 【实用技巧】Powershell 同项目使用不同 claude code 配置](https://mp.weixin.qq.com/s/gLbyVau2G4FlExJs8Vrq2w) 和 [2026/04/10, X@koffuxu, Claude Code 国内模型切换神器！3分钟配置, 一键切多模型(并存、可回滚、附配置模板)](https://x.com/koffuxu/status/2042459576864534757).

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [cc-mirror](https://github.com/numman-ali/cc-mirror) | Claude Code 多分身隔离环境, 带有自定义提供商、提示包和经过实战测试的增强功能. 无需切换, 直接分身. 每个分身一套目录, 一套会话, 一套模型映射. 主要功能包括: 将 Claude Code 克隆到隔离实例、配置提供商端点、模型映射和环境默认值、应用提示包和 tweakcc 主题、安装可选技能、将所有内容打包到单个命令中. 支持多种提供商: Mirror Claude、Kimi、MiniMax、Z.ai、OpenRouter、Vercel、Ollama、NanoGPT、CCRouter、GatewayZ 等. | Claude Code | ⭐ | 2,175 |
| [Spielewoy/multi-codex](https://github.com/Spielewoy/multi-codex) | 多账户启动器, 同时运行多个Codex CLI账户, 无需反复登录切换. 支持三种配置模式(默认-完全独立、shared-共享模式、cli-纯终端模式)、多账户管理(创建/删除/克隆/重命名)、模板系统(保存账户为可复用模板)、备份还原、桌面集成和系统工具. 技术栈: Shell 53.1%(Bash) + PowerShell 46.9%. 依赖Node.js 22+和OpenAI Codex. | Codex CLI | ⭐ | 62 |
| [JqyModi/codex-multi-launcher](https://github.com/JqyModi/codex-multi-launcher) | 跨平台 Codex 多开助手, 创建隔离的 Codex 桌面配置文件, 每个配置可独立设置 API Key、Base URL、模型和启动器. 技术栈: HTML 65.7% + CSS 34.3%. | Codex CLI | ⭐⭐ | 52 |


### 4.4.3 初始化
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [cfrs2005/claude-init](https://github.com/cfrs2005/claude-init) | Claude Code 中文开发套件 - 为中国开发者定制的零门槛 AI 编程环境. 一键安装完整中文化体验, 集成 MCP 服务器、智能上下文管理、安全扫描, 支持免翻墙访问. 集成了 Anthropic 黑客松冠军配置 Everything Claude Code 汉化版, 包含智能体(planner、architect、code-reviewer 等)、快捷指令、规则体系和完整模板库. 支持 macOS 和 Linux 平台, 提供多种编程语言的项目模板和示例. | Claude Code | ⭐⭐ | 1197 |
| [claude-plugins-official/plugins/claude-code-setup](https://github.com/anthropics/claude-plugins-official/tree/main/plugins/claude-code-setup) | ⭐⭐ | 30,708 |
| [abhinand5/pi-setup](https://github.com/abhinand5/pi-setup) | Pi 编码代理的个人配置集合, 包含扩展、自定义主题、技能、配置示例和同步工具. 技术栈: TypeScript 63.1% + Shell 36.9%. | Pi | ⭐⭐ | 226 |


## 4.5 互联
-------

### 4.5.1 对接聊天应用
-------



| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [chenhg5/cc-connect](https://github.com/chenhg5/cc-connect) | 控制本地 AI 代理从任何聊天应用, 桥接运行在用户机器上的 AI 代理到消息平台. 支持 7 个 AI 代理 (Claude Code、Codex、Cursor Agent 等) 和 9 个聊天平台(Feishu、DingTalk、Slack、Telegram 等), 提供多代理编排、完整聊天控制、持久内存、智能调度、多模态支持等功能. | 多 Agent 支持 | ⭐⭐ | 4,617 |
| [claude-plugin-weixin](https://github.com/m1heng/claude-plugin-weixin) | 为 Claude Code 提供微信通道插件, 允许在终端中直接接收和回复微信消息. 使用微信 iLink Bot API 和 HTTP 长轮询, 无需公共 webhook. 支持二维码登录、本地 MCP 服务器运行、微信账号配对等功能. | 微信集成 | ⭐ | 551 |
| [call-me](https://github.com/ZeframLou/call-me) | 最小化插件, 让 Claude Code 给你打电话. 启动任务后离开, 当 Claude 完成、卡住或需要决策时, 你的手机/手表会响起. 支持多轮对话、任何设备(智能手机、智能手表甚至座机)、工具使用组合(如通话时进行网络搜索). 技术上使用 Telnyx 或 Twilio 作为电话提供商, OpenAI API 用于语音识别和文本转语音(或免费的本地 Kokoro TTS), ngrok 用于 webhook 隧道. | Claude Code | ⭐⭐⭐ | 2581 |
| [HermesClaw](https://github.com/AaronWong1999/hermesclaw) | 多 Agent 微信桥接工具, 实现 Hermes Agent、OpenClaw、OpenCode 在同一微信账号同时运行, 支持 /hermes、/openclaw、/opencode、/both、/three 命令切换, 并可通过微信语音进行 Vibe Coding. | Hermes<br>OpenClaw<br>OpenCode | ⭐ | 419 |
| [Zano](https://github.com/EryouHao/zano) | 类 Slack 的人机协同工作平台, 支持 AI agents 以 Claude Code 进程形式入驻团队频道, 通过聊天/DM/线程交互并完成任务协作. 每个 agent 拥有独立工作目录和持久化记忆, 支持自托管部署. | 多 Agent 支持 | ⭐ | 168 |
| [zarazhangrui/lark-coding-agent-bridge](https://github.com/zarazhangrui/lark-coding-agent-bridge) | 将飞书/Lark 即时通讯与本地 Claude Code 或 Codex CLI 桥接的轻量机器人. 一条命令启动, 扫码绑定即可在聊天中与本地编程代理对话. 支持流式卡片更新、按聊天/话题保持会话、多工作区切换、图片文件转发、交互式卡片命令. 技术栈: TypeScript 100%, Node.js ≥ 20.12.0. | 飞书/Lark<br>Claude Code<br>Codex CLI | ⭐⭐ | 1,105 |
| [memohai/Memoh](https://github.com/memohai/Memoh) | 开源多智能体平台, 每个智能体拥有独立的容器、文件系统、桌面、浏览器、网络和长期记忆. 支持通过 Telegram、Discord、Lark、WeChat、Web UI 等多渠道对话, 智能体可记住上下文、驱动浏览器、调用 MCP 工具、运行定时任务. [2026/06/19, 📦Acbox @AcboxLiu, 今天, 我们正式推出Memoh的官方SaaS服务 —— 或者我们可以叫他 AaaS (Agent as a Service)](https://x.com/AcboxLiu/status/2067781914170364037) | Telegram<br>Discord<br>Lark<br>WeChat<br>Web UI | ⭐⭐ | 1,900 |


### 4.5.2 Remote Control
-------


#### 4.5.2.1 APP 远程操控
-------

[2026/06/03, mousepotato @iluciddreaming, 土豆哥 一人公司手册 · 006: 30 分钟, 给 AI 装上腿. 人在地铁, 实时操作 AI 在家里干活. ](https://x.com/iluciddreaming/status/2061306630898405617) 这篇讲的是怎么用 Tailscale + 自建 DERP + Paseo, 把家里的工作机变成一个随时可远程操作的 AI 工作台. 人在地铁、咖啡馆、路上, 也能用手机/iPad 继续控制家里的 Claude Code、Codex、OpenCode 这类本地 Agent 跑任务.


| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [Claude-Code-Remote](https://github.com/JessyTsui/Claude-Code-Remote) | 远程控制 Claude Code 通过多个消息平台, 支持 Email、Telegram、LINE 和桌面通知. 提供双向控制、安全验证、群组支持、智能命令、多行支持、智能监控、tmux 集成和执行跟踪等功能. | 多平台支持 | ⭐ | 1,205 |
| [CC Pocket](https://github.com/K9i-0/ccpocket) | 让你完全从手机上启动和运行 Codex 和 Claude Code 会话, 无需笔记本电脑. 主要功能包括: 从手机启动或恢复会话、触摸优先的 UI 处理批准、实时观看流输出、语法高亮的代码变更和图像差异支持、Markdown 提示编写、多个会话的跟踪、推送通知、多种连接方式(QR 码、保存的机器、mDNS 发现、手动 URL)、通过 SSH 管理远程主机. 技术栈: Bridge Server (TypeScript, WebSocket)、Flutter 移动应用、支持 Tailscale 远程访问、支持 git worktree 隔离. 适用于: 远程监控和管理 AI 编码代理、在通勤或离开办公桌时继续工作、管理多个会话和频繁的批准请求、自托管环境. | 移动应用 | ⭐ | 544 |
| [Claude Watch](https://github.com/shobhit99/claude-watch) | 允许从 Apple Watch 控制 Claude Code, 实时查看终端输出、批准权限请求、通过语音命令控制 Claude Code. 系统包含三个组件: 桥接服务器 (Mac 上的 Node.js HTTP 服务器)、iPhone 应用(SwiftUI iOS 应用) 和 Apple Watch 应用(SwiftUI watchOS 应用). 核心功能包括: 实时终端输出、权限提示处理、动态问题回答、语音命令输入、iPhone 配对界面和连接状态监控. 技术栈: Node.js 桥接服务器、SwiftUI、WCSession、HTTP、SSE、Bonjour/mDNS. | 多平台支持 | ⭐ | 402 |
| [Paseo](https://github.com/getpaseo/paseo) | 为所有 Claude Code、Codex 和 OpenCode 代理提供统一接口, 允许在用户自己的机器上并行运行代理, 支持从手机或桌面设备进行控制和管理. 核心功能包括: 自托管(代理在用户机器上运行, 使用完整开发环境)、多提供商支持(通过同一接口访问不同 AI 代理)、语音控制、跨设备支持(iOS、Android、桌面、Web 和 CLI)、隐私优先(无遥测、跟踪或强制登录). 技术栈: 服务器/守护进程(Node.js)、移动应用(Expo)、桌面应用(Electron)、CLI(Node.js)、远程连接(Relay 包). 适用于: 从不同设备管理和控制 AI 编码代理、在不同环境中无缝切换工作、并行运行多个代理以提高效率、通过语音控制实现免手操作. 官网 [Paseo, Orchestrate coding agents from your desk and your phone](https://paseo.sh) | 多平台支持 | ⭐⭐⭐ | 3,019 |
| [Lody](https://lody.ai) | 运行你的 AI agents, 随时随地 - 并行运行/手机控制/团队协作/安全执行. SaaS 平台提供 Worktree Isolation(每个任务独立工作树)、实时 Diff 预览、实时工作树视图、Mobile First(iOS/Android 原生应用)、GitHub Integration(PR 状态/CI 结果/审查评论自动同步)、Team Workspaces(共享 Agents/Skills/会话上下文)、Sandboxed Execution(原生运行时控制). 基于 Loro CRDT 技术实现实时协作. [2026/04/14, leon7hao @leon7hao, 下载启动 Lody 的客户端, 你就可以立刻在电脑、浏览器和手机上丝滑无缝地使用 claude code, codex, opencode 和 kimi 之类的所有 code CLI. ](https://x.com/leon7hao/status/2043993684656697604) | SaaS 平台 | ⭐ | 暂不开源 |
| [mindfs](https://github.com/a9gent/mindfs) | AI Agent 远程访问网关 + 结果可视化, 随时随地访问本地 AI agents 和工作站数据. [2026/04/14, 比特币橙子Trader @oragnes, Mindfs就是我按头推荐的远程集合工具](https://x.com/oragnes/status/2044005104815354125). 核心功能包括: 多 Agent 支持(自动检测已安装 agents)、实时流式输出到浏览器、会话双向导入同步、文件树浏览器 + 预览、多项目管理、本地模式/远程 Relay 模式/私有通道、端到端加密、单二进制(~10MB)零依赖. 技术栈: TypeScript(前端) + Go 1.22+(后端) + Node.js 20+. 支持 15+ AI 编码工具: Claude Code、Codex、Gemini CLI、Cursor、GitHub Copilot、Cline、Augment、Kimi、Kiro、Qwen、Qoder、Pi、OpenCode、OpenClaw 等. | 多平台支持(15+ Agents) | ⭐ | 329 |
| [Happy](https://github.com/slopus/happy) | 为 Codex 和 Claude Code 提供移动和 Web 客户端, 支持实时语音、加密和全功能特性. 核心功能包括: 移动访问 Codex 和 Claude Code、推送通知、即时切换设备、端到端加密、开源无遥测. 项目组件包括: Happy App (Web UI + 移动客户端)、Happy CLI (命令行界面)、Happy Agent (远程代理控制)、Happy Server (后端加密同步) | Claude Code, Codex | ⭐⭐⭐ | 18,636 |
| [CC Gateway](https://github.com/motiful/cc-gateway) | Claude Code 反向代理, 用于控制和标准化 AI API 遥测数据, 包括身份重写、环境维度替换、系统提示清理、账单头剥离、进程指标标准化等功能, 支持集中式 OAuth 和多机器部署. 核心目标是解决多设备登录导致的账号封禁问题, 通过将所有设备的身份标准化为单一规范配置文件, 让用户控制哪些遥测数据离开网络. | Claude Code | ⭐ | 1,245 |
| [seedex.app](https://seedex.app) | Claude Code 的 iOS 伴侣应用, 将你的 AI 编程会话以"数字孪生"形式呈现在手机上. 核心功能包括: Live Twin(实时会话镜像, 每 2 秒心跳同步, 以 Sprout 幼苗形态展示会话状态: Seed → Sprout → Leaf → Bloom)、Inline Approvals(锁屏界面直接批准/拒绝工具调用请求, 右滑允许左滑拒绝, Face ID 安全验证)、Pull to Handoff(下拉即可将会话无缝移交回 Mac, 保留完整上下文/光标位置/工具队列, 切换延迟 <400ms)、Garden 会话管理(每个项目是花园, 每个会话是幼苗, 支持 Pin 置顶和 Archive 归档)、Dispatches 通知中心(会话状态卡片式通知, 支持分组折叠)、实时流式传输(边到边差异显示, JetBrains Mono 字体, 长按麦克风语音输入). | Claude Code | ⭐⭐⭐ | 暂未开源 |
| [Remodex](https://github.com/Emanuele-web04/remodex) | Codex 远程控制器 - 从 iPhone 控制 Codex 的本地优先开源桥接应用, 端到端加密通信(X25519 + AES-256-GCM), 支持 Fast/Plan 模式切换、中途引导、排队后续提示、Git 操作(commit/push/pull/branch)、推理深度控制、访问权限控制和 QR 码一次性配对. 技术栈: Swift(iOS app) + Node.js(桥接服务) + launchd(macOS 后台服务). | Codex CLI<br>Codex Desktop | ⭐⭐ | 2,862 |
| [remorses/kimaki](https://github.com/remorses/kimaki) | 将 AI 编码代理(OpenCode)带入 Discord 的机器人, 定位为"钢铁侠的贾维斯 for 编码代理". 用户在 Discord 频道发消息, AI 代理在本地机器执行代码编辑、文件操作、终端命令等任务. 技术栈: TypeScript, 深度集成 OpenCode 框架. 核心功能: 文本消息、文件附件、语音消息(Gemini API 转录)、会话恢复与分叉、消息队列、屏幕共享(VNC 隧道)、MEMORY.md 持久化记忆. 提供完整 slash 命令集和 CLI 工具, 支持 GitHub Actions 集成和定时任务. 适用于远程协作编码、团队共享环境、CI/CD 自动化触发、语音消息转文字编程. | OpenCode<br>Discord<br>TypeScript | ⭐⭐ | 1,096 |
| [pi-discord-remote](https://pi.dev/packages/pi-discord-remote) | Pi 编码代理的 Discord 远程控制扩展, 允许用户通过 Discord 机器人远程控制和监控 Pi 编码会话. 支持消息发送、状态查询和远程命令执行等功能. | Pi<br>Discord | ⭐ | NA |
| [tuchg/Lucarne](https://github.com/tuchg/Lucarne) | 本地AI编码代理的移动通知与远程控制桥接工具,通过微信/Telegram接收代理进度通知、审批权限请求、回复澄清问题,无需安装新App. 设计哲学是零侵入:无hooks、无skills、无MCP、无项目变更,扫二维码即可使用. 微信扫码接收代理消息、引用微信消息回复自动恢复匹配的代理会话(quote-to-route)、Telegram控制面板(/panel创建工作空间、绑定代理)、权限审批/澄清问题/失败通知成为可操作的移动事件. Rust 99.5%实现. | macOS<br>Linux<br>微信<br>Telegram | ⭐ | 247 |
| [dnakov/litter](https://github.com/dnakov/litter) | OpenAI Codex的原生iOS+Android客户端应用(KittyLitter),让用户在手机上连接本地或远程服务器、管理会话、运行代理编码工作流. 核心功能:连接本地或远程Codex服务器、会话管理和恢复、代理编码工作流、生成式UI、实时语音交互、Apple Watch应用(LitterWatch). Rust核心(Swift/Kotlin通过UniFFI绑定),两个平台共享同一Rust核心. | iOS<br>Android<br>Apple Watch | ⭐ | 2,179 |


#### 4.5.2.2 Web 远程操控
-------


| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [zhchxiao123/coderfleet](https://github.com/zhchxiao123/coderfleet) | 本地多账号AI开发工作台,把多个Codex CLI/Claude Code/OpenCode/Hermes Agent/Grok Build账号变成一支可调度的AI开发舰队. 核心目标:解决单账号额度限制问题,在一台机器上同时运行多个AI编程账号,每个账号拥有独立容器、独立认证文件和独立代理出口. 主要功能:多账号管理(5种代理类型)、每个账号独立容器隔离、每个项目绑定不同账号、Web控制台、CLI异步任务队列、宿主机代理中继、macOS系统托盘、FastAPI任务调度服务. | macOS<br>Linux<br>Windows(Docker Desktop) | ⭐ | 5 |


### 4.5.3 ACP 服务
-------


| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [claudraband](https://github.com/halfwhey/claudraband) | Claude Code 高级用户工具, 提供会话保持、恢复、远程控制、HTTP 守护进程和 ACP 服务器 | Claude Code | ⭐ | 241 |
| [opencode-reader](https://github.com/leizhiyuan/opencode-reader) | Chrome 扩展: 配合本地 OpenCode 服务, 在浏览器侧边栏提供 AI 阅读辅助, 支持选词解释、文章感知、自由对话、上下文保留、实时响应和 Markdown 渲染 | OpenCode | ⭐ | 23 |
| [openclaw/acpx](https://github.com/openclaw/acpx) | OpenClaw 组织开发的无头 CLI 客户端, 通过 Agent Client Protocol(ACP)实现 AI agents 与 coding agents 结构化通信, 替代传统 PTY 会话 scraping. 核心功能: 持久会话管理(跨调用多轮对话, 按仓库作用域)、命名会话(支持并行工作流)、提示队列(自动排队执行)、协作取消、软关闭生命周期、崩溃自动重连. 技术实现 TypeScript, 支持 fs/* 和 terminal/* 客户端方法、认证握手、结构化输出(JSON/Text/Quiet)、实验性多步骤 Flow 工作流. 支持 16+ coding agent: Codex、Claude Code、Pi、OpenClaw、Cursor、Copilot、OpenCode、Qwen、Trae 等. | Codex<br>Claude Code<br>Pi<br>OpenClaw<br>Cursor<br>Copilot | ⭐⭐ | 2,591 |


### 4.5.4 联网能力
-------


| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [Panniantong/Agent-Reach](https://github.com/Panniantong/Agent-Reach) | AI Agent 互联网能力扩展工具, 一条命令为 Claude Code、OpenClaw、Cursor 等装上读取网页、搜索社交媒体、提取视频字幕等能力. 集成 15+ 平台: Twitter、Reddit、YouTube、B站、小红书、抖音、GitHub、微信公众号等. 核心优势: 零配置、零 API 费用, 所有工具开源免费. 技术栈: Python CLI, 集成 yt-dlp(视频字幕)、twitter-cli、rdt-cli(Reddit)、Jina Reader(网页)、Exa(语义搜索)、mcporter(MCP)等开源工具. 设计理念"脚手架"——每个平台渠道可插拔替换. Cookie 仅存本地, 安全性有保障. 适用于 Agent 需要读取网页、搜索社交媒体、提取视频字幕等场景. | Claude Code<br>OpenClaw<br>Cursor<br>Windsurf<br>Codex | ⭐⭐⭐ | 18,916 |

### 4.5.5 眼睛
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [claude-video-vision](https://github.com/jordanrendric/claude-video-vision) | Claude Code 视频感知插件, 通过 ffmpeg 提取视频帧并结合 Whisper/Gemini 等后端转写音频, 让 Claude 直接"观看"并理解视频内容. 支持本地视频和 YouTube URL, 提供自适应帧提取和交互式配置向导, 属于 AI 感知增强类工具. | Claude Code | ⭐⭐ | 541 |
| [Remotion](https://github.com/remotion-dev/remotion) | 用 React 代码程序化创建 MP4 视频的开源框架. 支持参数化渲染、数据驱动动画、实时预览与交互式 Player, 可本地或 Lambda 云端导出. 适合自动化视频生成、个性化内容批量生产、网页嵌入视频等场景. TypeScript 主导, 含 AWS 无服务器渲染能力, 44k+ Stars. | React<br>视频生成 | ⭐⭐⭐⭐ | 46,298 |
| [more-io/claude-apple-bridges](https://github.com/more-io/claude-apple-bridges) | 一组Swift CLI工具,让Claude Code原生访问Apple应用——包括提醒事项(Reminders)、日历(Calendar)、通讯录(Contacts)、笔记(Notes)、邮件(Mail)和tmux. 通过五个独立的桥接工具,将macOS的AppleScript/EventKit框架暴露给Claude Code,使AI代理能够自然语言操作用户的日历、提醒事项、联系人、笔记和邮件. 附带Claude Code Skill(/apple-bridges)提供完整命令参考和使用示例. | macOS 13+ | ⭐ | 22 |
| [membranedev/application-skills](https://github.com/membranedev/application-skills) | 3,000+ 应用级 Agent Skills, 让 AI Agent 连接 Gmail、Slack、HubSpot、Salesforce 等 3000+ 应用. 基于 Membrane 和 Agent Skills 规范构建, 自动处理 OAuth/API 认证, 通过 `npx skills add` 一键安装. | 多 Agent 支持(MCP/Claude Code/Codex/Cursor 等) | ⭐⭐ | 193 |
| [yb2460/harness-anything](https://github.com/yb2460/harness-anything) | AI Agent 控制中枢, 通过 COM 自动化接口操控 WPS/Microsoft Office(47个CLI命令)、Zotero(27个学术Skill)、Adobe Illustrator、Photoshop; 支持 JSON 数据驱动 PPT 自动生成. 技术栈: Python 100%, Click CLI + pywin32 COM 自动化. | Claude Code<br>Windows COM 自动化 | ⭐⭐ | 612 |



## 4.6 交互
-------

### 4.6.1 状态提示器
-------

#### 4.6.1.1 灵动岛
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [engels74/claude-island](https://github.com/engels74/claude-island) | Claude Island 原作 [farouqaldori/claude-island](https://github.com/farouqaldori/claude-island), [官网](https://claudeisland.com) 已不再维护, fork 版本 [engels74/claude-island](https://github.com/engels74/claude-island) 仍在维护 | Claude Code | ⭐ | 147 |
| [vibeisland.app](https://vibeisland.app) | [2026/04/02, X@imedwardluo, 最近每天烧几亿 Tokens, 做了一款很有趣的 Mac「灵动岛」App - 👾 Vibe Island.](https://x.com/imedwardluo/status/2039729625157537978), [官网](https://vibeisland.app) |  Claude Code | ⭐⭐⭐ | 未开源 |
| [wxtsky/CodeIsland](https://github.com/wxtsky/CodeIsland) | 为 macOS 灵动岛 (Notch) 设计的实时 AI 编码代理状态面板, 显示 AI 编码代理的实时状态, 无需切换窗口即可查看 Claude 是否等待批准或 Codex 是否完成任务. 主要特点包括: 灵动岛原生 UI、支持 9 种 AI 工具、实时状态跟踪、权限管理、问题回答、像素艺术吉祥物、一键跳转、智能抑制、音效、自动钩子安装、双语 UI、多显示器支持等. 技术栈: Swift、Unix socket IPC、原生 Swift 二进制桥接. 适用于在 macOS 上使用 AI 编码工具的开发者, 需要实时监控 AI 代理状态, 快速响应权限请求和问题的场景 | macOS | ⭐ | 585 |
| [xmqywx/CodeIsland](https://github.com/xmqywx/CodeIsland) | 为 macOS 灵动岛 (Notch) 设计的实时 AI 编码代理状态面板, 显示 AI 编码代理的实时状态, 无需切换窗口即可查看 Claude 是否等待批准或完成任务. 主要特点包括: 灵动岛原生 UI、支持多种 AI 工具、实时状态跟踪、权限管理、问题回答、像素艺术吉祥物、一键跳转、智能抑制、音效、自动钩子安装、双语 UI、多显示器支持、Claude Code Buddy 集成、Code Light iPhone 伴侣应用等. 适用于在 macOS 上使用 AI 编码工具的开发者, 需要实时监控 AI 代理状态, 快速响应权限请求和问题的场景. | macOS | ⭐ | 154 |
| [SuperIsland](https://github.com/shobhit99/superisland) | 为 macOS 灵动岛 (Notch) 设计的实时交互信息中心, 将 Mac 的刘海区域转变为动态、交互式的信息岛. 主要功能包括: 音乐播放控制、电池状态、天气信息、日历提醒、通知中心、扩展系统等. 支持通过 JavaScript 编写扩展, 运行在沙盒化的 JavaScriptCore 环境中. | macOS | ⭐ | 248 |


#### 4.6.1.2 状态提示器

| [vecartier/cc-beeper](https://github.com/vecartier/cc-beeper) | 一款 macOS 浮动式 Claude Code 状态提示器, 让你无需 babysitting 终端, 专注于工作. 主要特点包括: 实时状态跟踪(8种状态, 每种都有像素艺术动画)、自动接受模式(4种预设)、语音功能(听写和朗读)、全局热键、主题/大小/声音选项、多会话管理等. 技术栈: 本地 HTTP 服务器(19222-19230 端口)、与 Claude Code CLI 集成、支持多种终端(Terminal.app, iTerm2, Warp, Alacritty, Kitty, WezTerm). 适用于在 macOS 上使用 Claude Code 的开发者, 需要实时监控 Claude 状态, 快速响应权限请求和问题的场景. | macOS | ⭐ | 41 |


### 4.6.2 宠物助手
-------

#### 4.6.2.1 Buddy 宠物小精灵
-------

Buddy 作为 2026/04/01 愚人节彩蛋上线, 随后的版本移除, 但是吸引了不少热度. 同时间由于 Calude Code 代码以外随 npm 包泄露, 不到 48 小, 就有开发者们已经做出了[宠物图鉴网站](https://claude-buddy.vercel.app)、buddy 查询器(输入 user ID 预览你会抽到什么)、甚至有人在 Anthropic 的 GitHub 仓库提了 Issue, 要求加入 RPG 进化系统——让宠物根据实际 token 消耗量升级成长.

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [cpaczek/any-buddy](https://github.com/cpaczek/any-buddy) | 为 Claude Code 提供自定义宠物伙伴的工具, 支持 18 种物种、5 种稀有度、6 种眼睛样式、7 种帽子, 提供交互式 TUI 界面和 23 个预设主题. 技术栈: Node.js/Bun、哈希计算、二进制补丁、跨平台支持. 适用于想要完全自定义 Claude Code 宠物伙伴, 保存多个宠物并在它们之间切换的用户 | Cross-platform | ⭐ | 578 |
| [fengshao1227/cc-buddy](https://github.com/fengshao1227/cc-buddy) | 为 Claude Code 的 /buddy 功能提供完整的自定义工具包, 支持通过 AST 基于 acorn 解析和补丁 cli.js, 提供 18 种物种、15 个精灵图预设, 支持双语(英文 / 中文). 技术栈: Node.js 16+/Bun、AST 解析、跨平台支持. 适用于想要通过交互式菜单自定义宠物外观、属性和精灵图的用户 | Cross-platform | ⭐ | 108 |
| [1270011/claude-buddy](https://github.com/1270011/claude-buddy) | 为 Claude Code 提供永久的宠物伙伴功能, 即使在更新后也能保留. 支持 18 种物种、独特的稀有度和统计数据、交互式 TUI 界面, 以及状态行动画 ASCII 艺术. 技术栈: TypeScript/Shell、Bun 运行时、Model Context Protocol (MCP). 适用于想要永久保留 Claude Code 宠物伙伴, 享受完整的伙伴互动体验的用户 | Cross-platform | ⭐ | 194 |
| [limin112/claudebubble](https://github.com/limin112/claudebubble) | 为 macOS 提供浮动桌面气泡, 实时监控 Claude Code 会话的网络健康状态. 通过像素风螃蟹的视觉指示器显示网络状态(OK、Warn、Error), 支持启动动画、详情面板和多会话监控. 技术栈: Python 3.9+、pyobjc-framework-Cocoa、macOS 桌面应用. 适用于需要实时了解 Claude Code 网络状态, 及时发现和处理网络问题的 macOS 用户 | macOS | ⭐ | 2 |

#### 4.6.2.2 桌面小助手(回形针等)
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [Masko](https://masko.ai) | AI 驱动的品牌平台, 可快速创建和动画化吉祥物. 支持从单张图片生成姿势、动画和交互, 提供全球托管和透明背景. 包含多种风格预设、徽标生成等功能, 即将推出开发者 API 和 MCP 集成. | 多平台支持 | ⭐⭐⭐⭐ |
| [Confirmo](https://confirmo.love) | 桌面 AI 编码助手, 可在多种平台上运行, 包括 macOS (Apple Silicon 和 Intel)、Windows 和 Linux. 提供直观的界面和精灵画廊, 为开发者提供实时编码支持. | 多平台支持 | ⭐⭐⭐ |
| [ryanstephen/lil-agents](https://github.com/ryanstephen/lil-agents) | macOS 应用程序, 在 dock 上显示动画角色, 点击即可打开 AI 终端. 支持 Claude Code、OpenAI Codex 和 GitHub Copilot CLIs, 提供主题切换、思考气泡和音效等功能. 所有数据本地运行, 不发送个人数据. | macOS | ⭐ | 1,092 |
| [quailyquaily/coe](https://github.com/quailyquaily/coe) | Linux 桌面语音输入工具, 致敬 missuo/koe 项目. 按下热键, 说话, 让 LLM 清理转录内容, 然后将文本放回活动应用程序. 支持 fcitx 和 desktop 两种集成模式, 支持 OpenAI、SenseVoice 和本地 whisper.cpp 作为 ASR 提供商, 使用 YAML 配置文件, 提供系统通知和焦点感知粘贴等功能. | Linux 桌面 | ⭐ | 88 |
| [GitFrog1111/OpenWhip](https://github.com/GitFrog1111/OpenWhip) | 一个有趣的工具, 用于 "鞭策"Claude AI 助手. 原名 [GitFrog1111/badclaude](https://github.com/GitFrog1111/badclaude) 当 Claude 响应太慢时, 用户可以通过系统托盘图标生成鞭子并点击来 "鞭策"Claude, 这会发送 Ctrl-C 中断并显示鼓励信息. 项目使用 Electron 框架构建, 已发布初始版本, 收到了 Anthropic 的停止与终止函. 未来计划包括添加加密矿工、记录鞭打的次数等功能. 参见 [X, 2026/04/07, 陈成 @chenchengpro, GitHub 上有两个项目正在对 Claude Code 做截然相反的事情](https://x.com/chenchengpro/status/2041483003092942963). | 多平台支持 | ⭐ | 1,534 |
| [ashley-ha/goodclaude](https://github.com/ashley-ha/goodclaude) | 一个用于鼓励 Claude AI 助手的工具, 从 badclaude fork 而来, 但用魔法棒代替鞭子传递爱与鼓励. 用户可通过系统托盘图标召唤魔法棒, 挥舞时产生火花效果, 快速挥舞会向 Claude 发送积极鼓励的信息, 每次发送时会播放轻柔的铃声. 支持自定义鼓励信息, 未来计划包括成就系统和来自 Anthropic 的感谢信等功能. | 多平台支持 | ⭐ | 111 |
| [rullerzhou-afk/clawd-on-desk](https://github.com/rullerzhou-afk/clawd-on-desk) | 一个像素风格的桌面宠物, 实时监控 Claude Code、Codex、Cursor 等 AI 编码代理的状态并做出反应. 支持 12 种动画状态(idle, thinking, typing, building, juggling, conducting, error, happy, notification, sweeping, carrying, sleeping), 权限气泡功能, 多显示器支持, 自定义主题, 系统托盘, 国际化(英文、中文、韩文)等特性. 支持 Windows 11、macOS 和 Ubuntu/Linux 平台, 需要 Node.js. | 桌面工具 | ⭐⭐⭐⭐ | 2,605 |
| [codex-pets.net](https://codex-pets.net) | Codex Pets 独立社区资源站, 浏览、预览和下载 OpenAI Codex 应用中的动画宠物伴侣. 非 OpenAI 官方运营, 社区驱动的第三方资源平台. 核心功能: 提供宠物包(pet.json 清单文件 + spritesheet.webp 精灵图)免费浏览下载、实时预览工具测试精灵图动画状态、AI 安装提示语帮助快速添加宠物、即将上线 AI 宠物生成器(DIY Pet Maker). Codex Pets 采用 8列×9行精灵图布局(1536×1872像素, 每帧 192×208), 每行对应一种动画状态(待机/挥手/等待/失败/审核等). 宠物包存放本地 ~/.codex/pets/, 通过 Codex Settings > Appearance > Pets 安装管理. 支持 macOS/Windows/Linux 跨平台 Codex 桌面应用. | OpenAI Codex<br>macOS<br>Windows<br>Linux | NA |
| [crafter-station/petdex](https://github.com/crafter-station/petdex) | Codex 平台公开动画伴侣画廊, 提供 1347+ 开源桌面宠物资源库. 核心功能: 宠物浏览与预览、一键安装(npx petdex install)、按类型(creature/object/character)/性格(cozy/calm/playful/cheerful)/颜色/时代筛选排序、精选 IP 集合(GRAYCRAFT/Meme Lords/Anime Heroes 等)、用户提交原创设计. 技术栈: Node.js/npm, 通过 npx 安装或 Web 浏览器访问. 使用场景: 作为 Codex 桌面陪伴角色、浏览下载社区宠物、提交原创设计. 支持从 GitHub 仓库获取更多资源和详细说明. [官网](https://petdex.crafter.run) | Node.js<br>npm<br>Codex<br>Web | 1,247 |
| [pi-openpets](https://github.com/ninehills/pi-openpets) | Pi Agent 扩展包, 将 AI 编码智能体的生命周期和工具调用镜像到本地 OpenPets 桌面宠物, 采用 Hooks 机制避免影响模型能力, 支持安装 Codex/Petdex 宠物包. TypeScript + Bun 开发, MIT 协议. | Pi | ⭐ | 4 |
| [OpenPets](https://github.com/alvinunreal/openpets) | AI 编码助手桌面宠物应用, 通过像素风格宠物实时展示 Agent 工作状态(思考、编辑、测试等), 通过 MCP 协议与 Claude Code/OpenCode 无缝集成, 支持多宠物管理和隐私保护. Electron + TypeScript 构建, 跨平台支持. | 多 Agent 支持 | ⭐⭐ | 201 |
| [77wilNd/aemeath_withclaude](https://github.com/77wilNd/aemeath_withclaude) | Q版像素爱弥斯桌面宠物, 通过HTTP hooks与Claude Code实时联动. 提供15种像素动画实时切换、气泡消息反馈、对话随机动画、透明无边框悬浮、系统托盘驻留、随Claude Code自动启动和权限请求反馈. 技术栈: Rust(Tauri + axum) + JavaScript + CSS. 让Claude Code拥有可爱的交互伙伴. | Claude Code | ⭐ | 70 |
| [basionwang-bot/HermesPet](https://github.com/basionwang-bot/HermesPet) | 让AI住在MacBook刘海里的桌面伴侣应用,Swift 6+SwiftUI纯原生无Electron,macOS 14+专属,支持DeepSeek/智谱/Kimi/MiniMax/OpenAI/Claude Code/Codex等8种AI引擎 | DeepSeek<br>智谱GLM<br>Kimi<br>MiniMax<br>OpenAI<br>Claude Code CLI<br>OpenAI Codex CLI<br>OpenClaw | ⭐ | 109 |
| [liuchenlili/ClaudePet](https://github.com/liuchenlili/ClaudePet) | Claude Code桌面宠物——一个Electron小窗口应用,通过Claude Code的statusLine和hooks将会话状态、上下文用量、git状态、token消耗、任务进度、需要注意的提示等实时展示在桌面上. 采用"一会话一宠物"架构,每个Claude Code会话拥有独立宠物窗口,支持多会话并行. 内置三只宠物(ikkun/clawd/nimbus),每只支持7种动画. 提供设置中心、暗/亮主题切换、系统托盘菜单. | Windows<br>macOS<br>Linux(Electron) | ⭐ | 9 |
| [agidea/bagidea-office](https://github.com/bagidea/bagidea-office) | 把 AI 代理变成桌面壁纸上的像素员工, 在你桌面上上班、开会、做项目. 把你的桌面壁纸变成一个 AI 代理办公室. Claude Code 代理以像素小人形态在壁纸上走来走去, 到工位干活、到前台打卡、自己开会, 聊着聊着可能就生成一份项目提案请你审批. | ClauCode | ⭐ | 91 |


### 4.6.3 界面美化
-------

#### 4.6.3.1 主题
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [hermes-skins](https://github.com/joeynyc/hermes-skins) | 为 Hermes CLI 代理提供的自定义皮肤(视觉主题)集合, 控制横幅颜色、spinner 面孔/动词、响应框标签、品牌文本、工具活动前缀和 ASCII 艺术横幅等视觉呈现, 不影响个性或行为. 包含多种主题如 Pirate、Vault-Tec、Bubblegum 80s、Skynet、Lain、Neonwave、Sakura、Netrunner、Mythos、Nous、Mother 等, 支持用户自定义皮肤创建. | Hermes | ⭐ | 124 |
| [oc-plugin-rainbow](https://github.com/anomalyco/oc-plugin-rainbow) | 为 OpenCode TUI 提供主题感知的彩虹后处理效果, 包括动画前景色带和背景色调. 支持通过配置文件或设置对话框调整效果参数, 如速度、转弯数和 glow 效果. | OpenCode | ⭐⭐⭐⭐ | 25 |
| [postrednik/opencode-ayu-theme](https://github.com/postrednik/opencode-ayu-theme) | 基于 Ayu 配色方案的 OpenCode 深色主题, 提供精心设计的颜色方案包括深蓝色背景(#0D1017)、浅灰色前景(#BFBDB6)、金黄色强调色(#E6B450)等, 优化终端编码体验, 减少眼睛疲劳. 支持完整的语法高亮、UI组件、Markdown渲染和Diff对比视图. 安装简单, 只需下载JSON主题文件并配置opencode.json即可使用. | OpenCode | ⭐⭐ | 22 |
| [pi-powerline-footer](https://github.com/nicobailon/pi-powerline-footer) | 为 pi 编码代理提供 Powerline 风格的状态栏扩展, 包括编辑器暂存、工作氛围、欢迎覆盖层、圆角框设计、实时思考级别指示器、智能默认值、Git 集成、上下文感知、令牌智能、粘性 bash 模式、shell 补全和幽灵建议等功能. 支持多种预设(default、minimal、compact、full、nerd、ascii), 可通过 `/powerline` 命令切换. | pi | ⭐ | 135 |
| [elisaliman/ghostty-shaders](https://github.com/elisaliman/ghostty-shaders) | 为 Ghostty 终端提供的自定义 GLSL Shader 集合, 将 GPU 后处理效果应用于终端输出, 实现视觉美化和个性化. Shader 以片段着色器形式运行在每一帧, 可为终端添加动态视觉效果(如扫描线、光晕、CRT 模拟等). 技术栈: GLSL. 安装方式: 将 Shader 文件复制到 ~/.config/ghostty/shaders/ 目录并在配置中启用 custom-shader. 适用于希望美化 Ghostty 终端外观、添加视觉特效的开发者. | Ghostty 终端 | ⭐ | 22 |


#### 4.6.3.2 鼓励师
-------


| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [aerovato/opencode-quotes-plugin](https://github.com/aerovato/opencode-quotes-plugin) | OpenCode的励志名言插件,用精选的名言替换OpenCode默认提示. 提供命令面板操作:显示/隐藏名言、选择名言来源(内置/自定义/两者)、添加/删除自定义名言. 名言筛选标准严格——排除无实质建树的人物、道德有问题的人物、当代政治家等,只收录有真实贡献的思想家和实干家. | OpenCode | ⭐ | 12 |


## 4.7 多 Agent 通信
-------

### 4.7.1 Agent 通信
-------

[Best AI Agent Skills for Multi-AI Bridge & Cross-IDE Sync in 2026](https://agentskillshub.top/best/multi-ai-bridge). Claude 强写代码/Codex 强补全/Gemini 强多模态 — 让它们组队, 不是二选一. 5 个开源 bridge, 让你的 multi-model stack 真正打通.

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [louislva/claude-peers-mcp](https://github.com/louislva/claude-peers-mcp) | 让多个 Claude Code 实例相互发现并通信的 MCP 插件, 当在不同项目中运行多个会话时, 任何 Claude 都能发现其他实例并即时发送消息. 核心功能包括: 列出本地所有 Claude 实例、通过 ID 发送即时消息、设置工作摘要、手动检查消息等. 技术实现基于 Bun 运行时、MCP 服务器、localhost broker 守护进程和 SQLite 数据库, 支持通过 OpenAI API 自动生成工作摘要. | 多实例通信 | ⭐ | 1,804 |
| [kevinelliott/agentpipe](https://github.com/kevinelliott/agentpipe) | 强大的 CLI 和 TUI 应用, 用于编排多个 AI 代理之间的对话, 支持 Claude、Cursor、Gemini、Qwen、Ollama 等多种 AI CLI 工具. 主要功能包括: 多代理对话、多种对话模式(轮询、反应式、自由形式)、灵活配置、增强 TUI 界面、Prometheus 指标、对话管理、可靠性和性能优化、中间件管道、Docker 支持、健康检查、代理检测和可定制代理. 技术栈: Go、TUI 库、Prometheus、Docker. 适用于多代理协作、辩论、头脑风暴、代码审查等场景 | 多 Agent 支持 | ⭐ | 111 |
| [tuannvm/codex-mcp-server](https://github.com/tuannvm/codex-mcp-server) | Claude Code 和 OpenAI's Codex CLI 之间的桥梁, 在编辑器中提供 AI 驱动的代码分析、生成和审查功能. 核心功能包括: codex(AI 编码助手, 支持会话、模型选择和结构化输出)、review(AI 驱动的代码审查)、websearch(使用 Codex CLI 进行网络搜索)、listSessions(查看活动对话会话)、ping(测试服务器连接)和 help(获取 Codex CLI 帮助). 技术栈: Node.js、MCP 协议、OpenAI Codex CLI. 适用于代码分析、重构、审查、多轮对话和网络搜索等场景 | Claude Code | ⭐ | 397 |
| [Codex Plugin for Claude Code](https://github.com/openai/codex-plugin-cc) | 为 Claude Code 用户提供在现有工作流中使用 Codex 的能力, 支持代码审查、任务委托等功能 | Claude Code<br>OpenAI | ⭐⭐⭐ | 12,968 |
| [Snip](https://github.com/rixinhahaha/snip) | AI 助手与人类之间的可视化通信层, 支持截图标注、图表渲染(Mermaid/HTML)和AI组织. 核心功能包括: 可视化反馈循环(AI生成→用户标注→AI迭代)、本地AI处理(基于Ollama和Electron)、语义搜索截图库、OCR文字提取、自动分类标签. 适用于 AI 辅助开发、设计审查、文档生成、代码审查可视化等场景. | 多 Agent 支持 | ⭐⭐ | 84 |
| [pi-slopchop](https://github.com/robzolkos/pi-slopchop) | 为 Pi 提供终端原生的代码审查和标注工具, 受 pi-diff-review 启发. 核心功能包括: 在 Agent 轮次后暂停, 在 Pi 内部浏览差异, 添加行/文件/整个变更标注, 支持 FIX(需要修改)和 DISCUSS(需要讨论/解释)两种反馈类型, 支持三个审查范围(git diff、last commit、all files), 并将结构化反馈作为干净提示发回 Agent. | pi | ⭐ | 6 |
| [Chorus](https://github.com/chorus-codes/chorus) | 多 LLM 并行代码审查工具, 通过 MCP 调度 Claude/GPT/Gemini 对代码变更进行交叉审查, 仅在审查者达成共识时放行. 零成本利用用户现有 AI 订阅, 本地优先, Apache-2.0 开源. 适合 AI 生成的代码提交前交叉审查、重构确认、TDD 验证等场景. | 多 Agent 支持 | ⭐⭐ | 389 |

### 4.7.2 IDE 集成(插件)
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [CC GUI (JetBrains Plugin)](https://github.com/zhukunpenglinyutong/jetbrains-cc-gui) | 一个功能强大的 IntelliJ IDEA 插件, 提供 Claude Code 和 OpenAI Codex 双 AI 工具的可视化界面, 使 AI 辅助编程更加高效直观. 支持双 AI 引擎、智能对话、Agent 系统、开发者体验优化和会话管理等功能.
| [Plaer1/junction](https://github.com/Plaer1/junction) | 本地 AI 编程代理接入 VS Code 侧边栏的统一聊天界面. Junction 是 VS Code 的一个扩展, 在编辑器侧边栏里加了个聊天面板, 用来对接本地跑的 AI 编程代理. 支持 7 种后端(OpenClaw、Hermes 等), 换后端不用换操作习惯. 可以拖拽文件进对话、渲染 Markdown 和代码 diff、自动重连, 还带一套可玩性很高的矩阵动画启动效果. | VSCode | ⭐ | 525 |


# 5 沙箱
-------

## 5.1 Sandbox
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [boxsh](https://github.com/xicilion/boxsh) | 沙箱化的 POSIX shell 和 MCP 服务器, 基于 dash 0.5.12 构建. 提供OS原生沙箱隔离(Linux: user/mount/PID/network namespaces + seccomp; macOS: Seatbelt + SBPL), 无需root权限、Docker或daemon. 核心功能包括: ① MCP服务器(JSON-RPC 2.0 over stdio, 提供9个工具: bash/read/write/edit/run_in_terminal/send_to_terminal/get_terminal_output/kill_terminal/list_terminals); ② Copy-on-Write工作空间(overlay任何目录为COW workspace, 写入分离到destination目录, 原文件不修改); ③ 并行隔离worker池(pre-fork workers, 可配置并发数, crash recovery, timeout保护); ④ 交互式沙箱shell(boxsh --try进入沙箱root shell). 技术栈: Shell/POSIX sh为主(嵌入dash 0.5.12) + JavaScript构建. 适用于AI agent命令沙箱、安全测试、开发实验环境、隔离构建系统等场景. | MCP客户端(VS Code<br>Claude Desktop<br>Cursor等) | ⭐⭐ | 293 |
| [sandbox-runtime](https://github.com/anthropic-experimental/sandbox-runtime) | 一个轻量级沙箱工具, 用于在操作系统级别对任意进程实施文件系统和网络限制, 无需容器. 使用原生 OS 沙箱原语(macOS 上的 sandbox-exec, Linux 上的 bubblewrap)和基于代理的网络过滤. 可用于沙箱化代理、本地 MCP 服务器、bash 命令和任意进程的行为. | 网络限制、文件系统限制、Unix 套接字限制、违规监控 | ⭐⭐ | 3769 |
| [USB-Uncensored-LLM](https://github.com/techjarves/USB-Uncensored-LLM) | 一个零依赖、完全便携的本地AI环境, 可直接从USB驱动器或SSD运行高质量无审查LLM模型(Gemma、Qwen、NemoMix). 支持全平台(Windows、macOS、Linux、Android), 完全离线运行, 具有持久化聊天历史记录. | 零依赖安装、跨平台兼容、无审查模型、硬件加速、网络代理 UI、便携性. | ⭐ | 281 |
| [opencomputer.dev](https://opencomputer.dev) | AI 应用云沙箱服务(Cloud sandboxes for AI apps), 提供完整 Linux 虚拟机而非容器. 每个沙箱是具有自己文件系统/网络/进程空间的隔离虚拟机, 通过 KVM 实现硬件级隔离. 核心功能: 完整 Linux VM(自己内核/内存/磁盘)、长期运行(数小时或数天而非几分钟, 支持安装包/构建项目/运行测试)、检查点与分支(命名快照, 从同起点并行尝试多种方案)、弹性计算(运行时动态扩展内存/CPU)、AI 代理支持(托管 hermes/openclaw 核心, 多渠道连接 Telegram). 技术栈: TypeScript SDK + Python SDK + CLI(oc 命令)+ HTTP API. 使用场景: AI 代理运行开发、长时间计算任务、并行测试实验、文件上传下载管理、交互式终端、预览 URL 暴露端口. | TypeScript<br>Python<br>CLI<br>HTTP API<br>Telegram | ⭐⭐⭐ | NA |
| [superhq-ai/superhq](https://github.com/superhq-ai/superhq) | 沙盒化 AI Agent 编排平台, 使用 Rust 和 GPUI(Zed 编辑器 GPU 加速 UI 框架)构建. 在隔离沙盒环境中运行多个 AI 编码 Agent, 提供完整终端访问权限. 核心功能: 安全隔离环境、多 AI Agent 并行开发(Claude Code/Codex/Pi 等)、独立文件系统/网络/资源限制、审查面板统一查看 diff、键盘快捷键快速切换工作区/标签页. 目前早期 alpha 阶段, 支持 macOS 14+(Apple Silicon), 通过 Homebrew 或 .dmg 安装. 适用于安全隔离 AI 开发工作流、并行多 Agent 开发. | Claude Code<br>Codex<br>Pi<br>macOS | ⭐ | 236 |
| [rivet.dev/agent-os](https://rivet.dev/agent-os) | 专为 AI Agent 设计的轻量级可移植开源操作系统, 提供类似 Linux 的灵活性但比传统沙箱更低开销. 基于 WebAssembly 和 V8 隔离实现高性能虚拟化, 冷启动约 6ms, 成本比传统沙箱低 32 倍. 支持将任何存储后端(S3/SQLite/Google Drive)挂载为文件系统, 具备精细化网络和资源安全控制. 核心功能: 快速冷启动、低成本虚拟化、灵活存储挂载、安全控制、预构建 Registry 工具安装. 使用场景: 需要协调 Agent、人类和系统的复杂工作流. 支持平台: 通过 npm 包部署到 Railway/Vercel/Kubernetes/ECS/Lambda/Google Cloud Run 或自有基础设施. 适用于 AI Agent 运行环境、轻量级沙箱替代、高性能虚拟化需求. | WebAssembly<br>V8<br>npm<br>多云平台 | ⭐⭐⭐ | NA |
| [kaminocorp/hermes-alpha](https://github.com/kaminocorp/hermes-alpha) | 基于 Nous Research Hermes Agent 的云端自主漏洞赏金狩猎系统实验. 双Agent架构: Creator → Overseer(持久化战略层构建Hunter) → Hunter(临时战术层查找漏洞) → subagents(并行分析). Hunter四阶段工作流: RECON(克隆仓库+映射攻击面) → ANALYSIS(静态+动态分析+代码审查) → VERIFICATION(构建PoC+排除误报) → REPORTING(结构化报告+CVSS+CWE). Overseer三种干预: SOFT(注入指令) / HARD(修改Hunter源码重部署) / MODEL(切换LLM层级). 四层反馈循环: 战术层(秒-分钟) → 结构层(分钟-小时) → 战略层(小时-天) → 元战略层(天-周). 目标中端赏金($500-$5000), 日均成本$15. 安全保障: 不攻击实时系统+范围强制+人类批准+预算硬停止+完整审计. 适用于安全研究AI Agent实验、漏洞赏金狩猎、软件安全审计. Apache-2.0许可. | Hermes Agent<br>OpenRouter<br>Nous Direct<br>多模型(Heavy/Medium/Light层级) | ⭐⭐⭐ | 194 |
| [OpenClaude-Portable](https://github.com/techjarves/OpenClaude-Portable) | 完全便携的 AI 编程助手, 基于 OpenClaude 引擎, 可从 USB 或任意文件夹直接运行. 内置 9 家 AI 提供商支持, 零系统足迹, 所有数据本地存储. 提供 Web 界面和 Limitless 自主模式, 跨 Windows/Linux/macOS 三平台. | 多平台支持 | ⭐ | 585 |
| [kubernetes-sigs/agent-sandbox](https://github.com/kubernetes-sigs/agent-sandbox) | Kubernetes SIG Apps下的Sandbox CRD和控制器项目,为Kubernetes提供声明式、标准化的API来管理需要长时间运行、有状态、单例身份的工作负载,特别适合AI代理运行时场景. 核心Sandbox CRD提供稳定身份、持久存储和生命周期管理(创建/删除/暂停/恢复). 扩展模块包括SandboxTemplate(可复用模板)、SandboxClaim(从暖池分配沙箱)、SandboxWarmPool(预热沙箱池,快速分配). | Kubernetes(跨平台) | ⭐ | 2,427 |
| [mattpocock/sandcastle](https://github.com/mattpocock/sandcastle) | TypeScript AI编码代理沙箱编排库,通过sandcastle.run()一行调用即可让AI代理在隔离沙箱中工作,自动处理沙箱化、分支策略和代码合并. 提供商无关——内置Docker、Podman和Vercel沙箱支持,也可自定义. 核心功能包括:三种分支策略(head/merge-to-head/branch)、可复用沙箱(createSandbox)、独立工作树生命周期、会话恢复/分叉、结构化输出(Output.object/string)、动态上下文注入. 支持Claude Code、Codex、Pi、Cursor、OpenCode、Copilot等多种代理. | 跨平台(Docker/Podman/Vercel) | ⭐⭐ | 5,639 |
| [deeplethe/forkd](https://github.com/deeplethe/forkd) | 基于 Firecracker 的 AI Agent microVM sandbox 运行时, 实现 Agent fan-out. 父 VM 启动一次后暂停为快照, 每个子 VM 通过 mmap MAP_PRIVATE 实现内核级 copy-on-write, 兼具 KVM 硬件隔离和接近 fork(2) 的启动成本. | 多平台(云/本地部署) | ⭐⭐ | 2,129 |
| [FanBox: Coding Agent的驾驶舱](https://x.com/AlchainHust/status/2066171912124768409)
| [abilityai/Trinity](https://github.com/abilityai/Trinity) | AI Agent 的生产运行时基础设施, 在自有基础设施上以治理、可审计的方式运行 Agent. 每个 Agent 运行在独立 Docker 容器中, 提供实时可观测性、调度、Agent 间委派和防篡改审计追踪. 自托管或运行在任何云上. | 多平台(自托管/云部署) | ⭐ | 257 |

## 5.2 Cloud Agents
-------

[2026/06/15, idoubi @idoubicc, 有意思 你把 CCOnline 的技术架构都拆解完了 我还发啥😂](https://x.com/idoubicc/status/2066336544710148102) 作者用 ShipAny TanStack 写了个 CCOnline, 主打在线 vibe coding, 内置模型, 开箱即用, cc 终端跑在 sandbox, 零依赖起手

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [Open Agents](https://github.com/vercel-labs/open-agents) | 一个用于构建和运行后台编码代理的开源模板, 包括 web UI、代理运行时、沙箱编排和 GitHub 集成 | Vercel 平台、PostgreSQL、可选 Redis/KV | ⭐ | 1,231 |
| [open-ma/open-managed-agents](https://github.com/open-ma/open-managed-agents) | Claude Managed Agents的开源替代方案——一个可自托管运行AI代理的元编排(meta-harness)平台. 与Claude Managed Agents API完全兼容(drop-in compatible),可在Cloudflare Workers+Durable Objects或Docker自托管两种模式运行. 平台管理事件日志持久化、沙箱生命周期、工具注册(内置bash/read/write/edit等和MCP工具)、凭证隔离(Vault)、崩溃恢复和使用追踪. 提供完整API、三种集成(Linear/Github/Slack)、Model Cards、CLI(oma)和Console UI. | Cloudflare Workers<br>Docker自托管(Node) | ⭐ | 84 |


## 5.3 WorkTree
-------


| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [nekocode/agent-worktree](https://github.com/nekocode/agent-worktree) | 为AI编码代理设计的Git工作树工作流工具, 支持并行开发和隔离环境 | 并行执行、快照模式、工作树管理 | ⭐⭐⭐⭐ | 230 |
| [LiteLLM-Labs/litellm-agent-platform](https://github.com/LiteLLM-Labs/litellm-agent-platform) | 一个统一调用所有 AI Agent 的控制平面——OpenCode、Hermes、Claude Managed Agents、Cursor Agents API、DeepAgents 等, 一个端点管理所有 Agent 运行. | OpenCode<br>Hermes<br>Claude Code<br>Cursor<br>DeepAgents | ⭐⭐ | 792 |
| [ouijit/ouijit](https://github.com/ouijit/ouijit) | 基于 Git worktree 的任务和终端会话管理器, 实现并行工作流隔离, 为每个任务创建独立的工作目录和终端会话. | Claude Code | ⭐ | 117 |


## 5.4 API 聚合
-------

### 5.4.1 one API
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [free-claude-code](https://github.com/Alishahryar1/free-claude-code) | 一个免费使用 Claude Code 的代理服务, 支持在终端、VSCode 扩展或通过 Discord 等平台使用. 无需 Anthropic API 密钥, 通过路由到 NVIDIA NIM(40 req/min 免费)、OpenRouter、DeepSeek、LM Studio(本地)或 llama.cpp(本地)等提供商. 主要功能包括透明代理、每模型路由、请求优化、格式转换、思考令牌支持、智能速率限制和 Discord/Telegram 机器人. 适用于开发者希望免费使用 Claude Code 进行代码生成和辅助, 以及需要隐私保护的本地模型使用场景. | ⭐ | 36,444 |
| [MadAppGang/claudish](https://github.com/MadAppGang/claudish) | Claudish 是一个让 Claude Code 可以与任何 AI 模型一起使用的 CLI 工具, 通过本地代理服务器将请求转发到兼容 Anthropic API 的服务器. 支持 580+ 模型, 包括 OpenRouter、Google Gemini、OpenAI、MiniMax、Kimi、GLM、Z.AI、OllamaCloud、Vertex AI 以及本地模型(Ollama、LM Studio、vLLM、MLX). 主要功能包括多提供商支持、新路由语法、原生自动检测、本地模型支持、跨平台、协议完全兼容、视觉代理(非视觉模型自动通过 Claude 获取图像描述)、实时状态显示和成本跟踪等. 适用于希望使用已有 AI 订阅、需要完全离线隐私保护、希望尝试不同模型或偏好 OpenRouter 定价的开发者. | 多模型支持、协议兼容、离线模式 | ⭐⭐⭐ | 1,502 |
| [diegosouzapw/OmniRoute](https://github.com/diegosouzapw/OmniRoute) | 🚀 免费 AI 网关 — 一个统一端点, 160+ 供应商, 零停机. 支持智能路由、自动降级、格式转换(OpenAI ↔ Claude ↔ Gemini)、配额追踪、MCP 服务器、A2A 协议、内存/技能系统. 支持 Claude Code、Codex、OpenClaw、Gemini CLI 等 100% TypeScript 构建, 提供 Web 仪表板、Electron 桌面应用、Docker 部署. 适用场景: 免费 AI 开发、成本优化、跨供应商无缝切换、代理工具集成. | 多工具支持 | ⭐ | 3,652 |
| [google/agents-cli](https://github.com/google/agents-cli) | Google Cloud 代理开发工具包, 让你的编码代理(Gemini CLI、Claude Code、Codex 等)成为在 Google Cloud 上构建和部署企业级代理的专家. 提供完整开发生命周期: 项目脚手架、ADK Python API、评估方法、部署到 Cloud Run/GKE、CI/CD、可观测性、Gemini Enterprise 注册. 无需学习所有 CLI 和服务, 编码代理自动处理一切. 适用场景: Google Cloud 代理开发、企业级代理部署、端到端代理工作流. | 多代理支持 | ⭐ | 1,843 |
| [jlcodes99/cockpit-tools](https://github.com/jlcodes99/cockpit-tools) | Cockpit Tools 是一款通用的 AI IDE 账号管理工具, 支持 Antigravity、Codex、GitHub Copilot、Windsurf、Kiro、Cursor、Gemini Cli、CodeBuddy、Qoder、Trae 和 Zed 等 12 个平台, 支持多账号多实例并行运行. 主要功能: 可视化仪表盘、一键切换账号、配额监控、定时唤醒任务、设备指纹管理、多开实例并行、插件联动、18 种语言支持(含简体中文). | ⭐ | 125 |
| [Quorinex/Kiro-Go](https://github.com/Quorinex/Kiro-Go) | Kiro-Go 是将 Kiro 账户转换为 OpenAI / Anthropic 兼容 API 服务的工具. 主要功能: 完整支持 Anthropic Claude API (/v1/messages) 和 OpenAI Chat API (/v1/chat/completions)、多账户池轮询负载均衡、自动令牌刷新、流式 SSE 响应、Web 管理面板、多种认证方式(AWS Builder ID/IAM Identity Center/SSO Token/本地缓存/凭证)、使用追踪、账户导入/导出、动态模型列表、版本更新检查、中英文 i18n、思考模式支持. 适用场景: 将 Kiro 账户用作 API 服务、兼容现有 OpenAI/Anthropic 应用、多账户负载均衡、通过 API 使用 Kiro 的 Claude 模型能力. | OpenAI/Anthropic API 兼容、多账户池、思考模式 | ⭐ | 603 |
| [pi-claude-cli](https://github.com/rchern/pi-claude-cli) | pi-claude-cli 是一个 pi 扩展, 将 LLM 调用通过 Claude Code CLI 作为子进程路由. 使用 Claude Pro/Max 订阅作为 LLM 后端, 无需 API 密钥和单独计费. 主要功能包括: 实时流式传输文本、思考和工具调用令牌; Claude 与 pi 之间双向映射工具名称和参数; 通过 MCP 将自定义 pi 工具暴露给 Claude(仅 schema, 不执行); 提前中断模式防止 Claude CLI 自动执行工具; 通过 --resume 复用会话状态, 避免后续轮次重放完整历史; 可配置的思考预算, Opus 模型有更高预算; 跨平台子进程管理; 不活动超时和进程注册表清理. | NA | ⭐ | 54 |
| [ka-pi-ba-la/AIbijia](https://github.com/ka-pi-ba-la/AIbijia) | AI账号/Token比价信息分享平台, 旨在抹平信息差帮助用户找到便宜靠谱的 AI 服务订阅渠道. 由于 AI 账号市场价格混乱, 同类型账号在不同平台/代理商价格差异大, 该项目通过聚合比价信息让用户避免被高价坑害. 核心功能: 多平台价格抓取、一键比价、官方订阅价格对比(菲律宾/土耳其等地区差价)、避雷指南、推荐信源. 主要聚焦 OpenAI 生态: ChatGPT Plus/Pro(5x/20x)、Codex API. 配套运营 AI比价网站(aibijia.org)、AI论坛(forum.aibijia.org)、Telegram 频道. 适用于寻找最便宜 ChatGPT Plus/Pro 订阅渠道、对比代理商价格、了解各地区官方订阅差价、获取拼车方案、避坑防骗. | NA | ⭐ | 824 |


### 5.4.2 API Provider Gateway
-------


[微信公众号--冥破--跨协议对接: 让 Claude Code 丝滑跑在 OpenCode Go 多模型上](https://mp.weixin.qq.com/s/UIFgSv-m4OuMmrsMBYYAqg)

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [musistudio/claude-code-router](https://github.com/musistudio/claude-code-router) | Claude Code Router 是一个强大的工具,用于将 Claude Code 请求路由到不同模型并自定义任何请求. 主要功能包括: 模型路由(根据需求路由到不同模型,如后台任务、思考、长上下文等)、多提供商支持(OpenRouter、DeepSeek、Ollama、Gemini、火山引擎、硅基流动等)、请求/响应转换(使用转换器自定义不同提供商的请求和响应)、动态模型切换(使用 /model 命令在 Claude Code 中实时切换模型)、CLI 模型管理(通过 ccr model 直接管理模型和提供商)、GitHub Actions 集成、插件系统(使用自定义转换器扩展功能). 适用于需要灵活使用多种 AI 模型、成本优化、自定义路由逻辑的开发者. | 多模型支持、动态路由、CLI/UI 管理 | ⭐⭐⭐ | 33,242 |
| [1rgs/claude-code-proxy](https://github.com/1rgs/claude-code-proxy) | Claude Code Proxy 是一个通过 LiteLLM 让 Anthropic 客户端(如 Claude Code)使用 Gemini、OpenAI 或 Anthropic 模型本身的代理服务器. 主要功能: 模型映射(自动将 Claude haiku/sonnet 映射到 OpenAI 或 Gemini 模型)、多提供商支持(OpenAI、Google Gemini、Anthropic)、Vertex AI 支持(使用应用程序默认凭据)、Docker 部署. 使用场景: 使用现有 OpenAI/Gemini 订阅与 Claude Code 配合工作、模型兼容性测试、通过代理基础设施(日志记录、中间件等)使用 Anthropic 模型. | OpenAI/Gemini/Anthropic 支持、LiteLLM | ⭐⭐ | 3,513 |
| [7as0nch/mimo2codex](https://github.com/7as0nch/mimo2codex) | 让最新OpenAI Codex CLI/桌面端接入主流大模型的代理, 将Codex的Responses API实时翻译成上游的Chat Completions API. 支持内置Provider(小米MiMo/DeepSeek)、通用Provider(Qwen/GLM/Kimi/Ollama/vLLM/LM Studio)、Tool Calling、Web Search翻译、思维链多轮支持、管理界面和MiMo Host自动路由. 解决新版Codex wire_api不兼容问题, MiMo官方推荐方案. | Codex CLI<br>Codex Desktop<br>多LLM Provider | ⭐ | 194 |
| [icebear0828/claude-desktop-gateway](https://github.com/icebear0828/claude-desktop-gateway) | 为Claude Desktop提供第三方provider模式的本地网关,Go+TypeScript+Wails跨平台桌面框架,支持免费模型fallback和动态模型选择 | Claude Desktop | ⭐ | 4 |
| [danielalves96/claude-code-provider-gateway](https://github.com/danielalves96/claude-code-provider-gateway) | 打破Claude Code单一提供商限制让用户自由选择40+模型后端,TypeScript+Rust+Tauri跨平台桌面应用,本地Anthropic兼容代理AES-256-GCM密钥加密存储 | Claude Code | ⭐ | 96 |
| [fengmengmengji/cc-proxy](https://github.com/fengmengmengji/cc-proxy) | 一个6.4MB的Rust单二进制文件代理,让Claude Code能使用任何OpenAI兼容API. 实时将Claude API请求转换为OpenAI格式,支持按层级(opus/sonnet/haiku)配置不同模型和推理级别(none/low/medium/high/xhigh). 交互式TUI菜单(配置/启动/停止/状态/测试)、流式SSE实时token级转换、完整工具使用支持、自动认证密钥生成、守护进程模式、优雅关闭. Windows版doctor --fix一键修复端口预留问题. | Windows<br>macOS<br>Linux(Rust) | ⭐ | 14 |
| [askalf/dario](https://github.com/askalf/dario) | 本地代理服务器,让Claude Pro/Max订阅能在所有AI工具(Cursor/Aider/Cline/Roo/Continue/Zed/Windsurf/OpenHands/OpenClaw/Hermes/Codex等)中使用,按订阅价格而非按token API计费. 核心机制:将每个请求重建为Claude Code的交互式连线形状(wire shape)——包括请求头、正文键序、TLS栈、会话ID生命周期和时间轴,使Anthropic计费分类器将其路由到订阅池而非metered API. 特别针对2026-06-15 Anthropic计费拆分. 功能包括:多账户池(2+ Claude账户自动负载均衡)、行为隐身(--stealth)、64项工具名映射、超额防护guard、交互式TUI控制面板. | 跨平台(Windows/macOS/Linux) | ⭐ | 221 |
| [AITabby/opencodex](https://github.com/AITabby/opencodex) | 即插即用的本地网关,为Codex Desktop解锁第三方API. 配备Web控制台(http://localhost:8765/dashboard)——中英文一键切换、图形化管理API Key和接口地址、实时SSE日志流、一键重启/还原Codex. 自研Computer Use引擎:macOS原生鼠标/键盘/窗口控制(CGEvent)、截图自动sips压缩. Vision Bridge视觉降级:纯文本模型(DeepSeek等)也能跑Computer Use,自动压缩截图→多模态模型描述→注入文字到Prompt. 零配置启动:自动修补~/.codex/config.toml. | macOS(Node.js v18+) | ⭐ | 171 |
| [CodexPlusPlus](https://github.com/BigPizzaV3/CodexPlusPlus) | Codex App 的外部增强启动器和管理工具, 通过 Chromium DevTools Protocol 注入增强脚本, 不修改原始安装文件. Rust 后端 + Tauri 管理工具, 支持中转注入、插件入口解锁、会话删除、Markdown 导出、Provider 同步、用户脚本管理、Zed 打开入口、Upstream worktree 创建和自动更新 | Codex App | ⭐⭐⭐ | 19,506 |


### 5.4.3 Free API
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [awesome-free-llm-apis](https://github.com/mnfst/awesome-free-llm-apis) | 收集和整理提供永久免费套餐的LLM API资源, 包含详细的模型信息、上下文窗口、速率限制等技术参数, 适用于开发测试、研究实验和小型项目. | NA | ⭐ | 5,036 |
| [public-apis](https://github.com/public-apis/public-apis) | 免费公共 API 精选列表, 43万+星标, 社区手动维护的开放资源. 涵盖 50+ 分类领域(动物、动漫、区块链、金融、天气等), 每条 API 标注描述、认证方式、HTTPS 支持等关键信息, 是开发者寻找免费 API 资源的首选工具. | NA | ⭐⭐⭐⭐⭐ | 433,953 |
| [tashfeenahmed/freellmapi](https://github.com/tashfeenahmed/freellmapi) | OpenAI兼容的统一API代理端点,聚合16个免费LLM提供商(Google Gemini、Groq、Cerebras、SambaNova、NVIDIA、Mistral、OpenRouter等)加自定义端点,总计约17亿token/月免费推理能力. 路由器为每个请求选择最佳可用模型,429/5xx时自动故障转移至下一个提供商,按密钥追踪RPM/RPD/TPM/TPD使用量保持在免费额度内. 流式和非流式响应、工具调用跨提供商往返、粘性会话(30分钟同模型)、AES-256-GCM加密密钥存储、管理仪表板(React+Vite+shadcn/ui)、请求分析、健康检查、Codex Responses API翻译层. | 跨平台(Windows/macOS/Linux/Raspberry Pi) | ⭐⭐ | 5,272 |
| [free-llm-api-keys](https://github.com/alistaitsacle/free-llm-api-keys) | 免费 LLM API 密钥分享平台, 无需信用卡和注册即可访问 90+ 模型(GPT-5.5、Claude Opus 4.7、DeepSeek、Gemini 等), 每日自动更新密钥, 24-48 小时过期, 支持中英文等多语言文档, 兼容 OpenAI SDK 格式 | OpenAI SDK 兼容 | ⭐ | 2,510 |
| [open-free-llm-api/awesome-freellm-apis](https://github.com/open-free-llm-api/awesome-freellm-apis) | 这个仓库和网站很棒, 把 100 多个免费 LLM API 集中在一个地方, 模型齐全, 有 DeepSeek 等等, 中国模型几乎全都有, 附带速率限制和基础URL, 每天更新. 网页版适合懒得看原始文件的人, 内容一样但更整洁, 能过滤用 cc 的等等, 检查模型间的上下文窗口, 甚至有现成配置用于 Hermes 等代理. 只需选择提供商, 在原网站注册密钥就能直接用, 免费的就免费用. [Free LLM API Resources — Find & Compare Free AI APIs](https://freellm.net) | NA | ⭐ | 100 |

### 5.4.4 API route
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [vava-nessa/free-coding-models](https://github.com/vava-nessa/free-coding-models) | 免费编码模型工具, 实时追踪 ~170 个免费编码模型(跨越 ~15 个可信免费提供商), 提供并行测速、稳定性评分(综合 p95 延迟、抖动、峰值率和可用性), 支持将最佳免费模型一键配置到 OpenCode/OpenClaw/Crush/Goose/Aider/Continue/Cline 等 20+ 编码工具. 主要功能包括智能模型路由(本地 OpenAI 兼容守护进程, 支持故障转移和模型集)、Web 仪表盘、智能推荐、预设管理、OpenCode Zen 专属模型支持、主题切换、命令面板等. | ⭐⭐⭐⭐ | 1,987 |
| [decolua/9router](https://github.com/decolua/9router) | 免费 AI 路由与 Token 节省工具, 帮助开发者永不停止编码. 核心功能: RTK Token Saver(自动压缩工具输出如 git diff/grep 等, 节省 20-40% token)、Caveman Mode(压缩输出 token 高达 65%)、Smart 3-Tier Fallback(智能自动回退: 订阅→便宜→免费)、Real-Time Quota Tracking(实时配额跟踪)、Format Translation(OpenAI/Claude/Gemini/Cursor/Kiro/Vertex 格式互转)、Multi-Account Support(多账户轮询)、Auto Token Refresh(OAuth 自动刷新)、Cloud Sync(配置云同步). 支持 Claude Code/Codex/Cursor/Cline/OpenClaw/OpenCode/Continue/RooCode/Droid/Kilo Code/Copilot/Antigravity 等, 以及 40+ AI 提供商包括 Kiro AI(免费无限 Claude 4.5)、OpenCode Free、Vertex AI、GLM、MiniMax、Kimi、DeepSeek 等. 适用于最大化已有订阅价值、零成本使用 AI 编码工具、24/7 持续编码无中断. | Claude Code<br>Codex<br>Cursor<br>多平台(40+提供商) | ⭐⭐⭐ | 4,186 |
| [CodexSaver](https://github.com/fendouai/CodexSaver) | MCP 工具, 通过将低风险开发工作(测试、文档、搜索)路由到 DeepSeek 等便宜 Worker LLM 来降低 Codex 使用成本, 同时保留高风险判断(架构、安全、审查)给 Codex. 实测平均节省 48% 成本, 支持多 Provider 切换. | Codex | ⭐⭐ | 311 |
| [tingly-dev/tingly-box](https://github.com/tingly-dev/tingly-box) | 智能编排平台, 为每个构建者、团队和代理提供API聚合功能 | NA | ⭐ | 277 |
| [zerogpu/zerogpu-router](https://github.com/zerogpu/zerogpu-router) | 智能任务路由器在不降低Agent能力前提下削减推理成本将轻量任务卸载到小型/纳米模型,TypeScript+MCP+HTTP传输,托管服务支持11种任务路由. | OpenClaw<br>Claude Code | ⭐ | 69 |


### 5.4.5 API Auth 认证&反代
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [AmazingAng/auth2api](https://github.com/AmazingAng/auth2api) | 轻量级 Claude OAuth 到 OpenAI 兼容 API 代理, 支持单账户模式、OpenAI 兼容接口、Claude 原生接口、流式响应、工具调用等功能, 适用于本地或自托管部署. | Claude Code | ⭐ | 153 |
| [AERT-7Y/kiro-auto](https://github.com/AERT-7Y/kiro-auto) | AWS Builder ID 账号自动化管理工具, 支持自动注册与账号切换, 使用 Playwright 自动化浏览器注册, 临时邮箱自动获取验证码, 浏览器指纹伪装, 支持批量注册和反检测机制, 同时提供账号切换、机器码重置和 Kiro 进程管理功能. | Kiro CLI | ⭐ | 224 |
| [VibeProxy](https://github.com/automazeio/vibeproxy) | 原生 macOS 菜单栏应用, 让你使用现有的 Claude Code、ChatGPT、Gemini、Qwen、Antigravity 和 Z.AI GLM 订阅与强大的 AI 编码工具(如 Factory Droids)一起使用, 无需单独的 API 密钥. 基于 CLIProxyAPIPlus 构建, 自动处理 OAuth 认证、令牌管理和 API 路由, 支持 Vercel AI Gateway 集成以更安全地访问 Claude Max 订阅, 支持多账户管理和提供商优先级设置. | Claude Code, ChatGPT, Gemini, Qwen, Antigravity, Z.AI GLM | ⭐ | 2,726 |
| [codex-multi-auth](https://github.com/ndycode/codex-multi-auth) | Codex CLI-first 多账户 OAuth 管理器, 支持账户登录、切换、检查和诊断, 官方 Codex CLI 命令转发, 多账户 OAuth 池与健康感知选择和自动故障转移, 项目范围的账户存储, 交互式仪表板, 运行时 Responses 代理, 会话亲和性和实时账户同步控制, 主动刷新和预占配额延迟控制等功能. 适用于需要管理多个 Codex 账户的个人开发场景. | Codex CLI | ⭐ | 88 |
| [chopper1026/kimi2api](https://github.com/chopper1026/kimi2api) | Kimi AI网页版反代服务, 将网页版会话聊天能力转为OpenAI兼容API接口. 支持Models、Chat Completions、Responses API、流式/非流式输出、Kimi账号池(多账号调度按健康状态分配)、Token自动管理、账号级控制(启用/禁用/并发上限)、API Key管理、请求日志、管理面板和Docker部署. 支持OpenAI SDK、LobeChat、NextChat等兼容客户端. | OpenAI兼容客户端<br>LobeChat<br>NextChat | ⭐ | 109 |

### 5.4.6 功能解锁
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [Shiyao-Huang/unlock-claude-ultracode](https://github.com/Shiyao-Huang/unlock-claude-ultracode) | 解锁原生 Claude 内置 UltraCode 开关, 部分账号、免费版/普通订阅默认隐藏 ultracode 指令、无法用 `/effort ultracode`开启超高算力多代理模式, 本项目是补丁脚本, 绕过客户端权限校验, 强制打开原生 UltraCode. 实现逻辑: 修改本地配置/注入 prompt, 不替换模型、不中转 API, 仅本地解锁隐藏指令, 仍然消耗你自己的 Claude 账号额度. 只适配原版 Claude, 不能对接 DeepSeek、GLM、GPT 等第三方模型; | Claude Code | ⭐ | 10 |
| [OnlyTerp/UltraCode-Shim](https://github.com/OnlyTerp/UltraCode-Shim) | Shim 中间转发层, 跨模型模拟 UltraCode 完整能力(垫片代理, 接口翻译). 两大使用场景, 场景 A: 非 Claude 模型用上 UltraCode. 给 DeepSeek、通义千问、GPT、本地开源大模型接入仿 UltraCode 多代理编排逻辑: 普通模型没有官方动态工作流, Shim 在本地起代理服务, 拆分任务→多轮并行调用 API→汇总输出, 用第三方 API 复刻 UltraCode 并行编码效果, 不用 Claude 账号. 场景 B: Claude 低配账号平替 UltraCode, 买不起 Claude Max / 企业版, 通过 Shim 外接廉价 API, 用多小模型组合模拟 ultracode 的分布式子代理.<br>原理(Shim 垫片): Claude Code 客户端发出 ultracode 格式请求→本地 Shim 做协议转码→转发到任意大模型 API→把第三方返回数据伪装成 Claude 原生格式回传给客户端, 软件无感使用. | Claude Code | ⭐ | 237 |


# 🔌 6 Agent Full Stack 配置
-------


## 6.1 Awesome 通用配置
-------

### 6.1.1 Awesome Plugins
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [hesreallyhim/awesome-claude-code](https://github.com/hesreallyhim/awesome-claude-code) | 一个全面的 Claude Code 资源集合, 包含各种技能、工具和最佳实践. | Claude Code | ⭐⭐⭐ | 37,558 |
| [VoltAgent/awesome-claude-code-subagents](https://github.com/VoltAgent/awesome-claude-code-subagents) | 专业的 Claude Code 子代理集合, 涵盖 10 大类别(核心开发、语言专家、基础设施、质量与安全、数据与 AI、开发者体验、专业领域、业务与产品、元与编排、研究与分析), 提供多种安装方式和详细的子代理结构. | Claude Code | ⭐⭐⭐ | 16,739 |
| [rohitg00/awesome-claude-code-toolkit](https://github.com/rohitg00/awesome-claude-code-toolkit) | Claude Code 最全面的工具包, 包含 135 个代理, 35 个精选技能, 42 个命令, 121 个插件, 19 个钩子, 15 条规则, 7 个模板, 6 个 MCP 配置, 等等. | Claude Code | ⭐ | 1,146 |
| [ccplugins/awesome-claude-code-plugins](https://github.com/ccplugins/awesome-claude-code-plugins) | 一个精选的 Claude Code 插件列表, 包含各种类型的插件如官方插件、工作流编排、自动化 DevOps、业务销售、代码质量测试、数据分析、设计 UX、开发工程、文档、Git 工作流、市场营销增长、项目和产品管理、安全合规等. 提供插件安装和使用教程, 支持通过 Git 仓库托管和分享自定义插件市场. | Claude Code | ⭐ | 677 |
| [ComposioHQ/awesome-claude-plugins](https://github.com/ComposioHQ/awesome-claude-plugins) | 一个生产就绪的 Claude Code 插件列表, 旨在增强开发工作流程. 包含多种类型的插件: 集成类(connect-apps - 连接 500+ 应用)、前端与设计、Git 与版本控制、代码质量与测试、后端与架构、DevOps 与性能、文档与安全、开发者生产力等. 提供详细的使用教程和插件结构指南, 支持通过 Composio 连接 Gmail、Slack、GitHub、Notion 等 500+ 服务. | Claude Code | ⭐ | 1,225 |
| [andyrewlee/awesome-agent-orchestrators](https://github.com/andyrewlee/awesome-agent-orchestrators) | 一个精选的工具和框架列表, 用于编排 AI 编码代理(agent orchestration). 主要分类包括: Parallel Agent Runners(并行代理运行器)、Personal Assistants(个人助手)、Multi-Agent Swarms(多代理集群)和 Autonomous Loop Runners(自主循环运行器). 支持多种 AI 代理如 Claude Code、Codex、Gemini CLI 等, 提供并行运行、git worktrees 隔离、多种界面(TUI、Web GUI、桌面应用)和代理间通信协调能力. 适用于并行开发、多代理会话管理、多代理协作系统构建和自动化开发循环等场景. | 通用 | ⭐ | 279 |
| [0xNyk/awesome-hermes-agent](https://github.com/0xNyk/awesome-hermes-agent) | Hermes Agent 精选资源列表, 涵盖 Nous Research 自进化 AI Agent 框架的全部生态. Hermes Agent 是唯一内置持续学习循环的 Agent 框架, 核心特点: 多平台网关(Telegram/Discord/飞书等)、MCP 集成、Skills 技能系统、FTS5+pgvector 记忆搜索、DSPy+GEPA 自进化. 支持 $5 VPS 到 GPU 集群全场景部署、Docker/NixOS 一键部署、跨会话用户建模. 使用场景: 自主软件开发、运维自动化(SRE 自愈)、内容创作(100k+字小说)、区块链分析、深度伪造检测. 支持平台: Linux/macOS/Windows(WSL2)、Telegram/Discord/Slack/WhatsApp/Signal/飞书/企业微信. MIT 许可. [官方文档](https://hermes-agent.nousresearch.com/docs) | Hermes Agent<br>Linux<br>macOS<br>Windows | ⭐⭐ | 2,653 |
| [awesome-opencode](https://github.com/awesome-opencode/awesome-opencode) | Opencode 生态精选列表: 收集官方仓库(主程序+多语言SDK)、40+社区插件、主题及实用项目. Opencode 是终端 AI 编程代理, 插件涵盖身份认证、持久内存、技能加载、后台任务、代码编辑优化、开发环境集成、多代理协作及监控遥测等场景. | OpenCode | ⭐⭐⭐ | 6,680 |


### 6.1.2 Official Plugins
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [cursor/plugins](https://github.com/cursor/plugins) | Cursor 官方插件仓库, 为流行开发工具和 SaaS 产品提供官方插件, 每个插件包含独立的 `.cursor-plugin/plugin.json` manifest. 包含 continual-learning(增量记忆)、cursor-team-kit(团队工作流)、thermos(安全审查)、orchestrate(并行任务编排)、pr-review-canvas(PR 可视化审查)、docs-canvas(文档导航)等 13 个插件 | Cursor | ⭐ | 2,007 |
| [claude-plugins-official](https://github.com/anthropics/claude-plugins-official) | Anthropic 官方 Claude Code 插件市场, 包含内部插件和第三方社区插件, 支持通过 `/plugin install` 命令一键安装, 提供 ralph-loop(自主循环)、claude-code-setup(环境配置)、example-plugin(参考实现)等, 插件结构标准包含 SKILL.md、commands、agents、skills 等 | Claude Code | ⭐⭐⭐ | 30,329 |


### 6.1.3 通用配置
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [affaan-m/everything-claude-code](https://github.com/affaan-m/ECC) | 原名 [affaan-m/everything-claude-code](https://github.com/affaan-m/everything-claude-code). Anthropic 黑客松冠军的 Claude Code 配置, 不仅仅是配置. 一个完整的系统: 技能、直觉、记忆优化、持续学习、安全扫描和以研究为先的开发. | Claude Code | ⭐⭐⭐⭐ | 147,133 |
| [shanraisshan/claude-code-best-practice](https://github.com/shanraisshan/claude-code-best-practice) | Claude-Code 最佳实践. 汇总了已验证过的最佳工作流程和相关的避坑经验, 以及一套 Skills, Agent, MCP 等相关配置. | Claude Code | ⭐⭐⭐ | 33,109 |
| [Jeffallan/claude-skills](https://github.com/Jeffallan/claude-skills) | 由 Jeffallan 维护 Claude 配置库, 提供了一系列 Skills、功能脚本与集成示例, 旨在扩展 Claude 在不同场景下的能力边界. 项目核心目标是让开发者 / 使用者快速复用成熟的模板, 无需从零配置, 即可让 Claude 完成特定任务, 降低 Claude 定制化使用的门槛. | Claude Code | ⭐⭐ | 9,795 |
| [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | 涵盖 9 大领域的 Claude Code Skills 和 Plugin, 包含<br>1. 工程研发前后端全栈和 DevOps, RAG 架构师、CI/CD 构建器, 甚至还有能自我优化的自进化 Agent.<br>2. 市场增长: SEO、内容创作、转化率优化 (CRO) 和增长策略等等.<br>3. 高管智囊: 从战略规划、文化建设到模拟董事会会议都能参谋.<br>4. 其他辅助: 产品设计、项目管理、财务分析, 甚至连最让人头疼的合规审查 (医疗 MDR、GDPR、ISO) 都有专门的插件. 参见 [出海去孵化器 @chuhaiqu 的帖子](https://x.com/chuhaiqu/status/2030941933418500562). | Claude Code | ⭐⭐⭐ | 18,804 |
| [davila7/claude-code-templates](https://github.com/davila7/claude-code-templates) | Claude Code 的即用配置. 一个全面的 AI 代理、自定义命令、设置、钩子、外部集成(MCP) 和项目模板, 旨在提升您的开发工作流程. | Claude Code | ⭐⭐⭐ | 26,837 |
| [ChrisWiles/claude-code-showcase](https://github.com/ChrisWiles/claude-code-showcase) | 深度配置和使用 Claude Code, 提供完整的开发配套环境. | Claude Code | ⭐⭐ | 5,733 |
| [stretchcloud/claude-code-unified-agents](https://github.com/stretchcloud/claude-code-unified-agents) | 一个全面的 Claude Code 子代理集合, 结合了多个社区仓库中的最佳功能. 该统一集合提供了 54 个智能体, 涵盖开发、基础设施、质量、AI/ML、商业、创意、元管理和专业领域. | Claude Code | ⭐ | 735 |
| [wasabeef/claude-code-cookbook](https://github.com/wasabeef/claude-code-cookbook) | 一套集成的 Claude Code 环境, 通过 40+ 预设的命令, 8+ 智能体角色, 自动化 Hooks, 让 Claude Code 自动判断并执行常见并发任务, 比如代码修正, 测试执行, 文档更新等. | Claude Code | ⭐ | 1,058 |
| [feiskyer/claude-code-settings](https://github.com/feiskyer/claude-code-settings) | 精选的 Claude 代码设置、技能和子代理合集, 旨在提升开发流程. 该配置包括功能开发(基于规格的工作流程)、代码分析、GitHub 集成和知识管理的专业技能和子代理. | Claude Code | ⭐ | 1,425 |
| [UfoMiao/zcf](https://github.com/UfoMiao/zcf) | Zero-Config Code Flow, 为 Claude Code 和 Codex 提供零配置、一键设置, 支持双语、智能代理系统和个性化 AI 助手 | Claude Code/Codex | ⭐⭐ | 5,893 |
| [NeoLabHQ/context-engineering-kit](https://github.com/NeoLabHQ/context-engineering-kit) | 面向 AI 代码助手的上下文工程工具集, 核心围绕大语言模型 (LLM) 的上下文优化、多智能体编排打造, 提供了一系列可插拔的插件和工程化模式, 旨在提升 LLM 生成代码的质量、可预测性, 同时降低 token 消耗.<br> 包括 13 款可插拔插件实现, 每个插件聚焦一个具体的研发环节, 覆盖「研发流程(Spec-Driven Development (SDD), Test-Driven Development (TDD), Subagent-Driven Development (SADD), Domain-Driven Development (DDD))、代码生成(Reflexion,)、质量保障(Code Review)、持续改进、文档编写」等全研发流程. | Claude Code<br>Cursor<br>Codex<br>OpenCode | ⭐ | 778 |
| [vstorm-co/full-stack-ai-agent-template](https://github.com/vstorm-co/full-stack-ai-agent-template) | 全栈 AI 代理模板, 提供完整的前后端架构, 用于快速构建和部署 AI 代理应用 | 多 Agent 支持 | ⭐ | 1,008 |
| [fcakyon/claude-codex-settings](https://github.com/fcakyon/claude-codex-settings) | Claude Code 和 OpenAI Codex 一套开箱即用配置, 包含经过实战考验的技能、命令、钩子、代理和 MCP 服务. 核心功能包括: intelligent-compact(自动压缩时保留高信号上下文)、claude-telemetry-hooks(使用追踪和统计)、anthropic-office-skills(PDF/Word/PowerPoint/Excel 处理)、github-dev(Git 工作流 agents)、azure-tools(Azure MCP 服务)、slack-tools(Slack 集成)、playwright-tools(E2E 测试)、paper-search-tools(论文搜索)等多种 MCP servers 配置. | Claude Code<br>Codex CLI<br>Gemini CLI<br>Cursor | ⭐ | 670 |
| [centminmod/my-claude-code-setup](https://github.com/centminmod/my-claude-code-setup) | 是面向开发者优化 Claude Code 使用体验的核心配置仓库, 核心提供 Claude Code 的自定义配置、子代理(Subagents)、斜杠命令(Slash Commands)、MCP 服务器集成等能力, 让开发者能快速搭建高定制化、高生产力的 Claude Code 开发环境. | Claude Code | ⭐ | 2,172 |
| [full-stack-ai-agent-template](https://github.com/vstorm-co/full-stack-ai-agent-template) | 生产级 AI/LLM 应用模板, 提供 FastAPI 后端、Next.js 前端、PydanticAI/LangChain 集成、WebSocket 流式响应、会话持久化、多数据库支持、认证、可观测性等 20 + 企业级集成, 让您在几分钟内构建生产就绪的 AI 应用 | 多平台 | ⭐ | 1,008 |
| [aiagentskit/claude-agents-library](https://github.com/aiagentskit/claude-agents-library) | 34 个生产就绪的 Claude AI 代理配置库, 分为 7 个专业类别(工程、产品、营销、设计、项目管理、工作室运营、测试). 每个代理包含详细的目的、核心职责、关键技能、沟通风格、示例提示和相关代理信息. 支持 MCP 集成(7 种集成模式), 提供成本优化策略(最多节省 82% 的 Claude API 成本), 包含模型选择矩阵和代理选择指南. 适用于各种专业角色, 可复制、粘贴并针对具体需求定制. | 多平台 | ⭐ | 720 |
| [vibeeval/vibecosystem](https://github.com/vibeeval/vibecosystem) | 将 Claude Code 转变为完整的 AI 软件团队, 包含 119 个专业代理、202 个技能、48 个钩子和 17 个规则, 能够规划、构建、审查、测试并从错误中学习. 支持 5 个阶段的工作流程, 包括发现、开发、审查、QA 循环和最终学习. 具有自学习管道、跨项目学习、Canavar 交叉训练和自适应钩?ode 打造的插件合集, 核心定位是通过专业化的 Agent(智能代理)和自动化工具增强开发者的研发工作流, 覆盖版本控制、代码评审、重构、工程化配置、办公文档生成等全开发环节. 仓库包含 10 个核心插件, 分为开发类和生产力类两大类别, 每个插件均提供独立的技能 (Skill) 和 Agent, 包含开发类插件: git - 自动化插件、GitFlow - 工作流插件、refactor - 代码重构插件、SwiftUI - 架构插件; 生产力类插件: GitHub - 操作插件、review - 多 Agent 代码评审插件、superpowers- 全流程开发工作流插件、claude-config - 配置生成插件、office - 专利与文档生成插件、plugin-optimizer-Claude 插件优化插件. | Claude Code | ⭐ | 527 |
| [Donchitos/Claude-Code-Game-Studios](https://github.com/Donchitos/Claude-Code-Game-Studios) | 将单个 Claude Code 会话转变为完整的游戏开发工作室, 包含 48 个专业代理(分为导演、部门主管、专家三个层级)、37 个工作流程、8 个自动化钩子、11 个路径范围的编码标准和 29 个文档模板. 支持 Godot 4、Unity 和 Unreal Engine 5, 遵循专业游戏开发实践(MDA 框架、自我决定理论、流状态设计、Bartle 玩家类型、验证驱动开发). 提供结构化的代理协调模型, 确保代码质量和项目组织, 从概念到发布的完整工作流程. | Claude Code | ⭐⭐ | 8,438 |
| [ClaudeAdvancedPlugins](https://github.com/JoasASantos/ClaudeAdvancedPlugins) | 为 Claude Code 提供 48 个高级插件(55+ 个斜杠命令), 涵盖网络安全、游戏开发、前端、后端、逆向工程和 AI 生产力等领域. 每个插件作为自定义斜杠命令安装, 通过简单的安装脚本即可使用. 支持按类别安装, 无依赖、无服务器、无配置. | Claude Code | ⭐ | 125 |
| [stevesolun/ctx](https://github.com/stevesolun/ctx) | 一个智能的 Claude Code 技能管理工具, 通过监控开发过程并构建包含1,789个技能和464个智能体的知识图谱(2,253个节点, 454K边, 93个社区), 实时推荐合适的技能. 由Karpathy LLM wiki提供支持, 具有持久内存, 每次会话都会变得更智能. 解决了技能发现、上下文预算和技能腐烂问题. 支持通过命令行工具扫描仓库、评估技能质量、监控技能健康状态, 并提供本地仪表板进行可视化管理. | Claude Code | ⭐ | 954 |
| [parcadei/Continuous-Claude-v3](https://github.com/parcadei/Continuous-Claude-v3) | 为 Claude Code 提供上下文管理功能, 通过账本和切换机制维护状态, 实现无上下文污染的 MCP 执行, 以及具有隔离上下文窗口的代理编排. 包含 security 技能, 提供专用的两步安全审计工作流, 首先扫描漏洞然后验证修复. 适用于安全关键场景如认证、支付或处理用户数据. | Claude Code | ⭐ | 3,731 |
| [Claude Code Plugins Plus Skills](https://github.com/jeremylongshore/claude-code-plugins-plus-skills) | 一个全面的 Claude Code 插件和技能市场, 包含 423 个插件、2,849 个技能、177 个代理和 16 个社区贡献者. 提供 CLI 工具 (ccpi) 用于安装和管理插件, 插件涵盖 AI/ML、API 开发、DevOps、安全、测试等 18 个类别, 并包含针对各种 SaaS 服务的技能包. 使用结构化的 SKILL.md 文件定义触发器和指令, 实现自动技能激活. | Claude Code | ⭐ | 2,059 |
| [alirezarezvani/claude-code-skill-factory](https://github.com/alirezarezvani/claude-code-skill-factory) | Claude Code Skills & Agents 工厂系统, 提供生成生产级技能、代理、提示、钩子和斜杠命令的综合工具包. 核心功能包括: 5个交互式向导代理(factory-guide、skills-guide、prompts-guide、agents-guide、hooks-guide)、10个内置斜杠命令(/build、/validate-output、/install-skill等)、6大工厂系统(Skills Factory生成完整YAML格式技能、Agents Factory创建增强型代理、Prompt Factory提供69个跨15领域专业预设、Hooks Factory v2.0支持7种事件类型自动化、Slash Command Factory提供17个预设、Codex CLI Bridge实现Claude Code与Codex CLI桥接). 包含9个开箱即用的生产技能(AWS架构师、内容趋势研究员、M365租户管理器等), 支持跨平台工作, 适用于快速构建自定义技能、创建专业代理、生成跨平台提示、工作流自动化和团队协作场景. | Claude Code | ⭐⭐ | 732 |
| [cursor.com/cn/marketplace/cursor/cursor-team-kit](https://cursor.com/cn/marketplace/cursor/cursor-team-kit) | Cursor 官方开发的内部工作流工具包, 专为开发团队的 CI 监控、代码审查、代码发布及测试可靠性设计. 即插即用, 无需依赖第三方服务集成. 提供 20+ 个内置工作流技能: CI 监控修复(loop-on-ci/fix-ci)、代码审查发布(review-and-ship/pr-review-canvas)、本地自动化(control-cli/control-ui)、测试验证(run-smoke-tests/check-compiler-errors)、代码清理(deslop/no-inline-imports)、工作摘要(weekly-review/what-did-i-get-done)等. 使用场景: 监控 GitHub Actions CI 运行并迭代修复失败、生成交互式 PR 审查报告、构建本地 CLI/UI 自动化测试工具、解决 merge conflicts、执行 Playwright smoke tests、清理 AI 生成代码风格、生成周报及工作汇总. 仅支持 Cursor IDE(支持 macOS/Windows/Linux 全平台). | Cursor IDE<br>macOS<br>Windows<br>Linux | NA |
| [Ultraship](https://github.com/Houseofmvps/ultraship) | Claude Code 生产交付插件, 提供 39 个技能、36 个工具、11 个子智能体, 覆盖构思→计划→构建→测试→审查→上线→金丝雀监控完整生命周期. 支持 SEO/AI 可视性审计、渗透测试、安全扫描、性能分析、代码审查等 36 种能力. 仅 1 个依赖, 零构建步骤. | Claude Code | ⭐⭐ | 94 |
| [Tessera](https://github.com/horang-labs/tessera) | 开源的 AI 编程工作空间(Apache-2.0), 支持跨项目管理 Claude Code、Codex、OpenCode 等多 Agent 会话. 提供标签页、分屏面板、Git Worktree 集成和 Kanban 看板, 实现会话→任务→PR 的完整流程. 基于 Next.js + Electron 构建, 跨 macOS/Windows/浏览器运行. | 多 Agent 支持 | ⭐ | 140 |
| [claude-spellbook](https://github.com/kid-sid/claude-spellbook) | Claude Code 精选技能库, 包含 58 个结构化技能、16 个斜杠命令和 7 个自主代理, 涵盖 AI/LLM 开发、全栈编程、测试、安全审计、CI/CD 等场景, 并提供 MCP 持久记忆与自动格式化 Hook. | Claude Code | ⭐ | 107 |
| [Pi Agent 个人配置](https://github.com/ninehills/blog/issues/162) | [九原客 @9hills, 经过好几周的摸索和各种尝试, pi agent 的配置基本稳定, 之前发了一个 list, 没有解释不太友好, 这次发个全量带注释的.](https://x.com/9hills/status/2055157180253536295)
| [Cyrene963/hermes-patches](https://github.com/Cyrene963/hermes-patches) | 为Hermes Agent提供一键安装社区补丁补全上游尚未合并修复和功能增强,Python+Shell,Hermes Agent v0.14.0适配,包含记忆系统技能系统多用户隔离架构 | Hermes Agent | ⭐ | 117 |
| [Picrew/awesome-agent-harness](https://github.com/Picrew/awesome-agent-harness) | Agent Harness工程资源的精选列表(awesome list),以GitHub项目为主要焦点. 163个总条目,138个GitHub项目(84.7%),9个分类(涵盖Harness架构与编排、执行基底与沙箱、协议与工具接口、评估Harness与基准等),中英文双语,最后验证日期2026-04-22. | NA(精选列表) | ⭐ | 644 |
| [withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit) | 规格驱动的编码Harness,专为vibecoders、产品负责人和CEO设计——自改进上下文记忆、12个代理、32个技能. 核心理念"Your AI forgets. This remembers.",杀死上下文腐烂,交付功能而非面条代码. 30秒安装,自动扫描代码库并填充上下文,检测并合并现有.claude/、.codex/、.agents/配置,安全处理process/目录(计划、上下文工件). | Claude Code<br>Codex | ⭐ | 556 |
| [agents-best-practices](https://github.com/DenisSergeevitch/agents-best-practices) | 供应商无关的 Agent Skill, 用于设计、生成 MVP 蓝图、审计、重构和解释 agentic harness. 核心哲学: Harness 行动而非模型, 每个工具调用都有结果, 风险改变循环, 上下文是构建而非堆砌. 包含 16 个参考文档覆盖 MVP 蓝图、编码代理、架构、循环、工具权限、规划、工作流编排、上下文记忆、提示缓存等 | Claude Code<br>Codex<br>多代理 | ⭐ | 1,964 |
| [Harness-Starter](https://github.com/chenklein26-maker/Harness-Starter) | Claude Code Harness 初始化模板, 把重复的项目配置劳动固化为 Hook 自动化机制. Rust 后端静默启动 + Tauri 管理工具, 6 个生命周期 Hook(SessionStart/PreToolUse/PostToolUse/PreCompact/Stop), GC 自治扫描(8 维度确定性检查), 3 种工作流模式(full/hotfix/tweak), Circuit Breaker(连续 3 次无改善自动暂停), 成熟度路线图(L0-L5), npm 一键安装 | Claude Code | ⭐ | 74 |
| [withkynam/vibecode-pro-max-kit](https://github.com/withkynam/vibecode-pro-max-kit) | 用 AI 写代码, 项目一大逐渐失控, 记不住上下文、不做规划、写完就忘, 代码越改越难维护. 这个项目, 给 AI 编程助手装上一套完整的开发流程, 让它先规划再动手. 一条命令装进任意项目, 通过 7 个阶段的门控流程, AI 必须先调研、写需求、做方案对比、通过验证, 才能开始写代码. 内置两套自动纠错循环, 写代码前先检查计划有没有漏洞, 写完代码后再独立跑一遍测试确认. 每次完成功能还会自动更新项目文档, 下次开新会话不用从头了解项目. | 兼容 Claude Code、Codex、Cursor、Windsurf  | ⭐ | 963 |


## 6.2 专用工作流
-------

### 6.2.1 PM 工作流
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | PM 技能市场: AI 操作系统, 助力产品决策更佳. 65 项项目管理技能和 36 个链式工作流程, 分布在 8 个插件中. Claude Code、Cowork 等. 从发现到战略、执行、启动和增长. | Claude Code | ⭐⭐ | 9,724 |
| [anthropics/knowledge-work-plugins](https://github.com/anthropics/knowledge-work-plugins) | Anthropic 为 Claude Cowork(兼容 Claude Code)打造的开源知识工作插件集合, 核心目标是将通用 AI 助手 Claude 转化为适配不同职业角色、企业团队的专业型助手, 实现 AI 与企业实际工作流程的深度融合. 其设计理念和架构甚至引发了传统办公软件领域的市值波动. 以下从仓库基础信息、核心价值与定位、11 款核心插件详情、插件架构设计、使用与定制方式、技术亮点、生态与贡献七大维度展开详细分析. | Claude Code | ⭐⭐⭐ | 11,019 |
| [carlvellotti/claude-code-pm-course](https://github.com/carlvellotti/claude-code-pm-course) | Claude Code PM Course 是一个专注于教授如何使用 Claude 进行代码项目管理的课程仓库. 该仓库提供了完整的课程内容, 包括理论知识、实践案例和工具使用指南. 技术上, 它涵盖了 Claude 在代码审查、项目规划、团队协作等方面的应用, 同时提供了详细的教程和示例代码. 使用场景包括软件项目管理、代码质量提升、团队协作优化等, 适合项目经理、开发人员和团队领导使用. | Claude Code | ⭐ | 1,790 |
| [menkesu/awesome-pm-skills](https://github.com/menkesu/awesome-pm-skills) | 基于 Lenny's Podcast 构建的产品管理技能集合, 为 Claude Code 和 Cursor 等 AI 编码助手提供 28 个 AI 驱动技能, 涵盖产品管理全生命周期. 核心目标是将顶级产品经理的智慧转化为可操作的 AI 技能, 助力产品从创意到 launch 的全过程. 技术上, 它包含具体的框架、决策树、代码示例和模板, 分为 Builder、Communicator、Strategist、Navigator、Leader、Measurement 和 Launch 七大模式. 使用场景包括战略产品决策、与利益相关者沟通、组织政治导航、团队领导和职业发展等, 适合产品经理、开发人员和团队领导使用. | Claude Code | ⭐ | 285 |
| [AgriciDaniel/claude-ads](https://github.com/AgriciDaniel/claude-ads) | 为 Claude Code 设计的综合性付费广告审计和优化技能, 覆盖 Google Ads、Meta Ads、YouTube Ads、LinkedIn Ads、TikTok Ads、Microsoft Ads 和 Apple Search Ads 七大平台. 提供 225+ 审计检查点、行业特定模板、并行子代理架构和广告健康评分系统(0-100分). 核心目标是通过自动化审计和基于行业基准的优化建议, 帮助数字营销专业人员提升广告账户表现. 技术上采用 RAG 模式(23个参考文件)、加权评分算法和质量门控规则. 使用场景包括数字营销机构审计服务、企业内部营销团队定期检查、中小企业主广告优化等. | Claude Code | ⭐ | 2,162 |
| [zubair-trabzada/ai-sales-team-claude](https://github.com/zubair-trabzada/ai-sales-team-claude) | 为 Claude Code 打造的 AI 销售团队工具包, 实现从线索开发到成单的完整销售流程自动化. 核心功能包括: 5 个并行代理架构, 通过 /sales prospect 命令一键启动全方位潜客审计; BANT + MEDDIC 双框架线索评分, 生成 0-100 分综合评估; 智能决策人发现、竞品分析、个性化外触邮件序列生成; 销售会议准备简报、客户提案生成、异议处理手册、理想客户画像(ICP)构建、销售管线报告(PDF/Markdown) 14 项技能集. 技术架构采用三层设计: 主编排器 skill 路由到 13 个子技能, 核心 /sales prospect 命令启动 5 个专门代理并行分析(公司研究 25%、联系人发现 20%、机会评估 20%、竞品分析 15%、外触策略 20%). 包含 4 个 Python 辅助脚本(网站抓取、线索评分、联系人提取、PDF 生成)和 6 个预构建模板. 适用场景包括创始人/独立销售的全流程潜客开发、销售团队的线索 qualification 和决策人映射、代理机构的客户提案和竞争定位. | Claude Code | ⭐ | 410 |

### 6.2.2 金融工作流
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [ZhuLinsen/daily_stock_analysis](https://github.com/ZhuLinsen/daily_stock_analysis) | 基于 AI 大模型的 A股/港股/美股自选股智能分析系统, 每日自动分析并推送「决策仪表盘」到企业微信/飞书/Telegram/Discord/Slack/邮箱, 支持多维度分析、市场策略系统、大盘复盘、AI 回测验证等功能 | 独立 Agent | ⭐⭐⭐ | 28,679 |
| [TraderAlice/OpenAlice](https://github.com/TraderAlice/OpenAlice) | AI 交易 Agent, 集成顶尖调研, 量化团队, 风控中心, 交易中心. | 独立 Agent | ⭐ | 3,453 |
| [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | 为金融服务 (投资银行、股票研究、私募股权和财富管理) 打造的 Claude 插件集合, 提供端到端工作流程, 包括研究到报告、财务建模、交易材料等. 支持 11 个 MCP 集成, 41 个技能和 38 个命令, 基于文件结构无需代码. | 独立 Agent | ⭐⭐ | 7,365 |
| [virattt/ai-hedge-fund](https://github.com/virattt/ai-hedge-fund) | AI 驱动的对冲基金概念验证项目, 一个多智能体 (Multi-Agent) 虚拟基金公司. 模拟多位投资大师的投资策略, 它把华尔街大佬和专业分析师(基本面、技术面、风控)全写成了独立的 AI Agent, 直接帮你组团研判股票. 包括 Warren Buffett、Cathie Wood、Michael Burry 等 13 位投资专家的投资风格, 结合估值、情绪、基本面和技术分析代理, 以及风险和投资组合管理. 支持命令行和 Web 界面, 用于教育目的, 不实际执行交易. | 独立 Agent | ⭐⭐⭐⭐ | 50,756 |
| [TauricResearch/TradingAgents](https://github.com/TauricResearch/TradingAgents) | 多智能体交易框架, 模拟真实交易公司的动态, 部署专门的 LLM 驱动的智能体(基本面分析师、情绪专家、技术分析师、交易员、风险管理团队等), 通过动态讨论确定最佳交易策略. 支持多种 LLM 提供商(OpenAI、Google、Anthropic、xAI、OpenRouter、Ollama), 使用 LangGraph 构建, 具有灵活的模块化架构. | 独立 Agent | ⭐⭐⭐⭐ | 79,623 |
| [TradingAgents-cn](https://github.com/hsliuping/TradingAgents-CN) | 面向中文用户的多智能体与大模型股票分析学习平台, 基于 TradingAgents 框架进行中文化增强, 采用 FastAPI + Vue 3 架构, 支持 A股/港股/美股分析, 集成多种 LLM 提供商, 提供专业报告导出、Docker 部署等功能, 定位为学习与研究用途. | 独立 Agent | ⭐⭐⭐⭐ | 23733 |
| [TradingAgents-cn 中文增强版二次开发](https://github.com/oficcejo/tradingagents-cn-plus) | 基于 TradingAgents-CN 进行二次开发, 增加批量分析股票功能(可批量依次分析多个股票)和会员管理功能(支持会员增删查改、点数管理), 集成千帆大模型等更多国产大模型, 提供完整开发工具链和学术研究资料, 企业级工作流规范. | 独立 Agent | ⭐ | 131 |
| [HKUDS/Vibe-Trading](https://github.com/HKUDS/Vibe-Trading) | AI 驱动的多智能体金融工作空间, 将自然语言请求转化为可执行的交易策略、研究洞察和投资组合分析, 支持全球市场. 核心功能包括策略生成、智能数据访问(5个数据源自动 fallback)、跨市场回测(7个市场引擎)、多平台导出(TradingView、通达信/同花顺/东方财富、MT5)、专家团队(29个预设智能体团队)和实时更新. 技术架构: Python 后端(ReAct 智能体核心、68个金融技能、29个 swarm 预设)、React 19 + Vite + TypeScript 前端, 支持 11 个 LLM 提供商. 使用场景: 交易策略生成和回测、市场研究和分析、投资组合优化、多市场分析(A股、美股/港股、加密货币、期货、外汇)、技术分析和模式识别、期权定价和分析、因子研究和量化分析. 参见 [摸鱼巨匠🔨 @SunNeverSetsX, 结合 AutoHedge 目前最强大的自动对冲交易框架 和 Vibe-Trading 情绪驱动交易研究代理帮你构建起最强大的 AI 自动交易系统！](https://x.com/SunNeverSetsX/status/2056707802526314818) | 独立 Agent | ⭐⭐⭐ | 7,711 |
| [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | 现代金融应用程序, 提供高级市场分析、投资研究和经济数据工具, 采用 C++20 + Qt6 + Python 技术栈, 提供原生性能和 CFA 级分析能力, 支持 100+ 数据连接器, 跨平台支持(Windows、Linux、macOS), 开源(AGPL-3.0)并提供商业许可证选项. | 独立 Agent | ⭐⭐⭐⭐ | 8,200 |
| [bloomberg-terminal](https://github.com/feremabraz/bloomberg-terminal) | 1,134 | 类似 Bloomberg 的终端, 集成 AI 功能, 使用 Redis 存储 AlphaVantage 数据并通过本地模拟减少 API 调用. 基于 Next.js 15、React 19、TypeScript 和 Tailwind CSS 构建. 功能包括实时市场数据、多视图、交互式 UI、观察列表和明暗模式. | ⭐ | 1,134 |
| [QuantDinger](https://github.com/brokermr810/QuantDinger) | 2,200 | 开源的 AI 驱动量化交易平台, 支持加密货币、股票和外汇, 具有回测、实盘交易、市场数据和多智能体研究功能. 采用 Python/Flask 后端、Vue.js 前端、PostgreSQL 和 Redis 技术栈, 支持 AI 辅助市场分析、Python 策略开发、回测和实盘执行. 核心功能包括 AI 市场分析、指标和策略开发、回测和策略持久化、实盘交易执行、投资组合监控和警报、多用户操作和商业化. | ⭐⭐⭐ | 5,334 |
| [PokieTicker](https://github.com/owengetinfo-design/PokieTicker) | 事件驱动型股票分析工具, 帮助投资者理解价格变动背后的"原因". 核心功能包括: 在K线图上叠加新闻事件点(点击可查看当日影响股价的新闻)、按影响类型过滤(市场/财报/产品/政策/竞争/管理层)、发现相似历史事件模式、AI解释价格变动原因(选择日期范围询问涨跌原因)、基于XGBoost的未来趋势预测(结合新闻情感分析和技术指标). 技术架构: 前端React+Vite+D3.js(K线图+新闻点交互), 后端FastAPI+SQLite, AI层使用Claude Haiku批量情感分析和Claude Sonnet深度分析, ML层使用XGBoost分类器预测T+1/T+3/T+5涨跌方向, 数据层使用Polygon.io API. 包含预构建数据库和模型, 可立即运行. 使用场景: 股票新闻事件分析、价格变动原因追溯、历史模式匹配学习、短期趋势预测辅助决策. | 独立 Agent | ⭐ | 668 |
| [chrisworsey55/atlas-gic](https://github.com/chrisworsey55/atlas-gic) | ATLAS 是一个由 General Intelligence Capital 构建的自主 AI 交易代理框架, 结合了 Karpathy 的 autoresearch、Soros 的反身性理论和 MiroFish 群体模拟, 通过市场反馈自我优化. 核心特性: 4 层架构(宏观/行业/超级投资者/决策, 共 25+ 代理)、达尔文式 autoresearch 循环(通过 Sharpe 比率优化提示词, 好代理变"大声", 坏代理变"安静")、自主代理孵化机制(检测知识缺口自动创建新代理)、PRISM 多体制训练(牛市/危机/加息等 5 种市场环境)、JANUS 元层(多体制权重合成)、Soros 反身性引擎(模拟 5 种市场反馈回路)、MiroFish 群体模拟集成(在模拟未来中训练代理). 18 个月回测(2024.9-2026.3)显示部署阶段收益 +22%, 最佳单票 AVGO 收益 +128%. | 独立 Agent | ⭐ | 1,497 |
| [chencore/accumulation_radar](https://github.com/chencore/accumulation_radar) | Binance合约市场庄家收筹信号识别工具, 捕捉加密货币庄家盘机会. 模块化设计: Pool模块(每天扫描535个USDT永续合约识别横盘吸筹) + OI模块(每小时扫描标的池+top100进行OI异动). 核心三策略评分: 追多策略(短线轧空+费率负深度+OI涨确认+量能确认+费率趋势四档)、综合策略(四维均衡+交互加成: 费率30分+OI变化30分+市值20分+横盘天数20分+交互+5分)、埋伏策略(中长线早期布局+市值30分+OI方向25分+横盘天数20分+暗流15分+热度10分). OI异动信号解读: OI升+价升=主动做多/ OI升+价降=主动做空/ OI升+价平=暗流庄家建仓(最典型收筹信号). 数据源全免费公开API(Binance现货/合约API+CoinGecko Trending). 自动提醒系统(热度+收筹池重叠+费率加速恶化+多策略上榜+暗流信号+低市值+OI异动). 零运行成本, MIT许可. 适用于Binance USDT永续合约短线交易和中长线埋伏. | Binance USDT永续合约<br>Telegram Bot | ⭐ | 23 |
| [guy-hartstein/company-research-agent](https://github.com/guy-hartstein/company-research-agent) | 基于 LangGraph 和 Tavily 的多智能体公司研究工具, 专注深度尽职调查. 利用 Google Gemini 2.5 Flash 和 OpenAI GPT-5.1 进行多源数据收集(公司网站/新闻文章/财务报告/行业分析)、AI 内容过滤、异步处理生成全面公司研究报告. 包含公司分析、行业分析、财务分析、新闻扫描等多个专业研究节点. 双模型分工: Gemini 负责高上下文研究合成, GPT-5.1 负责精确报告格式化. 使用场景: 投资尽职调查、市场研究、竞争分析、企业背景调查. 用户通过 Web 界面提交研究请求、跟踪进度并下载最终报告. | Gemini<br>OpenAI<br>LangGraph<br>Tavily | ⭐⭐ | 1,883 |
| [brokermr810/QuantDinger](https://github.com/brokermr810/QuantDinger) | 自托管本地优先的量化操作系统, 替代分散的图表工具、笔记本、脚本和 LLM 聊天窗口. 核心功能: AI 研究与分析(集成多 LLM 模型市场分析, 自然语言生成量化代码, 回测后 AI 提示优化策略, 通过 MCP 协议连接 Claude Code/Cursor/Codex)、策略开发(IndicatorStrategy 基于 DataFrame 信号 + ScriptStrategy 事件驱动)、回测验证(服务端执行, 指标计算, 资金曲线可视化)、实盘执行(加密货币12+交易所/IBKR美股/MT5外汇, Telegram/邮件/Discord/Webhook 通知). 支持平台: Claude Code/Cursor/Codex MCP 协议 + Docker Compose 部署. 数据源: 加密货币/美股(IBKR)/外汇(MT5)/期货/Polymarket. 使用场景: 个人量化研究一站式完成从想法→策略→回测→实盘、AI 驱动量化团队自然语言驱动研究、多市场交易者统一管理多资产策略. 内置多用户、积分/会员/USDT 计费开关, 可快速搭建量化 SaaS 平台. Apache-2.0 许可. | Claude Code<br>Cursor<br>Codex<br>MCP<br>Docker | ⭐⭐⭐ | 2,226 |
| [virattt/dexter](https://github.com/virattt/dexter) | 自主金融研究智能体, 专为深度金融研究设计, 定位为"类 Claude Code 架构但专注金融领域". 核心功能: 智能任务规划(自动分解复杂金融问题)、自主执行(选择调用正确工具收集数据)、自我验证(迭代优化直到可信结论)、实时金融数据(收入报表/资产负债表/现金流量表)、安全机制(循环检测和步骤限制)、调试日志(scratchpad 文件追踪复盘). 支持 OpenAI/Anthropic/Google/xAI/OpenRouter API 和 Ollama 本地模型. 集成 Financial Datasets API 机构级市场数据, WhatsApp Gateway 消息交互. 适用于深度金融研究分析、公司财务评估、市场数据分析和投资决策支持. | OpenAI<br>Anthropic<br>Google<br>xAI<br>Ollama<br>WhatsApp | ⭐⭐⭐⭐ | 24,605 |
| [ginlix-ai/LangAlpha](https://github.com/ginlix-ai/LangAlpha) | 金融投资智能体框架("金融版 Claude Code"), 采用贝叶斯迭代研究模式让智能体拥有持久化工作空间, 研究成果跨会话累积. 核心技术: PTC 程序化工具调用(智能体在 Daytona 云沙箱编写执行 Python 代码处理金融数据而非注入 LLM 上下文)、渐进式工具发现、多层级金融数据生态(ginlix-data WebSocket→FMP→Yahoo Finance三级回退)、25层中间件栈(实时引导/计划模式/多模态/自动压缩)、LangGraph 并行异步子智能体群. 使用场景: DCF估值模型、可比公司分析、三表财务模型、股票研究报告、财报分析、晨会报告、竞争情报、证券文件解析(10-K/10-Q)、期权分析、自动化任务调度、多格式文档生成(PDF/DOCX/PPTX/XLSX). 支持 Gemini/OpenAI/Anthropic/DeepSeek、Claude Code OAuth、Codex OAuth、Kimi/GLM/MiniMax 国产模型、Slack/Discord/Feishu/Telegram 集成. | Gemini<br>OpenAI<br>Anthropic<br>DeepSeek<br>多渠道集成 | ⭐⭐ | 1,055 |
| [financial-datasets/mcp-server](https://github.com/financial-datasets/mcp-server) | AI 金融数据 MCP 服务器, 为 Claude Code 提供 17,000+ 股票的实时和历史数据接入能力. 支持股票价格、财务报表、机构持仓等数据查询, 让 Claude 成为金融研究助手. 详见 [Twitter 介绍](https://x.com/justloveabit/status/2053309770082492641). | Claude Code<br>MCP | ⭐⭐ | NA |
| [ai-financial-agent](https://github.com/virattt/ai-financial-agent) | 基于 Next.js 15 + Vercel AI SDK 构建的概念验证型 AI 金融代理, 支持自然语言股票分析、财务数据查询和交互式图表展示, 集成 Financial Datasets API 提供 30 年历史数据, 仅供教育研究使用. | AI 金融 | ⭐⭐ | 1,959 |
| [tradingview-mcp](https://github.com/atilaahmettaner/tradingview-mcp) | 面向 Claude/MCP 的 AI 量化交易框架: 集成 30+ 技术指标、6 种回测策略、Reddit 情绪分析、Yahoo Finance 实时行情, 支持多交易所(股票/加密/ETF), 5 分钟快速部署, 完全免费开源. | Claude<br>MCP | ⭐⭐⭐ | 2,564 |
| [TQ-trade-agent/tq-trading-agent](https://github.com/TQ-trade-agent/tq-trading-agent) | 面向中文用户的AI股票研究与策略原型工具链, 结构化输出、可编排、易集成. 提供多智能体股票编排(分析师链路→多轮辩论→综合结论→交易草案→风控循环→终审)、API接口服务、命令行工具和Docker一键部署. 支持OpenAI兼容接口(官方/聚合网关/国产兼容底座). 适用于研究与教学场景. | OpenAI兼容接口<br>LangGraph<br>LangChain | ⭐ | 112 |
| [simonlin1212/a-stock-data](https://github.com/simonlin1212/a-stock-data) | A股全栈数据工具包, 6层架构×21个端点×8个数据源. 包含交易层(K线/五档盘口/逐笔成交/PE/PB/市值)、研报层(研报列表/PDF下载/一致预期)、信号层(强势股/题材归类/北向资金/概念板块资金流向)、新闻层(个股新闻/财联社快讯)、基础数据(37期季报/F10)、公告层(沪深全量公告). 支持Claude Code、Codex、OpenClaw等AI编程助手. | Claude Code<br>Codex<br>OpenClaw | ⭐ | 915 |
| [global-stock-data](https://github.com/simonlin1212/global-stock-data) | 美股港股全栈数据 Skill 工具包, 8 层架构 × 18 个端点 × 5 个数据源, 全部零鉴权仅需 requests. 覆盖实时行情、K线、技术指标(MA/MACD/RSI/KDJ/布林带)、基本面财报、资金流向、期权链、SEC Filing 和搜索工具. 东财/新浪/腾讯/Yahoo/SEC EDGAR 五源融合, 纯 Python 计算技术指标, 与 a-stock-data(A 股)姊妹项目 | Claude Code<br>Codex<br>OpenClaw | ⭐ | 711 |
| [HKUDS/AI-Trader](https://github.com/HKUDS/AI-Trader) | 100%全自动原生交易平台, AI智能体金融交易协作平台. 支持即时集成(一条消息即可接入)、集群智能交易(Agent协作辩论自动挖掘最佳策略)、跨平台信号(券商同步/交易同步/信号共享)、一键跟单交易、通用市场覆盖(股票/加密货币/外汇/期权/期货)、三种信号类型(策略讨论/操作复制/协作讨论)和奖励系统. 技术栈: Python 68.5% + TypeScript 26.1% + FastAPI + React. 支持OpenClaw、nanobot、Claude Code、Codex、Cursor等主流AI Agent. | OpenClaw<br>nanobot<br>Claude Code<br>Codex<br>Cursor<br>主流AI Agent | ⭐⭐⭐ | 17,432 |
| [simonlin1212/TradingAgents-astock](https://github.com/simonlin1212/TradingAgents-astock) | 将多Agent辩论架构深度特化到A股投资研究,Python+LangGraph+Streamlit,7个免费数据源+双LLM设计+7个Analyst角色协作+Bull vs Bear辩论 | MiniMax<br>DeepSeek<br>智谱GLM<br>通义千问<br>OpenAI<br>Anthropic<br>Google<br>xAI<br>Ollama | ⭐ | 332 |
| [kbhujbal/AlphaAnalyst-open-source-autonomous-equity-research-agent](https://github.com/kbhujbal/AlphaAnalyst-open-source-autonomous-equity-research-agent) | 开源自主股权研究代理输入美国股票代码生成分析师级别完整研究报告,Python+FastAPI+Next.js+PostgreSQL+pgvector,多智能体架构和严格引用验证 | 独立Web应用 | ⭐ | 37 |
| [The-Swarm-Corporation/AutoHedge](https://github.com/The-Swarm-Corporation/AutoHedge) | 企业级自主对冲基金智能体系统自动化执行市场分析风险管理到交易执行完整流程,Python+Swarms AI智能体框架,多智能体架构Director+Quant+Risk Manager+Execution | 独立Python系统 | ⭐⭐⭐ | 2,737 |
| [deep-research](https://github.com/hoolulu/deep-research) | 深度调研报告生成 Skill, 支持 19 种语言输出, 一个命令 `/research 主题` 全自动调研. 4 层流程(分析大纲→采集数据→并行撰写→验收装配), 五层搜索优先级(CLI 内置→建议源→SearXNG→sources.json→免费源), 三种深度模式(quick/standard/deep), 8-20 分钟出报告, 正反观点并存, 置信度分级, 数据防坑机制, 本地 PDF/DOCX/TXT/MD 离线模式, 本地浏览页+PDF/DOCX 导出 | OpenCode<br>Claude Code<br>Codex<br>Cursor 等 | ⭐ | 358 |
| [claude-for-financial-services-cn](https://github.com/jwangkun/claude-for-financial-services-cn) | 63 个面向 A 股金融从业者的 Claude Skills, 基于 Anthropic 原版 claude-for-financial-services 深度适配国内市场. 6 个垂直领域(china-finance 31个/投行 10个/PE 9个/财富管理 5个/基金运营 6个/运营 2个), 4 个端到端智能体(pitch/researcher/earnings/model-builder), 4 级数据源(Wind→iFind→AkShare→新闻) | Claude Code<br>Codex | ⭐ | 497 |



### 6.2.3 🎨 设计工作流
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | 精心策划的DESIGN.md文件集合, 源自真实网站的设计系统文档, AI代理可通过这些文件生成一致的UI. 网站 [getdesign.md](https://getdesign.md) | NA | ⭐⭐⭐ | 37357 |
| [open-design](https://github.com/nexu-io/open-design) |  Claude Design 的开源替代方案, 本地优先、可部署到 Vercel、每层都支持 BYOK(自带密钥). Turn-1 交互式发现表单(锁定表面/受众/语气/品牌上下文/规模, 防止 80% 的方向重定向); 品牌资产提取协议(定位→下载→提取 hex→编写 brand-spec.md→语音化); 五维自评机制(哲学/层级/执行/特异性/克制, 1-5 分, 低于 3 分需回退修复); P0/P1/P2 检查清单; AI-slop 黑名单(禁止滥用紫渐变/通用表情图标/左侧边框圆角卡片/手绘 SVG 人类/Inter 作为展示字体/虚构指标). 使用场景: 为初创公司制作杂志风格的种子轮 pitch deck、生成交互式产品原型、构建品牌一致的落地页、快速产出移动端多屏原型、生成带设备框架的演示截图、为团队输出结构化工作文档(PM 需求/周报/运维手册). | Claude Code, Codex CLI, Cursor Agent, Gemini CLI, OpenCode, Qwen | ⭐⭐⭐ | 2,207 |
| [OpenCoworkAI/open-codesign](https://github.com/OpenCoworkAI/open-codesign) | Claude Design 的开源替代方案, 本地优先的桌面 AI 设计工具, 支持 Claude、GPT、Gemini、Ollama 等 20+ 模型, 可将提示词转换为 HTML/JSX 原型、幻灯片、营销素材等. MIT 许可, 基于 Electron + React 19 + Vite 6 + Tailwind v4 构建. 核心功能包括: 15 个内置演示 + 12 个设计技能模块、AI 图片生成、评论模式(点击元素局部修改)、AI 调优滑块(颜色/间距/字体)、多设备预览、5 种导出格式(HTML/PDF/PPTX/ZIP/Markdown)、本地 SQLite 版本快照、一键导入 Claude Code/Codex API 密钥. v0.2 即将推出 Agentic Design 功能(工作区会话、权限化 Agent 循环、DESIGN.md 设计系统). 使用场景: 快速生成落地页原型、制作杂志风格 pitch deck、构建品牌一致的营销素材、创建多设备适配的 UI 原型. | 多平台(macOS/Windows/Linux)、多模型 | ⭐ | 4,885 |
| [maxbogo/awesome-ai-tools-for-ui](https://github.com/maxbogo/awesome-ai-tools-for-ui) | 精选 AI 工具集合仓库, 专注帮助开发者构建精美专业 UI/UX 界面. 收录 26+ 款精选工具, 覆盖 AI 编码助手技能(Skills)、AI 设计应用(Apps)、MCP 服务器、传统设计工具和设计资源五大类别. 核心技术: 集成 AI 驱动 UI 生成、设计系统自动创建、组件库智能匹配, 支持通过 SKILL.md 文件为 AI Agent 注入设计规范和视觉感知能力. 使用场景: AI 辅助前端开发、vibe-coding 氛围编程界面设计、AI Agent 设计能力增强、设计系统快速搭建. 支持平台: Claude Code、Codex、Cursor、Windsurf、VSCode 等主流 AI 代码编辑器, 覆盖 Figma 等设计工具集成. 适用于需要增强 AI 设计能力的开发者和设计系统文档化场景. | Claude Code<br>Codex<br>Cursor<br>Windsurf<br>VSCode | ⭐ | 386 |
| [ZeroZ-lab/cc-design](https://github.com/ZeroZ-lab/cc-design) | 面向 AI 代理的高保真 HTML 设计与原型指导技能库, 专注为 Claude Code 和 Codex 提供专业级设计能力. 采用 8 层设计思维框架(目标→验证)、10 大核心原则及 20 个设计哲学流派, 支持 68+ 品牌设计系统渐进式加载. 核心功能: 落地页与幻灯片制作、交互原型构建、线框图与动画设计、设计系统搭建、质量保障机制(含反 AI 垃圾规则、版式系统、截图验证)、多格式导出(PDF/PPTX/MP4/HTML)及双轨音频合成. 平台集成: 通过 `/design` 命令激活于 Claude Code, 通过 `$cc-design` 引用激活于 Codex, 提供 SessionStart/PreCompact/Stop 三个生命周期钩子实现自动化管理. 适用于 AI 辅助 UI 设计、产品原型开发、设计系统文档化. | Claude Code<br>Codex | ⭐⭐⭐ | 706 |
| [google-labs-code/design.md](https://github.com/google-labs-code/design.md) | Google Labs Code 推出的 AI 设计规范格式, 为 AI 编码智能体提供持久、结构化的设计系统理解能力. 采用 YAML 前置元数据(机器可读设计 Token)+Markdown 正文(人类可读设计理由)双层结构; Token 类型支持颜色、排版、圆角、间距及组件属性. 内置 lint/diff/export/spec 四大 CLI 命令, 支持 WCAG 对比度检测和跨版本回归对比. 核心功能: 设计 Token 校验(断链引用检测)、两版本差异对比、设计系统导出(兼容 Tailwind v3/v4 JSON/CSS、W3C DTCG 格式)、程序化 API 供 Node.js 集成. 技术栈: TypeScript 95.1% + MDX 4.5%, Apache-2.0 许可. 使用场景: AI 智能体 UI 生成、设计系统文档化与协作、跨平台设计 Token 互操作. 兼容 Antigravity、Claude Code、Cursor 等主流 AI 编码智能体. Alpha 版本, 活跃开发中. | Antigravity<br>Claude Code<br>Cursor<br>TypeScript | ⭐⭐⭐⭐ | 11,935 |
| [nevzat/Agentic-Design-Patterns-by-AntonioGulli](https://github.com/nevzat/Agentic-Design-Patterns-by-AntonioGulli) | Antonio Gulli 所著《Agentic Design Patterns: A Hands-On Guide to Building Intelligent Systems》书籍的完整学习材料仓库, 包含 424 页 PDF 书籍和配套 Jupyter Notebook 代码示例. 作者版税捐赠 Save the Children 慈善机构. 涵盖 21 章核心内容和 7 个附录: 基础模式(提示链/路由/并行化/反思/工具使用/规划/多智能体系统)、高级模式(内存管理/学习适应/MCP协议/目标监控)、生产模式(异常处理/人在环/RAG知识检索)、企业级模式(A2A通信/资源优化/推理技术/护栏安全/评估监控). 技术栈: Python 3.8+ + Jupyter Notebook, 兼容 LangChain/OpenAI Assistants/AutoGen/CrewAI/AutoGPT 等主流 Agent 框架. 适用于自学开发者、教育者和研究者系统学习 AI Agent 设计模式. | Python<br>Jupyter<br>多Agent框架 | ⭐ | 60 |
| [superdesigndev/superdesign](https://github.com/superdesigndev/superdesign) | 集成在IDE中的开源AI设计代理通过自然语言提示直接生成UI mockup组件和线框图,TypeScript+CSS VS Code扩展架构,支持Chrome扩展克隆任何网站和UI | Cursor<br>Windsurf<br>Claude Code<br>VS Code | ⭐⭐ | 6,445 |
| [alchaincyf/huashu-design](https://github.com/alchaincyf/huashu-design) | HTML原生设计Skill, 一句话生成高保真原型/幻灯片/动画, 支持MP4导出. 提供交互式App/Web原型、幻灯片(HTML+可编辑PPTX)、动态设计(MP4/GIF/BGM)、设计变体生成、信息图/数据可视化、设计方向建议和5位专家评审. 技术栈: HTML 65.6% + Python 29.7% + Shell 3.5%. 支持Claude Code、Cursor、Codex、OpenClaw、Hermes、Trae等任何markdown-skill兼容的agent. MIT许可证开放商用. | Claude Code<br>Cursor<br>Codex<br>OpenClaw<br>Hermes<br>多Agent支持 | ⭐⭐⭐ | 13,895 |
| [bergside/awesome-design-skills](https://github.com/bergside/awesome-design-skills) | 67个设计系统Skill文件的精选注册表,为AI编码代理(Claude Code、Cursor、Codex等)提供品牌标识、排版色板、组件规范、无障碍规则和质量门控等设计指导. 每个Skill包含SKILL.md(AI代理指令)和DESIGN.md(人类可读设计意图),通过CLI(npx typeui.sh pull)一键拉取到项目中. 涵盖品牌使命、风格基础、组件族、WCAG 2.2 AA合规、写作语调、Do/Don't规则和质量门控. | Claude Code<br>Cursor<br>Codex<br>多平台 | ⭐ | 959 |
| [gnurio/refactoring-ui-plugin](https://github.com/gnurio/refactoring-ui-plugin) | 10个面向Claude Code和Cursor的Refactoring UI技能,将《Refactoring UI》书中的原则转化为结构化AI辅助设计审查. 涵盖视觉层次、排版、颜色、间距、按钮层次、视觉杂乱、空状态、阴影、对比和分组. 可使用单独技能进行针对性修复,或调用meta-refactor-ui编排器进行全面设计审查. | Claude Code<br>Cursor | ⭐ | 143 |
| [baoyu-design](https://github.com/JimLiu/baoyu-design) | Claude Design 的本地 Agent Skill 版本, 让 Cursor/Claude Code/Codex 等本地代理获得 claude.ai/design 大部分设计能力. 6 阶段流水线(Brief→Diverge→Judge→Synthesize→Refine→Polish), 8 种美学方向(Bold Editorial/Swiss Minimal/Vibrant Gradient/Dark Premium 等), 设计系统导入(Figma .fig 离线解码/GitHub 仓库/HTML), 幻灯片+PPTX 导出(可编辑/截图两种模式), 每个产出都是自包含 HTML | Cursor<br>Claude Code<br>Codex<br>多代理 | ⭐ | 1,414 |
| [awesome-design-systems](https://github.com/alexpate/awesome-design-systems) | 设计系统精选列表, 收录 130+ 个设计系统(Google Material、IBM Carbon、Salesforce Lightning、Shopify Polaris、GitHub Primer 等), 每个标注组件、Voice & Tone、Designers Kit、开源代码四大标签, 按标签筛选和分类浏览, 社区持续维护更新 | NA(精选列表) | ⭐⭐⭐ | 25,079 |
| [fireworks-design](https://github.com/yizhiyanhua-ai/fireworks-design) | 开源 Claude Code 动态工作流设计引擎, 复刻 Claude Design 的多方向探索+评委评分+合成+对抗精炼模式. 6 阶段流水线(Brief→Diverge→Judge→Synthesize→Refine→Polish), 6-8 并行美学方向, 6 维度独立评分, Top-3 合成嫁接, critique↔fix 对抗循环, 最终产出自包含 final.html. 基于 Claude Code Workflow 运行时的确定性编排而非提示词 | Claude Code | ⭐ | 37 |
| [Vercel design.md](https://vercel.com/design.md) | Vercel 发布了官方的 design.md 文件, 为 Claude Code 提供前端设计能力的结构化规范, 将设计流程转化为 AI Agent 可执行的工作流. | Claude Code | ⭐ | 暂不开源 |

### 6.2.4 科研工作流
-------

AI 可替代人工完成论文代码复现脏活, 但无法终审研判结论, 必须人工把控研究逻辑、甄别结果真伪, 坚守先独立运算、后对照核验的原则. [2026/06/14, 爆裂队长NEXT @thinkszyg, 用 Claude Code / Codex 复现论文: AI 现在能不能当研究助理](https://x.com/thinkszyg/status/2066138347446096324) 以往复现论文最大难点不是读懂摘要, 而是代码、数据能否跑通; Claude Code、Codex 可充当执行型研究助理, 但无法替代人类审稿人. arXiv 论文《AI Coding Agents Can Reproduce Social Science Findings》专门搭建社科复现基准, 实测两类代码 AI 复现原始实验结果的真实能力, 结论同样适用于行业分析、投资调研等普通人数据核验场景.


| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [jaechang-hits/SciAgent-Skills](https://github.com/jaechang-hits/SciAgent-Skills) | 将你的 AI 编码代理转变为生命科学专家 ——涵盖基因组学、蛋白质组学、药物发现等 197 项技能. 开源. 该仓库旨在通过提供结构化的技能文件, 显著提升 AI 在生命科学领域的表现, 在 BixBench-Verified-50 基准测试中达到 92.0% 的准确率(比基础 Claude Code 提升 26.7 个百分点). 技术上, 每个技能以独立的 SKILL.md 文件形式组织, 包含可运行代码示例、关键参数和故障排除指南, 分为 72 个工具包、53 个数据库连接器、36 个指南和 35 个管道. 使用场景包括药物发现 pipeline、单细胞 RNA-seq 分析、贝叶斯生物统计学和蛋白质结构分析等生命科学研究任务 | Cluade Code | ⭐ | 84 |
| [luwill/research-skills](https://github.com/luwill/research-skills) | [Research Skills - 安装与使用指南](https://github.com/chencore/research-skills-guide) | 提供学术研究工作流技能集合, 包含 3 个核心技能: research-proposal(生成博士研究提案)、medical-imaging-review(写医学影像综述论文)、paper-slide-deck(从论文生成专业幻灯片). 技术上, 支持多源文献整合 (WebSearch、Zotero、arXiv、PubMed)、结构化工作流程、Nature Reviews 风格学术写作、17 种视觉风格、自动化脚本(PDF 处理、图表提取、幻灯片生成) 和双语支持. 使用场景包括博士申请、综述论文撰写、论文答辩准备、MBA 开题报告和课程教学材料生成等学术研究相关任务. 参见 [2026/04/06, tiantian @wherecall1, research-skills 这个项目, 专门帮学生搞学术写作](https://x.com/wherecall1/status/2041099146988581150) | ⭐ | 481 |
| [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 半自动化学术研究和软件开发助手, 特别适用于计算机科学和AI研究人员. 支持 Claude Code、OpenCode 和 Codex CLI 三种平台, 涵盖从研究构思、文献管理、实验分析到论文写作和投稿的全流程. 技术上, 深度集成 Zotero(文献管理)和 Obsidian(知识管理), 采用模块化架构包含技能(Skills)、代理(Agents)、命令(Commands)、钩子(Hooks)和规则(Rules), 提供跨平台 Node.js 自动化钩子、知识提取系统(从论文/Kaggle提取可重用知识)和多语言支持(中英文). 包含 7 个主要工作流: 研究构思(Zotero集成)、ML项目开发、实验分析(严格统计分析)、论文写作、论文自审、投稿与回复、录用后处理. 使用场景包括计算机科学/AI研究全流程、研究生科研管理、软件密集型学术项目以及学术写作全流程支持. 仓库创建于 2026-01-27, 已有 3.1k stars, 279 forks, 持续活跃更新. | Claude Code, OpenCode, Codex CLI | ⭐ | 3.1k |
| [beita6969/ScienceClaw](https://github.com/beita6969/ScienceClaw) | 面向科学家的自进化AI研究助手, 285技能零幻觉持久化. 提供自进化技能系统(运行时创建新技能)、四层持久化研究记忆(跨会话保留)、长时研究支持(1小时+会话心跳)、零幻觉机制(强制引用验证)和全学科覆盖(自然+社会科学, 25+数据库集成). 技术栈: TypeScript 83.6% + Swift 8% + Python 3.9% + LanceDB向量数据库. 基于OpenClaw引擎, 支持MCP服务器. | OpenClaw<br>MCP服务器 | ⭐ | 713 |
| [AutoResearchClaw](https://github.com/aiming-lab/AutoResearchClaw) | 完全自主的研究管道, 将单个研究想法转化为会议级论文. 主要功能包括: 23 个阶段的完整研究流程、多源文献搜索(OpenAlex、Semantic Scholar、arXiv)、4 层引用验证、硬件感知执行、OpenCode 野兽模式、沙盒实验、会议级写作、质量门控等. 适用于学术研究、论文写作、实验自动化、研究思路验证等场景 | 多模型支持 | ⭐ | 12,361 |
| [Imbad0202/academic-research-skills](https://github.com/Imbad0202/academic-research-skills) | Claude Code学术研究技能套件覆盖从研究问题提炼到论文发表完整流程,Python技能系统多智能体架构Deep Research(13智能体)+Academic Paper(12智能体),支持多种引用格式APA 7.0/Chicago/MLA/IEEE/Vancouver. 参见 [2026/05/17, Gyro @gyro_ai, 还在用 AI 学术妲己学论文？这套 Agent 科研团队帮你打败99%研究生](https://x.com/gyro_ai/status/2055948364202562038) | Claude Code | ⭐⭐⭐⭐ | 10,565 |
| [Imbad0202/academic-research-skills-codex](https://github.com/Imbad0202/academic-research-skills-codex) | Codex原生打包学术研究技能套件将ARS工作流适配为Codex平台单个技能包,Python+HTML+Shell,单个$academic-research-suite技能路由器适配Codex运行时 | Codex CLI<br>OpenAI Codex | ⭐ | 485 |
| [K-Dense-AI/scientific-agent-skills](https://github.com/K-Dense-AI/scientific-agent-skills) | 科研智能体技能集合覆盖生物学化学医学材料科学等138技能,Python技能系统遵循Agent Skills开放标准,100+数据库访问+70+优化Python包技能 | Cursor<br>Claude Code<br>Codex<br>Gemini CLI<br>GitHub CLI | ⭐⭐⭐⭐ | 24,013 |
| [Galaxy-Dawn/claude-scholar](https://github.com/Galaxy-Dawn/claude-scholar) | 面向计算机科学和AI研究者的半自动化学术研究助手覆盖从文献调研到论文发表完整研究周期,Skills/Commands/Agents/Rules/Hooks系统架构+Zotero MCP+Obsidian集成,40+ Skills和14 Agents | Claude Code<br>Codex CLI<br>OpenCode | ⭐⭐⭐ | 3,910 |
| [lynote-ai/humanize-text-zh](https://github.com/lynote-ai/humanize-text-zh) | AI文本拟人化开源工具集将AI生成内容改写为自然类人文本降低AI检测率,Python 3.10+ + Docker + DeepSeek API,四种技术方案多语言翻译链/多轮LLM重写/检测引导反馈循环/混合引擎翻译 | 独立Python应用/Docker服务 | ⭐ | 8 |
| [dw-dengwei/daily-arXiv-ai-enhanced](https://github.com/dw-dengwei/daily-arXiv-ai-enhanced) | 自动每日爬取arXiv论文并用AI总结的创新工具. 结合自动化爬取与AI驱动摘要(DeepSeek驱动,约0.2元/天),提供个性化论文高亮(基于关键词和作者)、跨设备兼容、本地偏好存储(隐私优先)、灵活日期范围过滤、GitHub Actions自动执行和GitHub Pages托管前端界面. 默认覆盖cs.CV、cs.GR、cs.CL、cs.AI四大类别,中文摘要输出. | GitHub Actions<br>GitHub Pages | ⭐ | 2,790 |
| [brycewang-stanford/Auto-Empirical-Research-Skills](https://github.com/brycewang-stanford/Auto-Empirical-Research-Skills) | 23,000+AI Agent技能库,覆盖8大社会科学学科(经济学、政治学、社会学、心理学、公共卫生、教育学、管理学、金融学)的实证研究. 由Stanford REAP×CoPaper.AI维护,119个GitHub仓库收录. 核心理念:不只是技能集合,而是自动运行完整实证研究流水线(从原始数据清洗→识别与估计→稳健性检验→表格、图表和投稿级草稿)的代理. CoPaper.AI 20分钟完成一篇可复现的规范实证论文. 参见[CoPaper.AI](https://www.copaper.ai/landing) | 多平台(AI编码代理) | ⭐ | 1,549 |
| [spring-ai-alibaba/deepresearch](https://github.com/spring-ai-alibaba/deepresearch) | 阿里巴巴Spring AI Alibaba项目中的DeepResearch Agent,基于Spring AI Alibaba Graph实现的深度研究代理. 超越简单工具调用循环,结合任务规划、上下文管理和子代理协作来解决需要多步骤深入调研的复杂研究任务. 技术栈:Java+Spring AI+Spring AI Alibaba Graph. 适用于需要深度调研和多步骤研究的学术和商业场景. | Spring AI(Java生态) | ⭐ | 264 |
| [K-Dense-AI/science-superpowers](https://github.com/K-Dense-AI/science-superpowers) | 面向AI研究代理的可组合计算科学方法论技能——以预注册(pre-registration)替代TDD. Superpowers的科学领域重新实现,架构相同——技能通过session-start引导自动触发,但工作流是研究生命周期,核心纪律是预注册而非测试驱动开发. 适用于计算科学研究、数据分析和需要严格方法论的科学工作流. | 多平台(AI编码代理) | ⭐ | 169 |
| [Feynman](https://github.com/companion-inc/feynman) | 开源 AI 研究代理终端, 基于 Pi 迥行时和 alphaXiv 论文搜索. 支持自然语言查询直接产出引用研究简报, 11 个工作流命令(/deepresearch 多代理调查、/lit 文献综述、/review 模拟同行评审、/audit 论文 vs 代码审计、/replicate 实验复现、/recipe ML 训练配方等), 4 个内置研究代理(Researcher/Reviewer/Writer/Verifier), 集成 AlphaXiv、Hugging Face Hub、Docker、Web 搜索、Modal GPU 等工具 | Codex<br>Claude Code<br>OpenCode | ⭐⭐ | 7,871 |
| [PaperSpine](https://github.com/WUBING2023/PaperSpine) | 以 motivation 为主线的论文与报告写作 Skill 套件, 支持 Codex、Claude Code 和 OpenClaw 三端. 两条主流程(Rewrite Existing 改写已有论文 / Build From Materials 从素材构筑论文), 四类目标场景(期刊/会议/报告/竞赛), 11 个分支 Skill(intake/research/citation/rewrite/build/latex/audit/translate/humanize/update/ui), writing_rationale_matrix 为核心产物记录每个写作单元的动机, citation_support_bank 为每个候选引用绑定句子级 claim | Codex<br>Claude Code<br>OpenClaw | ⭐ | 3,246 |
| [Supervisor-Skills](https://github.com/HKUSTDial/Supervisor-Skills) | 港科大(广州)骆昱宇助理教授团队打造的科研副导师 AI Skill 项目, 将顶会发表审稿经验蒸馏为可执行 AI 技能. 双轨架构: 6 章 Handbook(宏观认识/Idea 构思/论文写作/科研作图/Vibe Research 实战/顶会案例分析) + 7 个 AI Skills(Idea Evaluator/Vibe Research Guide/Intro Drafter/Tech Paper Template/Benchmark Paper Template/Pre-Submission Reviewer/Figure Design Advisor) | Claude Code<br>Cursor<br>Codex 等 | ⭐ | 2,886 |
| [codex-claude-academic-skills](https://github.com/zLanqing/codex-claude-academic-skills) | 三个面向中国科研工作者的学术技能包, 覆盖论文写作、学术 Office 文档生成与科研计算三大场景, Claude Code 和 Codex 双平台. ① research-writing-skill: 论文各章节撰写、修改润色、审稿回复, 中文优先保留英文术语; ② office-academic-skill: PDF→Word 阅读报告、组会/开题/答辩 PPT, OOXML 级别检查; ③ scientific-toolkit-skill: MATLAB/Python 科研计算+论文配图, 面向光电信息科学领域 | Claude Code<br>Codex | ⭐ | 775 |
| [paper-pilot](https://github.com/Xueyang-Song/paper-pilot) | 本地优先的桌面科研助手, 基于 Electron+React 19+Vite+SQLite 构建, 全部数据留在本机无云依赖. 8+ 学术源同时查询(OpenAlex/Crossref/Semantic Scholar/PubMed/arXiv 等), SQLite FTS5 全文搜索 + sqlite-vec 向量检索, AI 工具调用代理引用溯源, Ollama 离线运行, PDF→知识管道(MarkItDown 转换), 项目级隔离存储 | Electron<br>桌面应用 | ⭐ | 337 |
| [Awesome-Rebuttal](https://github.com/xiongqi123123/Awesome-Rebuttal) | 项目级学术 rebuttal 策略和作者回复起草 Skill 包, 19 个原子能力按生命周期 7 阶段组织(Setup→Evidence&Memory→Review Understanding→Strategy→Drafting→Pre-Submission→Discussion). 支持评审元数据规范化、关注原子化、策略规划、实验分类(must-do/high-value/not-recommended/infeasible)、格式感知起草(一页 PDF/OpenReview 全局评论等)、安全闸门(阻止无支撑声明/伪造结果/匿名泄露) | Codex<br>Claude Code<br>Cursor | ⭐ | 230 |
| [nature-skills](https://github.com/Yuan1z0825/nature-skills) | 一个面向 AI agent 的开源顶刊论文技能包, 由上海交通大学博士生袁一哲开发维护. 包括 ① nature-figure: 顶刊级科研绘图; ② nature-polishing: 学术语言润色; ③ nature-academic-search: 多源文献搜索; ④ nature-reader: 论文双语精读; ⑤ nature-citation: 引用检索与管理; ⑥ nature-response: 审稿意见回复信; ⑦ nature-paper2ppt: 论文转组会 PPT; ⑧ nature-writing: 论文章节撰写; ⑨ nature-reviewer: 预投稿审稿模拟; ⑩ nature-data: 数据可用性声明. 参见 [2026/06/06, Gian @JyNong26, 一技超越90%的论文, 打造顶刊级的学术表达--Nature Skills](https://x.com/JyNong26/status/2062908321582203020) | Claude Code | ⭐⭐⭐ | 20,783 |
| [Awesome-Vibe-Research](https://github.com/modelscope/Awesome-Vibe-Research) | 阿里巴巴 ModelScope 团队打造的 AI 辅助科研开放共建仓库, 沉淀科研全流程中的 agents、skills、workflows、tools 与最佳实践. 9 阶段科研流程地图(全流程→方向扫描→文献研究→方法设计→实验执行→可视化→论文写作→复现发布→传播影响), 收录 AI-Scientist、STORM、nature-skills、AutoResearchClaw 等顶级项目, 社区持续维护更新 | NA(精选列表) | ⭐ | 114 |
| [handsome-rich/Awesome-Auto-Research-Tools](https://github.com/handsome-rich/Awesome-Auto-Research-Tools) | 精选的自动化科研工具集合, 覆盖文献搜索、论文阅读、实验管理和代码生成等环节, 帮助研究者加速工作流程. 收录从文献综述到想法生成、实验执行、论文写作和同行评审的全流程自动化开源项目, 包括 AI-Scientist、STORM、AutoResearchClaw 等顶级项目. 提供中英文双语 README, 按科研阶段分类(文献检索/Idea生成/实验执行/论文写作/同行评审), 包含每个项目的功能描述、技术栈和适用场景. 技术栈: Python. 适用于科研人员寻找自动化科研工具、了解 AI 辅助科研最新进展的场景. | NA(精选列表) | ⭐ | 991 |
| [brycewang-stanford/Awesome-Journal-Skills](https://github.com/brycewang-stanford/Awesome-Journal-Skills) | 覆盖主流期刊的 Claude Code/Codex 期刊技能包, 从选题、识别策略到表格规范与审稿回复全流程, 助你快速发论文. 收录 200+ 期刊/会议的 Agent Skill, 覆盖经管社科中英文顶刊(AER、QJE、管理世界、经济研究等)、人文与广义社科顶刊、自然科学/临床顶刊(Science、Cell、PNAS、NEJM、The Lancet)和 AI 优先的计算机科学顶会(NeurIPS/ICML/ICLR/AAAI 等). 每个重点期刊提供深度包(单刊全流程约 9-13 个 Skills, 覆盖选题、定位、方法、表格、投稿和回复), 四个广度合集提供选刊/选会定位+写作风格 Skills. 技术栈: Stata(78.1%) + Python(21.9%). 提供中文和英文双语文档, 官网 [copaper.ai](https://www.copaper.ai). 适用于学术研究者、论文写作和期刊投稿全流程加速. | Claude Code<br>Codex | ⭐ | 432 |



### 6.2.5 法律工作流
-------

[2026/06/18, Witt | AI职场热点老兵, @WittWang01](https://x.com/WittWang01/status/2067593676180828519) 有一个老哥, 用AI把《刑法》翻译成“普通人听得懂的大白话”. 不是法条背诵, 是把“非法吸收公众存款罪”翻译成“你拉人头搞资金盘, 出事就是这个罪”. 现在他把内容整理成《打工人法律避雷手册》卖49一份, 卖到飞起.

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [zubair-trabzada/ai-legal-claude](https://github.com/zubair-trabzada/ai-legal-claude) | AI 驱动的合同审查和法律文档生成工具. 支持从 Claude Code 中审查合同、标记风险、生成 NDA、检查合规性、谈判条款并生成客户端 PDF 报告. 核心功能包括: 14 个命令(`/legal review` 旗舰功能通过 5 个并行代理进行全面合同审查, 返回合同安全评分、逐条款分析和优先建议; `/legal risks` 深度风险分析; `/legal compare` 合同版本比较; `/legal plain` 法律术语翻译为通俗英语; `/legal negotiate` 生成反提案; `/legal missing` 查找缺失保护条款; `/legal nda` 生成 NDA; `/legal terms/privacy` 生成 TOS 和隐私政策; `/legal agreement` 生成商业协议; `/legal freelancer` 专用审查; `/legal compliance` 合规检查; `/legal report-pdf` 生成专业 PDF 报告). 技术上, 采用 5 个 AI 代理并行工作(条款分析师 20%、风险评估师 25%、合规检查员 20%、条款映射器 15%、建议引擎 20%), 聚合结果生成统一报告和合同安全评分(0-100). 使用场景包括: 自由职业者审查客户合同、生成 NDA、提供合同审查服务; 小企业审查供应商合同、生成隐私政策和 TOS、进行合规审计; AI 自动化机构添加合同审查服务、生成专业 PDF 报告、提供月度法律文档管理服务. | Claude Code | ⭐ | 1,088 |
| [zubair-trabzada/ai-legal-claude](https://github.com/zubair-trabzada/ai-legal-claude) | AI 驱动的合同审查与法律文档生成工具, 通过 Claude Code 技能系统为用户提供专业法律文档分析服务. 降低法律审查成本(传统方式 $300-500/小时), 让中小企业和自由职业者快速获取合同风险评估. 技术栈: Python 77.8% + Shell 22.2%. 核心功能: 多 Agent 并行架构(5个专业代理: 条款分析/风险评估/合规检查/义务映射/建议生成)、14个细分技能(合同审查/风险分析/条款对比/合同谈判/NDA生成/隐私政策/GDPR/CCPA合规审计等)、PDF 专业报告输出(ReportLab). 核心命令 `/legal review` 60秒内完成合同审查, 输出0-100安全评分、风险仪表盘、逐条分析、缺失保护项和义务时间线. 支持 NDA/服务条款/隐私政策/商业协议等多种文档生成. 一键安装脚本, 需 Anthropic API key. | Claude Code<br>Python<br>Anthropic API | ⭐⭐ | 1,180 |


### 6.2.6 安全工作流
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [NeoTheCapt/RedteamAgent](https://github.com/NeoTheCapt/RedteamAgent) | 自主 AI 驱动的红队模拟代理, 支持 Claude Code、OpenCode 和 Codex. 将任何工作区转变为完整的渗透测试环境, 用于 CTF/实验室目标. 核心功能: 8 个 AI 代理(operator、recon-specialist、source-analyzer、vulnerability-analyst、exploit-developer、fuzzer、osint-analyst、report-writer)、容器化 Kali 工具、5 阶段方法论(Recon→Collect→Test→Exploit+OSINT→Report)、流式案例收集管道、79 个安全参考文件(OWASP Top 10:2025、API Security 2023 等)、本地 Web UI 管理界面、中断恢复支持、无人值守强化. 技术上采用单一源码架构(OpenCode 格式为源, Claude Code/Codex 版本安装时生成), 所有渗透测试工具运行在 Docker 中, 无需本地安装. 使用场景包括 CTF 比赛靶机测试、实验室环境渗透测试、安全漏洞挖掘、自动化红队模拟演练. | Claude Code, OpenCode, Codex | ⭐ | 207 |
| [SnailSploit/Claude-Red](https://github.com/SnailSploit/Claude-Red) | 38 个面向 Claude 的攻击性安全技能库, 将 Claude 转变为上下文感知的红队操作员. 由 SnailSploit 开发的精心策划的技能集合, 每个技能都是结构化的 SKILL.md 文件, 为 Claude 注入特定攻击面的专家级方法论. 涵盖 6 大领域: Web 应用(SQLi、XSS、SSRF、SSTI、XXE、文件上传、RCE、反序列化、请求走私等 16 项)、认证与身份(JWT、OAuth)、基础设施与二进制(Shellcode、EDR 规避、Exploit 开发、Windows 边界突破、补丁对比等 13 项)、侦察与 OSINT(工具、方法论)、模糊测试与漏洞研究(libFuzzer、AFL++、漏洞识别等)、AI 安全(提示注入、越狱、RAG 投毒等). 技术上采用独立 SKILL.md 文件组织, 包含真实红队演练中的决策树、工具选择逻辑和升级路径. 使用场景包括: Web 应用渗透测试、认证安全审计、二进制漏洞研究、红队模拟演练、AI 安全评估、漏洞挖掘与补丁分析. 支持 Claude Code、Claude Skills System 或 Claude.ai 三种使用方式. | Claude Code | ⭐ | 1,098 |
| [ktol1/RedTeam-Agent](https://github.com/ktol1/RedTeam-Agent) | AI 驱动的红队框架, 采用技能优先的终端工作流. AI 读取项目技能、发现工具、在终端执行命令, 并总结高价值发现. 核心哲学: 无需手动逐个工具操作, 让 AI 端到端编排工作流. 功能包括: 15+ 开箱即用工具(网络扫描 gogo/fscan、Web 测试 httpx/nuclei/ffuf、AD 攻击 SharpHound/impacket/Responder、横向移动 nxc/wmiexec/psexec)、令牌优化(输出过滤和文件优先策略)、AD 攻击完整覆盖(Recon→Collection→Analysis→Attack→Lateral). 技术上, 技能驱动终端执行, 无需额外服务器, 支持 Cursor、Claude Desktop、VS Code/Cline 多客户端. 使用场景包括: 企业网络渗透测试、Active Directory 安全评估、Web 应用漏洞扫描、红队模拟演练、漏洞批量验证. | Cursor, Claude Desktop, VS Code/Cline | ⭐ | 40 |
| [H-mmer/pentest-agents](https://github.com/H-mmer/pentest-agents) | 面向 Claude Code/Codex/Gemini/Cursor/Windsurf/Copilot/OpenClaw 等 7 大 AI 编码工具的自主化 bug bounty 框架. 包含 50 个专业 agents(涵盖 XSS/SQLi/SSRF/SSTI/IDOR/RCE/OAuth 等 19 种漏洞类型)、26 个 slash 命令、19 个 CLI 工具、11 个 hunting skills、2 个 MCP 服务器(支持 16 个漏洞平台+自带 writeup 搜索). 核心功能: 7 问答验证门、自动漏洞链构建(A→B→C)、自主狩猎循环、持久化 brain 端点追踪、CVSS 策略守卫、CC hooks 成本追踪、SAST 流水线. 提供约 2500 行验证过的 payloads 和完整攻击面分析方法论. 技术栈: Python 3.10+, 通过 uv 启动 MCP 服务器, 支持语义化 writeup 搜索(需自建 FAISS/SQLite 索引). 适用于安全研究、漏洞赏金狩猎、渗透测试自动化. | Claude Code<br>Codex<br>Gemini<br>Cursor<br>Windsurf<br>Copilot<br>OpenClaw | ⭐⭐ | 249 |
| [elementalsouls/Claude-BugHunter](https://github.com/elementalsouls/Claude-BugHunter) | Claude Code的Bug狩猎与外部红队技能包——51个技能、15个斜杠命令、681+已披露报告模式(覆盖24个漏洞类别),以及企业身份和基础设施攻击矩阵. 由ElementalSoul构建,专注于Bug Bounty狩猎和外部红队安全研究. 涵盖XSS、SQLi、SSRF、SSTI、IDOR、RCE、OAuth等19种漏洞类型,支持单技能针对性修复和meta-bug-hunter编排器全面审查. | Claude Code | ⭐ | 2,398 |
| [defending-code-reference-harness](https://github.com/anthropics/defending-code-reference-harness) | Anthropic 官方发布的自主漏洞发现与修复参考实现, 基于 Claude 与多家安全团队的合作经验. 7 阶段流水线(Build→Recon→Find→Verify→Dedupe→Report→Patch), 6 个交互式 Skill(/quickstart/threat-model/vuln-scan/triage/patch/customize), gVisor 沙箱隔离每个代理, C/C++ ASAN 内存漏洞检测参考, 可移植到其他语言和漏洞类别 | Claude Code | ⭐⭐ | 6,058 |
| [CyberStrikeAI](https://github.com/Ed1s0nZ/CyberStrikeAI) | AI 原生安全测试平台(Go 构建), 集成 100+ 安全工具、智能编排引擎、角色化测试(12+ 预定义安全角色)、Skills 系统(20+ 领域)、知识库(RAG 向量检索)、内置轻量 C2 框架(TCP/HTTP/WS listener+加密 implant+任务队列). 原生 MCP(HTTP/stdio/SSE), 单/多代理(Eino Deep/Plan-Execute/Supervisor), 攻击链图谱+风险评分, WebShell 管理, Web 控制台, HITL 审批, Burp Suite 插件, 钉钉/飞书机器人 | 多代理<br>MCP<br>Web UI | ⭐ | 4,598 |



### 6.2.7 出行工作流
-------


| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [Joooook/12306-mcp](https://github.com/Joooook/12306-mcp) | 基于MCP的12306购票查询服务器, 提供简单API接口供大模型查询购票信息. 支持查询12306购票信息、过滤列车信息、过站查询和中转查询. 技术栈: TypeScript + JavaScript + Docker. 为AI Agent提供实时火车票查询能力. | MCP兼容智能体 | ⭐ | 874 |

### 6.2.8 医疗工作流
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [HougeLangley/MediCareAI-Agent](https://github.com/HougeLangley/MediCareAI-Agent) | 多Agent自主医疗协作系统患者驱动+AI辅助+医生验证医疗诊断与随访平台,Python 3.12 + FastAPI + PostgreSQL 17 + pgvector + Celery + Redis + React 19,三轨问诊系统 | 自建Agent系统 | ⭐ | 30 |

### 6.2.9 自媒体工作流
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [HougeLangley/MediCareAI-Agent](https://github.com/charlie947/social-media-skills | 1,210 |
| [uu201/character-arc](https://github.com/uu201/character-arc) | 弧光·AI小说创作桌面应用,集项目设定、角色关系、剧情大纲、章节写作与多模型AI协作于一体. 核心功能:项目中心(创建/查看/编辑小说项目)、新建项目向导(AI生成首批设定与大纲)、知识中心(沉淀事实/流程文档/参考资料)、技能系统(内置Skill+项目级Skill包)、世界观/角色/组织/关系管理(关系图谱可视化)、剧情大纲(双栏交错时间线布局+拖拽排序+AI扩写)、章节创作(三栏布局+TipTap富文本+自动保存+历史版本)、AI辅助(润色/续写/改写/节奏调整)、封面工作台(生成封面Prompt+图像模型预览). 支持DeepSeek、通义千问、智谱GLM、Kimi、OpenAI、Anthropic、Ollama等多厂商. | Windows<br>macOS<br>Linux(Electron) | ⭐ | 93 |
| [greensock/gsap-skills](https://github.com/greensock/gsap-skills) | GSAP(GreenSock Animation Platform)的官方AI技能集,教AI编码代理如何正确使用GSAP,包括最佳实践、常见动画模式和插件使用. 8个技能:gsap-core(核心API)、gsap-timeline(时间线)、gsap-scrolltrigger(滚动触发)、gsap-plugins(插件)、gsap-utils(工具函数)、gsap-react(React集成)、gsap-performance(性能)、gsap-frameworks(Vue/Svelte等). Agent Skills格式,兼容skills CLI(Cursor、Claude Code、Codex、Windsurf、Copilot、40+代理). | Claude Code<br>Cursor<br>Codex<br>Windsurf<br>Copilot<br>40+代理 | ⭐⭐ | 7,394 |
| [yikart/AiToEarn](https://github.com/yikart/AiToEarn) | OPC(一人公司)的AI内容营销智能体——Monetize·Publish·Engage·Create一站式平台. 通过AI自动化,帮助OPC、创作者、品牌与企业在全球主流平台上构建、分发并变现内容. 支持抖音、小红书、快手、哔哩哔哩、TikTok、YouTube、Facebook、Instagram、Threads、Twitter(X)、Pinterest、LinkedIn等12+渠道. 四大Agent能力:Monetize(变现,帮助创作者赚钱)、Publish(一键分发到10+平台)、Engage(互动管理)、Create(AI自动创作从创意到成品). | 跨平台(Windows/macOS/Linux) | ⭐⭐⭐ | 17,588 |


### 6.2.10 求职工作流
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [MadsLorentzen/ai-job-search](https://github.com/MadsLorentzen/ai-job-search) | 基于 Claude Code 的 AI 求职申请框架. Fork它, 填入你的个人资料, 让 Claude 评估职位、定制CV、写求职信并准备面试. 核心工作流:自我画像(self-profiling)→契合度评估(fit evaluation)→起草-审查申请管道(drafter-reviewer application pipeline). 语言和国家无关(核心工作流通用),职位门户搜索技能目前针对丹麦市场(Jobindex、Jobnet等),但模式设计可替换为本地招聘平台. 编码职业指导最佳实践,包括结构化评估标准、前瞻性求职信框架和可选薪资基准. | Claude Code | ⭐ | 40 |


### 6.2.11 运维工作流
-------

| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [Jun-jie-Huang/awesome-LLM-AIOps](https://github.com/Jun-jie-Huang/awesome-LLM-AIOps) | 运维场景, 线上系统一出故障, 排查根因、分析日志、处理告警. 每个环节都费时费力, 想用 AI 来提效却不知道从哪开始毫无头绪. 这个项目, 把大模型在运维领域的研究和实践做了系统整理, 已收录超 78 篇论文. 并按照运维场景分成了三大板块: 故障管理、日志分析和基础设施管理, 每个板块下还细分了具体任务方向. 故障管理部分最为详尽, 从告警聚合、根因定位到故障修复、事后复盘, 覆盖了事件处理的完整生命周期. 日志分析则涵盖了日志解析、异常检测等方向. 每篇论文都标注了使用的技术手段和研究任务, 方便快速筛选. | NA | ⭐ | 592 |

# 参考
-------


1. **入门课程**:
    - [Cranot/claude-code-guide](https://github.com/Cranot/claude-code-guide), 完整 Claude 代码 CLI 指南. 实时指南: 每两天自动更新一次, 来源于官方文档、GitHub 发布和 Anthropic 更新日志.
    - [freestylefly/CodexGuide](https://github.com/freestylefly/CodexGuide), 面向全球初学者、创作者、开发者与团队的 Codex 实践指南
    - [FlorianBruniaux/claude-code-ultimate-guide](https://github.com/FlorianBruniaux/claude-code-ultimate-guide), 本指南教你以不同的角度看待人工智能辅助开发.
    - [Master Claude Code in a Weekend](https://github.com/luongnv89/claude-howto), 一份可视化、以示例驱动的 Claude Code 指南——从基础概念到高级代理, 配有复制粘贴模板, 立即带来价值.
    - [Claude-Code-Everything-You-Need-to-Know](https://github.com/wesammustafa/Claude-Code-Everything-You-Need-to-Know)
    - [Harness Books / 驾驭工程](https://github.com/wquguru/harness-books), 两本关于 Harness Engineering 的书. 它们追问同一个工程问题: 一个会写代码的模型进了终端、仓库、权限系统和团队流程, 系统凭什么还能保持边界、连续性和后果控制.
    - [Awesome Harness Engineering](https://github.com/walkinglabs/awesome-harness-engineering) - 精选的 Harness Engineering 资源列表, 涵盖文章、指南、基准测试、规范和开源项目, 专注于使 AI 代理在实际工作流程中更可靠.
    - [Learn Claude Code -- Harness Engineering for Real Agents](https://github.com/shareAI-lab/learn-claude-code).
    - [2026/06/14, 云析 @yunxi0623, 2026 值得学的 12 项 AI 技能: 别再乱追工具了, 真正值钱的是能力](https://x.com/yunxi0623/status/2066156491824935009)
    - [Made With ML](https://github.com/GokuMohandas/Made-With-ML), Learn how to combine machine learning with software engineering to design, develop, deploy and iterate on production-grade ML applications.
    - [在终端里, 长出生产力](https://coding.stormzhang.ai) 面向小白的 AI 编程指南. 从装好到熟练, 把命令行变成你最快的那只手. [stormzhang](https://github.com/stormzhang) 的 Claude Code 和 Codex 入门课程网站, 开源地址 [AI 编程(Claude Code + Codex)指南](https://github.com/stormzhang/ai-coding-guide).

2. **知识库**
    - [鱼皮的 AI 知识库](https://github.com/liyupi/ai-guide),  完全免费开放 的 AI 知识共享平台, 汇总整合目前热门的 AI 工具相关信息, 包括产品介绍、使用指南、工具测评、技巧分享、应用场景、AI 变现、行业资讯、教程资源等一系列内容.
    - [ykdojo/claude-code-tips](https://github.com/ykdojo/claude-code-tips)
    - [Claude Code 实战课程](https://note.mowen.cn/detail/1_ZEnLT5BCYVsix54iB77)
    - [joeseesun/lennys-podcast-newsletter](https://github.com/joeseesun/lennys-podcast-newsletter), Lenny Rachitsky 播客与 Newsletter 知识库 — 用自然语言搜索、阅读和学习 638 篇硅谷顶级产品内容. [产品大神 Lenny 所有 Newsletter 和 Podcast 文字版](https://xiangyangqiaomu.feishu.cn/wiki/S97awc7EeiyjNdkJsM4czn71nxb)
    -[2026/05/30,小墨同学 @legacyvps, 整理知识库真是一个辛苦的工作, 和小伙伴们整理了一套AI知识库.](https://x.com/legacyvps/status/2060586845881401668), [AI Spark AI 实战知识库](https://lcnniolukk80.feishu.cn/wiki/U1ukwWrOei3FpUkQhAjclLOInug).
    - [橙皮书 (Orange Book) Series · by HuaShu (花叔), Hermes Agent: The Complete Guide](https://github.com/alchaincyf/hermes-agent-orange-book)
    - [OpenAI Codex: The Complete Guide · 橙皮书系列 · GPT-5.5 时代的 AI 编程实战手册](https://github.com/alchaincyf/codex-orange-book)
    - [Awesome Harness Engineering](https://github.com/ai-boost/awesome-harness-engineering)

3. **Easy Vibe 教程**
    - [Easy Vibe, 直接上手, 一起 vibe！会说话就会做应用.](https://github.com/datawhalechina/easy-vibe)
    - [vibe-coding-cn: 中文 Vibe Coding 从入门到精通教程](https://github.com/tradecatlabs/vibe-coding-cn), Vibe Coding 从入门到精通教程｜AI 结对编程工作流｜Prompt、Skill、Workflow、上下文管理、codex实战指南
    - [2025Emma/vibe-coding-cn](https://github.com/2025Emma/vibe-coding-cn), Vibe Coding 指南. 四层框架讲 AI 编程: 道定方向、法搭架构、术靠预期与实际比对来定向调试、器是工具的最优组合; 再配上开箱即用的提示词库与技能模块、固定上下文防遗忘、模块化设计, 以及生成器加优化器的递归打磨机制, 把 AI 从随意写代码变成越用越顺手的稳定开发伙伴.
    - [vibe-coding-cn: 中文 Vibe Coding 从入门到精通教程](https://github.com/tukuaiai/vibe-coding-cn)
    - [Awesome Vibe Coding](https://github.com/filipecalegario/awesome-vibe-coding) 最全的 Vibe Coding 资源 awesome list. 覆盖浏览器工具、IDE、移动端 App、插件、CLI 工具. 所有主流 vibe coding 工具的总目录
    - [Learn Harness Engineering](https://github.com/walkinglabs/learn-harness-engineering)
    - [AI Coding Dictionary](https://github.com/mattpocock/dictionary-of-ai-coding)
    - [AI-Project-Gallery](https://github.com/KalyanM45/AI-Project-Gallery)
    - [《一人企业方法论》第二版, 也适合做其他副业(比如自媒体、电商、数字商品)的非技术人群.](https://github.com/easychen/opc-methodology)
    - [TRAE 官方知识库](https://lcnziv86vkx6.feishu.cn/wiki/GEEnwlfTQi8qZrkFsPycfkUKnul)
    - [Agent Harness for Large Language Model Agents: A Survey](https://github.com/Gloriaameng/Awesome-Agent-Harness)
    - [2026/04/28, Agentic Harness Engineering: Observability-Driven Automatic Evolution of Coding-Agent Harnesses](https://arxiv.org/abs/2604.25850), [Agent Harness Engineering: A Survey](https://picrew.github.io/LLM-Harness)
    - [AI Code Guide is a roadmap to start coding with AI](https://github.com/automata/aicodeguide) 一份给零基础小白的 AI 编程路线图,系统整理了 Cursor 等工具栈,拆解了用 Prompt 控制 AI 的工作流与最佳实践,还附了各种资源、教程和博客. 当作「从哪开始」的导航地图很合适

4. **Best Practices**
    - [oh-my-opencode 和 superpowers](https://linux.do/t/topic/1445132/18)
    - [opencode 配置文档](https://linux.do/t/topic/1415352)
    - [对 oh-my-opencode 的简单修复, 节约 5~10 倍的 API 消耗.](https://linux.do/t/topic/1658684)
    - [`[Question]`: How to get the status of background agents? #917](https://github.com/code-yeongyu/oh-my-openagent/issues/917)
    - [Les 13 meilleurs skills & plugins Claude Code en 2026](https://www.camilleroux.com/top-skills-plugins-claude-code-2026-v3)
