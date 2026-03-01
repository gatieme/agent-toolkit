# Sisyphus 工作模式配置文档

## 📋 模式概览

已创建两种 Sisyphus 工作模式，支持不同的工作流程需求：

| 模式 | 配置文件 | 描述 | 适用场景 |
|------|---------|------|---------|
| **交互式模式** | `oh-my-opencode-INTERACTIVE.jsonc` | 每个工作步骤完成后询问用户，允许调整流程、变更计划、调整任务 | 需要灵活控制、调试、学习 |
| **完全自动化模式** | `oh-my-opencode-ULTRAWORKER.jsonc` | 按照 Superpowers 工作流程自动执行所有步骤，不询问用户 | 需要快速完成、批量任务、自动化流程 |

---

## 🔄 模式切换

### 方法 1: 使用切换脚本（推荐）

```bash
# 切换到交互式模式
~/switch-opencode-config.sh omo

# 切换到完全自动化模式
~/switch-opencode-config.sh

# 切换到原生配置
~/switch-opencode-config.sh native

# 查看当前配置状态
~/switch-opencode-config.sh status
```

### 方法 2: 手动切换配置文件

```bash
cd ~/.config/opencode

# 切换到交互式模式
cp oh-my-opencode-INTERACTIVE.jsonc opencode.json

# 切换到完全自动化模式
cp oh-my-opencode-ULTRAWORKER.jsonc opencode.json

# 切换到原生配置
cp opvercode-native.json opencode.json
```

---

## 📊 模式详细说明

### 交互式模式 (oh-my-opencode-INTERACTIVE.jsonc)

**配置特点**:
- ✅ Sisyphus agent 配置
- ✅ 包含 `prompt_append` 指令
- ✅ 每个步骤完成后询问用户

**prompt_append 内容**:
```
你处于 Sisyphus 交互式模式。每个工作步骤完成后，必须询问用户：

1. 是否继续下一步
2. 是否需要调整当前步骤
3. 是否需要修改计划
4. 是否需要添加新的任务

等待用户明确确认后再继续。不要自动推进到下一步。
```

**工作流程**:
1. ✅ Brainstorming - 探索需求和设计
2. ⏸ **询问用户**: 是否继续？
3. ✅ Writing Plans - 编写实现计划（如果需要）
4. ⏸ **询问用户**: 是否继续？
5. ✅ Subagent-driven Development - 通过子智能体协作实现
6. ⏸ **询问用户**: 是否继续？
7. ✅ Test-driven Development - TDD 开发
8. ⏸ **询问用户**: 是否继续？
9. ✅ Verification - 完成前验证
10. ⏸ **询问用户**: 是否继续？
11. ✅ Code Review - 请求代码审查（如果需要）

**适用场景**:
- ✅ 需要灵活控制工作流程
- ✅ 调试和探索新功能
- ✅ 学习 Superpowers 工作流程
- ✅ 需要频繁调整计划
- ✅ 不确定最佳实现方案

**使用示例**:
```bash
# 切换到交互式模式
~/switch-opencode-config.sh omo

# 启动 OpenCode
opencode "实现一个用户认证系统"

# 工作流程：
# 1. Brainstorming 完成 → 询问用户
# 2. 用户确认继续 → Writing Plans
# 3. Writing Plans 完成 → 询问用户
# 4. 用户调整计划 → 重新 Writing Plans
# 5. 用户确认继续 → Subagent-driven Development
# ... 每个步骤都询问用户
```

---

### 完全自动化模式 (oh-my-opencode-ULTRAWORKER.jsonc)

**配置特点**:
- ✅ Sisyphus (Ultraworker) agent 配置
- ✅ 包含 `prompt_append` 指令
- ✅ 自动执行所有步骤，不询问用户

**prompt_append 内容**:
```
你处于 Sisyphus (Ultraworker) 完全自动化模式。按照 Superpowers 工作流程自动执行所有步骤，不询问用户。只有遇到无法解决的严重错误时才停止并询问用户。

工作流程：
1. Brainstorming - 探索需求和设计
2. Writing Plans - 编写实现计划（如果需要）
3. Subagent-driven Development - 通过子智能体协作实现
4. Test-driven Development - TDD 开发
5. Verification - 完成前验证
6. Code Review - 请求代码审查（如果需要）

自动执行所有步骤，直到任务 100% 完成。
```

**工作流程**:
1. ✅ Brainstorming - 探索需求和设计
2. ✅ Writing Plans - 编写实现计划（如果需要）
3. ✅ Subagent-driven Development - 通过子智能体协作实现
4. ✅ Test-driven Development - TDD 开发
5. ✅ Verification - 完成前验证
6. ✅ Code Review - 请求代码审查（如果需要）
7. ✅ 自动完成，不询问用户

**适用场景**:
- ✅ 需要快速完成任务
- ✅ 批量任务处理
- ✅ 自动化流程
- ✅ 明确的需求和实现方案
- ✅ 不需要中途调整

**使用示例****:
```bash
# 切换到完全自动化模式
~/switch-opencode-config.sh

# 启动 OpenCode
opencode "实现一个用户认证系统"

# 工作流程：
# 1. Brainstorming → 自动继续
# 2. Writing Plans → 自动继续
# 3. Subagent-driven Development → 自动继续
# 4. Test-driven Development → 自动继续
# 5. Verification → 自动继续
# 6. Code Review → 自动继续
# 7. 任务完成，不询问用户
```

---

## 🤖 Agents 配置对比

### Sisyphus Agent

