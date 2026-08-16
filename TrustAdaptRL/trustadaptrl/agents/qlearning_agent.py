import numpy as np
class QLearningAgent:
    def __init__(self,cfg,seed=11):
        q=cfg['qlearning']; self.lr=q['learning_rate']; self.gamma=q['gamma']; self.eps=q['epsilon_start']; self.eps_min=q['epsilon_min']; self.decay=q['epsilon_decay']; self.bins=q.get('bins',3); self.rng=np.random.default_rng(seed); self.Q={}
    def key(self,s):
        x=np.clip(np.asarray(s,float),0,1); return tuple(np.minimum((x*self.bins).astype(int),self.bins-1))
    def values(self,s): return self.Q.setdefault(self.key(s),np.zeros(3,dtype=np.float32))
    def act(self,s,explore=True):
        if explore and self.rng.random()<self.eps: return int(self.rng.integers(0,3))
        return int(np.argmax(self.values(s)))
    def update(self,s,a,r,ns,done=False):
        q=self.values(s); target=r if done else r+self.gamma*np.max(self.values(ns)); q[a]+=self.lr*(target-q[a]); self.eps=max(self.eps_min,self.eps*self.decay)
