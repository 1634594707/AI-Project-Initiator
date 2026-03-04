# AI Project Initiator

一个面向“写第一行代码之前”的项目启动 Skill：用结构化的提问与文档产出，把需求、范围、技术选型、里程碑对齐，并且支持通过一组精选扩展 skills 把启动阶段做得更专业、更可复用。

本仓库除了 `project-init` 本体（见 `SKILL.md`），还包含一套可选的扩展 skills 示例库。你可以把它当作：

- **[核心]** 项目启动的主流程（PRD / MVP / 架构 / 路线图）
- **[扩展]** 按阶段增强（优先级、文档协作、代码产出、测试、交付物格式化）
- **[资产]** 文档模板与编辑器规则

---

## 你将获得的产出物（Outputs）

- **PRD**（产品需求文档）
- **MVP 边界**（包含明确排除项）
- **技术架构与项目结构建议**（技术栈、目录、模块拆分、关键约束）
- **开发路线图**（里程碑、风险点、时间估算）

对应模板位于：

- [PRD-template.md](./docs/PRD-template.md)
- [MVP-template.md](./docs/MVP-template.md)
- [ROADMAP-template.md](./docs/ROADMAP-template.md)

---

## 核心流程（5 个 Phase）

`project-init` 的主流程固定为：

```
Phase 1: Requirements Clarification
Phase 2: PRD Generation
Phase 3: MVP Definition
Phase 4: Technical Architecture
Phase 5: Development Roadmap
```

你可以把扩展 skills 理解为“外挂能力”，只在需要时触发或显式调用。

---

## 扩展 Skills：筛选结果（适配 AI Project Initiator 目标）

下面是从当前仓库内 skills 中，**筛选出最贴合“项目启动”目标**的一组推荐组合。它们的共同特点是：

- **[能直接增强启动五阶段]** 而不是偏纯设计/纯格式/纯艺术
- **[产出可落地]** 能生成明确文档、可执行计划、可运行代码或可验证结果
- **[低耦合]** 不绑定特定公司品牌或特定场景

### A. 必选（启动主流程）

- **`@project-init`**
  - 覆盖：Phase 1-5 全流程
  - 产出：PRD/MVP/架构/路线图

### B. 强烈推荐（让启动“更像一个团队在做”）

- **`@pm-kit`**
  - 用途：优先级排序（RICE/MoSCoW）、访谈/调研归纳、成功指标框架
  - 最适配：Phase 2/3（PRD/MVP）之后的“功能优先级与范围收敛”

- **`@doc-coauthor`**
  - 用途：把 PRD / 技术方案 / 决策记录写得更可读、可评审、可复用
  - 最适配：Phase 2（PRD）与 Phase 4（架构文档）的“共同写作流程”

### C. 可选（进入实现阶段的加速器）

- **`@web-build`**
  - 用途：快速生成可运行的前端原型/页面（React + TS + Tailwind + shadcn/ui）
  - 最适配：Phase 4 之后，用于“把架构方案落到可运行 UI”

- **`@ux-kit`**
  - 用途：生成“可检索的设计系统建议”（风格/配色/字体/UX 规范/图表类型 + 具体栈落地建议），适合在实现前把 UI 方案定下来
  - 最适配：Phase 4 之后，用于“先定设计系统，再开始写 UI”
  - 备注：当前仓库里该 skill 以 **Trae-only** 形式保留（路径见下方目录结构示例）

- **`@web-test`**
  - 用途：用 Playwright 对本地 Web 应用进行自动化交互、截图、日志排查
  - 最适配：MVP 开发后，用于“验证关键路径”

### D. 可选（把交付物做成特定格式文件）

这些并不改变项目启动逻辑，但能把输出变成更“正式的交付物格式”：

- **`@word`**：把 PRD/方案输出成 Word
- **`@slides`**：把 PRD/路线图做成演示稿
- **`@sheets`**：把估算、里程碑、资源表做成表格
- **`@pdf`**：把文档导出/合并/水印等

