# Planning Skills

Skills for product planning, prioritization, and strategy.

## Available Skills

### pm-kit
Comprehensive toolkit for product managers.

**Capabilities**:
- RICE prioritization framework
- Customer interview analysis
- PRD templates and frameworks
- Success metrics definition

**When to use**:
- After PRD generation (Phase 2)
- When you have 10+ features to prioritize
- When you need quantitative decision-making

**Quick start**:
```bash
# Feature prioritization
python skills/extensions/planning/pm-kit/scripts/rice_prioritizer.py features.csv

# Interview analysis
python skills/extensions/planning/pm-kit/scripts/customer_interview_analyzer.py interview.txt
```

**Documentation**: [pm-kit/SKILL.md](pm-kit/SKILL.md)

---

## Best Practices

1. Use RICE prioritization after defining all MVP features
2. Analyze customer interviews before writing PRD
3. Define success metrics early in Phase 2
4. Revisit prioritization quarterly

## Integration with Core Workflow

```
Phase 1: Requirements Clarification
Phase 2: PRD Generation
    ↓
    [Use pm-kit for prioritization]
    ↓
Phase 3: MVP Definition
Phase 4: Technical Architecture
Phase 5: Development Roadmap
```
