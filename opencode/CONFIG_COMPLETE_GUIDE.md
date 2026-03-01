# OpenCode 配置切换完成指南

## ✅ 配置已完成

### 📋 配置文件结构

| 配置文件 | 类型 | 描述 |
|---------|------|------|
| **opencode.json** | OpenCode 主配置 | 当前激活的配置（通过切换脚本管理）|
| **opencode-omo.json** | Oh-My-OpenCode | Oh-My-OpenCode 配置备份 |
| **opencode-native.json** | 原生配置 | 不使用 Oh-My-OpenCode 的原生配置 |
| **oh-my-opencode.jsonc** | Oh-My-OpenCode 插件配置 | Superpowers 技能配置 |

---

## 🔄 配置切换

### 切换脚本

**位置**: `~/switch-opencode-config.sh`

**使用方法**:

```bash
# 切换到 Oh-My-OpenCode 配置
~/switch-opencode-config.sh omo

# 切换到原生配置
~/switch-opencode-config.sh native

# 查看当前配置状态
~/switch-opencode-config.sh status
```

### 添加别名（可选）

```bash
# 添加到 ~/.bashrc 或 ~/.zshrc
alias opencode-omo='~/switch-opencode-config.sh omo'
alias opencode-native='~/switch-opencode-config.sh native'
alias opencode-status='~/switch-opencode-config.sh status'

# 重新加载配置
source ~/.bashrc  # 或 ~/.zshrc

# 使用
opencode-omo        # 切换到 Oh-My-OpenCode
opencode-native    # 切换到原生配置
opencode-status      # 查看当前配置状态
```

---

## 📊 配置对比

### Oh-My-OpenCode 配置 (opencode.json)

**启用插件**:
- ✅ `oh-my-opencode@latest`

**Superpowers 技能配置**:
- 📁 配置文件: `~/.config/opencode/oh-my-opencode.jsonc`
- 📊 技能引用: **34 个**
- ⚡ 核心技能: brainstorming, systematic-debugging, test-driven-development, writing-plans, subagent-driven-development

**工作流程支持**:
- ✅ 新功能开发流程（复杂功能）
- ✅ Bug 修复流程
- ✅ 复杂功能 vs 简易功能的自动区分

**适用场景**:
- 复杂功能开发
- 需要 TDD 开发
- 需要代码审查
- 需要系统化调试
- 需要并行任务调度

---

### 原生配置 (opencode-native.json)

**启用插件**:
- ❌ 无（不使用 Oh-My-OpenCode）

**特点**:
- ✅ 轻量级，快速响应
- ✅ 适合简单任务
- ✅ 无复杂工作流程开销

**适用场景**:
- 简单文件修改
- 快速原型开发
- 不需要复杂工作流程
- 需要最快响应速度

---

## 🚀 使用示例

### 使用 Oh-My-OpenCode（推荐用于复杂任务）

```bash
# 切换配置
~/switch-opencode-config.sh omo

# 启动 OpenCode
opencode "实现一个用户认证系统，包括登录、注册和密码重置功能"
```

**自动执行的工作流程**:
1. ✅ Brainstorming - 探索需求和设计
2. ✅ Writing Plans - 编写实现计划
3. ✅ Subagent-driven Development - 通过子智能体协作实现
4. ✅ Test-driven Development - TDD 开发
5. ✅ Verification - 完成前验证

### 使用原生配置（推荐用于简单任务）

```bash
# 切换配置
~/switch-opencode-config.sh native

# 启动 OpenCode
opencode "修复一个拼写错误"
```

**执行方式**:
- ✅ 直接开发，不加载复杂 Superpowers 技能
- ✅ 快速完成，适合简单任务

---

## 🔍 检查当前配置

```bash
# 使用切换脚本
~/switch-opencode-config.sh status

# 或直接查看配置
cat ~/.config/opencode/opencode.json | grep -E "plugin|model"

# 检查 Oh-My-OpenCode 配置
bunx oh-my-opencode doctor
```

