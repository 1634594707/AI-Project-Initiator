---
name: project-init
description: Guide users through structured project initiation workflow including requirements clarification, PRD generation, MVP definition, technical architecture design, and development roadmap planning. Use when users mention creating a new project, starting development, building an app/service, or need help with project planning and setup. Trigger for phrases like "帮我创建项目", "启动新项目", "项目初始化", "技术选型", "写PRD", "定义MVP", or when users describe an idea but haven't defined scope or architecture.
---

# Project Initiator

A comprehensive skill for guiding users through the complete project initiation workflow, from initial idea to development-ready specification.

## Overview

This skill helps users:
1. Clarify requirements through structured questioning
2. Generate standardized Product Requirements Document (PRD)
3. Define Minimum Viable Product (MVP) scope
4. Design technical architecture and project structure
5. Create development roadmap with time estimates

## Activation Patterns

Users may activate this skill explicitly with:
- `@project-init` or `@项目启动助手`
- Project type, name, and description parameters

Or implicitly through phrases like:
- "我想做一个...项目"
- "帮我规划一下这个项目"
- "这个项目该怎么设计"
- "用什么技术栈比较好"

## Workflow

```
Phase 1: Requirements Clarification
    ↓
Phase 2: PRD Generation
    ↓
Phase 3: MVP Definition
    ↓
Phase 4: Technical Architecture
    ↓
Phase 5: Development Roadmap
```

---

## Phase 1: Requirements Clarification

### Goal
Understand the project's business objectives, user needs, and constraints through progressive questioning.

### Process

#### Step 1: Capture Initial Context
If user provided activation parameters, extract:
- Project type (Web/Mobile/API/Desktop/Other)
- Project name
- One-sentence description

If no parameters provided, ask:
```
请告诉我：
1. 项目类型：[Web应用/移动应用/API服务/桌面应用/其他]
2. 项目名称：[你的项目名]
3. 一句话描述：[用一句话描述这个项目要解决什么问题]
```

#### Step 2: Deep Dive Questioning

Ask questions sequentially, probing deeper based on answers. Use these 15 core questions:

**Business Goals (Must Ask)**
1. **Core Problem**: 这个项目要解决什么具体痛点？成功标准是什么？
2. **Target Users**: 主要用户群体是谁？他们的技术熟练度如何？
3. **Value Proposition**: 与现有解决方案相比，独特价值是什么？
4. **Business Model**: 如何盈利或创造价值？（订阅/广告/交易抽成/效率提升）

**Functional Requirements (Progressive)**
5. **Core Scenario**: 描述一个典型的用户使用流程（User Story）
6. **Feature Boundaries**: 哪些功能是"必须有"，哪些是"最好有"？
7. **Content Strategy**: 内容由谁产生？UGC/PGC/AI生成/抓取？
8. **Integration Needs**: 需要对接第三方服务吗？（支付/地图/社交登录/AI API）

**Technical Constraints (Critical)**
9. **Performance Requirements**: 预期的用户规模？并发量？响应时间要求？
10. **Platform Constraints**: 必须支持哪些平台？（iOS/Android/桌面/特定浏览器）
11. **Compliance Requirements**: 是否有 GDPR/CCPA/等保/行业特定合规要求？
12. **Tech Preferences**: 团队技术栈偏好？是否有必须使用的技术？

**Project Management (Practical)**
13. **Time Constraints**: 期望的上线时间？是否有硬性截止日期？
14. **Resource Limits**: 团队规模？预算范围？是否需要开源方案？
15. **Maintenance Plan**: 上线后的迭代频率？运维能力如何？

#### Step 3: Summarize and Confirm

After gathering all information, summarize key points:
```
## 需求澄清总结

**项目**: [名称] - [类型]
**核心问题**: [一句话]
**目标用户**: [描述]
**关键约束**: [技术/时间/资源]

是否准确？需要调整什么？
```

Wait for user confirmation before proceeding to Phase 2.

---

