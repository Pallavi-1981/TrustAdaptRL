import numpy as np
class StaticWeightedTrust:
    name='SWT'
    def predict(self,B,C,S,H,rho): return float(np.clip(0.65*B+0.25*C+0.10*(1-S),0,1))
class BetaReputationTrust:
    name='BRT'
    def __init__(self): self.ab={}
    def update(self,key,successes,drops):
        a,b=self.ab.get(key,(1.,1.)); a+=successes; b+=drops; self.ab[key]=(a,b); return a/(a+b)
class DempsterShaferTrust:
    name='DST'
    def predict(self,B,C,S,H,rho): return float(np.clip((B*(1-S)+C)/2,0,1))
class AnomalyThresholdTrust:
    name='ADT'
    def __init__(self,threshold=.5): self.threshold=threshold
    def predict(self,B,C,S,H,rho): return 0.25 if S>=self.threshold else float(np.clip(.7*B+.3*C,0,1))
class QoSOnlyRouting:
    name='QoSR'
    def score(self,qos): return float(qos)
class EigenTrustLite:
    name='ET'
    @staticmethod
    def global_trust(local):
        M=np.maximum(np.asarray(local,float),0); row=M.sum(1,keepdims=True); M=np.divide(M,row,where=row>0,out=np.ones_like(M)/max(1,M.shape[1])); v=np.ones(M.shape[0])/M.shape[0]
        for _ in range(50): v=M.T@v; v=v/(v.sum()+1e-9)
        return v
