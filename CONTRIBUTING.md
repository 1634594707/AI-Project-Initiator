# Contributing to AI Project Initiator

感谢你考虑为 AI Project Initiator 做贡献！

## 如何贡献

### 报告问题（Issues）

发现 bug 或有功能建议？请创建 Issue 并包含：
- 清晰的标题和描述
- 复现步骤（如果是 bug）
- 预期行为 vs 实际行为
- 你的环境信息（OS、Python 版本等）

### 提交代码（Pull Requests）

1. Fork 本仓库
2. 创建特性分支：`git checkout -b feature/my-feature`
3. 进行修改
4. 运行验证：`python scripts/validate.py`
5. 提交变更：`git commit -m "Add: my feature"`
6. 推送分支：`git push origin feature/my-feature`
7. 创建 Pull Request

### 代码规范

**Python**:
- 遵循 PEP 8 风格指南
- 使用 Black 格式化：`black .`
- 使用 Ruff 检查：`ruff check .`
- 添加类型注解（Python 3.8+）
- 编写文档字符串

**文档**:
- 使用清晰的标题层级
- 包含代码示例
- 保持中英文版本同步（如果修改 README）
- 使用 Markdown 格式

**提交信息**:
- 使用清晰的提交信息
- 格式：`<type>: <description>`
- 类型：Add, Fix, Update, Remove, Refactor, Docs

示例：
```
Add: RICE prioritization script
Fix: Import path in word skill
Update: README with new structure
Docs: Add best practices guide
```

---

## 项目结构

在贡献前，请理解项目结构：

```
.
├── skills/
│   ├── core/           # 核心 skill（不要随意修改）
│   ├── extensions/     # 扩展 skills（可以添加新 skill）
│   └── shared/         # 共享工具（修改需谨慎，会影响多个 skill）
├── docs/
│   ├── templates/      # 文档模板
│   └── guides/         # 使用指南
├── presets/            # 预设配置
└── scripts/            # 工具脚本
```

---

## 添加新 Skill

### 1. 选择分类

确定你的 skill 属于哪个类别：
- `planning/` - 规划和优先级
- `collaboration/` - 协作和文档
- `development/` - 开发和测试
- `delivery/` - 格式转换和输出

### 2. 创建目录结构

```bash
mkdir -p skills/extensions/[category]/[skill-name]
cd skills/extensions/[category]/[skill-name]
```

### 3. 创建 SKILL.md

必须包含 frontmatter：
```markdown
---
name: skill-name
description: Brief description of what this skill does
license: MIT. See ../../../../LICENSE
---

# Skill Name

## Overview
[What this skill does]

## Quick Start
[How to use it]

## Capabilities
[What it can do]

## When to Use
[When to use this skill]

## Examples
[Usage examples]
```

### 4. 添加脚本（如果需要）

```bash
mkdir scripts
# Add your Python scripts here
```

### 5. 更新文档

- 在分类的 README.md 中添加你的 skill
- 如果适合，创建新的预设配置
- 更新主 README.md（如果是重要 skill）

### 6. 验证

```bash
python scripts/validate.py
```

### 7. 提交 PR

包含：
- SKILL.md 文件
- 脚本和示例
- 更新的文档
- 测试（如果适用）

---

## 修改现有 Skill

### 小改动
- 直接修改并提交 PR
- 说明修改原因

### 大改动
- 先创建 Issue 讨论
- 获得反馈后再实施
- 确保向后兼容

### 修改共享工具
- 特别谨慎，会影响多个 skill
- 必须测试所有依赖的 skill
- 在 PR 中说明影响范围

---

## 文档贡献

### 改进现有文档
- 修正错别字和语法错误
- 添加缺失的示例
- 澄清模糊的说明
- 更新过时的信息

### 添加新文档
- 教程和指南放在 `docs/guides/`
- 参考文档放在相应 skill 目录
- 保持文档简洁实用

### 翻译
- 保持中英文版本同步
- 使用自然的语言表达
- 保留技术术语的原文

---

## 测试

### 运行验证
```bash
python scripts/validate.py
```

### 手动测试
1. 测试你修改的 skill
2. 验证与其他 skill 的集成
3. 检查文档链接是否有效
4. 确保示例代码可运行

### 添加测试（推荐）
```bash
# 在 tests/ 目录添加测试
mkdir -p tests/unit
# 编写测试文件
```

---

## 代码审查

PR 会被审查以确保：
- 代码质量和可读性
- 符合项目规范
- 文档完整
- 没有破坏现有功能
- 通过验证脚本

请耐心等待审查，并根据反馈进行修改。

---

## 行为准则

- 尊重所有贡献者
- 建设性的反馈
- 专注于改进项目
- 欢迎新手贡献

---

## 获取帮助

- 查看现有 Issues 和 PRs
- 阅读项目文档
- 在 Issue 中提问

感谢你的贡献！🎉