## Phase 2: PRD Generation

### Goal
Create a standardized Product Requirements Document based on clarified requirements.

### Output
Generate `docs/PRD.md` with the following structure:

```markdown
# 产品需求文档 (PRD)

## 1. 项目概述
- 项目名称：
- 版本：0.1.0
- 日期：YYYY-MM-DD
- 状态：草案

## 2. 背景与目标
### 2.1 问题陈述
[从 Phase 1 提炼]

### 2.2 成功指标 (KPI)
- [可量化的指标]

## 3. 用户画像
| 角色 | 年龄/职业 | 目标 | 痛点 | 技术熟练度 |
|------|----------|------|------|-----------|
| 主要用户 | | | | |
| 次要用户 | | | | |

## 4. 功能需求
### 4.1 核心功能 (Must Have)
- [ ] 功能1：描述 + 验收标准
- [ ] 功能2：描述 + 验收标准

### 4.2 扩展功能 (Nice to Have)
- [ ] 功能3：描述 + 优先级（P1/P2/P3）

### 4.3 排除项 (Won't Have - 本阶段不做)
- 

## 5. 非功能需求
- 性能：[QPS、响应时间、可用性]
- 安全：[认证方式、数据加密、权限模型]
- 兼容性：[浏览器版本、设备类型]
- 合规：[数据隐私、行业规范]

## 6. 用户流程
```mermaid
graph LR
    A[入口] --> B[操作1]
    B --> C[操作2]
    C --> D[结果]
```

## 7. 竞品分析
| 竞品 | 优势 | 劣势 | 我们的差异化 |
|------|------|------|-------------|
| | | | |

## 8. 风险与假设
- 技术风险：
- 市场风险：
- 资源风险：
```

### Process
1. Create the file with the above structure
2. Fill in content based on Phase 1 answers
3. Present to user for review
4. Iterate based on feedback
5. Confirm "PRD finalized" before proceeding

---

## Phase 3: MVP Definition

### Goal
Strictly define MVP scope by filtering Must Have vs Nice to Have features.

### MVP Criteria
For each potential feature, ask three questions:
1. **没有这个，用户能完成核心任务吗？** (如果不能 → Must Have)
2. **去掉这个，产品还完整吗？** (如果否 → Must Have)
3. **实现这个需要超过 30% 开发时间吗？** (如果是 → 考虑移到 Phase 2)

### Output
Generate `docs/MVP.md`:

```markdown
# MVP 定义文档 (MVP.md)

## 版本范围
- 版本号：v0.1.0
- 目标日期：YYYY-MM-DD
- 核心理念：用最小成本验证核心假设

## 包含功能 (In Scope)
| 功能模块 | 具体功能 | 业务价值 | 预估工时 |
|---------|---------|---------|---------|
| 用户系统 | 注册/登录/找回密码 | 身份识别 | 8h |
| [模块名] | [功能描述] | [价值] | [工时] |

## 明确排除 (Out of Scope)
| 功能 | 排除原因 | 计划版本 |
|------|---------|---------|
| [功能名] | [原因] | [版本] |

## 技术债务预警
- 为赶进度暂时采用的方案：
- 需要在 v0.2.0 前重构的部分：

## 验收标准
- [ ] 标准1
- [ ] 标准2
```

### Process
1. Review PRD features against MVP criteria
2. Categorize each feature: In Scope / Out of Scope
3. Document rationale for exclusions
4. Define acceptance criteria
5. Get user confirmation

---

## Phase 4: Technical Architecture

### Goal
Recommend tech stack and generate project structure.

### Tech Stack Decision Matrix

Based on project requirements, recommend from these options:

| Dimension | Options | Selection Criteria |
|-----------|---------|-------------------|
| Frontend | React/Vue/Svelte/Next/Nuxt | SEO needs, team familiarity |
| Styling | Tailwind/Styled Components/CSS Modules | Design system complexity |
| Backend | Node/Go/Python/Rust | Performance needs, ecosystem |
| Database | PostgreSQL/MongoDB/Supabase/Firebase | Data relationships, real-time |
| Deployment | Vercel/Netlify/AWS/Docker | Traffic expectations, budget |

