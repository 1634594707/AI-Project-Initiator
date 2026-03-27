# Skills Directory Structure

This directory contains all skills organized by purpose and usage pattern.

## Directory Layout

```
skills/
├── core/                    # Core project initiation workflow
│   └── project-init/        # Main project-init skill (links to root SKILL.md)
├── extensions/              # Extension capabilities by category
│   ├── planning/           # Planning & prioritization tools
│   │   └── pm-kit/         # RICE prioritization, interview analysis
│   ├── collaboration/      # Documentation & collaboration
│   │   └── doc-coauthor/   # Structured co-authoring workflow
│   ├── development/        # Development tools
│   │   ├── web-test/       # Playwright testing automation
│   │   └── ux-kit/         # UI/UX design system recommendations
│   └── delivery/           # Output format converters
│       ├── word/           # Word document generation
│       ├── slides/         # PowerPoint generation
│       ├── sheets/         # Excel spreadsheet handling
│       └── pdf/            # PDF processing
└── shared/                 # Shared utilities
    └── office/             # Common Office file format utilities
```

## Usage Patterns

### Core Skill
The `project-init` skill is the main entry point for project initiation:
```
@project-init
项目类型: Web应用
项目名称: 我的项目
一句话描述: 项目描述
```

### Extension Skills
Extensions enhance specific phases of the workflow:

**Planning Phase**:
- `@pm-kit` - Use after PRD generation for feature prioritization

**Documentation Phase**:
- `@doc-coauthor` - Use for collaborative PRD/spec writing

**Development Phase**:
- `@web-test` - Use for automated testing
- `@ux-kit` - Use for design system recommendations

**Delivery Phase**:
- `@word` / `@slides` / `@sheets` / `@pdf` - Convert outputs to specific formats

## Recommended Combinations

### Minimal (Quick Start)
```
@project-init
```

### Professional (Recommended)
```
@project-init
@pm-kit
@doc-coauthor
```

### Full Stack (Development Ready)
```
@project-init
@pm-kit
@doc-coauthor
@web-test
@ux-kit
```

## Shared Utilities

The `shared/` directory contains code used by multiple skills to avoid duplication:
- `office/` - Office file format utilities (used by word, slides, sheets)

Skills automatically reference shared utilities via relative imports.
