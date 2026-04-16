# Airport Infrastructure Analytics

> Data-driven analysis of military airport relocation and former-site redevelopment strategies

[![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)](https://python.org)
[![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)](LICENSE)

## Problem

Military airport relocations in South Korea create massive urban development opportunities (former-site land often exceeds 1M㎡). Current planning approaches underestimate spatial spillover effects on surrounding property values, transportation networks, and land use patterns.

## Solution

A quantitative framework combining:

1. **Difference-in-Differences (DID)** estimation of property value impacts
2. **Hedonic price modeling** with spatial lag for noise exposure valuation
3. **Transportation network analysis** for accessibility changes post-relocation
4. **Scenario simulation** for optimal land use mix in former-site development

## Research Background

Developed from direct experience as **ROKAF Civil Engineering Officer** managing runway repaving and hangar construction at Seoul Air Base, combined with doctoral research on urban spatial economics.

## Methods

```
Treatment Group: Properties within 5km buffer of airport boundary
Control Group:   Comparable properties outside noise contour zone
Time:            Pre-announcement → Post-relocation decision → Post-completion

DID Estimator:   δ = (Ȳ_treat,post - Ȳ_treat,pre) - (Ȳ_ctrl,post - Ȳ_ctrl,pre)
Spatial DID:     Incorporates spatial weight matrix for spillover effects
```

## Repository Structure

```
airport-infrastructure-analytics/
├── src/
│   ├── did_estimator.py        # DID with spatial extension
│   ├── hedonic_model.py        # Noise-adjusted hedonic pricing
│   ├── network_analysis.py     # Road network accessibility
│   └── scenario_builder.py     # Land use mix optimization
├── notebooks/
│   ├── 01_suwon_airbase_case.ipynb
│   ├── 02_property_value_did.ipynb
│   ├── 03_noise_contour_hedonic.ipynb
│   └── 04_redevelopment_scenarios.ipynb
├── data/
│   └── README.md
├── docs/
│   └── methodology.md
├── tests/
├── requirements.txt
└── LICENSE
```

## Quick Start

```bash
git clone https://github.com/DongsooJung/airport-infrastructure-analytics.git
cd airport-infrastructure-analytics
pip install -r requirements.txt
jupyter notebook notebooks/01_suwon_airbase_case.ipynb
```

## Key Findings

| Metric | Pre-Announcement | Post-Decision | Change |
|--------|-----------------|---------------|--------|
| Avg. Apt Price (treatment) | — | — | — |
| Avg. Apt Price (control) | — | — | — |
| DID Estimate | — | — | — |
| Noise Premium Reduction | — | — | — |

*Populated upon running with actual MOLIT transaction data.*

## References

- Nelson, J.P. (2004). Meta-analysis of airport noise and hedonic property values.
- Pope, D.G. & Pope, J.C. (2015). When Walmart comes to town: Always low housing prices?
- Korean Ministry of National Defense. Military Installation Relocation Plan.

## License

MIT License

## Author

**Dongsoo Jung** — ROKAF Civil Engineering Officer (Veteran) · SNU Ph.D. Candidate
