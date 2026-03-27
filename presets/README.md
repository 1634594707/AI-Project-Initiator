# Presets

Presets are pre-configured combinations of skills for common project initiation scenarios.

## Available Presets

### minimal.yaml
**Use when**: You need a fast project setup with basic documentation

**Includes**: project-init only

**Time**: 1-2 hours

**Outputs**: PRD, MVP, Architecture, Roadmap

---

### professional.yaml (Recommended)
**Use when**: You want thorough planning with prioritization and collaborative documentation

**Includes**: project-init + pm-kit + doc-coauthor

**Time**: 2-4 hours

**Outputs**: All minimal outputs + feature prioritization + co-authored docs

**Best for**: Team projects, multiple stakeholders, quality documentation

---

### full-stack.yaml
**Use when**: You want to go from idea to testable prototype

**Includes**: project-init + pm-kit + doc-coauthor + ux-kit + web-test

**Time**: 3-6 hours

**Outputs**: All professional outputs + design system + test setup

**Best for**: Web applications, UI/UX consistency, automated testing

---

## How to Use Presets

### Option 1: Reference in Conversation
```
@project-init --preset professional

项目类型: Web应用
项目名称: 我的项目
```

### Option 2: Manual Selection
Simply mention which skills you want to use:
```
我想用 @project-init、@pm-kit 和 @doc-coauthor 来启动项目
```

### Option 3: Custom Combination
Mix and match skills based on your needs:
```
@project-init
@pm-kit  # 只用优先级排序
@web-test  # 只用测试自动化
```

## Creating Custom Presets

Copy an existing preset and modify:
1. Change the `name` and `description`
2. Add/remove skills from the `skills` list
3. Adjust `phases` to match your workflow
4. Update `outputs` to reflect what will be generated
5. Estimate `estimated_time` based on complexity

Save as `custom-name.yaml` in this directory.
