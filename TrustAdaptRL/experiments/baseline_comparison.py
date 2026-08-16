"""Run classical trust baselines on an existing TrustAdaptRL interaction log."""
import argparse,pandas as pd,numpy as np
from trustadaptrl.baselines.methods import StaticWeightedTrust,DempsterShaferTrust,AnomalyThresholdTrust,BetaReputationTrust
from trustadaptrl.metrics.evaluation import classification
p=argparse.ArgumentParser(); p.add_argument('csv'); p.add_argument('--threshold',type=float,default=.5); a=p.parse_args(); df=pd.read_csv(a.csv)
models=[StaticWeightedTrust(),DempsterShaferTrust(),AnomalyThresholdTrust()]
for m in models:
    t=np.array([m.predict(r.B,r.C,r.S,r.H,r.rho) for r in df.itertuples()]); pred=(t<a.threshold).astype(int); print(m.name,classification(df.true_malicious,pred))
br=BetaReputationTrust(); vals=[]
for r in df.itertuples(): vals.append(br.update((r.src,r.nbr),int(round(r.pdr*10)),int(round((1-r.pdr)*10))))
print('BRT',classification(df.true_malicious,(np.array(vals)<a.threshold).astype(int)))
