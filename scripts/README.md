# Scripts

Utility scripts for managing the AI Project Initiator.

## Available Scripts

### setup.sh / setup.bat
One-command installation of all dependencies.

**Linux/Mac**:
```bash
bash scripts/setup.sh
```

**Windows**:
```cmd
scripts\setup.bat
```

**What it does**:
- Checks Python installation
- Installs Python dependencies from requirements.txt
- Optionally installs Playwright for web testing
- Creates .gitignore if missing

---

### validate.py
Validates the project structure and configurations.

**Usage**:
```bash
python scripts/validate.py
```

**What it checks**:
- Skills directory structure
- Required SKILL.md files
- Shared utilities presence
- Preset configuration validity
- Documentation completeness

**Exit codes**:
- 0: All validations passed
- 1: Validation failed with errors

---

## Development Scripts

These scripts are for maintaining the project itself:

### Adding a New Skill

1. Create directory in appropriate category:
   ```bash
   mkdir -p skills/extensions/[category]/[skill-name]
   ```

2. Create SKILL.md with frontmatter:
   ```markdown
   ---
   name: skill-name
   description: What this skill does
   ---
   
   # Skill Name
   ...
   ```

3. Add scripts if needed:
   ```bash
   mkdir skills/extensions/[category]/[skill-name]/scripts
   ```

4. Run validation:
   ```bash
   python scripts/validate.py
   ```

### Creating a New Preset

1. Copy an existing preset:
   ```bash
   cp presets/minimal.yaml presets/my-preset.yaml
   ```

2. Edit the configuration:
   - Update `name` and `description`
   - Modify `skills` list
   - Adjust `phases` and `outputs`

3. Validate:
   ```bash
   python scripts/validate.py
   ```

---

## Troubleshooting

### Python dependencies fail to install
- Ensure Python 3.8+ is installed
- Try upgrading pip: `pip install --upgrade pip`
- Use virtual environment: `python -m venv venv && source venv/bin/activate`

### Playwright installation fails
- Ensure you have internet connection
- Try manual installation: `playwright install chromium`
- Check system requirements: https://playwright.dev/python/docs/intro

### Validation errors
- Read error messages carefully
- Check file paths are correct
- Ensure SKILL.md files have proper frontmatter
- Verify YAML syntax in presets
