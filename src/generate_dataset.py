# Deterministic synthetic dataset generator for Arrowstack Project 1
import numpy as np
import pandas as pd
from pathlib import Path
SEED=20260925
N=1200
# The committed CSV is the canonical generated artifact. This script documents the simulation design.
def generate():
    rng=np.random.default_rng(SEED)
    plans=rng.choice(['Basic','Standard','Premium'],N); contracts=rng.choice(['Month-to-month','One year','Two year'],N)
    payments=rng.choice(['Electronic check','Mailed check','Bank transfer','Credit card'],N); regions=rng.choice(['North','South','East','West'],N)
    tenure=np.maximum(1,np.rint(rng.normal(18,12,N)).astype(int))
    monthly=np.where(plans=='Basic',rng.normal(34,5,N),np.where(plans=='Standard',rng.normal(58,7,N),rng.normal(86,9,N)))
    support=np.maximum(0,np.rint(rng.normal(np.where(contracts=='Month-to-month',2.2,1.1),1.7)).astype(int)); tech=np.maximum(0,np.rint(rng.normal(np.where(plans=='Basic',1.4,1.0),1.2)).astype(int))
    usage=np.maximum(2,np.rint(rng.normal(np.where(plans=='Premium',42,np.where(plans=='Standard',31,22)),9)).astype(int)); late=np.maximum(0,np.rint(rng.normal(np.where(contracts=='Month-to-month',1.3,.6),1.2)).astype(int))
    satisfaction=np.clip(np.round(rng.normal(3.4-.12*support-.16*tech-.08*late,.65),1),1,5); autopay=rng.choice(['Yes','No'],N)
    total=np.round(monthly*tenure*(.94+rng.random(N)*.10),2)
    score=-2.1+np.where(contracts=='Month-to-month',1.25,np.where(contracts=='One year',-.35,-.85))+.28*support+.34*tech+.38*late+np.where(satisfaction<=2,1,np.where(satisfaction<=3,.45,np.where(satisfaction>=4,-.55,0)))+np.where(tenure<=6,.8,np.where(tenure<=12,.3,np.where(tenure>=36,-.55,0)))+np.where(autopay=='No',.35,-.15)+np.where(monthly>=75,.25,0)
    churn=(rng.random(N)<1/(1+np.exp(-score))).astype(int)
    return pd.DataFrame({'customer_id':[f'CUST-{i:05d}' for i in range(1,N+1)],'tenure_months':tenure,'plan_type':plans,'monthly_charges':np.round(monthly,2),'total_charges':total,'contract_type':contracts,'payment_method':payments,'support_tickets':support,'tech_issues':tech,'usage_hours_month':usage,'late_payments':late,'satisfaction_score':satisfaction,'autopay':autopay,'region':regions,'churn':churn})
if __name__=='__main__':
    out=Path(__file__).resolve().parents[1]/'data'/'customer_churn_simulated.csv'; out.parent.mkdir(parents=True,exist_ok=True); generate().to_csv(out,index=False); print(out)
