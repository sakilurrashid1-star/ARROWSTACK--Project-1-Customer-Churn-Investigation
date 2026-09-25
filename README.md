# Arrowstack Project 1 — Customer Churn Investigation

**Intern:** Alkamah Sakilur Rashid  
**Project:** Customer Churn Investigation  
**Status:** Complete — reproducible, reviewable submission package

## Executive Summary
This project investigates churn in a **synthetic subscription dataset** created for the Arrowstack assignment. The workflow covers stakeholder framing, data validation, business-question EDA, evidence-based insights, limitations and a professional handoff.

**Dataset:** 1,200 synthetic subscriptions  
**Churned:** 539  
**Overall churn:** 44.9%

### Headline findings
- Month-to-month churn: **74.6%**
- One-year churn: **34.1%**
- Two-year churn: **25.7%**
- Satisfaction 1–2 churn: **68.8%**
- Satisfaction 3 churn: **51%**
- Satisfaction 4–5 churn: **32.8%**
- Autopay Yes churn: **39.6%**
- Autopay No churn: **49.9%**

These are descriptive results from simulated data, not causal estimates and not evidence about any real customer population.

## Repository Structure
~~~
.
├── data/
│   ├── customer_churn_simulated.csv
│   └── README.md
├── docs/
│   ├── data_dictionary.md
│   ├── decision_log.md
│   ├── requirements.md
│   └── validation_report.md
├── notebooks/
│   └── 01_customer_churn_investigation.ipynb
├── presentation/
│   └── final_presentation.md
├── src/
│   └── generate_dataset.py
├── requirements.txt
└── README.md
~~~

## Business Problem
**Stakeholder:** subscription/customer-success manager.

**Decision enabled:** identify customer segments and operational signals that warrant retention investigation.

**Scope:** descriptive and diagnostic analysis only. No automated individual decisions and no causal claims.

## Data Quality
- 0 duplicate customer IDs
- 0 missing values
- 0 invalid satisfaction values
- 0 invalid churn labels

Executable checks are in the notebook; the written evidence is in docs/validation_report.md.

## Investigation Segment
A transparent descriptive segment is defined as:
**month-to-month + at least 3 support tickets + satisfaction <= 3**

Segment size: **115 records (9.6%)**.

This is an investigation lens, not a customer-treatment rule.

## Limitations
1. The dataset is synthetic.
2. Simulation design can create associations by construction.
3. No causal inference or real-world benchmark is available.
4. Production use requires authorized data, lineage, privacy controls and appropriate governance.

## Next Steps
1. Validate on authorized production data.
2. Add cohort/time-based retention analysis.
3. Test retention interventions with measurable outcomes.
4. Add monitoring for schema drift and changing churn rates.
5. Review privacy/fairness before operational use.

## Reproduce
~~~bash
python -m venv .venv
# Windows: .venv\Scripts\activate
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
jupyter notebook notebooks/01_customer_churn_investigation.ipynb
~~~

## Arrowstack Requirement Mapping
| Requirement | Evidence |
|---|---|
| Data dictionary | docs/data_dictionary.md |
| Cleaning & quality checks | notebook + docs/validation_report.md |
| EDA with business questions | notebook |
| Evidence-based insights | README + notebook |
| Limitations & next steps | README + notebook |
| Requirements | docs/requirements.md |
| Traceable decisions | docs/decision_log.md |
| Final presentation | presentation/final_presentation.md |

## Author
**Alkamah Sakilur Rashid**  
Arrowstack Data Science Internship