| 配置项 | 交互式模式 | 完全自动化模式 |
|-------|---------|---------|
| **model** | `ZhiPuGLM-ZWZ/ep-20260212143352-vtb7j` | `ZhiPuGLM-ZWZ/ep-20260212143352-vtb7j` |
| **temperature** | 0.3 | 0.3 |
| **concurrency** | 1 | 1 |
| **description** | 主协调器: 最强推理能力, 负责整体规划 (交互式模式) | Sisyphus (Ultraworker): 完全自动化模式，不询问用户 |
| **skills** | 4 个核心技能 | 6 个完整技能 |

### 其他 Agents

所有其他 agents 的配置在两种模式下保持一致，包括：
- ✅ Hephaestus - 执行者，包含 TDD 支持
- ✅ Oracle - 调试专家，包含 systematic-debugging
- ✅ Prometheus - 规划专家，包含 writing-plans
- ✅ Momus - 代码审查专家，包含 systematic-debugging 和 test-driven-development

---

## 🚀 使用建议

### 何时使用交互式模式

**推荐场景**:
- ✅ 新功能开发（需要探索和调整）
- ✅ 不确定最佳实现方案
- ✅ 需要学习和理解 Superpowers 工作流程
- ✅ 调试和测试
- ✅ 需要频繁调整计划

**使用示例**:
```bash
# 切换到交互式模式
~/switch-opencode-config.sh omo

# 启动 OpenCode
opencode "探索一个创新的用户引导流程"
```

### 何时使用完全自动化模式

**推荐场景**:
- ✅ 明确的需求和实现方案
- ✅ 需要快速完成任务
- ✅ 批量任务处理
- ✅ 自动化流程
- ✅ 不需要中途调整

**使用示例**:
```bash
# 切换到完全自动化模式
~/switch-opencode-config.sh

# 启动 OpenCode
opencode "实现一个标准的用户认证系统，包括登录、注册和密码重置功能"
```

---

## 🔍 查看当前模式

```bash
# 使用切换脚本查看当前配置
~/switch-opencode-config.sh status

# 预期输出：
# 📊 当前配置状态:
# 
# 📄 当前配置: opencode.json
#    🎯 类型: Oh-My-OpenCode
#    🔄 模式: 交互式（每个步骤完成后询问用户）
#    ⚡ Superpowers: ✅ 已配置
```

---

## 📝 配置文件位置

| 文件 | 位置 | 用途 |
|------|------||------|
| **oh-my-opencode-INTERACTIVE.jsonc** | `~/.config/opencode/` | 交互式模式配置 |
| **oh-my-opencode-ULTRAWORKER.jsonc** | `~/.config/opencode/` | 完全自动化模式配置 |
| **opencode.json** | `~/.config/opencode/` | 当前激活的配置 |
| **switch-opencode-config.sh** | `~` | 配置切换脚本 |

---

## 💡 重要说明

### 模式切换原则

1. **交互式模式**:
   - 适合需要灵活控制的场景
   - 每个步骤都询问用户
   - 可以中途调整计划
   - 可以添加新任务

2. **完全自动化模式**:
   - 适合需要快速完成的场景
   - 自动执行所有步骤
   - 不询问用户
   - 只在遇到严重错误时停止

### Superpowers 技能

两种模式都包含完整的 Superpowers 技能配置：
- ✅ using-superpowers - Superpowers 框架入口
- ✅ brainstorming - 头脑风暴
- ✅ systematic-debugging - 系统化调试
- ✅ test-driven-development - TDD 开发
- ✅ writing-plans - 编写计划
- ✅ subagent-driven-development - 子智能体驱动的开发
- ✅ verification-before-completion - 完成前验证
- ✅ requesting-code-review - 请求代码审查

### 模型配置

两种模式使用相同的模型配置：
- ✅ Sisyphus: `ZhiPuGLM-ZWZ/ep-20260212143352-vtb7j` (高质量推理)
- ✅ Hephaestus: `opencode/minimax-m2.5-free` (中等)
- ✅ Oracle: `ZhiPuGLM-ZWZ/ep-20260212143352-vtb7j` (高质量推理)
- ✅ Prometheus: `opencode/trinity-large-preview-free` (大模型)
- ✅ 其他 agents: 根据任务类型配置

---

## 📚 相关文档

- [工作流程配置](~/.config/opencode/WORKFLOW_CONFIG.md)
- [模型更新文档](~/.config/opencode/MODEL_UPDATE.md)
- [配置切换指南](~/.config/opencode/CONFIG_SWITCH_GUIDE.md)
- [配置完成指南](~/.config/opencode/CONFIG_COMPLETE_GUIDE.md)
- [Superpowers 集成文档](~/.config/opencode/SUPERPOWERS_INTEGRATION.md)

---

## ✅ 配置完成

### 已完成的工作

1. ✅ **创建交互式模式配置**
   - 每个步骤完成后询问用户
   - 允许调整流程、变更计划、调整任务

2. ✅ **创建完全自动化模式配置**
   - 按照 Superpowers 工作流程自动执行
   - 不询问用户
   - 只在遇到严重错误时停止

3. ✅ **更新配置切换脚本**
   - 支持切换到交互式模式
   - 支持切换到完全自动化模式
   - 支持切换到原生配置
   - 显示当前配置状态

4. ✅ **文档生成**
   - 模式配置文档
   - 使用指南和示例

### 🚀 现在可以

1. ✅ **在两种 Sisyphus 工作模式之间快速切换**
2. ✅ **交互式模式**: 灵活控制，每个步骤都询问用户
3. ✅ **完全自动化模式**: 快速完成，自动执行所有步骤
4. ✅ **完整的 Superpowers 工作流程支持**
5. ✅ **所有模型均为可用模型**
6. ✅ **Oh-My-OpenCode 和原生配置之间的快速切换**

**使用建议**:
- 🎯 **新功能开发/调试**: 使用交互式模式
- 🚀 **明确需求/批量任务**: 使用完全自动化模式