---

## 🔧 配置验证

### Oh-My-OpenCode 配置验证

```bash
# 验证配置文件
bunx oh-my-opencode doctor

# 预期输出:
# ✓ Configuration Validity → Valid JSONC config
# ✓ Model Resolution → 10 agents, 8 categories (14 overrides), 3053 available
```

### Superpowers 技能验证

```bash
# 统计 Superpowers 技能引用
grep -c "superpowers/" ~/.config/opencode/oh-my-opencode.jsonc

# 预期输出: 34

# 查看具体配置的技能
grep "superpowers/" ~/.config/opencode/oh-my-opencode.jsonc | sort -u
```

---

## 📝 配置文件位置

| 文件 | 位置 | 用途 |
|------|------||------|
| **opencode.json** | `~/.config/opencode/opencode.json` | 当前激活的配置 |
| **opencode-omo.json** | `~/.config/opencode/opencode-omo.json` | Oh-My-OpenCode 配置备份 |
| **opencode-native.json** | `~/.config/opencode/opencode-native.json` | 原生配置 |
| **oh-my-opencode.jsonc** | `~/.config/opencode/oh-my-opencode.jsonc` | Superpowers 技能配置 |
| **switch-opencode-config.sh** | `~/switch-opencode-config.sh` | 配置切换脚本 |

---

## 💡 重要说明

### OpenCode Tab 功能

OpenCode 的 tab 功能是通过多个配置文件实现的。当前配置包括：

1. **opencode.json** - 当前激活的配置
2. **opencode-omo.json** - Oh-My-OpenCode 配置
3. **opencode-native.json** - 原生配置

**切换方法**:
- 使用 `~/switch-opencode-config.sh` 脚本
- 或在 OpenCode 界面中手动切换配置文件

### Superpowers 配置说明

**重要**: Superpowers 技能配置在 `oh-my-opencode.jsonc` 中，而不是 `opencode.json` 中。

- `opencode.json` - OpenCode 主配置，只引用 oh-my-opencode 插件
- `oh-my-opencode.jsonc` - Oh-My-OpenCode 插件配置，包含 Superpowers 技能配置

**验证 Superpowers 配置**:
```bash
# 检查 oh-my-opencode.jsonc
grep -c "superpowers/" ~/.config/opencode/oh-my-opencode.jsonc

# 预期输出: 34
```

---

## 🎯 配置完成总结

### ✅ 已完成的工作

1. ✅ 创建了原生配置文件 `opencode-native.json`
2. ✅ 创建了配置切换脚本 `switch-opencode-config.sh`
3. ✅ 配置了 Superpowers 工作流程（34 个技能引用）
4. ✅ 支持新功能开发流程
5. ✅ 支持 Bug 修复流程
6. ✅ 支持复杂功能 vs 简易功能的自动区分

### 🚀 现在可以

1. ✅ 在 Oh-My-OpenCode 和原生配置之间快速切换
2. ✅ 使用完整 Superpowers 工作流程进行复杂任务
3. ✅ 使用轻量级原生配置进行简单任务
4. ✅ 无需手动输入 `use skill` 命令

### 📚 相关文档

- [配置切换指南](~/.config/opencode/CONFIG_SWITCH_GUIDE.md)
- [工作流程配置](~/.config/opencode/WORKFLOW_CONFIG.md)
- [Superpowers 集成文档](~/.config/opencode/SUPERPOWERS_INTEGRATION.md)

---

## 🎉 快速开始

### 复杂任务（使用 Oh-My-OpenCode）

```bash
~/switch-opencode-config.sh omo
opencode "实现一个用户认证系统"
```

### 简单任务（使用原生配置）

```bash
~/switch-opencode-config.sh native
opencode "修复一个拼写错误"
```

### 查看当前配置

```bash
~/switch-opencode-config.sh status
```
