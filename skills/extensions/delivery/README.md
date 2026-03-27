# Delivery Skills

Skills for converting outputs to specific file formats.

## Available Skills

### word
Generate and edit Word documents (.docx).

**Capabilities**:
- Unpack DOCX for editing
- Pack directories back to DOCX
- Track changes and comments
- Schema validation

**When to use**:
- Converting PRD to Word format
- Creating formal documentation
- Sharing with non-technical stakeholders

**Quick start**:
```bash
# Unpack for editing
python skills/shared/office/unpack.py document.docx unpacked/

# Pack back to DOCX
python skills/shared/office/pack.py unpacked/ output.docx
```

**Documentation**: [word/SKILL.md](word/SKILL.md)

---

### slides
Generate PowerPoint presentations (.pptx).

**Capabilities**:
- Create presentation slides
- Add content to slides
- Generate thumbnails
- Clean and optimize presentations

**When to use**:
- Creating roadmap presentations
- Stakeholder demos
- Team alignment meetings

**Documentation**: [slides/SKILL.md](slides/SKILL.md)

---

### sheets
Work with Excel spreadsheets (.xlsx).

**Capabilities**:
- Formula recalculation
- Data manipulation
- Spreadsheet validation

**When to use**:
- Creating feature matrices
- Resource planning spreadsheets
- Timeline and milestone tracking

**Documentation**: [sheets/SKILL.md](sheets/SKILL.md)

---

### pdf
Process PDF documents.

**Capabilities**:
- PDF form filling
- Field extraction
- Image conversion
- Bounding box analysis

**When to use**:
- Working with PDF forms
- Extracting data from PDFs
- Converting PDFs to images

**Documentation**: [pdf/SKILL.md](pdf/SKILL.md)

---

## Best Practices

1. Use delivery skills at the end of each phase
2. Keep source markdown files as single source of truth
3. Generate formatted outputs for stakeholder sharing
4. Version control both source and generated files

## Shared Utilities

All delivery skills use the shared `office/` utilities located at `skills/shared/office/`:
- Reduces code duplication
- Ensures consistent behavior
- Simplifies maintenance

## Integration with Core Workflow

```
Phase 1-5: Complete project initiation
    ↓
    [Generate markdown outputs]
    ↓
    [Use delivery skills to convert formats]
    ↓
    • word: PRD.docx for formal review
    • slides: Roadmap.pptx for presentation
    • sheets: Features.xlsx for tracking
    • pdf: Final documentation package
```
