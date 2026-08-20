# TopPrism

**Decision intelligence for the physical business world.**

TopPrism builds two compounding systems: Customer Decision Intelligence and Native AI. This repository is the public index of what TopPrism works on and what its evidence layer shows.

---

## Customer Decision Intelligence

We model real business operations and turn complex states, constraints and objectives into computable decisions.

```text
Business World
        ↓
World Model
        ↓
Decision Engine
        ↓
Execution
        ↓
Outcome & Feedback
        └──────────────→ better next decision
```

**Representative capabilities**

- **Business World Modeling** — entities, spatial context, demand, resources, relations and constraints.
- **Decision Engines** — market design, territory, visit planning, routing, warehouse decisions and other optimization problems.
- **Open Evidence** — anonymized operational studies, public real-world datasets, benchmarks and reproducible research.

### Spatial intelligence stack

The spatial repos form a deliberate stack rather than a set of demos:

```
TopPrism AI Decision OS
          |
   Geo Intelligence
          |
Spatial Foundation  <- spatial-decision-intelligence
   |         |          |             |
Fence      Route      Store        Territory
Diagnosis  Optimization Potential  Planning
```

[`spatial-decision-intelligence`](https://github.com/topprismdata/spatial-decision-intelligence) diagnoses the foundation layer (coordinates, geometry, duplicates) *before* the optimization and planning engines above it consume the data.

### Public Decision / World Model projects

- [`visit-scheduling-optimizer`](https://github.com/topprismdata/visit-scheduling-optimizer) — periodic field-sales visit planning.
- [`agentic-warehouse-engine`](https://github.com/topprismdata/agentic-warehouse-engine) — decision-science research on dynamic warehouse reconfiguration.
- [`market-partition`](https://github.com/topprismdata/market-partition) — deterministic spatial partitioning with agentic interpretation and verification.
- [`bge-entity-match`](https://github.com/topprismdata/bge-entity-match) — business entity resolution engine.
- [`spatial-decision-intelligence`](https://github.com/topprismdata/spatial-decision-intelligence) — spatial decision diagnosis engine: conflicts between business objectives and spatial constraints, with explainable findings and zero auto-merge. First scenario: geofence diagnosis.
- [`themed-street-engine`](https://github.com/topprismdata/themed-street-engine) — discovering commercial corridors from POI and road-network signals.
- [`logistics-dispatch-clustering`](https://github.com/topprismdata/logistics-dispatch-clustering) — learning dispatch grouping and driver sequence preferences.
- [`open-dispatch`](https://github.com/topprismdata/open-dispatch) — local-first reference engine for delivery routing and dispatch optimization.
- [`fashion-lifecycle-pricing`](https://github.com/topprismdata/fashion-lifecycle-pricing) — decision research on demand forecasting and markdown optimization.

---

## Native AI

We also use AI to improve how TopPrism itself learns and works.

```text
Project
   ↓
Experience
   ↓
Knowledge
   ↓
Reusable Skill
   ↓
Better Agent
   ↓
Next Project starts from a higher baseline
```

**Representative capabilities**

- [`cultivating-ml-agent`](https://github.com/topprismdata/cultivating-ml-agent) — an ML agent that compounds capability across projects.
- [`agent-nurture-framework`](https://github.com/topprismdata/agent-nurture-framework) — methodology for turning repeated AI-agent work into reusable skills.
- [`skill-tester`](https://github.com/topprismdata/skill-tester) — quality and trigger-evaluation gate for reusable agent skills.
- [`notebook-knowledge-distillation`](https://github.com/topprismdata/notebook-knowledge-distillation) — source-to-skill workflow for converting external knowledge into validated capability.
- [`three-layer-wisdom-extraction`](https://github.com/topprismdata/three-layer-wisdom-extraction) — promoting project events into domain knowledge and transferable principles.
- [`3-ai-debate`](https://github.com/topprismdata/3-ai-debate) — multi-model second-opinion utility for structured deliberation.
- [`hf-agents-skill`](https://github.com/topprismdata/hf-agents-skill) — local/private inference access layer for employee coding agents.
- [`auto-receipt`](https://github.com/topprismdata/auto-receipt) — Native AI employee skill for receipt recognition and reimbursement workflows.

---

## Why Decision Science, Learning Projects, and Upstream Forks also exist

TopPrism's public GitHub is not a flat catalog of customer products. It is the engineering evidence layer behind the two compounding systems above. Three other categories are explicitly labeled so they strengthen rather than blur the story:

- **Decision Science** — `agentic-warehouse-engine`, `fashion-lifecycle-pricing` — research into decision models, optimization, simulation or theory.
- **Learning Projects** — `kaggle-store-sales`, `kaggle-ps-s6e4` — capability-formation cases; explicitly *not* a customer product.
- **Upstream Forks** — `flint-chart`, `autogluon`, `autogluon-assistant`, `knowledge-catalog`, `ml-knowledge-graph` — upstream code retained for evaluation, dependency or reference.

These forks are not presented as TopPrism originals. Each carries a `TOPPRISM_NOTES.md` declaring upstream, relationship to TopPrism, and any TopPrism-specific modifications.

---

## How to read our repositories

Every original TopPrism repository declares:

**Purpose** — `customer-decision` / `world-model` / `native-ai` / `decision-science` / `learning-project` / `upstream-fork`

**Maturity** — `production` / `applied` / `real-data-validated` / `research` / `framework` / `internal-utility` / `learning` / `reference`

**Evidence** — `customer-production` / `customer-pilot` / `anonymized-operational-data` / `historical-operational-data` / `public-real-world-data` / `benchmark` / `kaggle-benchmark` / `internal-evaluation` / `internal-use` / `none`

Technical evidence is deliberately separated from commercial maturity. A real-data research result is not presented as a production deployment, and an internal evaluation is not presented as an external benchmark.

---

## Contact

TopPrism Data

Public company site: [topprismdata.com](https://www.topprismdata.com/) (currently in development)

Public technical contact for engineering / GitHub matters should route through the company contact channel rather than personal addresses.

---

## License

The contents of this profile repository are released under the MIT License — see [`LICENSE`](LICENSE).
