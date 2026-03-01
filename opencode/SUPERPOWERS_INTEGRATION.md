# Oh-My-OpenCode + Superpowers 集成配置说明

## 配置位置

**正确配置文件**: `~/.config/opencode/oh-my-opencode.jsonc`

**错误配置文件**（已删除）: `~/.config/oh-my-opencode/config.yaml`

## 已完成的配置

已为以下所有 agents 和 categories 添加 Superpowers 核心技能：

### Agents（智能体）

| Agent | Superpowers 技能 |
|-------|-----------------|
| **sisyphus** | using-superpowers, brainstorming, dispatching-parallel-agents, verification-before-completion |
| **hephaestus** | using-superpowers, subagent-driven-development, executing-plans, verification-before-completion |
| **oracle** | using-superpowers |
| **librarian** | using-superpowers |
| **explore** | using-superpowers |
| **multimodal-looker** | using-superpowers |
| **prometheus** | using-superpowers, writing-plans |
| **metis** | using-superpowers |
| **momus** | using-superpowers |

### Categories（任务分类）

| Category | Superpowers 技能 |
|----------|-----------------|
| **visual-engineering** | using-superpowers, subagent-driven-development |
| **ultrabrain** | using-superpowers, subagent-driven-development |
| **deep** | using-superpowers, subagent-driven-development |
| **artistry** | using-superpowers, brainstorming |
| **quick** | using-superpowers |
| **unspecified-low** | using-superpowers |
| **unspecified-high** | using-superpowers, subagent-driven-development |
| **writing** | using-superpowers |

## 工作原理

1. **自动加载**: 所有由 oh-my-opencode 调度的智能体启动时，会自动加载配置的 Superpowers 技能
2. **无需手动输入**: 不再需要手动输入 `use skill` 命令
3. **永久生效**: 一次配置，所有任务自动遵循 Superpowers 工程规范

## 验证配置

运行以下命令验证配置是否生效：

```bash
# 重启 OpenCode 以加载新配置
opencode --version

# 或者直接开始使用，Sisyphus 会自动遵循 Superpowers 流程
```

## Superpowers 核心技能说明

### using-superpowers
- **作用**: Superpowers 框架的入口技能
- **功能**: 确保智能体遵循 Superpowers 工程规范

### brainstorming
- **作用**: 创造性任务前的头脑风暴
- **功能**: 探索用户意图、需求和设计方案

### dispatching-parallel-agents
- **作用**: 并行任务调度
- **功能**: 将复杂任务分解为多个独立的并行子任务

### subagent-driven-development
- **作用**: 子智能体驱动的开发流程
- **功能**: 通过子智能体协作完成复杂任务

### executing-plans
- **作用**: 执行已制定的计划
- **功能**: 按照规划逐步实施

### verification-before-completion
- **作用**: 完成前的验证
- **功能**: 确保工作完成前经过充分验证

### writing-plans
- **作用**: 编写工作计划
- **功能**: 在复杂任务前制定详细的实施计划

## 使用示例

### Sisyphus 任务分解（自动遵循 Superpowers）

```bash
# 只需正常使用，Sisyphus 会自动：
# 1. 调用 brainstorming 技能进行头脑风暴
# 2. 调用 dispatching-parallel-agents 进行并行任务调度
# 3. 调用 verification-before-completion 进行验证
# 4. 所有步骤自动完成，无需手动干预

opencode "实现一个用户认证系统，包括登录、注册和密码重置功能"
```

### 分类任务（自动加载对应技能）

```bash
# visual-engineering 任务会自动加载 subagent-driven-development
opencode "创建一个响应式的仪表盘组件"

# ultrabrain 任务会自动加载 subagent-driven-development
opencode "设计一个高并发的消息队列系统"

# artistry 任务会自动加载 brainstorming
opencode "设计一个创新的用户引导流程"
```

## 故障排查

### 技能未生效

1. **检查配置文件位置**: 确认配置在 `~/.config/opencode/oh-my-opencode.jsonc`
2. **重启 OpenCode**: 修改配置后需要重启 OpenCode
3. **检查技能目录**: 确认 Superpowers 技能存在于 `~/.config/opencode/skills/superpowers/`

### 查看当前加载的技能

在 OpenCode 中运行：

```
/skills
```

## 技术细节

### 配置格式

Oh-My-OpenCode 使用 **JSONC** 格式（支持注释和尾随逗号）：

```jsonc
{
  "agents": {
    "sisyphus": {
      "model": "your-model",
      "skills": [              // ← 技能数组
        "superpowers/using-superpowers",
        "superpowers/brainstorming"
      ]
    }
  }
}
```

### 技能加载优先级

1. Agent 配置中的 `skills` 字段
2. Category 配置中的 `skills` 字段
3. 全局默认技能（如有配置）

## 相关资源

- [Oh-My-OpenCode 官方文档](https://github.com/code-yeongyu/oh-my-opencode)
- [Superpowers 技能目录](~/.config/opencode/skills/superpowers/)
- [OpenCode 配置文档](https://opencode.ai/docs/configuration/)
