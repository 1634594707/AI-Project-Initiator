# AI Project Initiator

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-orange)

AI-powered project initiation tool that generates PRD, MVP definition, technical architecture, and development roadmap through structured questioning.

## Quick Start

### Basic Usage
```
@project-init
Project Type: Web Application
Project Name: My Project
Description: Project description
```

### Presets

- **minimal**: Basic initiation (1-2h)
- **professional**: Professional initiation with prioritization and collaboration (2-4h, recommended)
- **full-stack**: Full stack initiation with design system and testing (3-6h)

Details: [presets/README.md](presets/README.md)

---

## Core Workflow

```
Requirements → PRD → MVP → Architecture → Roadmap
```

Details: [docs/WORKFLOW.md](docs/WORKFLOW.md)

---

## Outputs

- **PRD** - Product Requirements Document ([Template](docs/templates/PRD-template.md))
- **MVP** - Minimum Viable Product definition ([Template](docs/templates/MVP-template.md))
- **Architecture** - Tech stack and project structure ([Example](docs/ARCHITECTURE.md))
- **Roadmap** - Development plan and estimates ([Template](docs/templates/ROADMAP-template.md))

---

## Extension Skills

- **planning/pm-kit**: RICE prioritization, interview analysis
- **collaboration/doc-coauthor**: Structured documentation workflow
- **development/web-test**: Playwright automation testing
- **development/ux-kit**: UI/UX design system
- **delivery**: Word/PowerPoint/Excel/PDF export

Details: [skills/README.md](skills/README.md)

---

## Installation

**Automatic**:
```bash
# Linux/Mac
bash scripts/setup.sh

# Windows
scripts\setup.bat
```

**Manual**:
```bash
pip install -r requirements.txt
playwright install chromium  # if using web-test
```

---

## Project Structure

```
.
├── SKILL.md              # Core definition
├── skills/
│   ├── core/             # Core functionality
│   ├── extensions/       # Extensions (categorized)
│   └── shared/           # Shared utilities
├── presets/              # Preset configurations
├── docs/                 # Documentation and templates
└── scripts/              # Automation scripts
```

---

## Documentation

- [SKILL.md](./SKILL.md) - Core definition
- [WORKFLOW.md](./docs/WORKFLOW.md) - Detailed workflow
- [Getting Started](./docs/guides/getting-started.md)
- [Best Practices](./docs/guides/best-practices.md)
- [CHANGELOG](./CHANGELOG.md)
- [CONTRIBUTING](./CONTRIBUTING.md)

---

## License

MIT License - See [LICENSE](LICENSE)

**Author**: jhc  
**Last Updated**: 2026-03-27
