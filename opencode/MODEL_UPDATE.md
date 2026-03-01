# 模型配置更新文档

## 📊 更新概览

**更新时间**: 2026-03-01
**配置文件**: `~/.config/opencode/oh-my-opencode.jsonc`
**状态**: ✅ 已验证通过

---

## 🔧 模型替换

### ❌ 失效的模型

| 失效模型 | 替换为 | 原因 |
|---------|---------|------|
| `opencode/kimi-k2.5-free` | `opencode/minimax-m2.5-free` | 模型不可用 |
| `opencode/glm-4.7-free` | `opencode/trinity-large-preview-free` | 模型不可用 |

### ✅ 可用的模型

| 模型 | 用途 | 配置次数 |
|------|------|---------|
| `ZhiPuGLM-ZWZ/ep-20260212143352-vtb7j` | 高质量推理 | 3 次 |
| `ZhiPuGLM-CGS/ep-20260212143331-qbknz` | 快速推理 | 9 次 |
| `opencode/trinity-large-preview-free` | 大模型任务 | 5 次 |
| `opencode/minimax-m2.5-free` | 中等任务 | 5 次 |
| `opencode/big-pickle` | 深度探索 | 1 次 |
| `opencode/gpt-5-nano` | 快速任务 | 1 次 |

---

## 🤖 Agents 模型配置

### Sisyphus（主协调器）

**模型**: `ZhiPuGLM-ZWZ/ep-20260212143352-vtb7j`
**温度**: 0.3
**并发**: 1
**描述**: 主协调器，最强推理能力，负责整体规划

**Superpowers 技能**:
- `using-superpowers`
- `brainstorming`
- `dispatching-parallel-agents`
- `verification-before-completion`

---

### Hephaestus（锻造之神）

**模型**: `opencode/minimax-m2.5-free` ⚡️ 已替换
**温度**: medium
**描述**: 代码构建与编译专家

**Superpowers 技能**:
- `using-superpowers`
- `subagent-driven-development`
- `executing-plans`
- `test-driven-development`
- `verification-before-completion`

---

### Oracle（先知）

**模型**: `ZhiPuGLM-ZWZ/ep-20260212143352-vtb7j`
**温度**: high
**描述**: 架构设计专家，深度分析能力

**Superpowers 技能**:
- `using-superpowers`
- `systematic-debugging`

---

### Prometheus（普罗米修斯）

**模型**: `opencode/trinity-large-preview-free` ⚡️ 已替换
**温度**: max
**描述**: 任务规划与分解专家

**Superpowers 技能**:
- `using-superpowers`
- `writing-plans`

---

### Metis（智慧女神）

**模型**: `opencode/trinity-large-preview-free` ⚡️️ 已替换
**温度**: max
**描述**: 需求分析与预规划专家

**Superpowers 技能**:
- `using-superpowers`

---

### Momus（批评家）

**模型**: `opencode/trinity-large-preview-free` ⚡️ 已替换
**温度**: medium
**描述**: 代码审查与质量保证专家

**Superpowers 技能**:
- `using-superpowers`
- `systematic-debugging`
- `test-driven-development`

---

### Atlas（阿特拉斯）

**模型**: `opencode/minimax-m2.5-free` ⚡️ 已替换
**描述**: 地图绘制与代码结构可视化

---

### Document Writer（文档编写者）

**模型**: `opencode/minimax-m2.5-free` ⚡️ 已替换
**描述**: 文档编写者，技术文档生成与维护

---

### Doc Agent（文档代理）

**模型**: `opencode/minimax-m2.5-free` ⚡️ 已替换
**温度**: 0.7
**描述**: 长文本处理代理，文档分析与摘要生成

---

### Frontend（前端开发）

**模型**: `opencode/trinity-large-preview-free` ⚡️ 已替换
**描述**: 前端开发专家，UI/UX 实与优化

---

###**其他 Agents（未变更）**

- **Librarian**: `ZhiPuGLM-CGS/ep-20260212143331-qbknz` - 图书管理员
- **Explore**: `ZhiPuGLM-CGS/ep-20260212143331-qbknz` - 探索者
- **Multimodal-Looker**: `ZhiPuGLM-ZWZ/ep-20260212143352-vtb7j` - 多模态观察者
- **Codegen**: `ZhiPuGLM-CGS/ep-20260212143331-qbknz` - 代码生成专用代理

---

## 📂 Categories 模型配置

### Visual-engineering（视觉工程）

**模型**: `ZhiPuGLM-CGS/ep-20260212143331-qbknz`
**描述**: 前端、UI/UX、设计、样式、动画

**Superpowers 技能**:
- `using-superpowers`
- `subagent-driven-development`

---

### Ultrabrain（超级大脑）

**模型**: `ZhiPuGLM-CGS/ep-20260212143331-qbknz`
**温度**: high
**描述**: 逻辑密集型复杂任务，仅给出目标而非步骤

**Superpowers 技能**:
- `using-superpowers`
- `subagent-driven-development`

---

### Deep（深度探索）

**模型**: `opencode/big-pickle`
**温度**: medium
**描述**: 目标导向的自主问题解决，深入理解后行动

**Superpowers 技能**:
- `using-superpowers`
- `subagent-driven-development`
- `test-driven-development`

---

### Artistry（艺术创造）

**模型**: `ZhiPuGLM-CGS/ep-20260212143331-qbknz`
**温度**: high
**描述**: 非常规创造性方法解决复杂问题

**Superpowers 技能**:
- `using-superpowers`
- `brainstorming`

---

### Quick（快速任务）

