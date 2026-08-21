# TopPrism 公开项目组合

这是 [TopPrism 主页](README.zh-CN.md) 背后的完整公开目录，用于区分两条核心能力主线、学习项目和上游参考实现。

本页由 [`portfolio/portfolio.yml`](portfolio/portfolio.yml) 渲染。登记表是项目展示顺序、双语简介、用途、成熟度、证据类型和当前旗舰集合的单一来源，并不是按热度排序的榜单。

`flagship` 表示“当前在主页展示的旗舰项目”，不表示永久排名或永远不变。旗舰集合的任何变化都需要明确评审并更新登记表，渲染器不会自动晋升仓库。

<!-- GENERATED:PORTFOLIO:START -->
### World Model & Decision

| Project | Summary | Status | Evidence |
| --- | --- | --- | --- |
| [visit-scheduling-optimizer](https://github.com/topprismdata/visit-scheduling-optimizer) | 基于数据校准的周期性外勤拜访计划决策引擎。 | `flagship` | `anonymized operational data` |
| [spatial-decision-intelligence](https://github.com/topprismdata/spatial-decision-intelligence) | 以可解释结果诊断业务目标与空间约束之间的冲突。 | `catalog` | `internal evaluation` |
| [market-partition](https://github.com/topprismdata/market-partition) | 结合智能体语义解释与视觉核验的确定性空间分区。 | `catalog` | `public real world data` |
| [bge-entity-match](https://github.com/topprismdata/bge-entity-match) | 面向企业规范世界模型的上下文业务实体解析。 | `catalog` | `internal evaluation` |
| [themed-street-engine](https://github.com/topprismdata/themed-street-engine) | 从 POI、路网与业务渠道信号中发现商业走廊。 | `catalog` | `public real world data` |
| [logistics-dispatch-clustering](https://github.com/topprismdata/logistics-dispatch-clustering) | 基于历史运营数据研究调度分组与司机序列偏好。 | `catalog` | `historical operational data` |
| [open-dispatch](https://github.com/topprismdata/open-dispatch) | 本地优先的配送路径与调度优化参考引擎。 | `catalog` | `none` |

### Decision Science

| Project | Summary | Status | Evidence |
| --- | --- | --- | --- |
| [agentic-warehouse-engine](https://github.com/topprismdata/agentic-warehouse-engine) | 面向变化需求下动态仓位配置的序贯专家路由研究。 | `catalog` | `none` |
| [fashion-lifecycle-pricing](https://github.com/topprismdata/fashion-lifecycle-pricing) | 面向时尚零售需求预测、生命周期状态与折扣优化的决策研究。 | `catalog` | `none` |

### Native AI

| Project | Summary | Status | Evidence |
| --- | --- | --- | --- |
| [three-layer-wisdom-extraction](https://github.com/topprismdata/three-layer-wisdom-extraction) | 将项目事件沉淀为领域知识与可迁移原则。 | `flagship` | `internal evaluation` |
| [topprismwiki](https://github.com/topprismdata/topprismwiki) | 面向企业智能体的证据治理型知识基础设施。 | `flagship` | `internal evaluation` |
| [cultivating-ml-agent](https://github.com/topprismdata/cultivating-ml-agent) | 通过跨项目知识结晶与技能复用持续积累能力的 ML 智能体。 | `catalog` | `internal use` |
| [agent-nurture-framework](https://github.com/topprismdata/agent-nurture-framework) | 将重复的智能体工作转化为可复用能力的方法框架。 | `catalog` | `internal use` |
| [skill-tester](https://github.com/topprismdata/skill-tester) | 面向可复用智能体技能的质量与触发评测门。 | `catalog` | `internal evaluation` |
| [notebook-knowledge-distillation](https://github.com/topprismdata/notebook-knowledge-distillation) | 将外部知识转化为经过验证的技能能力的来源到技能工作流。 | `catalog` | `internal evaluation` |
| [3-ai-debate](https://github.com/topprismdata/3-ai-debate) | 用于结构化审议的多模型第二意见工具。 | `catalog` | `internal use` |
| [hf-agents-skill](https://github.com/topprismdata/hf-agents-skill) | 为员工编码智能体提供本地与私有推理访问层。 | `catalog` | `internal use` |
| [auto-receipt](https://github.com/topprismdata/auto-receipt) | 用于票据识别与报销准备的 Native AI 员工技能。 | `catalog` | `internal evaluation` |

### Learning Projects

| Project | Summary | Status | Evidence |
| --- | --- | --- | --- |
| [kaggle-store-sales](https://github.com/topprismdata/kaggle-store-sales) | 使用公开时间序列竞赛作为训练场的 ML 智能体纵向学习项目。 | `catalog` | `kaggle benchmark` |
| [kaggle-ps-s6e4](https://github.com/topprismdata/kaggle-ps-s6e4) | 面向 Cultivating ML Agent 的表格分类学习项目。 | `catalog` | `kaggle benchmark` |

### Upstream Forks

| Project | Summary | Status | Evidence |
| --- | --- | --- | --- |
| [flint-chart](https://github.com/topprismdata/flint-chart) | 面向智能体生成图表的上游可视化语言参考。 | `catalog` | `none` |
| [autogluon](https://github.com/topprismdata/autogluon) | 为评测与 ML 工作流保留的 AutoML 参考与依赖。 | `catalog` | `none` |
| [autogluon-assistant](https://github.com/topprismdata/autogluon-assistant) | 为比较与评测保留的外部智能体 ML 架构参考。 | `catalog` | `none` |
| [knowledge-catalog](https://github.com/topprismdata/knowledge-catalog) | 为评测保留的知识系统实现参考。 | `catalog` | `none` |
| [ml-knowledge-graph](https://github.com/topprismdata/ml-knowledge-graph) | 为比较保留的机器学习知识图谱参考。 | `catalog` | `none` |
<!-- GENERATED:PORTFOLIO:END -->

## 如何阅读标签

- **Purpose / 用途**描述计划解决的问题类型，不是客户或产品声明。
- **Maturity / 成熟度**描述当前工程形态，不等同于商业成熟度。
- **Evidence / 证据**描述仓库中可检查的基础；除非明确说明，不代表外部验证。
- **Upstream Forks / 上游 Fork**用于依赖、比较或参考，不作为 TopPrism 原创能力展示。

## 登记表校验

在仓库根目录执行以下命令：

```bash
python3 -m pip install -r requirements.txt
python3 scripts/render_profile.py --check
python3 scripts/validate_profile.py
```

校验会检查登记表、明确的旗舰状态、最多六个拟同步 GitHub Pins、安全的本地资产引用，以及私有本地路径和明显密钥材料。

GitHub Pins 属于账号级界面状态。评审后的变更合并后，由账号所有者在 GitHub 主页手动更新，并可使用 `python3 scripts/report_pin_drift.py` 与登记表对比。

## 语言镜像

English portfolio: [PORTFOLIO.md](PORTFOLIO.md)
