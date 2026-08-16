from __future__ import annotations
import numpy as np, pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import IsolationForest

COMMON = ['packet_rate','byte_rate','mean_packet_size','flow_duration','inter_arrival','traffic_intensity']

class UnifiedTrafficPreprocessor:
    """Maps heterogeneous flow tables to a dataset-agnostic traffic representation."""
    def __init__(self, random_state=11):
        self.scaler = StandardScaler()
        self.detector = IsolationForest(n_estimators=100, contamination='auto', random_state=random_state)
        self.fitted = False

    def _numeric_projection(self, df:pd.DataFrame)->pd.DataFrame:
        num = df.select_dtypes(include=[np.number]).replace([np.inf,-np.inf], np.nan).fillna(0.0)
        if num.shape[1] == 0:
            raise ValueError('No numeric columns found in dataset.')
        arr = num.to_numpy(float)
        cols = []
        for i,name in enumerate(COMMON):
            src = arr[:, i % arr.shape[1]]
            if name == 'traffic_intensity': src = np.log1p(np.abs(src))
            cols.append(src)
        out = pd.DataFrame(np.column_stack(cols), columns=COMMON, index=df.index)
        return out

    def fit_transform(self, df:pd.DataFrame)->pd.DataFrame:
        out = self._numeric_projection(df)
        z = self.scaler.fit_transform(out)
        self.detector.fit(z)
        anomaly = -self.detector.decision_function(z)
        anomaly = (anomaly-anomaly.min())/(anomaly.max()-anomaly.min()+1e-9)
        out = pd.DataFrame(z, columns=COMMON, index=df.index)
        out['anomaly_score'] = anomaly
        self.fitted = True
        return out.reset_index(drop=True)

    def transform(self, df:pd.DataFrame)->pd.DataFrame:
        if not self.fitted: raise RuntimeError('Call fit_transform first.')
        out = self._numeric_projection(df)
        z = self.scaler.transform(out)
        anomaly = -self.detector.decision_function(z)
        anomaly = 1/(1+np.exp(-anomaly))
        out = pd.DataFrame(z, columns=COMMON, index=df.index)
        out['anomaly_score'] = anomaly
        return out.reset_index(drop=True)

def synthetic_traffic(n=10000, seed=11):
    rng=np.random.default_rng(seed)
    benign=rng.normal(size=(n,6))
    spikes=(rng.random(n)<0.2)[:,None]*rng.normal(2.5,1.0,size=(n,6))
    x=benign+spikes
    df=pd.DataFrame(x,columns=COMMON)
    df['anomaly_score']=np.clip((np.linalg.norm(x,axis=1)-1.5)/5,0,1)
    return df
