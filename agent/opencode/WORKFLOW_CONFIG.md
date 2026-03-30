# Oh-My-OpenCode + Superpowers 工作流程配置文档

## 📋 配置概览

**配置文件**: `~/.config/opencode/oh-my-opencode.jsonc`
**配置时间**: 2026-03-01
**配置状态**: ✅ 已验证通过

---

## 🎯 工作流程设计

### 新功能开发流程

```
需求 → Brainstorming → 设计文档 → 实现计划 → 执行（TDD）→ 验证 → 代码评审 → 完成
```

**涉及的技能：**
1. **brainstorming** - 探索用户意图、需求和设计
2. **writing-plans** - 编写详细的实现计划
3. **subagent-driven-development** - 通过子智能体协作实现
4. **test-driven-development** - TDD 开发，先写测试
5. **verification-before-completion** - 完成前验证
6. **requesting-code-review** - 请求代码审查

### Bug 修复流程

```
问题 → Systematic Debugging → 根因定位 → TDD 修复 → 验证 → 完成
```

**涉及的技能：**
1. **systematic-debugging** - 找到根本原因
2. **test-driven-development** - 编写失败测试，修复
3. **verification-before-completion** - 验证修复
4. **requesting-code-review** - 代码审查

---

## 🤖 Agents 配置

### Sisyphus（主协调器）

**角色**: 主协调器，最强推理能力，负责整体规划

**配置的技能**:
- `using-superpowers` - Superpowers 框架入口
- `brainstorming` - 头脑风暴，探索需求和设计
- `dispatching-parallel-agents` - 并行任务调度
- `verification-before-completion` - 完成前验证

**适用场景**: 复杂任务的整体规划和协调

---

### Hephaestus（锻造之神）

**角色**: 代码构建与编译专家

**配置的技能**:
- `using-superpowers` - Superpowers 框架入口
- `subagent-driven-development` - 子智能体驱动的开发流程
- `executing-plans` - 执行已制定的计划
- `test-driven-development` - TDD 开发，先写测试
- `verification-before-completion` - 完成前验证

**适用场景**: 新功能开发和 Bug 修复的执行阶段

---

### Oracle（先知）

**角色**: 架构设计专家，深度分析能力

**配置的技能**:
- `using-superpowers` - Superpowers 框架入口
- `systematic-debugging` - 系统化调试

**适用场景**: Bug 修复、架构问题、复杂调试

---

### Prometheus（普罗米修斯）

**角色**: 任务规划与分解专家

**配置的技能**:
- `using-superpowers` - Superpowers 框架入口
- `writing-plans` - 编写工作计划

**适用场景**: 新功能开发的规划阶段

---

### Momus（批评家）

**角色**: 代码审查与质量保证专家

**配置的技能**:
- `using-superpowers` - Superpowers 框架入口
- `systematic-debugging` - 系统化调试
- `test-driven-development` - TDD 开发

**适用场景**: 代码审查、质量保证、Bug 修复

---

### 其他 Agents

**Librarian**（图书管理员）:
- `using-superpowers` - 代码理解与文档搜索

**Explore**（探索者）:
- `using-superpowers` - 快速响应，代码库探索

**Multimodal-Looker**（多模态观察者）:
- `using-superpowers` - 图像与多媒体内容分析

**Metis**（智慧女神）:
- `using-superpowers` - 需求分析与预规划

---

## 📂 Categories 配置

### 复杂功能（启用完整 Superpowers）

#### visual-engineering（视觉工程）

**描述**: 前端、UI/UX、设计、样式、动画

**配置的技能**:
- `using-superpowers` - Superpowers 框架入口
- `subagent-driven-development` - 子智能体驱动的开发流程

**工作流程**: 新功能开发流程

---

#### ultrabrain（超级大脑）

**描述**: 逻辑密集型复杂任务，仅给出目标而非步骤

**配置的技能**:
- `using-superpowers` - Superpowers 框架入口
- `subagent-driven-development` - 子智能体驱动的开发流程

**工作流程**: 新功能开发流程

---

#### deep（深度探索）

**描述**: 目标导向的自主问题解决，深入理解后行动

**配置的技能**:
- `using-superpowers` - Superpowers 框架入口
- `subagent-driven-development` - 子智能体驱动的开发流程
- `test-driven-development` - TDD 开发

**工作流程**: 新功能开发流程

---

#### unspecified-high（未分类高耗）

**描述**: 不符合其他类别、高工作量任务

**配置的技能**:
- `using-superpowers` - Superpowers 框架入口
- `subagent-driven-development` - 子智能体驱动的开发流程

**工作流程**: 新功能开发流程

---

#### artistry（艺术创造）

**描述**: 非常规创造性方法解决复杂问题

**配置的技能**:
- `using-superpowers` - Superpowers 框架入口
- `brainstorming` - 头脑风暴

**工作流程**: 新功能开发流程（创造性任务）

---

### 简易功能（直接开发）

#### quick（快速任务）

**描述**: 简单任务 - 单文件修改、拼写修复、简单变更

**配置的技能**:
- `using-superpowers` - Superpowers 框架入口

**工作流程**: 直接开发，不加载复杂 Superpowers 技能

---

#### unspecified-low（未分类低耗）

**描述**: 不符合其他类别、低工作量任务

