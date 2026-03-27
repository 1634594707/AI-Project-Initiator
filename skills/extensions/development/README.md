# Development Skills

Skills for development, testing, and design implementation.

## Available Skills

### web-test
Playwright-based automation for testing local web applications.

**Capabilities**:
- Browser automation and interaction
- Screenshot capture
- Console log inspection
- Server lifecycle management

**When to use**:
- After MVP development
- For regression testing
- To verify critical user paths
- For debugging UI behavior

**Quick start**:
```bash
# Run with server management
python skills/extensions/development/web-test/scripts/with_server.py \
  --server "npm run dev" --port 5173 \
  -- python your_test.py
```

**Documentation**: [web-test/SKILL.md](web-test/SKILL.md)

---

### ux-kit
UI/UX design system recommendations and guidelines.

**Capabilities**:
- Design system recommendations
- Color palette suggestions
- Typography guidelines
- Component library recommendations
- Stack-specific UI patterns

**When to use**:
- After technical architecture (Phase 4)
- Before starting UI implementation
- When establishing design consistency
- For teams without dedicated designers

**Quick start**:
```bash
# Search design recommendations
python skills/extensions/development/ux-kit/scripts/search.py "button styles"

# Generate design system
python skills/extensions/development/ux-kit/scripts/design_system.py --stack react
```

**Documentation**: [ux-kit/SKILL.md](ux-kit/SKILL.md)

---

## Best Practices

### For web-test
1. Always use `--help` on scripts first
2. Wait for `networkidle` before DOM inspection
3. Use descriptive selectors (text=, role=)
4. Treat scripts as black boxes - don't read source unless necessary

### For ux-kit
1. Define design system before writing components
2. Choose stack-specific recommendations
3. Document design decisions in ARCHITECTURE.md
4. Share design system with entire team

## Integration with Core Workflow

```
Phase 1-3: Requirements, PRD, MVP
    ↓
Phase 4: Technical Architecture
    ↓
    [Use ux-kit for design system]
    ↓
Phase 5: Development Roadmap
    ↓
    [Development begins]
    ↓
    [Use web-test for validation]
```
