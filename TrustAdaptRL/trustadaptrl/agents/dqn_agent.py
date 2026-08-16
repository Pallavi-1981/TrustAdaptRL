from collections import deque
import random, numpy as np, torch
from torch import nn
class Net(nn.Module):
    def __init__(self,h):
        super().__init__(); dims=[5]+list(h)+[3]; layers=[]
        for a,b in zip(dims[:-2],dims[1:-1]): layers += [nn.Linear(a,b),nn.ReLU()]
        layers += [nn.Linear(dims[-2],dims[-1])]; self.net=nn.Sequential(*layers)
    def forward(self,x): return self.net(x)
class DQNAgent:
    def __init__(self,cfg,seed=11):
        c=cfg['dqn']; torch.manual_seed(seed); random.seed(seed); np.random.seed(seed); self.gamma=c['gamma']; self.batch=c['batch_size']; self.capacity=c['replay_capacity']; self.target_update=c['target_update']; self.eps=c['epsilon_start']; self.eps_min=c['epsilon_min']; self.decay=c['epsilon_decay']; self.online=Net(c['hidden_layers']); self.target=Net(c['hidden_layers']); self.target.load_state_dict(self.online.state_dict()); self.opt=torch.optim.Adam(self.online.parameters(),lr=c['learning_rate']); self.buf=deque(maxlen=self.capacity); self.steps=0
    def act(self,s,explore=True):
        if explore and random.random()<self.eps: return random.randrange(3)
        with torch.no_grad(): return int(self.online(torch.tensor(s,dtype=torch.float32).unsqueeze(0)).argmax(1).item())
    def remember(self,*tr): self.buf.append(tuple(tr))
    def train_step(self):
        if len(self.buf)<self.batch: return None
        batch=random.sample(self.buf,self.batch); s,a,r,ns,d=map(np.array,zip(*batch)); st=torch.tensor(s,dtype=torch.float32); nst=torch.tensor(ns,dtype=torch.float32); at=torch.tensor(a,dtype=torch.long); rt=torch.tensor(r,dtype=torch.float32); dt=torch.tensor(d,dtype=torch.float32)
        q=self.online(st).gather(1,at[:,None]).squeeze(1)
        with torch.no_grad(): y=rt+self.gamma*(1-dt)*self.target(nst).max(1).values
        loss=nn.functional.smooth_l1_loss(q,y); self.opt.zero_grad(); loss.backward(); nn.utils.clip_grad_norm_(self.online.parameters(),5.0); self.opt.step(); self.steps+=1
        if self.steps%self.target_update==0: self.target.load_state_dict(self.online.state_dict())
        self.eps=max(self.eps_min,self.eps*self.decay); return float(loss.item())
