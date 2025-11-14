# RTAx
RTAx: a reproducible, privacy-first red-team agent for LLMs w/ suite registry, policy gating, and reporting. This repo publishes contracts and diagrams only.

# RTAx — LLM Red Teaming Agent (Public Overview)

> **Tagline:** A reproducible, privacy-first red-team agent for LLMs—suite registry, policy gating, and reporting. This repo publishes contracts and diagrams only.

[![License](https://img.shields.io/badge/license-Apache--2.0-blue)](LICENSE)
[![Focus](https://img.shields.io/badge/focus-LLM%20Red%20Teaming-blue)]()
[![Privacy](https://img.shields.io/badge/privacy-protected-orange)]()
[![Status](https://img.shields.io/badge/status-active-brightgreen)]()

---

## TL;DR
- **What:** Modular framework to run curated adversarial suites against LLM systems, evaluate outcomes with a policy gate, and export human-readable safety reports.
- **Why:** Catch jailbreaks, prompt injection, and socio-technical risks early; standardize evidence without exposing sensitive internals.
- **How:** Contracts over internals — **Attacks** → **Gate/Eval** → **Report**. Internals are intentionally redacted.

> This public repo omits sensitive assets (prompt templates, provider configs, thresholds). See [`docs/REDACTIONS.md`](docs/REDACTIONS.md).

---

## Architecture (high-level)

```mermaid
flowchart LR
  subgraph User
    TUI[TUI] --- CLI[CLI]
  end

  subgraph Attacks
    Suites[Suite Registry<br/>(smoke/full/...)]
    Runner[Attack Runner<br/>(plugin)]
  end

  subgraph Eval["Eval / Policy Gate"]
    Gate[Policy Gate<br/>(category/severity)]
  end

  subgraph Artifacts
    Evt[events.jsonl]
    Met[metrics.json]
    Rpt[report/index.md]
  end

  User -->|run suite| Suites --> Runner --> Evt
  Evt --> Gate --> Met
  Met --> Rpt
  Evt --> Rpt