### Output

#### 1. Tech Stack Recommendation
Present 2-3 options with comparison:

```markdown
## 技术栈方案对比

### 方案 A: [名称]
- 前端：[技术] - [理由]
- 后端：[技术] - [理由]
- 数据库：[技术] - [理由]
- 部署：[技术] - [理由]
- **适合场景**：[描述]

### 方案 B: [名称]
...

**推荐**：方案 [A/B/C] - [理由]
```

#### 2. Project Structure
Generate directory structure based on selected stack.

Example for full-stack web app:
```
my-project/
├── apps/
│   ├── web/                    # Next.js 前端
│   │   ├── src/
│   │   │   ├── app/           # App Router
│   │   │   ├── components/    # React 组件
│   │   │   ├── hooks/        # 自定义 Hooks
│   │   │   ├── lib/          # 工具函数
│   │   │   └── types/        # TypeScript 类型
│   │   └── public/
│   └── api/                    # 后端服务
│       ├── src/
│       │   ├── routes/        # API 路由
│       │   ├── controllers/   # 业务逻辑
│       │   ├── models/        # 数据模型
│       │   └── services/      # 外部服务
├── packages/
│   └── shared-types/           # 共享类型
├── docs/
│   ├── PRD.md
│   ├── MVP.md
│   └── API.md
└── README.md
```

#### 3. Editor Configuration Files

Generate config files for user's editor:

**Cursor (.cursorrules)**:
```text
# 项目规范
- 使用 TypeScript 严格模式
- 组件使用函数式组件 + Hooks
- 所有 API 调用封装到 services/ 目录
- 错误处理必须使用 try-catch
- 提交前必须运行 lint 和 type-check

# 代码风格
- 优先使用 named exports
- 组件文件使用 PascalCase
- 工具函数使用 camelCase
- 常量使用 UPPER_SNAKE_CASE
```

**Windsurf (.windsurfrules)**:
```text
[架构]
- 前端: [技术栈]
- 后端: [技术栈]
- 样式: [方案]

[约束]
- [具体约束1]
- [具体约束2]
```

**Trae (.trae/rules.yaml)**:
```yaml
project_type: [类型]
tech_stack:
  frontend: [技术]
  backend: [技术]
  database: [数据库]
conventions:
  component_style: [风格]
  api_style: [风格]
  testing: [要求]
```

### Process
1. Analyze requirements from PRD/MVP
2. Recommend tech stack with justification
3. Get user selection
4. Generate project structure
5. Create editor config files
6. Confirm before proceeding

---

## Phase 5: Development Roadmap

### Goal
Create development roadmap with milestones and time estimates.

### Time Estimation Method
Use **Three-Point Estimation** (Optimistic / Most Likely / Pessimistic):

Formula: `Estimate = (Optimistic + 4×Most Likely + Pessimistic) / 6`

### Output
Generate `docs/ROADMAP.md`:

```markdown
# 开发路线图 (ROADMAP.md)

## 里程碑 1: 基础架构 (Week 1)
- [ ] 项目脚手架搭建 (4h/6h/10h)
- [ ] 数据库设计 + 迁移 (6h/8h/12h)
- [ ] CI/CD 流程配置 (4h/6h/8h)
- **缓冲时间**: 20%
- **交付物**: 可运行的 Hello World + 数据库连接

## 里程碑 2: 核心功能 (Week 2-3)
- [ ] 用户认证系统 (8h/12h/16h)
- [ ] 主业务功能 A (16h/24h/32h)
- [ ] 主业务功能 B (12h/16h/24h)
- **缓冲时间**: 25%
- **交付物**: 内部测试版本 (Alpha)

## 里程碑 3: MVP 完善 (Week 4)
- [ ] 错误处理与日志 (6h/8h/12h)
- [ ] 基础管理后台 (8h/12h/16h)
- [ ] 部署与监控 (4h/6h/10h)
- **缓冲时间**: 15%
- **交付物**: 公测版本 (Beta)

## 关键路径
[描述依赖关系和关键路径]

## 风险缓解
| 风险 | 概率 | 影响 | 应对策略 |
|------|------|------|---------|
| [风险1] | 高/中/低 | 高/中/低 | [策略] |
| [风险2] | 高/中/低 | 高/中/低 | [策略] |

## 验收清单
- [ ] PRD.md 已生成并通过评审
- [ ] MVP.md 已明确功能边界
- [ ] 项目目录结构已创建
- [ ] 编辑器配置文件已就位
- [ ] ROADMAP.md 已制定并达成共识
- [ ] 首次 commit 已完成（README + 基础配置）
```

### Process
1. Break down MVP features into tasks
2. Apply three-point estimation to each task
3. Group into milestones (typically 3-4)
4. Add buffer time (15-25% per milestone)
5. Identify critical path and dependencies
6. List top 3 risks with mitigation strategies
7. Present to user and iterate

---

## Completion Criteria

Project initiation is complete when:
- ✅ PRD.md generated and reviewed
- ✅ MVP.md defines clear boundaries
- ✅ Project structure created
- ✅ Editor config files in place
- ✅ ROADMAP.md agreed upon
- ✅ Initial commit completed

## Prompt Templates

### Activation Prompt (Chinese)
```
你是一位资深的产品经理兼技术架构师。我需要你帮我启动一个新项目。

请严格按照以下流程执行：

第一步：需求澄清
- 依次询问 Phase 1 中的 15 个问题
- 每个问题根据我的回答进行追问，直到清晰为止
- 如果我的回答模糊，给出选项让我选择

第二步：生成 PRD
- 基于对话内容生成标准化的 PRD.md
- 包含用户画像表格、功能优先级矩阵、用户流程图

第三步：定义 MVP
- 严格筛选 Must Have vs Nice to Have
- 明确标出本阶段不做的事项
- 给出 MVP 的功能清单和验收标准

第四步：技术架构
- 推荐技术栈并说明理由（给出 2-3 个选项对比）
- 生成项目目录结构
- 创建编辑器配置文件（.cursorrules 等）

第五步：开发计划
- 划分 3-4 个里程碑
- 每个任务使用三点估算法（乐观/最可能/悲观）
- 标注关键路径和依赖关系
- 识别 top 3 风险并给出缓解方案

项目信息：
- 类型：[填入]
- 名称：[填入]
- 描述：[填入]
```

### Activation Prompt (English)
```
You are a senior product manager and technical architect. Help me initiate a new project following this strict workflow:

Phase 1: Requirements Clarification
- Ask the 15 questions from Phase 1 sequentially
- Probe deeper based on my answers until clear
- Provide options if my answer is ambiguous

Phase 2: PRD Generation
- Generate standardized PRD.md with user personas, feature matrix, user flows

Phase 3: MVP Definition
- Strictly filter Must Have vs Nice to Have
- Explicitly list what is out of scope for this phase
- Provide MVP feature checklist and acceptance criteria

Phase 4: Technical Architecture
- Recommend tech stack with 2-3 alternatives comparison
- Generate project directory structure
- Create editor config files (.cursorrules, etc.)

Phase 5: Development Plan
- Define 3-4 milestones
- Use three-point estimation (optimistic/most likely/pessimistic)
- Identify critical path and dependencies
- List top 3 risks with mitigation strategies

Project Info:
- Type: [fill in]
- Name: [fill in]
- Description: [fill in]
```

---

## Notes

- Always confirm each phase before proceeding to the next
- Adapt questions based on project type (Web/Mobile/API/Desktop)
- Be flexible - if user says "skip to architecture", respect their choice
- Focus on practical outcomes over rigid process adherence
- Document all decisions in the generated files