**配置的技能**:
- `using-superpowers` - Superpowers 框架入口

**工作流程**: 直接开发，不加载复杂 Superpowers 技能

---

#### writing（写作任务）

**描述**: 文档、散文、技术写作

**配置的技能**:
-`using-superpowers` - Superpowers 框架入口

**工作流程**: 直接开发

---

## 🔍 配置验证

### 配置文件验证

```bash
✅ 配置文件存在: ~/.config/opencode/oh-my-opencode.jsonc
📝 文件大小: 7284 字节
```

### Oh-My-OpenCode 配置验证

```bash
✅ bunx 可用
✓ Configuration Validity → Valid JSONC config
✓ Model Resolution → 10 agents, 8 categories (14 overrides), 3053 available
```

### Superpowers 技能配置统计

```bash
📊 配置文件中的 Superpowers 技能引用: 34 个
```

### Superpowers 技能目录验证

```bash
✅ Superpowers 技能目录存在: ~/.config/opencode/skills/superpowers
📊 技能总数: 14 个
```

---

## 📊 技能配置总结

| 技能 | 配置位置 | 用途 |
|------|---------|------|
| **using-superpowers** | 所有 agents 和 categories | Superpowers 框架入口 |
| **brainstorming** | sisyphus, artistry | 头脑风暴，探索需求和设计 |
| **dispatching-parallel-agents** | sisyphus | 并行任务调度 |
| **subagent-driven-development** | hephaestus, visual-engineering, ultrabrain, deep, unspecified-high | 子智能体驱动的开发流程 |
| **executing-plans** | hephaestus | 执行已制定的计划 |
| **test-driven-development** | hephaestus, momus, deep | TDD 开发，先写测试 |
| **verification-before-completion** | sisyphus, hephaestus | 完成前验证 |
| **writing-plans** | prometheus | 编写工作计划 |
| **systematic-debugging** | oracle, momus | 系统化调试，找到根本原因 |

---

## 🚀 使用示例

### 新功能开发（复杂功能）

```bash
# 使用 ultrabrain category（自动加载完整 Superpowers）
opencode "实现一个用户认证系统，包括登录、注册和密码重置功能"

# 或使用 deep category
opencode "设计一个高并发的消息队列系统"

# 或使用 visual-engineering category
opencode "创建一个响应式的仪表盘组件"
```

**自动执行的工作流程：**
1. ✅ Brainstorming - 探索需求和设计
2. ✅ Writing Plans - 编写实现计划
3. ✅ Subagent-driven Development - 通过子智能体协作实现
4. ✅ Test-driven Development - TDD 开发
5. ✅ Verification - 完成前验证

---

### Bug 修复

```bash
# 使用 oracle agent（自动加载 systematic-debugging）
opencode "修复登录功能的 bug：用户无法重置密码"

# 或使用 momus agent
opencode "调试内存泄漏问题"
```

**自动执行的工作流程：**
1. ✅ Systematic Debugging - 找到根本原因
2. ✅ Test-driven Development - 编写失败测试，修复
3. ✅ Verification - 验证修复

---

### 简易功能（直接开发）

```bash
# 使用 quick category（不加载复杂 Superpowers）
opencode "修复一个拼写错误"

# 或使用 unspecified-low category
opencode "更新配置文件中的一个参数"
```

**执行方式：**
- ✅ 直接开发，不加载复杂 Superpowers 技能
- ✅ 快速完成，适合简单任务

---

## 🔧 故障排查

### 技能未生效

1. **检查配置文件位置**: 确认配置在 `~/.config/opencode/oh-my-opencode.jsonc`
2. **重启 OpenCode**: 修改配置后需要重启 OpenCode
3. **检查技能目录**: 确认 Superpowers 技能存在于 `~/.config/opencode/skills/superpowers/`
4. **验证配置**: 运行 `bunx oh-my-opencode doctor`

### 查看当前加载的技能

在 OpenCode 中运行：

```
/skills
```

---

## 📚 相关资源

- [Oh-My-OpenCode 官方文档](https://github.com/code-yeongyu/oh-my-opencode)
- [Superpowers 技能目录](~/.config/opencode/skills/superpowers/)
- [OpenCode 配置文档](https://opencode.ai/docs/configuration/)
- [Superpowers 集成文档](~/.config/opencode/SUPERPOWERS_INTEGRATION.md)

---

## 📝 配置变更历史

### 2026-03-01

**新增配置：**
- ✅ 为 oracle 添加 `systematic-debugging`
- ✅ 为 momus 添加 `systematic-debugging` 和 `test-driven-development`
- ✅ 为 hephaestus 添加 `test-driven-development`
- ✅ 为 deep 添加 `test-driven-development`

**配置验证：**
- ✅ JSONC 语法验证通过
- ✅ 模型解析验证通过
- ✅ Superpowers 技能引用：34 个
- ✅ 所有技能目录存在

---

## ✅ 配置完成

所有配置已完成并验证通过。OpenCode 现在支持：

1. ✅ **新功能开发流程**（复杂功能）
2. ✅ **Bug 修复流程**
3. ✅ **复杂功能 vs 简易功能的自动区分**
4. ✅ **所有 Superpowers 核心技能的自动加载**

无需手动输入 `use skill` 命令，所有技能会自动加载。
