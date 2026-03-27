#!/usr/bin/env python3
"""
Validate skill configurations and structure.

Usage:
    python scripts/validate.py
"""

import sys
from pathlib import Path
import yaml

def validate_skill_structure():
    """Validate that all skills have required files."""
    errors = []
    warnings = []
    
    skills_dir = Path("skills")
    
    # Check core skill
    core_skill = skills_dir / "core" / "project-init" / "SKILL.md"
    if not core_skill.exists():
        errors.append(f"Missing core skill: {core_skill}")
    
    # Check extensions
    extension_categories = ["planning", "collaboration", "development", "delivery"]
    for category in extension_categories:
        category_path = skills_dir / "extensions" / category
        if not category_path.exists():
            warnings.append(f"Missing extension category: {category}")
            continue
        
        # Check each skill in category
        for skill_dir in category_path.iterdir():
            if skill_dir.is_dir():
                skill_md = skill_dir / "SKILL.md"
                if not skill_md.exists():
                    errors.append(f"Missing SKILL.md in {skill_dir}")
    
    # Check shared utilities
    shared_office = skills_dir / "shared" / "office"
    if not shared_office.exists():
        errors.append(f"Missing shared office utilities: {shared_office}")
    else:
        required_files = ["pack.py", "unpack.py", "soffice.py", "__init__.py"]
        for file in required_files:
            if not (shared_office / file).exists():
                errors.append(f"Missing shared office file: {file}")
    
    return errors, warnings

def validate_presets():
    """Validate preset configurations."""
    errors = []
    warnings = []
    
    presets_dir = Path("presets")
    if not presets_dir.exists():
        errors.append("Missing presets directory")
        return errors, warnings
    
    preset_files = list(presets_dir.glob("*.yaml"))
    if not preset_files:
        warnings.append("No preset files found")
    
    for preset_file in preset_files:
        try:
            with open(preset_file, 'r', encoding='utf-8') as f:
                preset = yaml.safe_load(f)
            
            # Check required fields
            required_fields = ['name', 'description', 'skills']
            for field in required_fields:
                if field not in preset:
                    errors.append(f"Preset {preset_file.name} missing field: {field}")
            
            # Validate skills exist
            if 'skills' in preset:
                for skill in preset['skills']:
                    # Check if skill exists (simplified check)
                    if skill == 'project-init':
                        continue  # Core skill
                    # Extension skills should be in extensions/
                    found = False
                    for category in ["planning", "collaboration", "development", "delivery"]:
                        skill_path = Path("skills") / "extensions" / category / skill
                        if skill_path.exists():
                            found = True
                            break
                    if not found:
                        warnings.append(f"Preset {preset_file.name} references unknown skill: {skill}")
        
        except yaml.YAMLError as e:
            errors.append(f"Invalid YAML in {preset_file.name}: {e}")
        except Exception as e:
            errors.append(f"Error reading {preset_file.name}: {e}")
    
    return errors, warnings

def validate_docs():
    """Validate documentation structure."""
    errors = []
    warnings = []
    
    docs_dir = Path("docs")
    required_docs = [
        "WORKFLOW.md",
        "templates/PRD-template.md",
        "templates/MVP-template.md",
        "templates/ROADMAP-template.md",
        "guides/getting-started.md",
        "guides/best-practices.md"
    ]
    
    for doc in required_docs:
        doc_path = docs_dir / doc
        if not doc_path.exists():
            errors.append(f"Missing documentation: {doc_path}")
    
    return errors, warnings

def main():
    print("🔍 Validating AI Project Initiator structure...\n")
    
    all_errors = []
    all_warnings = []
    
    # Validate skills
    print("Checking skills structure...")
    errors, warnings = validate_skill_structure()
    all_errors.extend(errors)
    all_warnings.extend(warnings)
    
    # Validate presets
    print("Checking presets...")
    errors, warnings = validate_presets()
    all_errors.extend(errors)
    all_warnings.extend(warnings)
    
    # Validate docs
    print("Checking documentation...")
    errors, warnings = validate_docs()
    all_errors.extend(errors)
    all_warnings.extend(warnings)
    
    # Report results
    print("\n" + "="*60)
    
    if all_errors:
        print(f"\n❌ Found {len(all_errors)} error(s):\n")
        for error in all_errors:
            print(f"  • {error}")
    
    if all_warnings:
        print(f"\n⚠️  Found {len(all_warnings)} warning(s):\n")
        for warning in all_warnings:
            print(f"  • {warning}")
    
    if not all_errors and not all_warnings:
        print("\n✅ All validations passed!")
        return 0
    
    if all_errors:
        print("\n❌ Validation failed!")
        return 1
    else:
        print("\n✅ Validation passed with warnings")
        return 0

if __name__ == "__main__":
    sys.exit(main())
