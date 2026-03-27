# Changelog

All notable changes to this project will be documented in this file.

## [1.0.0] - 2026-03-27

### 🎉 Major Refactoring

This release represents a complete restructuring of the project for better maintainability and usability.

### Added
- ✨ Preset configurations (minimal, professional, full-stack)
- 📚 Comprehensive documentation structure
- 🌍 English README (README.en.md)
- 📖 Getting started guide (docs/guides/getting-started.md)
- 📖 Best practices guide (docs/guides/best-practices.md)
- 🔧 Setup scripts (setup.sh, setup.bat)
- ✅ Validation script (validate.py)
- 📦 Modern Python project configuration (pyproject.toml)
- 📝 Detailed workflow documentation (docs/WORKFLOW.md)
- 📂 README files for each skill category

### Changed
- 🏗️ **Major**: Restructured skills directory
  - `skills/curated/` → `skills/extensions/planning/`, `skills/extensions/collaboration/`, `skills/extensions/development/`
  - `skills/optional/` → `skills/extensions/delivery/`
  - Added `skills/core/` for project-init
  - Added `skills/shared/` for common utilities
- 📄 **Major**: Streamlined SKILL.md from 300+ lines to ~50 lines
  - Moved detailed content to docs/WORKFLOW.md
  - Improved readability and maintainability
- 📁 Moved templates to `docs/templates/` subdirectory
- 📝 Completely rewrote README.md with clearer structure
- 🔧 Enhanced .gitignore with more patterns

### Removed
- 🗑️ Eliminated 70% code duplication by extracting shared office utilities
- 🗑️ Removed redundant office/ directories from word, slides, sheets skills

### Fixed
- 🐛 Import paths now use shared office module
- 🐛 Consistent directory structure across all skills

---

## [0.1.0] - 2026-03-04

### Initial Release
- Initial project structure
- Core project-init skill
- Extension skills (pm-kit, doc-coauthor, web-test, etc.)
- Basic documentation and templates
