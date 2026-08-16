import numpy as np
class TrafficReplay:
    def __init__(self, frame, seed=11):
        self.frame=frame.reset_index(drop=True); self.rng=np.random.default_rng(seed); self.i=0
    def next_window(self):
        if len(self.frame)==0: raise ValueError('Empty traffic frame')
        row=self.frame.iloc[self.i % len(self.frame)]; self.i+=1
        vals=row.to_dict()
        return {k:float(v) for k,v in vals.items() if np.isscalar(v)}
