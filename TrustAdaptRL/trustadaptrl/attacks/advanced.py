import numpy as np
class RewardPoisoner:
    def __init__(self,rate=0.1,mode='flip',seed=11): self.rate=rate; self.mode=mode; self.rng=np.random.default_rng(seed)
    def apply(self,r):
        if self.rng.random()>=self.rate: return r
        if self.mode=='flip': return -float(r)
        return float(r+self.rng.normal(0,0.5))
class AdaptiveGrayholeController:
    def __init__(self,low=.20,high=.60,trust_threshold=.5): self.low=low; self.high=high; self.th=trust_threshold
    def drop_probability(self,trust): return self.low if trust<self.th else self.high
class CoordinatedSchedule:
    def __init__(self,period=100,duty=.5): self.period=period; self.duty=duty
    def active(self,t): return (t%self.period)<int(self.period*self.duty)
