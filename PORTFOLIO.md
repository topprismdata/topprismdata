# TopPrism public portfolio

This page is the complete public catalog behind the [TopPrism profile](README.md). It distinguishes the two compounding pillars from learning projects and upstream references.

The catalog is rendered from [`portfolio/portfolio.yml`](portfolio/portfolio.yml). The registry is the source of truth for display order, bilingual summaries, purpose, maturity, evidence and the current reviewed flagship set. It is intentionally not a popularity ranking.

`flagship` means “currently selected for the profile homepage”, not “most important forever”. Any change to that set requires explicit review and a registry update; the renderer never promotes a repository automatically.

<!-- GENERATED:PORTFOLIO:START -->
### World Model & Decision

| Project | Summary | Status | Evidence |
| --- | --- | --- | --- |
| [visit-scheduling-optimizer](https://github.com/topprismdata/visit-scheduling-optimizer) | Data-calibrated decision engine for recurring field-sales visit scheduling. | `flagship` | `anonymized operational data` |
| [spatial-decision-intelligence](https://github.com/topprismdata/spatial-decision-intelligence) | Diagnose conflicts between business objectives and spatial constraints with explainable findings. | `catalog` | `internal evaluation` |
| [market-partition](https://github.com/topprismdata/market-partition) | Deterministic spatial partitioning with agentic semantic interpretation and visual verification. | `catalog` | `public real world data` |
| [bge-entity-match](https://github.com/topprismdata/bge-entity-match) | Contextual business-entity resolution for canonical enterprise world models. | `catalog` | `internal evaluation` |
| [themed-street-engine](https://github.com/topprismdata/themed-street-engine) | Discover commercial corridors from POI, road-network and business-channel signals. | `catalog` | `public real world data` |
| [logistics-dispatch-clustering](https://github.com/topprismdata/logistics-dispatch-clustering) | Applied research on dispatch grouping and driver sequence preferences from historical operations. | `catalog` | `historical operational data` |
| [open-dispatch](https://github.com/topprismdata/open-dispatch) | Local-first reference engine for delivery routing and dispatch optimization. | `catalog` | `none` |

### Decision Science

| Project | Summary | Status | Evidence |
| --- | --- | --- | --- |
| [agentic-warehouse-engine](https://github.com/topprismdata/agentic-warehouse-engine) | Research on sequential expert routing for dynamic warehouse slotting under changing demand. | `catalog` | `none` |
| [fashion-lifecycle-pricing](https://github.com/topprismdata/fashion-lifecycle-pricing) | Decision research for fashion demand forecasting, lifecycle state and markdown optimization. | `catalog` | `none` |

### Native AI

| Project | Summary | Status | Evidence |
| --- | --- | --- | --- |
| [three-layer-wisdom-extraction](https://github.com/topprismdata/three-layer-wisdom-extraction) | Promote project events into domain knowledge and transferable principles. | `flagship` | `internal evaluation` |
| [topprismwiki](https://github.com/topprismdata/topprismwiki) | Evidence-governed knowledge infrastructure for enterprise AI agents. | `flagship` | `internal evaluation` |
| [cultivating-ml-agent](https://github.com/topprismdata/cultivating-ml-agent) | A self-improving ML agent that compounds capability across projects. | `catalog` | `internal use` |
| [agent-nurture-framework](https://github.com/topprismdata/agent-nurture-framework) | A framework for turning repeated AI-agent work into reusable capability. | `catalog` | `internal use` |
| [skill-tester](https://github.com/topprismdata/skill-tester) | Quality and trigger-evaluation gate for reusable AI-agent skills. | `catalog` | `internal evaluation` |
| [notebook-knowledge-distillation](https://github.com/topprismdata/notebook-knowledge-distillation) | A source-to-skill workflow for converting external knowledge into validated capability. | `catalog` | `internal evaluation` |
| [3-ai-debate](https://github.com/topprismdata/3-ai-debate) | Multi-model second-opinion utility for structured deliberation. | `catalog` | `internal use` |
| [hf-agents-skill](https://github.com/topprismdata/hf-agents-skill) | Local and private inference access for employee coding agents. | `catalog` | `internal use` |
| [auto-receipt](https://github.com/topprismdata/auto-receipt) | Native AI employee skill for receipt recognition and reimbursement preparation. | `catalog` | `internal evaluation` |

### Learning Projects

| Project | Summary | Status | Evidence |
| --- | --- | --- | --- |
| [kaggle-store-sales](https://github.com/topprismdata/kaggle-store-sales) | Longitudinal learning project for an ML agent using a public time-series competition. | `catalog` | `kaggle benchmark` |
| [kaggle-ps-s6e4](https://github.com/topprismdata/kaggle-ps-s6e4) | Tabular-classification learning project for the Cultivating ML Agent. | `catalog` | `kaggle benchmark` |

### Upstream Forks

| Project | Summary | Status | Evidence |
| --- | --- | --- | --- |
| [flint-chart](https://github.com/topprismdata/flint-chart) | Upstream visualization-language reference for agent-generated charts. | `catalog` | `none` |
| [autogluon](https://github.com/topprismdata/autogluon) | AutoML reference and dependency retained for evaluation and ML workflows. | `catalog` | `none` |
| [autogluon-assistant](https://github.com/topprismdata/autogluon-assistant) | External agentic-ML architecture retained for comparison and evaluation. | `catalog` | `none` |
| [knowledge-catalog](https://github.com/topprismdata/knowledge-catalog) | Knowledge-system implementation reference retained for evaluation. | `catalog` | `none` |
| [ml-knowledge-graph](https://github.com/topprismdata/ml-knowledge-graph) | Machine-learning knowledge-graph reference retained for comparison. | `catalog` | `none` |
<!-- GENERATED:PORTFOLIO:END -->

## Reading the labels

- **Purpose** describes the intended problem family; it is not a customer or product claim.
- **Maturity** describes the current engineering form, not commercial readiness.
- **Evidence** describes the basis that can be inspected in the repository; it does not imply external validation unless explicitly stated.
- **Upstream Forks** are retained for dependency, comparison or reference. They are not presented as TopPrism originals.

## Registry checks

Run the following from the repository root before opening a pull request:

```bash
python3 -m pip install -r requirements.txt
python3 scripts/render_profile.py --check
python3 scripts/validate_profile.py
```

The checks enforce a valid registry, explicit flagship status, a maximum of six proposed GitHub pins, safe local asset references, and the absence of private local paths or obvious secret material.

GitHub Pins are account-level UI state. After a reviewed change is merged, the account owner can compare them with the registry using `python3 scripts/report_pin_drift.py`.

## Language mirror

中文项目组合：[PORTFOLIO.zh-CN.md](PORTFOLIO.zh-CN.md)
