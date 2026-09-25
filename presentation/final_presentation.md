# Customer Churn Investigation — Final Presentation

## Slide 1 — Title
**Customer Churn Investigation**  
Arrowstack Data Science Internship — Project 1  
Alkamah Sakilur Rashid

## Slide 2 — Business Context
- Stakeholder: Customer Success / Retention
- Problem: understand where churn is concentrated
- Decision: prioritize segments for retention investigation
- Scope: descriptive analysis of synthetic data

## Slide 3 — Dataset
- 1,200 synthetic subscription records
- 15 analytical fields
- No real customer PII
- Reproducible dataset design

## Slide 4 — Data Quality
- 0 duplicate customer IDs
- 0 missing values
- 0 invalid satisfaction scores
- 0 invalid churn labels
- Automated checks in notebook

## Slide 5 — Baseline
**44.9%** simulated churn rate.

This is the baseline for this synthetic dataset only.

## Slide 6 — Contract Pattern
| Contract | Churn |
|---|---:|
| Month-to-month | 74.6% |
| One year | 34.1% |
| Two year | 25.7% |

Descriptive association; not a causal estimate.

## Slide 7 — Satisfaction Pattern
| Satisfaction | Churn |
|---|---:|
| 1–2 | 68.8% |
| 3 | 51% |
| 4–5 | 32.8% |

Lower satisfaction bands show higher simulated churn.

## Slide 8 — Operational Signals
- Support-ticket volume is segmented and visualized.
- Late-payment behavior is included as a diagnostic feature.
- Autopay groups are compared descriptively.
- Tenure is examined as an early-lifecycle signal.

## Slide 9 — Investigation Segment
**Month-to-month + ≥3 support tickets + satisfaction ≤3**

115 records (9.6%).

Use: prioritize further investigation, not automatic customer treatment.

## Slide 10 — Limitations
- Synthetic data
- No causal inference
- No real-world benchmark
- Simulation relationships may be designed
- Production use requires authorized data and governance

## Slide 11 — Next Steps
1. Validate on authorized production data.
2. Add cohort/time retention analysis.
3. Test retention interventions with measurable outcomes.
4. Add monitoring and schema-drift checks.
5. Review privacy/fairness before operational use.

## Slide 12 — Handoff
Dataset + notebook + requirements + data dictionary + validation evidence + decision log + presentation.

**Core message:** the workflow is reproducible and evidence-backed, while conclusions remain appropriately limited to the simulated dataset.
