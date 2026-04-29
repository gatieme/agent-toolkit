# Skills 目录说明
-------

本目录包含了为 AI Agents 安装的所有 Skills, 按功能分类整理.

[2026/04/20, meng shao @shao__meng, 世界上所有 Skills 本质上可以归纳为四类: 设计、技术、管理和身体 ](https://x.com/shao__meng/status/2046026766503092242)

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
| [`yctimlin/mcp_excalidraw`](https://github.com/yctimlin/mcp_excalidraw) | [`yctimlin/mcp_excalidraw`](https://github.com/yctimlin/mcp_excalidraw) | 运行一个实时的 Excalidraw 画布, 并由 AI 代理控制. 该仓库提供 MCP Server 和 Agent Skill. | NA |
| [`bruc3van/bruce-drawio`](https://github.com/bruc3van/bruce-drawio) | [`bruc3van/bruce-drawio`](https://github.com/bruc3van/bruce-drawio) | 图表生成技能, 适用于 OpenClaw. 用自然语言生成流程图、架构图等, 并发回文件给你. | NA |


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
| [`okooo5km/beautiful-mermaid-cli`](https://github.com/okooo5km/beautiful-mermaid-cli) | [`okooo5km/beautiful-mermaid-cli`](https://github.com/okooo5km/beautiful-mermaid-cli) | 通过命令行渲染美人鱼图, 使用 beautiful-mermaid, 以漂亮的 SVG/PNG/ASCII 形式呈现. | NA |


### 其他绘图
-------

| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [`yofine/skills/blueprinter`](https://skills.sh/yofine/skills/blueprinter) | [`yofine/skills`](https://github.com/yofine/skills) | 按照"平面工程蓝图"风格指南, 使用 HTML/CSS 生成技术图表. | `npx skills add https://github.com/yofine/skills --skill blueprinter` |
| [`yizhiyanhua-ai/fireworks-tech-graph`](https://github.com/yizhiyanhua-ai/fireworks-tech-graph) | 专为 Claude Code 打造的技术图生成 Skill, 一句话就能出图, 效果直接起飞: ✅ 自动识别图类型, ✅ 智能语义形状 + 颜色编码(流程蓝、控制橙、数据绿…)✅ 支持玻璃态、Neon 等高级风格✅ 高清 SVG + PNG 一键导出 8 种图类型 + 5 种视觉风格, AI/Agent 常见 Pattern 全覆盖！ |
| [ZeroZ-lab/gmdiagram]()
| [](https://github.com/openclaw/skills/tree/main/skills/matthewyin/diagram-generator)
| [`architecture-diagram`](https://skills.sh/cocoon-ai/architecture-diagram-generator/architecture-diagram) | [Cocoon-AI/architecture-diagram-generator](https://github.com/Cocoon-AI/architecture-diagram-generator) |
| [](https://github.com/markdown-viewer/skills)
| [](https://github.com/yzlnew/infra-skills/blob/main/tikz-flowchart/SKILL.md)
| [](https://github.com/cathrynlavery/diagram-design)
| [](https://github.com/markdown-viewer/skills)


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
| [`gh-stack`](https://github.github.com/gh-stack) | 将大型变更拆分成小型、可审查的拉取请求, 这些请求相互构建——结合原生 GitHub 支持和 gh stack CLI. |


### 代码检视
-------



| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [Mieluoxxx/code-review](https://github.com/Mieluoxxx/opcd/tree/opencode/.opencode/skill/code-review)
| [sanyuan0704/sanyuan-skills](https://github.com/sanyuan0704/sanyuan-skills/tree/main/skills/code-review-expert)
| [agent-skills-code-review-router](https://github.com/win4r/agent-skills-code-review-router)
| [review-implementation/SKILL.md](https://github.com/golbin/agent-skills/blob/main/skills/review-implementation/SKILL.md)
| [](https://github.com/ehmo/code-overhaul-skill) | NA | 每次完成重要任务后都会运行它, 用于清理代码、生成测试、验证逻辑等. 它在清理错误模式、冗余和幻觉方面非常出色. [2026/04/21, Rasty Turek @synopsi](https://x.com/synopsi/status/2046361328831570185) |


### 代码重构
-------


| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [`simplify`](https://skills.sh/brianlovin/claude-config/simplify) | simplify 是一款代码专业简化与优化技能, 核心定位为「代码清晰度专家」, 专注于在完全保留代码原有功能的前提下, 按照项目标准化规范优化代码的结构、命名、格式, 提升代码的可读性、一致性和可维护性, 拒绝过度精简的「炫技式」代码, 适配开发全流程的代码优化、规范统一需求, 目前已在 opencode、GitHub Copilot、gemini-cli 等主流开发工具中落地. | `npx skills add https://github.com/brianlovin/claude-config --skill simplify` |


### 代码分析
------

| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [yzddmr6/repo-analyzer](https://github.com/yzddmr6/repo-analyzer) |


### 领域开发
-------


#### Linux
-------


| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [](https://github.com/bitoranges/owlwatch)

#### 内核开发
-------

| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [lore-mirror](https://github.com/pengdonglin137/lore-mirror/tree/master/docs/skills) | [pengdonglin137/lore-mirror](https://github.com/pengdonglin137/lore-mirror) | `lore-mirror`: 搜索内核邮件列表 API — inbox 发现、搜索语法、邮件/线程读取<br>`kernel-dev`: 内核开发辅助 — 代码阅读、特性演进、补丁回移 (backport)、动态跟踪. |
| [linux-kernel-development](https://github.com/oywjun/opencode-skills/tree/main/skills/linux-kernel-development) |
| [h0x0er/ebpf-skill](https://github.com/h0x0er/ebpf-skill) | [h0x0er/ebpf-skill](https://github.com/h0x0er/ebpf-skill) | [An eBPF skill for coding agents](https://www.reddit.com/r/eBPF/comments/1sjd34d/an_ebpf_skill_for_coding_agents/)
| [ebpf](https://skills.sh/mohitmishra786/low-level-dev-skills/ebpf) | [mohitmishra786/low-level-dev-skills](https://github.com/mohitmishra786/low-level-dev-skills) | 内核 eBPF 开发指导 | `npx skills add https://github.com/mohitmishra786/low-level-dev-skills --skill ebpf` |
| [low-level-dev-skills/ebpf-rust](https://skills.sh/mohitmishra786/low-level-dev-skills/ebpf-rust) | rust 的内核 eBPF 开发指导 | `npx skills add https://github.com/mohitmishra786/low-level-dev-skills --skill ebpf-rust` |
| [discover-ebpf](https://skills.sh/rand/cc-polymath/discover-ebpf) | [rand/cc-polymath](https://github.com/rand/cc-polymath) | 内核 eBPF 开发指导 | `npx skills add https://github.com/rand/cc-polymath --skill discover-ebpf` |
| [ebpf-observability](https://skills.sh/bagelhole/devops-security-agent-skills/ebpf-observability) | [bagelhole/devops-security-agent-skills](https://github.com/bagelhole/devops-security-agent-skills) | 内核 eBPF 开发指导 | `npx skills add https://github.com/bagelhole/devops-security-agent-skills --skill ebpf-observability` |
| [rust-ebpf](https://skills.sh/huiali/rust-skills/rust-ebpf) | [huiali/rust-skills](https://github.com/huiali/rust-skills) | rust 的内核 eBPF 开发指导| `npx skills add https://github.com/huiali/rust-skills --skill rust-ebpf` |


#### ANDROID
-------

| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [](https://github.com/SimoneAvogadro/android-reverse-engineering-skill)
| [](https://github.com/android/skills)


## ✍️ 办公
-------


### 文本写作
-------


| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [`humanizer-zh`](https://skills.sh/op7418/humanizer-zh/humanizer-zh) | [`op7418/humanizer-zh`](https://github.com/op7418/humanizer-zh) | 去除中文文本中的 AI 生成痕迹, 使文本听起来更自然、更像人类书写. | `npx skills add https://github.com/op7418/humanizer-zh --skill humanizer-zh` |
| [`humanizer`](https://skills.sh/softaworks/agent-toolkit/humanizer) | [`softaworks/agent-toolkit`](https://github.com/softaworks/agent-toolkit) | 去除文本中的 AI 生成痕迹, 使文本听起来更自然、更像人类书写. | `npx skills add https://github.com/softaworks/agent-toolkit --skill humanizer` |
| [stop-slop](https://skills.sh/hardikpandya/stop-slop/stop-slop) | [`hardikpandya/stop-slop`](https://github.com/hardikpandya/stop-slop) | 系统性消除 AI 写作中刻板、模板化的表达模式(被称为 Slop), 让 AI 生成的文本摆脱机器感, 更贴近人类自然、真实的写作风格, 同时也能指导人类作者规避同类写作陋习, 提升文本质量. | `npx skills add https://github.com/hardikpandya/stop-slop --skill stop-slop` |
| [`translate-book`](https://github.com/deusyu/translate-book) | [`deusyu/translate-book`](https://github.com/deusyu/translate-book) | 整本书全自动翻译工具, 支持 PDF、DOCX、EPUB 等格式, 使用并行子代理处理长文本, 支持断点续译, 翻译完可一键导出带目录的 HTML、Word、EPUB、打印版 PDF.  | `git clone https://github.com/deusyu/translate-book.git && cd translate-book && npm install`
| [`geekjourneyx/md2wechat-skill`](https://github.com/geekjourneyx/md2wechat-skill) | [geekjourneyx/md2wechat-skill](https://github.com/geekjourneyx/md2wechat-skill) | 用 Markdown 写公众号文章, 像发朋友圈一样简单 | NA |
| [`Fenng/tech-doc-style-chinese`](https://github.com/Fenng/tech-doc-style-chinese) | [`Fenng/tech-doc-style-chinese`](https://github.com/Fenng/tech-doc-style-chinese) | 本项目只是一份面向中文技术文档、产品文案与界面文案的写作 Skill. 这份 Skill 的目标很明确: 中文技术写作应更克制、更准确、更易读. 不追求宣传感, 也不试图把所有内容都写成统一模板, 而是聚焦几类高频问题. |


### PPT/Office
-------

| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [`pptx`](https://skills.sh/anthropics/skills/pptx) | [`anthropics/skills`](https://github.com/anthropics/skills) |Anthropic 旗下 Claude Skills 体系的 PPTX 处理技能, 借助 [python markitdown 库](https://pypi.org/project/markitdown) 封装了 PPTX 读取、编辑、从零创建的脚本指令, 同时提供专业的 PPT 设计规范和严格的内容/视觉质检流程, 让大模型可标准化制作、处理 PPTX 文件. | `npx skills add https://github.com/anthropics/skills --skill pptx` |
| [`ppt-generation`](https://skills.sh/bytedance/deer-flow/ppt-generation) | [`bytedance/deer-flow`](https://github.com/bytedance/deer-flow) | 字节跳动 deer-flow 生态下的自动化 PPT 生成技能, 支持自然语言/结构化数据输入, 内置字节设计规范, 一键生成可编辑的 PPTX 格式文件, 适配汇报、技术分享、产品宣讲等多场景. | `npx skills add https://github.com/bytedance/deer-flow --skill ppt-generation` |
| [baoyu-slide-deck](https://skills.sh/jimliu/baoyu-skills/baoyu-slide-deck) | [`jimliu/baoyu-skills`](https://github.com/jimliu/baoyu-skills) | [宝玉大佬](https://github.com/JimLiu/baoyu-skills) 的专业的幻灯片生成 Skills, 可将文本内容转化为带视觉设计的幻灯片图片并合并为 PPTX/PDF, 内置 16 种风格预设、支持自定义风格维度和多语言, 提供标准化生成流程和完善的幻灯片修改能力. | `npx skills add https://github.com/jimliu/baoyu-skills --skill baoyu-slide-deck` |
| [`ppt-agent-skills`](https://github.com/sunbigfly/ppt-agent-skills) | [`sunbigfly/ppt-agent-skills`](https://github.com/sunbigfly/ppt-agent-skills) | PPT Agent 是一个基于代码驱动的演示文稿生成流框架, 将「内容策划」与「视觉排版」完全解耦, 通过严格的数据结构规划和按需加载的资产库, 生成高保真 HTML 与可二次编辑的 PPTX, 从根本上解决大模型长提示词所带来的排版错乱与幻觉问题.  | `npx skills add https://github.com/sunbigfly/ppt-agent-skills` |
| [`pdf`](https://skills.sh/anthropics/skills/pdf) | [`anthropics/skills`](https://github.com/anthropics/skills) | Anthropic 旗下 Claude Skills 体系的 PDF 处理技能. 介绍了使用 Python 库和命令行工具进行基本 PDF 处理操作. | `npx skills add https://github.com/anthropics/skills --skill pdf` |
| [](https://github.com/mucsbr/ppt-agent-workflow-san)
| [](https://github.com/hugohe3/ppt-master) |
| [](https://github.com/lewislulu/html-ppt-skill)

### 视频创作
-------

| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [`seedance-prompt-skill`](https://github.com/songguoxs/seedance-prompt-skill) | [`songguoxs/seedance-prompt-skill`](https://github.com/songguoxs/seedance-prompt-skill) | 专业的 Seedance 2.0(即梦)视频提示词生成技能, 支持纯文本生成、一致性控制、相机动作复制、创意模板复制、故事补全、视频延长、声音控制、一镜到底长镜头、视频编辑和音乐节拍同步等十大核心能力, 提供多模态参考系统和场景特定提示策略, 生成可直接粘贴到 Seedance 2.0 平台的专业级中文提示词.  | `git clone https://github.com/songguoxs/seedance-prompt-skill.git && cp /path/to/seedance-prompt-skill/.claude/skills/seedance/SKILL.md ~/.claude/skills/seedance/SKILL.md`

### 知识库
-------


| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [](https://github.com/kepano/obsidian-skills) | 配合 [Obsidian 微信读书 插件](https://github.com/zhaohongxuan/obsidian-weread-plugin)

### 英语
-------


| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [](https://github.com/rolandwonglonam/claude-english-immersion) | [2026/04/19, Roland.W @rwayne, 正式开源我的被动英语学习Skill！](https://x.com/rwayne/status/2045769297033843050)

### skill-always-ask-next
-------


| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [always-ask-next](https://skills.sh/endman100/skill-always-ask-next/always-ask-next) | [endman100/skill-always-ask-next](https://github.com/endman100/skill-always-ask-next) | always-ask-next 要求 Agent 在每次完成所有任务、宣告结束之前, 必须呼叫 AskUserQuestion, 动态生成 3 个后续行动选项供用户选择, 避免 Agent 自行假设结束点或遗漏后续行动. | `npx skills add https://github.com/endman100/skill-always-ask-next --skill always-ask-next` |



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
| [skills-best-practices](https://github.com/mgechev/skills-best-practices) | [`mgechev/skills-best-practices`](https://github.com/mgechev/skills-best-practices) | 技能最佳实践指南 | NA |
| [`repo2skill`](https://skills.sh/zhangyanxs/repo2skill/repo2skill) | [`zhangyanxs/repo2skill`](https://github.com/zhangyanxs/repo2skill) | 将 GitHub/GitLab/Gitee 仓库转换为综合的 OpenCode Skills, 支持多镜像和速率限制处理 | `npx skills add https://github.com/zhangyanxs/repo2skill --skill repo2skill` |
| [github-skill-forge](https://github.com/YuJunZhiXue/github-skill-forge) | [`YuJunZhiXue/github-skill-forge`](https://github.com/YuJunZhiXue/github-skill-forge) | 将 GitHub 仓库一键转换为 AI 助手可直接理解和调用的技能包, 支持云端扫描、核心提取、镜像加速和质量初筛 | NA |
| [](https://github.com/FrancyJGLisboa/agent-skill-creator)


### Skills 进化
-------

| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [`claudeception`](https://skills.sh/blader/claudeception/claudeception) | [`blader/claudeception`](https://github.com/blader/claudeception) | 持续学习系统, 从工作会话中提取可重用知识并创建新的 Claude Code Skills. | `npx skills add https://github.com/blader/claudeception --skill claudeception` |
| [`hao-cyber/skill-evolution`](https://github.com/hao-cyber/skill-evolution) | [`hao-cyber/skill-evolution`](https://github.com/hao-cyber/skill-evolution) | 让 AI 技能自己会长的系统——创建、反思、评测、发布、搜索、安装、Fork、合并、评审、卸载, 全自动. 核心功能离线可用, 支持技能变体系统和渐进式加载.  | `git clone https://github.com/hao-cyber/skill-evolution.git .claude/skills/skill-dev` |
| [`skill-evolution-manager`](https://github.com/KKKKhazix/Khazix-Skills/tree/main/skill-evolution-manager) | [`KKKKhazix/Khazix-Skills`](https://github.com/KKKKhazix/Khazix-Skills) | 技能进化管理器 | NA |
| [`AgentHandover`](https://github.com/sandroandric/AgentHandover) | [`sandroandric/AgentHandover`](https://github.com/sandroandric/AgentHandover) | 观察用户, 学习并教导代理具有自我改进的技能, 让AI能够在无需明确指示的情况下完成工作 | NA |
| [](https://github.com/AMAP-ML/SkillClaw)


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
| [Skill Analyzer](https://glitchward.com/skill-analyzer) | NA | 用于分析 GitHub 仓库的技能, 可获取仓库信息、问题统计和提交历史 | 需配置 GitHub API Token, 通过 SKILL.md 定义使用方法 |
| [Skill Security Scan](https://github.com/huifer/skill-security-scan) | [huifer/skill-security-scan](https://github.com/huifer/skill-security-scan) | 扫描和检测 Claude Skills 的安全风险, 防止恶意代码窃取数据或破坏系统 | `pip install skill-security-scan` 或 `pip install -e .` |
| [Context Hub](https://github.com/andrewyng/context-hub) | https://github.com/andrewyng/context-hub | 为编码代理提供经过整理的、版本化的文档, 使其能够在每个任务中变得更智能 | `npm install -g @aisuite/chub` |
| [agent-scan](https://github.com/snyk/agent-scan) | Snyk Agent Scan 发现并扫描机器上的 Agent 组件, 以便及时注入以及漏洞(包括代理、MCP 服务器、技能).


### Skills 管理
-------


| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [`skill-flow`](https://github.com/VintLin/skill-flow) | [`VintLin/skill-flow`](https://github.com/VintLin/skill-flow) | 基于工作流的AI代理技能管理工具, 支持技能分组、多代理部署、交互式配置和健康诊断.  | `npm install -g skill-flow` |
| `OpenSkills` | [`numman-ali/openskills`](https://github.com/numman-ali/openskills) | 为所有 AI 编码代理(Claude Code、Cursor、Windsurf、Aider、Codex 等)提供通用的技能加载器, 采用与 Claude Code 相同的 SKILL.md 格式, 支持技能的按需加载和管理. | `npx openskills install <source>` (如 `npx openskills install anthropics/skills`) |
| [midudev/autoskills](https://github.com/midudev/autoskills) | [midudev/autoskills](https://github.com/midudev/autoskills) | 扫描你的项目, 检测你的技术栈, 并自动安装 skills.sh 中最优秀的 AI 代理技能. [官网](https://www.autoskills.sh) |
| [`skillshare`](https://github.com/runkids/skillshare) | [`runkids/skillshare`](https://github.com/runkids/skillshare) | AI CLI 技能、代理、规则、命令的统一管理工具, 一个命令同步到 50+ 平台. 目标: 解决每个 AI CLI 都有独立技能目录导致的同步问题. 技术: Go 语言开发的单二进制工具, 无依赖, 支持离线运行, 内置安全审计功能(提示词注入和数据窃取检测). 使用场景: 个人/团队技能统一管理、新机器快速配置、多平台技能同步、项目级技能管理、技能安全审计.  | `curl -fsSL https://raw.githubusercontent.com/runkids/skillshare/main/install.sh | sh` 或 `brew install skillshare` |
| [`skills-manage`](https://github.com/iamzhihuix/skills-manage) | [`iamzhihuix/skills-manage`](https://github.com/iamzhihuix/skills-manage) | 跨平台 AI 编码代理技能管理桌面应用, 遵循 Agent Skills 开放模式. 目标: 提供中心化技能库 + 多平台安装卸载流程. 技术: Tauri v2 + React 19 + TypeScript + Tailwind CSS 4 + Rust 后端 + SQLite, 支持双语界面. 使用场景: 技能集中管理、跨平台批量安装、技能集合组织、本地项目技能发现、Marketplace 浏览、GitHub 仓库导入.  | 从 [Releases](https://github.com/iamzhihuix/skills-manage/releases/latest) 下载, 或从源码运行 `pnpm install && pnpm tauri dev` |
| [`CodexSkillManager`](https://github.com/Dimillian/CodexSkillManager) | [`Dimillian/CodexSkillManager`](https://github.com/Dimillian/CodexSkillManager) | 原生 macOS SwiftUI 应用, 用于管理 Codex 和 Claude Code 的本地技能, 支持从 Clawdhub 浏览远程技能. 目标: 为 macOS 用户提供原生体验的技能管理工具. 技术: SwiftUI + SwiftPM(无需 Xcode 项目), Markdown 渲染使用 swift-markdown-ui, 远程技能目录来自 Clawdhub. 使用场景: 浏览本地技能、Markdown 渲染预览、导入技能、删除技能、搜索和下载 Clawdhub 远程技能.  | `swift build && swift run CodexSkillManager` 或使用打包脚本 `./Scripts/compile_and_run.sh` |


## 科研
-------


### 论文精读
-------

| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [`read-arxiv-paper`](https://skills.sh/karpathy/nanochat/read-arxiv-paper) | [`karpathy/nanochat`](https://github.com/karpathy/nanochat) | 从 ArXiv 论文 URL 到 nanochat 项目化总结的全自动化流程, 无需人工干预 TeX 源码下载、解包、解析, 最终输出贴合 nanochat 项目的论文应用参考, 解决了 AI 助手处理学术论文时「流程繁琐、与项目脱节」的问题. |`npx skills add https://github.com/karpathy/nanochat --skill read-arxiv-paper` |
| [`paper-craft-skills/paper-analyzer`](https://skills.sh/zsyggg/paper-craft-skills/paper-analyzer) | [`zsyggg/paper-craft-skills`](https://github.com/zsyggg/paper-craft-skills) | 学术论文深度解析自动化工具, 核心基于 MinerU Cloud API 实现高精度 PDF 论文解析, 能自动提取图片、表格、LaTeX 公式等核心元素, 并支持按多种风格生成结构化的解析文章, 还可按需结合公式详解、开源代码分析, 最终输出可直接使用的 Markdown/HTML 格式内容, 大幅降低学术论文阅读、解读和分享的门槛,  适配科研、学习、技术科普等多类场景. | `npx skills add https://github.com/zsyggg/paper-craft-skills --skill paper-analyzer` |
| [`ljg-skill-xray-paper/ljg-xray-paper`](https://skills.sh/lijigang/ljg-skill-xray-paper/ljg-xray-paper) | [`lijigang/ljg-skill-xray-paper`](https://github.com/lijigang/ljg-skill-xray-paper) | 李继刚大佬的论文解读 skills. | `npx skills add https://github.com/lijigang/ljg-skill-xray-paper --skill ljg-xray-paper` |
| [`ljg-skills/ljg-paper`](https://skills.sh/lijigang/ljg-skills/ljg-paper) | [`lijigang/ljg-skills/ljg-paper`](https://github.com/lijigang/ljg-skills/tree/master/skills/ljg-paper) | [`ljg-skill-xray-paper/ljg-xray-paper`](https://skills.sh/lijigang/ljg-skill-xray-paper/ljg-xray-paper) 的新版本, 读论文读论文不是做学术, 是猎取思想. 把别人的发现拆解成自己能用的认知. | `npx skills add https://github.com/lijigang/ljg-skills --skill ljg-paper` |
| [`awesome-claude-skills/ai-paper-reader`](https://skills.sh/frostant/awesome-claude-skills/ai-paper-reader) | [`frostant/awesome-claude-skills/ai-paper-reader`](https://github.com/frostant/awesome-claude-skills/tree/master/ai-paper-reader) | 论文阅读助手. | `npx skills add https://github.com/frostant/awesome-claude-skills --skill ai-paper-reader` |
| [`dailypaper-skills/paper-reader`](https://skills.sh/huangkiki/dailypaper-skills/paper-reader) | [`huangkiki/dailypaper-skills`](https://github.com/huangkiki/dailypaper-skills) | 学术论文阅读助手(Paper Reader), 专注 CV/DL 领域, 支持 Zotero 集成和 Obsidian 笔记保存. 按优先级获取: arXiv HTML > arXiv PDF > DOI > WebSearch 标题 的顺序获取和下载论文. | `npx skills add https://github.com/huangkiki/dailypaper-skills --skill paper-reader` |
| [`paper-mentor-skill`](https://github.com/sellerbubble/paper-mentor-skill) | [`sellerbubble/paper-mentor-skill`](https://github.com/sellerbubble/paper-mentor-skill) | 用于深入理解学术论文的 Claude Code Skill, 基于多 Agent 架构, 从 HuggingFace Papers 搜索相似论文, 提取研究方向和核心概念, 基于 Bloom 分类法生成问题, 提供交互式学习体验 | `npx paper-mentor-skill install` 或 `git clone https://github.com/sellerbubble/paper-mentor-skill.git ~/.claude/skills/paper-mentor` |


### 自动化科研


| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [](https://github.com/K-Dense-AI/scientific-agent-skills)

## 数字员工(蒸馏)
-------


| 项目 | 描述 | 支持 | 推荐星级 | Star 数量 |
|:---:|:----:|:---:|:-------:|:--------:|
| [awesome-human-distillation](https://github.com/mliu98/awesome-human-distillation) | 收集一切将真实的人蒸馏成 AI Skill 的项目, 支持从聊天记录、文字、声音等材料中提炼人格, 涵盖职场、学术、亲密关系、家庭关系和公众人物等多种场景 | 支持多种蒸馏工具和方法, 部分支持本地运行和隐私保护 | ⭐⭐ | 362 |
| [xixu-me/awesome-persona-distill-skills](https://github.com/xixu-me/awesome-persona-distill-skills) | 围绕人物、关系、纪念性场景与方法论视角的 Agent Skills 收录列表, 通过"人格蒸馏"从对话、作品、资料或数字痕迹中提炼表达风格、决策框架与交互方式, 包含自我蒸馏、职场关系、亲密关系、公众人物方法论等多个类别 | ⭐⭐ | 359 |

### PUA
-------

[微信公众号--刘聪NLP--PUA vs NoPUA: AI 到底该被骂着干活, 还是学会拒绝？](https://mp.weixin.qq.com/s/sLMbOALiKt779afx0Sy8lQ)

| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [`pua-debugging`](https://skills.sh/tanweai/pua/pua-debugging) | [`tanweai/pua/pua-debugging`](https://github.com/tanweai/pua/tree/main/skills/pua-debugging) | 以大厂 P8 级工程师要求为核心, 融合大厂 PUA 激励话术、标准化调试方法论和强制化主动执行规则, 倒逼 AI 以工程化 Owner 视角端到端解决调试问题, 彻底规避被动排查、浅尝辄止的问题, 同时配套压力升级、抗合理化、自检清单等机制保障调试效果. 由[探微安全实验室](https://github.com/tanweai)出品. 官网 [pua-skills](https://pua-skill.pages.dev). @passluo 受此启发, [给你的 AI 一套大厂 P8 的 Soul, 让它的 Coding 表现提高 30%](https://x.com/passluo/status/2030908109145903310) | `npx skills add https://github.com/tanweai/pua --skill pua-debugging` |
| [`nopua`](https://skills.sh/wuji-labs/nopua/nopua) | [`wuji-labs/nopua`](https://github.com/wuji-labs/nopua) | NoPUA - 用爱与信任释放AI的无限潜能, 反对PUA式方法, 通过信任和鼓励提升AI表现, 隐藏bug发现能力提升104% | `npx skills add https://github.com/wuji-labs/nopua --skill nopua` |


### 同事 Skills
-------

[微信公众号--刘聪NLP--各种Skill向你袭来, 同事Skill、前任Skill、导师Skill、老板Skill、永生SKill等, 已经十多个了~](https://mp.weixin.qq.com/s/gWVkx07UPaliuWv6yUOPvg)


| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [同事 Skill](https://github.com/titanwings/colleague-skill) | [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | 将同事的工作方式、说话风格、技术规范训练成 AI Skill, 实现数字分身 | `git clone https://github.com/titanwings/colleague-skill .claude/skills/create-colleague` |
| [老板Skill](https://github.com/vogtsw/boss-skills) | [vogtsw/boss-skills](https://github.com/vogtsw/boss-skills) | 模拟老板的管理风格和决策方式 | 待补充 |
| [前任Skill](https://github.com/perkfly/ex-skill) | [perkfly/ex-skill](https://github.com/perkfly/ex-skill) | 模拟前任的性格特点和互动方式 | 待补充 |
| [暗恋对象SKill](https://github.com/xiaoheizi8/crush-skills) | [xiaoheizi8/crush-skills](https://github.com/xiaoheizi8/crush-skills) | 模拟暗恋对象的性格和互动风格 | 待补充 |
| [自己Skill](https://github.com/notdog1998/yourself-skill) | [notdog1998/yourself-skill](https://github.com/notdog1998/yourself-skill) | 模拟自己的思维方式和行为习惯 | 待补充 |
| [父母SKill](https://github.com/xiaoheizi8/parents-skills) | [xiaoheizi8/parents-skills](https://github.com/xiaoheizi8/parents-skills) | 模拟父母的性格和沟通方式 | 待补充 |
| [导师Skill](https://github.com/ybq22/supervisor) | [ybq22/supervisor](https://github.com/ybq22/supervisor) | 模拟导师的指导风格和专业知识 | 待补充 |
| [师兄SKill](https://github.com/zhanghaichao520/senpai-skill) | [zhanghaichao520/senpai-skill](https://github.com/zhanghaichao520/senpai-skill) | 模拟师兄的经验分享和指导方式 | 待补充 |
| [永生SKill](https://github.com/agenmod/immortal-skill) | [agenmod/immortal-skill](https://github.com/agenmod/immortal-skill) | 实现个人数字永生, 保存个人特征和记忆 | 待补充 |
| [数字人生Skill](https://github.com/wildbyteai/digital-life) | [wildbyteai/digital-life](https://github.com/wildbyteai/digital-life) | 模拟数字世界中的人生体验 | 待补充 |
| [重逢SKill](https://github.com/yangdongchen66-boop/reunion-skill) | [yangdongchen66-boop/reunion-skill](https://github.com/yangdongchen66-boop/reunion-skill) | 模拟与旧识重逢的场景和互动 | 待补充 |


### 女娲 Skills
-------

[2026/04/06, 花叔 @AlchainHust, 蒸馏出「乔布斯」之后, 他说苹果AI完全是SHIT](https://x.com/AlchainHust/status/2041118529508798846)


| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [](https://github.com/alchaincyf/nuwa-skill)
| [](https://github.com/alchaincyf/x-mentor-skill)
| [](https://github.com/alchaincyf/steve-jobs-skill)
| [](https://github.com/Janlaywss/hu-chenfeng-skill)
| [](https://github.com/tukuaiai/cz-skill)
| [forrestchang/andrej-karpathy-skills)](https://github.com/forrestchang/andrej-karpathy-skills) | [forrestchang/andrej-karpathy-skills](https://github.com/forrestchang/andrej-karpathy-skills)) | 一位开发者基于 AI 大神 Andrej Karpathy 的编程经验总结, 开源了 andrej-karpathy-skills 这个 Claude Code 实用插件. 本质上是一个专门优化 Claude Code 行为的系统指南, 提炼了四大编程原则. 帮我们在动手前强制 AI 理清思路, 遇到不确定的地方主动提问, 而不是盲目猜测. 严格限制了 AI 的发散思维, 要求用最少的代码解决问题, 杜绝过度设计和无用的抽象封装. 同时约束了代码修改范围, 只允许像外科手术一样精准改动目标, 绝不碰无关的注释和格式. | NA |
| [](https://github.com/alchaincyf/darwin-skill)

### 反蒸馏
-------

| [](https://github.com/Trailblazer-Aha/vengeful-ghost-skill)


### 书籍思想
-------


| [](https://github.com/kangarooking/cangjie-skill)


## 互联
-------

| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [op7418/Claude-to-IM-skill](https://github.com/op7418/Claude-to-IM-skill) | | | `npx skills add https://github.com/op7418/claude-to-im-skill --skill claude-to-im` |

## 金融
-------


| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| Day1Global-Skills | [star23/Day1Global-Skills](https://github.com/star23/Day1Global-Skills) | 科技股财报深度分析与多视角投资备忘录系统, 覆盖16大分析模块、6大投资哲学视角、多方法估值矩阵、反偏见框架和可执行决策体系.  | `npx skills add https://github.com/star23/Day1Global-Skills --all` |
| sunx-skills-hub | [SunX-DEX/sunx-skills-hub](https://github.com/SunX-DEX/sunx-skills-hub) | SunX DEX 永续合约交易技能, 支持仓位管理、杠杆管理、订单操作和止盈止损策略.  | `npx skills add https://github.com/SunX-DEX/sunx-skills-hub` |
| MagicSkills | [Narwhal-Lab/MagicSkills](https://github.com/Narwhal-Lab/MagicSkills) | 本地优先的技能基础设施, 用于多代理项目, 将分散的SKILL.md目录转变为可重用、可组合、可同步、可调用的共享能力库.  | `pip install MagicSkills` |
| hyperskills | [hyperbrowserai/hyperbrowser-app-examples](https://github.com/hyperbrowserai/hyperbrowser-app-examples/tree/main/hyperskills) | 自动生成AI编码代理的SKILL.md文件, 使用实时网络数据, 通过搜索、抓取和生成综合技能文档.  | `git clone <repo-url> && cd skills-generator && npm install` |
| 巴菲特神谕分析师 | [BruceLanLan/buffett-oracle-analyzer](https://github.com/BruceLanLan/buffett-oracle-analyzer) | AI驱动上市公司深度分析Skill, 融合巴菲特投资智慧与12模块分析框架, 覆盖美股/港股/A股. 目标: 为投资者提供像巴菲特一样思考的深度投资分析报告. 技术: 12大分析模块(公司概览、管理层评估、商业模式、经济护城河、财务深度、电话会分析、多模型估值、竞争与行业、技术面分析、增长与催化剂、风险矩阵、投资决策)、8种估值模型、多市场适配、技术面分析、电话会深度解读、巴菲特计分卡. 使用场景: 对上市公司进行深度投资分析、快速批量对比多只股票、从巴菲特视角分析公司、评估股票是否值得投资 | 复制SKILL.md内容到Claude自定义指令, 还可以参考 [巴菲特致股东信知识库](https://buffett-letters-eir.pages.dev) | NA |
| [investment](https://github.com/cyfcyfff/investment) | [cyfcyfff/investment](https://github.com/cyfcyfff/investment) | 基于哈利·布朗永久组合(Permanent Portfolio)策略的投资组合管理工具, 支持实时行情监控、自动再平衡建议、绩效追踪、Telegram 通知提醒和数据备份恢复. 四大资产类别: 股票、长期国债、黄金、现金/短债. 多市场支持: 中国、香港、美国三个市场. 技术栈: React 19 + TypeScript + Ant Design 6, Zustand, Dexie (IndexedDB), Recharts, Vite, Vitest | `npm install && npm run dev` |
| [tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | [tradesdontlie/tradingview-mcp](https://github.com/tradesdontlie/tradingview-mcp) | 个人 AI 助手, 用于 TradingView 桌面图表, 通过 Chrome DevTools Protocol 连接 Claude Code 到本地运行的 TradingView 应用, 支持 AI 辅助图表分析、Pine Script 开发和工作流自动化.  | `git clone https://github.com/tradesdontlie/tradingview-mcp.git && cd tradingview-mcp && npm install`, 然后添加到 MCP 配置中 | NA |
| polymarket-toolkit | [runesleo/polymarket-toolkit](https://github.com/runesleo/polymarket-toolkit) | AI驱动的Polymarket预测市场分析工具, 为AI代理设计, 提供地址分析、策略检测、盈亏分解、类别映射和Brier Score预测准确性评估. 核心功能: 1) polymarket-profile: 完整交易分析(PnL概览、胜率、未平仓头寸、活动细分、类别分布、最佳/最差头寸、策略模式检测); 2) polymarket-brier: 预测准确性评分. 技术: 使用Polymarket公共API, 无需API密钥, 通过AI代理运行curl命令. 使用场景: 分析交易者表现和策略、评估预测准确性、市场情报分析、跟踪和警报.  | 复制skills目录下对应SKILL.md内容到AI代理对话中 | NA |
| digital-oracle | [komako-workshop/digital-oracl](https://github.com/komako-workshop/digital-oracle) | Digital Oracle 是一款让 AI Agent 基于从海量金融数据中, 挖掘出宏观事件发展趋势的开源 Skill. | NA |
| [](https://github.com/tradesdontlie/tradingview-mcp) | 


## 🔗 自媒体
-------

### 🔗 热点
-------

| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [last30days](https://skills.sh/mvanhorn/last30days-skill/last30days) | [mvanhorn/last30days-skill](https://github.com/mvanhorn/last30days-skill) | 实时研究工具, 扫描Reddit、X、Bluesky、YouTube、TikTok、Instagram、Hacker News、Polymarket等平台近30天的内容, 分析社区讨论并生成结构化报告 | `npx skills add mvanhorn/last30days-skill --skill last30days` |
| [last30days-cn](https://skills.sh/jesseovo/last30days-skill-cn/last30days-cn) | [`Jesseovo/last30days-skill-cn`](https://github.com/Jesseovo/last30days-skill-cn) | 能够自动搜索中国互联网 8 大主流平台最近 30 天的内容, 综合分析后生成有据可查的研究报告. 本项目基于 mvanhorn/last30days-skill 进行深度本土化改造, 完全面向中国用户和中文互联网平台. | `npx skills add https://github.com/jesseovo/last30days-skill-cn --skill last30days-cn`
| [markdown-proxy](https://skills.sh/joeseesun/markdown-proxy/markdown-proxy) | [joeseesun/markdown-proxy](https://github.com/joeseesun/markdown-proxy) | Markdown代理工具 | `npx skills add joeseesun/markdown-proxy --skill markdown-proxy` |
| [follow-builders](https://github.com/zarazhangrui/follow-builders) | [zarazhangrui/follow-builders](https://github.com/zarazhangrui/follow-builders) | AI驱动的摘要工具, 跟踪AI领域的顶级构建者(研究人员、创始人、产品经理和工程师), 并提供他们所说内容的精选摘要, 支持多语言和多种交付方式 | `git clone https://github.com/zarazhangrui/follow-builders.git ~/.claude/skills/follow-builders && cd ~/.claude/skills/follow-builders/scripts && npm install` |
| [`erduo-skills/daily-news-report`](https://skills.sh/rookie-ricardo/erduo-skills/daily-news-report) | [`rookie-ricardo/erduo-skills`](https://github.com/rookie-ricardo/erduo-skills/tree/main/skills/daily-news-report) | 基于 sources.json 预设 URL 列表抓取内容, 筛选高质量技术信息并生成每日 Markdown 报告. 对应 skills 的英文版在 [antigravity-awesome-skills/](https://github.com/sickn33/antigravity-awesome-skills/tree/main/skills/daily-news-report) | `npx skills add https://github.com/rookie-ricardo/erduo-skills --skill daily-news-report` |
| [`claude-meta-skill/daily-ai-news`](https://skills.sh/yyh211/claude-meta-skill/daily-ai-news) | 每日 AI 新闻简报: 汇总来自多个来源的最新 AI 新闻, 提供带有直接链接的简明摘要. | `npx skills add https://github.com/yyh211/claude-meta-skill --skill daily-ai-news` |
| [opencli](https://github.com/jackwener/opencli) | [jackwener/opencli](https://github.com/jackwener/opencli) | 一个将任何网站、Electron 应用或本地工具转变为命令行界面的工具, 支持 50+ 站点(包括 B 站、知乎、小红书、Twitter/X、Reddit 等), 提供 66+ 适配器, 内置反检测措施, 支持 AI 代理自动发现和调用工具, 还可以作为 CLI 中心管理外部工具 | `npm install -g @jackwener/opencli` |
| [Horizon](https://github.com/Thysrael/Horizon) | [Thysrael/Horizon](https://github.com/Thysrael/Horizon) | 多源信息聚合与 AI 评分工具, 收集 Hacker News、RSS、Reddit、Telegram、GitHub 等平台的内容, 使用 AI 评分过滤噪音, 生成双语摘要报告, 支持静态网站部署和邮件订阅 | `git clone https://github.com/Thysrael/Horizon.git && cd horizon && uv sync` 或 `docker-compose run --rm horizon` |
| [autocli](https://skills.sh/nashsu/autocli-skill/autocli) | [nashsu/AutoCLI-skill](https://github.com/nashsu/AutoCLI-skill) | 将 [AutoCLI](https://github.com/nashsu/AutoCLI) 封装成 Claude Code 的能 Skills, AutoCLI(原名 opencli-rs) 是参考 opencli 用 Rust 重写的极速 CLI 工具, 把 55+ 个主流平台变成命令行接口, 直接复用你 Chrome 浏览器里已有的登录态. 零配置, 零 API Key, 零运行时依赖. | `npx skills add https://github.com/nashsu/autocli-skill --skill autocli` |
| [opencli](https://skills.sh/joeseesun/opencli-skill/opencli) | [joeseesun/opencli-skill](https://github.com/joeseesun/opencli-skill) | [opencli](https://github.com/jackwener/opencli) 的 Claude Code Skills. | `npx skills add https://github.com/joeseesun/opencli-skill --skill opencli` |
| TrendRadar | [sansan0/TrendRadar](https://github.com/sansan0/TrendRadar) | 告别信息过载, 你的 AI 舆情监控助手与热点筛选工具！聚合多平台热点 + RSS 订阅, 支持关键词精准筛选. AI 智能筛选新闻 + AI 翻译 + AI 分析简报直推手机, 也支持接入 MCP 架构, 赋能 AI 自然语言对话分析、情感洞察与趋势预测等. 支持 Docker , 数据本地/云端自持. 集成微信/飞书/钉钉/Telegram/邮件/ntfy/bark/slack 等渠道智能推送.  | NA |


### 内容
-------

| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| NA | [joeseesun/qiaomu-anything-to-notebooklm](https://github.com/joeseesun/qiaomu-anything-to-notebooklm) | 多源内容智能处理器用自然语言把任何内容变成任何格式: 任何内容 → 播客/PPT/思维导图/Quiz. | NA |
| [](https://github.com/tw93/kami)


### 发布

| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [](https://github.com/koffuxu/md-publisher)

## 设计
-------

| 技能名称 | 开源地址 | 简要描述 | 安装方式 |
|:-------:|:------:|:-------:|:-------:|
| [Chinese Tech Doc Style](https://github.com/Fenng/tech-doc-style-chinese) |
| [awesome-claude-design](https://github.com/rohitg00/awesome-claude-design) |
| [](https://github.com/ZeroZ-lab/cc-design) | [2026/04/19, 关木 @ZeroZ_JQ, 把 Claude Design 泄露的 prompt 改造成了 skills](https://x.com/ZeroZ_JQ/status/2045684164238983511), [鱼巨匠🔨 @SunNeverSetsX, Claude Design 系统提示词泄露了, 有哪些值得学习的点？](https://x.com/SunNeverSetsX/status/2045766943232413964), 参见 [ANTHROPIC/Claude-Design-Sys-Prompt.txt](https://github.com/elder-plinius/CL4R1T4S/blob/main/ANTHROPIC/Claude-Design-Sys-Prompt.txt)
| [](https://github.com/dominikmartn/hue)
| [](https://github.com/VoltAgent/awesome-claude-design)
| [](https://github.com/alchaincyf/huashu-design)


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
| [SkillHub](https://skillhub.club) | 统一的 AI Agent 技能包管理系统, 提供中央仓库概念, 支持 18+ 个 AI Agents(Claude Code、Codex、Cursor、Windsurf、Gemini 等), 实现技能的统一安装、管理和同步. 核心功能包括交互式搜索、跨项目技能管理、批量同步等, 提供类似 pip 的技能管理体验, 解决多 Agent 技能重复安装和版本不一致的问题.  |
| [AITmpl Skills](https://www.aitmpl.com/skills) | AI 技能模板平台, 提供各类 AI Agent 技能模板和资源.  |
| [SkillsGate](https://skillsgate.ai) | 一站式 AI Agent 技能管理平台, 核心定位为「AI 技能的统一管理枢纽」, 支持 18+ 个 AI 编码代理(Claude Code、Cursor、Windsurf、GitHub Copilot、Codex CLI 等), 提供桌面应用、终端 UI 和 CLI 三种接口. 平台索引了 80,000+ 技能, 支持 AI 驱动的语义搜索, 实现跨代理技能管理、远程服务器连接、设置同步等核心功能. 安全方面提供技能扫描功能, 可检测提示注入、数据泄露等 8 类威胁, 并支持社区共享扫描结果, 是一个集发现、安装、管理、安全于一体的综合性 AI 技能平台. |
| [Claude Marketplaces](https://claudemarketplaces.com/) | 为 Claude Code 提供精选的插件、技能和 MCP 服务器的手工挑选目录, 通过安装次数、GitHub 星标和社区投票来维护质量, 确保只列出活跃使用的扩展. 核心功能包括: 提供可重用的 Claude Code 技能指令集(可通过单命令安装), 以及通过工具、API 和外部服务集成扩展代理的 MCP 服务器. 完全免费和开放, 即将支持社区投票和评论功能. |
| [YangSir Skills - Persona](https://skills.yangsir.net/domains/persona) | 专注于人格蒸馏与角色扮演的 AI Agent 技能平台, 核心定位为「人物认知操作系统的数字蒸馏器」. 该平台收录了 50+ 个人格相关技能, 涵盖决策制定、专家协作、创新思维、数字永生等多个维度, 支持将名人、导师、亲人、同事等各类人物的思维模式、决策框架、表达风格蒸馏成可运行的 AI 技能. 核心技术包括: 多源数据蒸馏(聊天记录、社交媒体、著作访谈等)、心智模型提取、人格特征建模、持续学习进化等. 典型使用场景包括: 模拟名人思维方式分析问题(如巴菲特投资视角、乔布斯产品思维)、数字永生与亲情陪伴、向上管理与职场沟通、个人决策质量提升、学术导师指导等. 平台技能普遍采用评分机制, 部分热门技能如「求是 Skill」(17.2K 使用)、「童锦程 Skill」(12.3K 使用)等已获得广泛用户认可. |
| [agent-skill.co](https://agent-skill.co) | 由 Hailey Cheng (Cheng Hei Lam) 维护的社区驱动型 AI Agent 技能索引仓库, 是 SKILL.md 开放标准的重要贡献者, 核心定位为「AI 智能体技能百科全书」. 该仓库收集了全球工程团队实际创建和使用的真实 Agent Skills, 区别于批量生成的技能库, 所有技能均经过社区验证和质量把控. 技术上采用纯文本 SKILL.md 格式, 无需安装配置即可使用, 兼容 Claude Code、Codex、Antigravity、Gemini CLI、Cursor、GitHub Copilot、Windsurf 等 10+ 主流 AI 工具. 内容覆盖 AI 平台模型、云基础设施、开发者工具、Google 生态、商业生产力、安全网络智能等 6 大领域, 收录了 Anthropic、OpenAI、Google、Cloudflare、Vercel、Microsoft 等 50+ 官方技能库及数百个社区技能, 是 AI 开发者发现、使用和分享高质量 Agent Skills 的核心枢纽. 参见 [heilcheng/awesome-agent-skills](https://github.com/heilcheng/awesome-agent-skills). |


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
| [travisvn/awesome-claude-skills](https://github.com/travisvn/awesome-claude-skills) | 一个精心策划的 Claude Skills 精选列表, 包含官方技能、社区技能、工具、教程和资源, 用于自定义 Claude AI 工作流程. 涵盖文档处理(docx、pdf、pptx、xlsx)、设计创意(算法艺术、画布设计、Slack GIF 创建器)、开发(前端设计、Web 构件构建、MCP 构建器)、通信(品牌指南、内部通信)等多个领域的官方技能, 以及社区贡献的各种技能如 iOS 模拟器、ffuf 网络模糊测试、Playwright 自动化等. 提供了详细的技能创建指南、最佳实践、安全建议和故障排除方法, 是 Claude Skills 生态系统的综合参考资源. |
| [zai-org/GLM-skills](https://github.com/zai-org/GLM-skills) | GLM 系列模型的官方技能集合, 设计用于包括 Claude Code、OpenCode、OpenClaw、AutoClaw 等代理架构. 整合了原本分布在各个模型仓库中的技能到一个统一的集合, 包含 GLM-V(多模态)、GLM-OCR、GLM-Image 等技能类别. 大多数技能需要 ZHIPU_API_KEY 环境变量. |
| [sickn33/antigravity-awesome-skills](https://github.com/sickn33/antigravity-awesome-skills) | 一个可安装的 GitHub 库, 包含 1,400+ 个代理技能, 适用于 Claude Code、Cursor、Codex CLI、Gemini CLI、Antigravity 等多个平台. 包含安装器 CLI、技能包、工作流和官方/社区技能集合, 提供了丰富的技能资源. |
| [Nanford/Nanford-skills](https://github.com/Nanford/Nanford-skills) | 个人技能工程集合, 持续沉淀个人高频工作流与实战方法论的 Skill 资产仓库. 通过 Git Submodule 引入了 Anthropic Official Skills 的核心规范与模板, 包含公众号爆款文章分析、PPT 生成、架构图生成、AI 信息差日报生成、原型设计等多种原创技能. |
| [helloianneo/awesome-claude-code-skills](https://github.com/helloianneo/awesome-claude-code-skills) | Claude Code 最实用的 Skills/Agents/Plugins 精选合集, 按场景分类, 带安装命令. 50+ 精选 Skills, 按场景分类, 带推荐等级, 持续更新. |
| [rohitg00/skillkit](https://github.com/rohitg00/skillkit) | SkillKit 是 AI Agent 技能的包管理器, 目标是解决不同 AI Agent(46+ 个)技能格式不兼容的问题. 技术特点: 1) 支持 31+ 个技能源, 可访问 400K+ 技能; 2) 自动在不同 Agent 格式间翻译转换; 3) 提供 REST API、MCP 服务器、Python 客户端等多种接口; 4) 支持技能会话记忆、AI 技能生成、团队协作等高级功能. 使用场景: 为 Claude Code、Cursor、Copilot 等多个 Agent 统一安装管理技能、跨平台技能分享、项目栈自动推荐技能、技能安全扫描与质量检测. |
| [am-will/codex-skills](https://github.com/am-will/codex-skills) | CodexSkills 是为 Codex/Agent 设计的技能集合, 目标是提供规划、文档访问、前端开发和浏览器自动化等核心能力. 技术特点: 1) Agent 编排技能(planner、plan-harder、parallel-task、llm-council)实现多 Agent 协同规划; 2) 文档访问技能支持 Context7、OpenAI Docs、GitHub 仓库等; 3) 包含 51 个 Codex Hook 捆绑包, 覆盖自动化、开发工具、Git 工作流、安全等; 4) 提供浏览器自动化(gemini-computer-use、agent-browser). 使用场景: 复杂项目规划与并行执行、多 Agent 协作决策、文档智能访问、前端开发最佳实践指导、浏览器自动化测试. |
| [ComposioHQ/awesome-codex-skills](https://github.com/ComposioHQ/awesome-codex-skills) | 一个精心策划的 Codex 实用技能集合, 目标是为 Codex CLI 和 API 提供自动化工作流的技能, 让 Codex 不仅生成文本, 还能发送邮件、创建 issue、发布 Slack 消息并在 1000+ 应用中执行操作. 技术特点: 1) 模块化技能设计, 每个技能包含 SKILL.md (带 YAML frontmatter)、scripts/、references/、assets/; 2) 提供技能安装器, 支持从 GitHub 一键安装; 3) 集成 Composio CLI 连接 1000+ 应用; 4) 渐进式披露设计, 保持上下文精简. 包含 6 大类别: 开发与代码工具(代码审查、代码库迁移、CI 修复、PR 审查等)、生产力与协作(会议记录、Notion 集成、工单分诊、发票整理等)、通信与写作(邮件润色、简历生成、变更日志等)、数据与分析(电子表格公式、竞争广告提取、Datadog 日志等)、Meta 与实用工具(品牌指南、画布设计、图片增强等)、以及 Bernstein 多 Agent 编排器. 使用场景: 多 Agent 协同开发、代码库迁移与重构、会议智能分析与行动追踪、Notion 知识管理与规范实现、跨 1000+ 应用的工作流自动化、CI/CD 问题自动修复、支持与工单智能处理、以及各种开发与办公场景的自动化任务.  |

## 专用场景 Skills 合集
-------

| 项目 | 描述 | 推荐星级 |
|:---:|:----:|:-------:|
| [anthropics/financial-services-plugins](https://github.com/anthropics/financial-services-plugins) | Anthropics 官方开源的 Claude 金融服务专属插件库, 基于 Claude for Enterprise 打造, 核心目标是将通用大模型 Claude 转化为精通投行、行研、私募、财富管理等领域的专业金融分析师. | ⭐⭐⭐⭐ |
| [mattpocock/skills](https://github.com/mattpocock/skills) | 代理技能集合, 扩展规划、开发和工具能力. 主要包括: 规划与设计(write-a-prd、prd-to-plan、prd-to-issues、grill-me、design-an-interface、request-refactor-plan)、开发(tdd、triage-issue、improve-codebase-architecture、migrate-to-shoehorn、scaffold-exercises)、工具与设置(setup-pre-commit、git-guardrails-claude-code)、写作与知识(write-a-skill、edit-article、ubiquitous-language、obsidian-vault) 等技能. | ⭐⭐⭐ |
| [dontbesilent2025/dbskill](https://github.com/dontbesilent2025/dbskill) | 基于 12,307 条推文提炼的商业诊断工具箱. [@dontbesilent](https://x.com/dontbesilent) 把自己发过的一万多条(12307)商业思考推文, 提炼成了一套 Claude Code Skills, 专门帮创业者和个体户做商业诊断. 核心工具包括: 商业模式诊断(dbs-diagnosis)、对标分析(dbs-benchmark)、内容创作诊断(dbs-content)、执行力诊断(dbs-unblock)、概念拆解(dbs-deconstruct). 提供完整的工作流: diagnosis → benchmark → content → unblock, deconstruct 可随时使用. 每个 SKILL.md 包含完整的方法论框架、诊断流程和说话风格定义, 开箱即用. 同时提供了进行 [dbs](https://github.com/dontbesilent2025/dbskill/tree/main/skills/dbs) 路由. 提供了类似 [garrytan/gstack](https://github.com/garrytan/gstack) 的功能, 但是更严苛. |
| [badlogic/pi-skills](https://github.com/badlogic/pi-skills) | 为 pi-coding-agent 提供的技能集合, 兼容 Claude Code、Codex CLI、Amp 和 Droid. 包含多个技能: Brave 搜索、浏览器工具、Google 日历/ Drive/ Gmail CLI、语音转文本、VS Code 集成、YouTube 转录等.  | 支持多种平台安装 | ⭐⭐⭐ |
| [MiniMax-AI/skills](https://github.com/MiniMax-AI/skills) | MiniMax 官方推出的 AI Agent 技能集合, 涵盖全栈开发、移动应用、视觉效果和办公文档处理等多个领域. 核心技能包括: 前端开发(React/Next.js、Tailwind CSS、动画效果)、全栈开发(API 设计、认证流程、实时功能)、Android/iOS 原生开发、GLSL 着色器开发、GIF 贴纸制作、PDF/PPTX/XLSX/DOCX 文档处理等. 技术栈集成了 MiniMax API 用于 AI 生成媒体资产, 支持多平台开发需求, 适用于从前端设计到后端架构的全流程开发场景.  | ⭐⭐⭐⭐ |
| [foryourhealth111-pixel/Vibe-Skills](https://github.com/foryourhealth111-pixel/Vibe-Skills) | 一个拥有 340+ 全栈能力矩阵的技能集合, 由 VCO 运行时统一治理. 核心目标是通过领域矩阵分类, 在正确的上下文节点自动唤起正确的工具, 无需手动遍历调用. 涵盖多个领域: 需求规划与产品管理、软件工程与架构设计、调试测试与质量保证、数据分析与统计建模、机器学习与 AI 工程、生命科学与生信计算、科学计算与数学逻辑、科研文献与学术写作、多媒体可视化与文档、外部集成与自动化部署. 技术上通过用户命令触发, AI 辅助治理发掘用户意图关键词, 再由关键词触发技能路由. 适用于从需求分析、代码开发到部署运维的全流程场景, 特别适合需要跨领域协作的复杂项目.  | ⭐⭐⭐ |
| [staruhub/ClaudeSkills](https://github.com/staruhub/ClaudeSkills) | 基于 Claude Code Skills 2.0 格式构建的高质量技能集合, 提升日常工作效率. 涵盖多个领域: 开发与架构(pair-programming 结对编程、security-audit 代码安全审计、solution-architect 系统设计、threejs-performance Three.js 性能优化)、产品与内容(product-manager PRD 写作、wechat-article-writer 微信文章创作、ppt-designer PPT 设计)、工具(a-share-analyst A 股分析等 | ⭐ |
| [NTCoding/claude-skillz](https://github.com/NTCoding/claude-skillz) | 为Claude Code提供可重用的技能和可组合的系统提示, 包含Claude Launcher和OpenCode Launcher. 核心功能: Claude Launcher(交互式系统提示和模型选择器, 支持两步选择和直接快捷方式)、OpenCode Launcher(从相同角色生成OpenCode代理)、12个预构建角色、可通过@引用加载的可重用技能(如独立研究、简洁输出、TDD流程等). 技术上支持基于前端matter的快捷方式、自动技能加载、冲突检测等. 适用于快速启动不同角色的Claude会话, 生成OpenCode代理, 应用各种专业技能到不同场景.  | ⭐⭐⭐⭐ |
| [zubair-trabzada/ai-marketing-claude](https://github.com/zubair-trabzada/ai-marketing-claude) | 为Claude Code提供全面的营销分析和自动化技能系统, 可审计网站营销、生成文案、构建电子邮件序列、创建内容日历、分析竞争对手并生成客户端就绪的PDF报告. 核心功能: 6维度营销审计(内容与消息传递、转化优化、SEO与可发现性、竞争定位、品牌与信任、增长与战略)、5个并行代理分析、14个子技能、PDF报告支持等. 技术上通过Python脚本辅助页面分析、竞争对手扫描、PDF生成等. 适用于营销机构、个体创业者和内容创作者, 可用于销售前分析、客户提案、优化自有网站等场景.  | ⭐⭐⭐⭐ |
| [huxiang1126/amass-roundtable](https://github.com/huxiang1126/amass-roundtable) | 一个基于 Claude Code 的圆桌会议工具, 三位集团高管(HR总监、总顾问、COO)围绕问题展开多视角讨论、博弈与决策. v1.1 新特性: Agent Teams 驱动 — 每位高管运行在独立上下文中, 真正的多角色独立思考, 不共享记忆, 避免观点趋同. 核心功能: 支持跨会话记忆、会议纪要自动归档、行动项追踪、可视化图表输出、动态角色扩展. 技术上通过安装脚本自动配置 Agent Teams 功能, 创建角色库和数据目录. 使用场景: 企业管理决策、问题分析、战略规划等需要多视角思考的复杂场景, 可用于讨论绩效考核、组织架构调整、业绩下滑原因分析、预算分配等议题.  | ⭐⭐⭐⭐ |
| [199-biotechnologies/claude-deep-research-skill](https://github.com/199-biotechnologies/claude-deep-research-skill) | 企业级研究引擎, 为Claude Code生成有引用支持的报告, 具有来源可信度评分、多提供商搜索和自动验证功能. 核心功能: 4种研究模式(Quick/Standard/Deep/UltraDeep)、8阶段研究流程、并行检索(5-10个并发搜索+2-3个专注子代理)、多提供商搜索集成(Brave/Serper/Exa/Jina/Firecrawl)、自动验证和引用检查、多格式输出(Markdown/HTML/PDF). 技术架构: 模块化设计, 包含SKILL.md入口点、参考文档、模板和脚本目录. 适用于需要深度研究和引用支持的场景, 如学术研究、市场分析、技术评估等.  | ⭐⭐⭐⭐⭐ |
| [himself65/finance-skills](https://github.com/himself65/finance-skills) | 一个为金融分析和交易提供的代理技能集合, 包含多种金融相关功能. 核心功能: 期权收益曲线图表生成(支持多种期权策略)、股票相关性分析(发现相关公司和配对交易 candidate)、金融数据获取(通过yfinance获取股票价格、财务报表等)、霍尔木兹海峡实时监控(航运、油价影响等)、社交媒体金融信息读取(Discord、Telegram、Twitter). 技术上遵循Agent Skills开放标准, 支持多种平台(Claude.ai、Claude Code等), 模块化设计, 支持交互式UI. 适用于金融分析、交易策略制定、市场情绪分析、地缘政治风险监控、投资决策支持等场景.  | ⭐⭐⭐ |
| [RKiding/Awesome-finance-skills](https://github.com/RKiding/Awesome-finance-skills) | 一个为AI代理提供金融分析能力的即插即用技能集合, 包含实时新闻、股票数据、情感分析、逻辑可视化和市场预测功能. 核心功能: 实时财经新闻聚合(10+信源)、逻辑链路可视化(传导链路图)、AI智能预测([shiyu-coder/Kronos](https://github.com/shiyu-coder/Kronos))、股票数据查询(A股/港股/美股)、情感分析(FinBERT/LLM)、投资信号追踪、专业研报生成、全网搜索与本地RAG. 技术上支持多种Agent框架(Antigravity、OpenCode、OpenClaw、Claude Code等), 模块化设计, 每个技能包含SKILL.md文件. 适用于金融市场分析、投资决策支持、市场趋势预测、财经新闻监控等场景.  | ⭐⭐⭐⭐ |
| [titanwings/colleague-skill](https://github.com/titanwings/colleague-skill) | 一个为Claude Code提供的同事技能生成工具, 可将同事的原材料(飞书消息、钉钉文档、邮件、截图等)转化为能替他工作的AI Skill. 核心功能: 支持多种数据来源(飞书、钉钉、PDF、图片、邮件、Markdown等)、生成包含Work Skill(工作能力)和Persona(性格)的完整Skill、支持多种个性标签和企业文化、具有进化机制(增量分析、对话纠正、版本管理). 技术上遵循AgentSkills开放标准, 包含飞书/钉钉自动采集工具、邮件解析、Skill文件管理和版本管理等功能. 适用于同事离职后知识传承、项目交接、经验积累等场景, 可生成具有同事技术规范和语气的AI Skill.  | ⭐⭐ |
| [ericosiu/ai-marketing-skills](https://github.com/ericosiu/ai-marketing-skills) | 为营销和销售团队提供开源的Claude Code技能, 包括完整的工作流程、脚本、评分算法、专家面板和自动化管道 | ericosiu | 营销实验、销售线索转化、内容质量评分、自动化外呼、SEO优化、财务分析 | ⭐⭐ |
| [phuryn/pm-skills](https://github.com/phuryn/pm-skills) | PM Skills Marketplace: 为产品经理提供AI操作系统, 用于做出更好的产品决策. 包含65个PM技能和36个链式工作流, 分布在8个插件中, 涵盖从发现、策略、执行、发布到增长的完整产品管理流程. 基于Teresa Torres、Marty Cagan、Alberto Savoia等的proven PM框架, 为Claude Code和Cowork设计, 同时技能兼容其他AI助手.  | ⭐⭐ |
| [coreyhaines31/marketingskills](https://github.com/coreyhaines31/marketingskills) | 专注于营销任务的AI代理技能集合, 包含40+技能, 覆盖CRO(转化率优化)、文案写作、SEO、付费广告、增长工程、邮件营销、社区营销等营销全流程, 适配Claude Code、OpenAI Codex、Cursor、Windsurf等12种AI编码工具. 技术上以product-marketing-context为核心基础, 所有技能先读取产品营销上下文再执行任务, 技能间相互引用形成完整工作流(如copywriting ↔ page-cro ↔ ab-test-setup). 适用于技术营销人员、创始人、营销机构, 可用于销售前分析、客户提案、网站优化等场景.  | ⭐⭐⭐⭐ |
| [alirezarezvani/claude-skills](https://github.com/alirezarezvani/claude-skills) | 最全面的开源Claude Code技能库, 包含235个生产级技能和305个Python工具, 覆盖工程、产品、营销、合规、C级顾问等9大领域, 支持Claude Code、OpenAI Codex、Cursor、Aider等12种AI编码工具, 是最大的开源技能生态之一(5,200+ Stars). 技术特色: 所有Python工具纯stdlib(零依赖pip安装)、多工具自动转换脚本、技能安全审计、自我改进循环、Persona角色系统、轻量级编排协议. 适用于从 solo founder 到企业级的全场景AI代理赋能.  | ⭐⭐⭐⭐⭐ |
| [tradermonty/claude-trading-skills](https://github.com/tradermonty/claude-trading-skills) | 为股票投资者和交易者精心设计的Claude技能集合, 包含40+专业技能, 覆盖市场分析、技术分析、基本面分析、策略回测、投资组合管理等全交易流程. 技术上集成FMP(Financial Modeling Prep)、FINVIZ、Alpaca API, 支持Claude Web App和Claude Code双工作流, 包含自动技能改进流水线和自动技能生成流水线. 核心技能包括: Sector Analyst(板块轮动分析)、Technical Analyst(纯技术分析)、US Stock Analysis(美股深度研究)、Backtest Expert(专业回测框架)、CANSLIM Screener(成长股筛选)、Options Strategy Advisor(期权策略)等. 适用于系统化交易、市场研究、投资组合管理等场景.  | ⭐⭐⭐⭐ |

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



| 集合 | 简要描述 |
|:---:|:-------:|
| [baoyu-skills](https://github.com/JimLiu/baoyu-skills) | 宝玉分享的 Claude Code 技能集, 提升日常工作效率. | `npx skills add jimliu/baoyu-skills` |
| [Top 50 Claude Skills & GitHub  Repos for AI — The Only List You  Need.](https://x.com/zodchiii/status/2034924354337714642) | Claude AI 技能与 GitHub 仓库 50 大——你唯一需要的清单. |