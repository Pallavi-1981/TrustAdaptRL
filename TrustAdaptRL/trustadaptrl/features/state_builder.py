import numpy as np
class StateBuilder:
    def __init__(self,cfg): self.cfg=cfg
    def build(self,src,nbr,neighbors_by_id,traffic,successes,drops,delay_norm):
        delta=self.cfg['state']['additive_smoothing']; B=(successes+delta)/(successes+drops+2*delta)
        raw_context=float(np.clip(1.0-0.55*delay_norm-0.25*abs(float(traffic.get('traffic_intensity',0)))/4,0,1))
        beta=self.cfg['state']['context_smoothing']; prev=src.context_smoothed.get(nbr.device_id,raw_context); C=beta*prev+(1-beta)*raw_context; src.context_smoothed[nbr.device_id]=C
        S=float(np.clip(traffic.get('anomaly_score',0.0),0,1))
        hist=src.reliability_history[nbr.device_id]; hist.append(B); w=self.cfg['state']['history_window']; arr=np.array(list(hist)[-w:],float)
        H=float(np.std(arr)) if len(arr)>1 else 0.0
        corrs=[]
        for k in neighbors_by_id:
            if k==nbr.device_id: continue
            h2=np.array(list(src.reliability_history[k])[-w:],float)
            m=min(len(arr),len(h2))
            if m>=3 and np.std(arr[-m:])>1e-8 and np.std(h2[-m:])>1e-8:
                c=np.corrcoef(arr[-m:],h2[-m:])[0,1]
                if np.isfinite(c): corrs.append(max(0.0,float(c)))
        rho=max(corrs) if corrs else 0.0
        return np.array([B,C,S,H,rho],dtype=np.float32)
