---
name: project-init
description: Guide users through structured project initiation workflow including requirements clarification, PRD generation, MVP definition, technical architecture design, and development roadmap planning. Use when users mention creating a new project, starting development, building an app/service, or need help with project planning and setup.
---

# Project Initiator

AI-driven project initiation skill that guides users from idea to development-ready specification.

## Workflow

```
Phase 1: Requirements Clarification (15 key questions)
    ↓
Phase 2: PRD Generation (docs/PRD.md)
    ↓
Phase 3: MVP Definition (docs/MVP.md)
    ↓
Phase 4: Technical Architecture (project structure + configs)
    ↓
Phase 5: Development Roadmap (docs/ROADMAP.md)
```

## Usage

```
@project-init
项目类型: Web应用
项目名称: 个人博客
一句话描述: 支持 Markdown 的极简博客平台
```

## Outputs

- **PRD** - Product Requirements Document ([Template](docs/templates/PRD-template.md))
- **MVP** - Minimum Viable Product scope ([Template](docs/templates/MVP-template.md))
- **Architecture** - Tech stack and structure ([Example](docs/ARCHITECTURE.md))
- **Roadmap** - Development plan ([Template](docs/templates/ROADMAP-template.md))

## Extension Skills

- `@pm-kit` - RICE prioritization, interview analysis
- `@doc-coauthor` - Structured documentation workflow
- `@web-test` - Playwright automated testing
- `@ux-kit` - UI/UX design system
- `@word/@slides/@sheets/@pdf` - Export to various formats

## Completion Criteria

- ✅ PRD.md generated and reviewed
- ✅ MVP.md defines clear boundaries
- ✅ Project structure created
- ✅ Editor configs in place
- ✅ ROADMAP.md agreed upon

For detailed instructions, see [docs/WORKFLOW.md](docs/WORKFLOW.md).
