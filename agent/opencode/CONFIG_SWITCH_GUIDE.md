# OpenCode 配置切换指南

## 📋 配置文件说明

OpenCode 支持通过多个配置文件进行切换。

### 当前配置文件

| 配置文件 | 类型 | 描述 |
|---------|------|------|
| **opencode.json** | Oh-My-OpenCode | 主配置，启用 Oh-My-OpenCode 插件 + Superpowers |
| **opencode-native.json** | 原生配置 | 不使用 Oh-My-OpenCode 插件的原生配置 |

---

## 🔄 配置切换方法

### 方法 1: 重命名文件（推荐）

```bash
# 切换到 Oh-My-OpenCode 配置
cd ~/.config/opencode
mv opencode.json opencode-native.json
mv opencode-omo.json opencode.json

# 切换到原生配置
cd ~/.config/opencode
mv opencode.json opencode-omo.json
mv opencode-native.json opencode.json
```

### 方法 2: 使用符号链接

```bash
# 创建切换脚本
cat > ~/switch-opencode-config.sh << 'EOF'
#!/bin/bash
CONFIG_DIR=~/.config/opencode

case "$1" in
  omo|oh-my-opencode)
    echo "切换到 Oh-My-OpenCode 配置..."
    cd "$CONFIG_DIR"
    [ -f opencode.json ] && mv opencode.json opencode-native.json
    [ -f opencode-omo.json ] && mv opencode-omo.json opencode.json
    echo "✅ 已切换到 Oh-My-OpenCode"
    ;;
  native)
    echo "切换到原生配置..."
    cd "$CONFIG_DIR"
    [ -f opencode.json ] && mv opencode.json opencode-omo.json
    [ -f opencode-native.json ] && mv opencode-native.json opencode.json
    echo "✅ 已切换到原生配置"
    ;;
  *)
    echo "用法: $0 {omo|native}"
    echo "  omo    - 切换到 Oh-My-OpenCode 配置"
    echo "  native - 切换到原生配置"
    exit 1
    ;;
esac
EOF

chmod +x ~/switch-opencode-config.sh

# 使用示例
~/switch-opencode-config.sh omo          # 切换到 Oh-My-OpenCode
~/switch-opencode-config.sh native      # 切换到原生配置
```

### 方法 3: 使用 OpenCode Tab Tab 功能（如果支持）

如果 OpenCode 支持多配置 tab，你应该能在界面上看到：
- **opencode.json** - Oh-My-OpenCode 配置
- **opencode-native.json** - 原生配置

直接点击切换即可。

---

## 🔍 检查当前配置

```bash
# 查看当前使用的配置
cat ~/.config/opencode/opencode.json | grep -E "plugin|model"

# 检查是否启用了 Oh-My-OpenCode
if grep -q "oh-my-opencode" ~/.config/opencode/opencode.json; then
  echo "当前配置: Oh-My-OpenCode"
else
  echo "当前配置: 原生配置"
fi
```

---

## 📊 配置对比

### Oh-My-OpenCode 配置 (opencode.json)

- ✅ 启用 Oh-My-OpenCode 插件
- ✅ 配置 Superpowers 技能
- ✅ 支持新功能开发流程
- ✅ 支持 Bug 修复流程
- ✅ 自动区分复杂/简易功能

**适用场景：**
- 复杂功能开发
- 需要系统化工作流程
- 需要代码审查和质量保证

### 原生配置 (opencode-native.json)

- ❌ 不使用 Oh-My-OpenCode 插件
- ✅ 轻量级，快速响应
- ✅ 适合简单任务

**适用场景：**
- 简单文件修改
- 快速原型开发
- 不需要复杂工作流程

---

## 💡 使用建议

### 何时使用 Oh-My-OpenCode 配置

- ✅ 开发新功能（复杂）
- ✅ 需要 TDD 开发
- ✅ 需要代码审查
- ✅ 需要系统化调试
- ✅ 需要并行任务调度

### 何时使用原生配置

- ✅ 简单文件修改
- ✅ 快速原型开发
- ✅ 不需要复杂工作流程
- ✅ 需要最快响应速度

---

## 🔧 快速切换脚本

我已经为你创建了快速切换脚本：

```bash
# 切换到 Oh-My-OpenCode
~/switch-opencode-config.sh omo

# 切换到原生配置
~/switch-opencode-config.sh native
```

**使用别名（可选）：**

```bash
# 添加到 ~/.bashrc 或 ~/.zshrc
alias opencode-omo='~/switch-opencode-config.sh omo'
alias opencode-native='~/switch-opencode-config.sh native'

# 使用
opencode-omo        # 切换到 Oh-My-OpenCode
opencode-native    # 切换到原生配置
```

---

## ✅ 配置验证

切换配置后，重启 OpenCode 并验证：

```bash
# 重启 OpenCode
opencode --version

# 检查配置
bunx oh-my-opencode doctor
```

---

## 📝 配置文件位置

- **Oh-My-OpenCode 配置**: `~/.config/opencode/opencode.json`
- **原生配置**: `~/.config/opencode/opencode-native.json`
- **Superpowers 配置**: `~/.config/opencode/oh-my-opencode.jsonc`
- **切换脚本**: `~/switch-opencode-config.sh`

---

## 🚀 快速开始

### 使用 Oh-My-OpenCode（推荐用于复杂任务）

```bash
# 切换配置
~/switch-opencode-config.sh omo

# 启动 OpenCode
opencode "实现一个用户认证系统"
```

### 使用原生配置（推荐用于简单任务）

```bash
# 切换配置
~/switch-opencode-config.sh native

# 启动 OpenCode
opencode "修复一个拼写错误"
```
