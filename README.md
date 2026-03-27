# AI Project Initiator

![Version](https://img.shields.io/badge/version-1.0.0-blue)
![Python](https://img.shields.io/badge/python-3.8+-green)
![License](https://img.shields.io/badge/license-MIT-orange)

AI 驱动的项目启动工具，通过结构化提问生成 PRD、MVP 定义、技术架构和开发路线图。

## 快速开始

### 基础使用
```
@project-init
项目类型: Web应用
项目名称: 我的项目
一句话描述: 项目描述
```

### 预设配置

- **minimal**: 基础启动（1-2h）
- **professional**: 专业启动，含优先级排序和协作（2-4h，推荐）
- **full-stack**: 全栈启动，含设计系统和测试（3-6h）

查看详情：[presets/README.md](presets/README.md)

---

## 核心流程

```
需求澄清 → PRD 生成 → MVP 定义 → 技术架构 → 开发路线图
```

详细说明：[docs/WORKFLOW.md](docs/WORKFLOW.md)

---

## 产出物

- **PRD** - 产品需求文档 ([模板](docs/templates/PRD-template.md))
- **MVP** - 最小可行产品定义 ([模板](docs/templates/MVP-template.md))
- **架构** - 技术栈和项目结构 ([示例](docs/ARCHITECTURE.md))
- **路线图** - 开发计划和时间估算 ([模板](docs/templates/ROADMAP-template.md))

---

## 扩展 Skills

- **planning/pm-kit**: RICE 优先级排序、用户访谈分析
- **collaboration/doc-coauthor**: 结构化文档协作
- **development/web-test**: Playwright 自动化测试
- **development/ux-kit**: UI/UX 设计系统
- **delivery**: Word/PowerPoint/Excel/PDF 导出

详细说明：[skills/README.md](skills/README.md)

---

## 安装

**自动安装**:
```bash
# Linux/Mac
bash scripts/setup.sh

# Windows
scripts\setup.bat
```

**手动安装**:
```bash
pip install -r requirements.txt
playwright install chromium  # 如果使用 web-test
```

---

## 项目结构

```
.
├── SKILL.md              # 核心定义
├── skills/
│   ├── core/             # 核心功能
│   ├── extensions/       # 扩展功能（按类别分类）
│   └── shared/           # 共享工具库
├── presets/              # 预设配置
├── docs/                 # 文档和模板
└── scripts/              # 自动化脚本
```

---

## 文档

- [SKILL.md](./SKILL.md) - 核心定义
- [WORKFLOW.md](./docs/WORKFLOW.md) - 详细流程
- [快速上手](./docs/guides/getting-started.md)
- [最佳实践](./docs/guides/best-practices.md)
- [CHANGELOG](./CHANGELOG.md)
- [CONTRIBUTING](./CONTRIBUTING.md)

---

## License

MIT License - 详见 [LICENSE](LICENSE)

**作者**: jhc  
**最后更新**: 2026-03-27