### E. 不推荐默认集成（与“项目启动”目标弱相关）

以下 skills 更偏艺术/品牌/内部沟通等，不建议作为默认依赖；仅在你明确需要时再引用：

- `algorithmic-art`
- `canvas-design`
- `brand-guidelines`
- `internal-comms`
- `theme-factory`（适合做 Deck/报告统一主题，但与启动流程无强绑定）
- `frontend-design`（偏“高质量 UI 设计实现”，属于实现阶段能力，不是启动阶段必需）

---

## 推荐的组合用法（按你要的启动深度选）

### 组合 1：最小启动（只要 PRD/MVP/路线图）

只用：

- `@project-init`

### 组合 2：专业启动（推荐默认）

在组合 1 基础上追加：

- `@pm-kit`
- `@doc-coauthor`

### 组合 3：启动 + 快速原型 + 可验证

在组合 2 基础上追加：

- `@web-build`
- `@web-test`

---

## 快速开始

### 方式一：作为 Skill 使用（推荐）

1. 让你的 AI 编辑器加载本仓库的 `SKILL.md`。
2. 在对话中输入：

```text
@project-init
项目类型: Web应用
项目名称: 个人博客系统
一句话描述: 一个支持 Markdown 编辑、标签分类、RSS 订阅的极简博客平台
```

3. 需要优先级或文档协作时，在对话中显式加上：

```text
附加需求:
- 使用 @pm-kit 做优先级排序（RICE 或 MoSCoW）
- 使用 @doc-coauthor 把 PRD 写成可评审的版本
```

### 方式二：作为模板手动推进

你也可以直接复制 `docs/` 里的模板到你的项目中，按模板填写并评审。

---

## 项目结构（建议重构后的布局）

你当前仓库中 `skills/` 同时承载了：

- 你自己的扩展 skills（例如 `pm-kit`）
- 一个较大的“示例技能库”（`skills/vendor/skills/*`）

为方便长期维护与“只加载你真正需要的 skills”，建议按**核心 / 扩展 / vendor 示例库**三层拆分：

```
.
├── SKILL.md
├── README.md
├── docs/
│   ├── PRD-template.md
│   ├── MVP-template.md
│   ├── ROADMAP-template.md
│   └── editor-configs/
│       └── .trae/
└── skills/
    ├── curated/                 # 你“明确推荐给 AI Project Initiator”用的精选集合
    │   ├── pm-kit/
    │   ├── doc-coauthor/
    │   ├── web-build/
    │   └── web-test/
    ├── optional/                # 可选交付物类技能（docx/pptx/pdf/xlsx 等）
    │   ├── ux-kit/               # UI/UX 设计系统建议（可选，Trae-only）
    │   ├── word/
    │   ├── slides/
    │   ├── sheets/
    │   └── pdf/
```

说明：

- `curated/` 里的 skills 是你希望“默认搭配项目启动”使用的集合。
- `vendor/` 里的内容更像素材库/参考库，除非你要用到其中某个具体能力，否则不建议让编辑器默认加载（会稀释触发与降低可控性）。

---

## 文档索引

### 核心

- [SKILL.md](./SKILL.md)
- [PRD-template.md](./docs/PRD-template.md)
- [MVP-template.md](./docs/MVP-template.md)
- [ROADMAP-template.md](./docs/ROADMAP-template.md)

### 编辑器配置

- [Cursor 配置示例](./docs/editor-configs/.cursorrules)
---

## 贡献与优化方向

如果你要继续“优化并重建项目结构”，建议优先做三件事：

- **[收敛]** 把 `curated/` 固定下来：只保留你项目启动真的会用到的 5-8 个 skills
- **[标准化]** 统一每个扩展 skill 的“输入/输出约定”（例如：必须产出哪些文件、文件路径约定）
- **[可组合]** 在 `README.md` 固化几套组合（最小/专业/启动+原型+可验证），让使用者一眼就会用

---

**作者**: jhc  \
**最后更新**: 2026-03-04
