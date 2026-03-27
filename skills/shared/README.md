# Shared Utilities

This directory contains shared code used across multiple skills to avoid duplication.

## office/

Common utilities for working with Office file formats (DOCX, PPTX, XLSX):
- `pack.py` - Pack directories into Office files
- `unpack.py` - Unpack Office files for editing
- `validate.py` - Validate Office file structure
- `soffice.py` - LibreOffice integration helpers
- `helpers/` - XML processing utilities
- `validators/` - Schema validators
- `schemas/` - Office XML schemas

Used by: word, slides, sheets skills