**模型**: `opencode/gpt-5-nano`
**描述**: 快速任务，单文件修改、拼写修复、简单变更

**Superpowers 技能**:
- `using-superpowers`

---

### Unspecified-low（未分类低耗）

**模型**: `ZhiPuGLM-CGS/ep-20260212143331-qbknz`
**描述**: 不符合其他类别、低工作量任务

**Superpowers 技能**:
- `using-superpowers`

---

### Unspecified-high（未分类高耗）

**模型**: `ZhiPuGLM-CGS/ep-20260212143331-qbknz`
**温度**: max
**描述**: 不符合其他类别、高工作量任务

**Superpowers 技能**:
- `using-superpowers`
- `subagent-driven-development`

---

### Writing（写作任务）

**模型**: `ZhiPuGLM-CGS/ep-20260212143331-qbknz`
**描述**: 写作任务，文档、散文、技术写作

**Superpowers 技能**:
- `using-superpowers`

---

## 🔍 并发配置

### 全局并发

```json
"globalMax": 5  // 全局最大并发数
```

### 模型级并发

```json
"perModelMax": {
  "opencode/minimax-m2.5-free": 2,        // 中等任务：2 并发
  "opencode/trinity-large-preview-free": 2,  // 大模型：2 并发
  "opencode/big-pickle": 3,              // 深度探索：3 并发
  "opencode/gpt-5-nano": 2,              // 快速任务：2 并发
  "ZhiPuGLM-CGS/ep-20260212143331-qbknz": 1,  // 快速推理：1 并发
  "ZhiPuGLM-ZWZ/ep-20260212143352-vtb7j": 1   // 高质量推理：1 并发
}
```

---

## ✅ 验证结果

### Oh-My-OpenCode 配置验证

```bash
✓ Configuration Validity → Valid JSONC config
✓ Model Resolution → 10 agents, 8 categories (14 overrides), 3053 available
```

### 模型验证

```bash
✅ 失效模型已完全替换
✅ 所有模型均为可用模型
✅ 并发配置已更新
```

---

## 🚀 使用建议

### 根据任务复杂度选择模型

#### 简单任务（单文件修改、拼写修复）

```bash
# 使用 quick category
opencode "修复一个拼写错误"

# 或使用 unspecified-low category
opencode "更新配置文件中的一个参数"
```

#### 中等复杂度任务

```bash
# 使用 visual-engineering category
opencode "创建一个响应式的仪表盘组件"

# 或使用 ultrabrain category
opencode "设计一个用户认证系统"
```

#### 高复杂度任务

```bash
# 使用 deep category
opencode "实现一个高并发的消息队列系统"

# 或使用 unspecified-high category
opencode "重构整个后端架构"
```

#### 创造性任务

```bash
# 使用 artistry category
opencode "设计一个创新的用户引导流程"
```

---

## 📝 配置文件位置

| 文件 | 位置 | 用途 |
|------|------||------|
| **oh-my-opencode.jsonc** | `~/.config/opencode/` | Oh-My-OpenCode 主配置 |
| **oh-my-opencode.jsonc.backup-before-model-fix** | `~/.config/opencode/` | 模型修复前的备份 |

---

## 🔄 配置切换

### 切换到 Oh-My-OpenCode 配置

```bash
~/switch-opencode-config.sh omo
```

### 切换到原生配置

```bash
~/switch-opencode-config.sh native
```

### 查看当前配置状态

```bash
~/switch-opencode-config.sh status
```

---

## 💡 重要说明

### 模型选择原则

1. **Sisyphus（主协调器）**: 使用高质量推理模型 `ZhiPuGLM-ZWZ`，确保整体规划质量
2. **快速任务**: 使用 `opencode/gpt-5-nano`，快速响应
3. **中等任务**: 使用 `opencode/minimax-m2.5-free`，平衡速度和质量
4. **复杂任务**: 使用 `opencode/trinity-large-preview-free`，确保深度分析
5. **深度探索**: 使用 `opencode/big-pickle`，适合复杂问题解决

### 并发控制

- **高质量推理模型**: 并发限制为 1，避免资源竞争
- **快速推理模型**: 并发限制为 1，快速响应
- **中等模型**: 并发限制为 2，平衡性能
- **大模型**: 并发限制为 2，避免超限
- **深度探索**: 并发限制为 3，充分利用

### Superpowers 技能

所有 Superpowers 技能已正确配置，支持：
工作流程
- ✅ Bug 修复流程
- ✅ 复杂功能 vs 简易功能的自动区分

---

## 📚 相关文档

- [工作流程配置](~/.config/opencode/WORKFLOW_CONFIG.md)
- [配置切换指南](~/.config/opencode/CONFIG_SWITCH_GUIDE.md)
- [配置完成指南](~/.config/opencode/CONFIG_COMPLETE_GUIDE.md)
- [Superpowers 铆成文档](~/.config/opencode/SUPERPOWWS_INTEGRATION.md)

---

## ✅ 配置完成

所有模型已替换为可用模型，配置已验证通过。

**关键变更**:
- ✅ 替换失效模型 `opencode/kimi-k2.5-free` → `opencode/minimax-m2.5-free`
- ✅ 替换失效模型 `opencode/glm-4.7-free` → `opencode/trinity-large-preview-free`
- ✅ 更新并发配置
- ✅ 验证所有模型可用
- ✅ Superpowers 技能配置完整

**现在可以**:
1. ✅ 使用所有可用模型
2. ✅ 根据任务复杂度自动选择合适模型
3. ✅ 完整的 Superpowers 工作流程支持
4. ✅ Oh-My-OpenCode 和原生配置之间的快速切换
