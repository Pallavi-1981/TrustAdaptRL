from __future__ import annotations
import numpy as np, pandas as pd
from .topology import Topology
from .mobility import RandomWaypointLite
from ..attacks.attack_manager import AttackManager
from ..features.state_builder import StateBuilder
from ..rewards.attack_aware_reward import AttackAwareReward
from ..routing.trust_qos_router import TrustQoSRouter
from ..datasets.traffic_replay import TrafficReplay

class FogIoTTrustEnv:
    ACTION_DELTA={0:-1,1:0,2:1}
    def __init__(self,cfg,traffic_frame,seed=11):
        self.cfg=cfg; self.seed=seed; self.rng=np.random.default_rng(seed); self.topology=Topology(cfg,seed); self.mobility=RandomWaypointLite(cfg,seed+1); self.attacks=AttackManager(cfg,seed+2); self.attacks.assign(self.topology.devices); self.state_builder=StateBuilder(cfg); self.rewarder=AttackAwareReward(cfg); self.router=TrustQoSRouter(cfg); self.replay=TrafficReplay(traffic_frame,seed+3); self.t=0; self.logs=[]
        init=cfg['state']['initial_trust']
        for d in self.topology.devices:
            for n in self.topology.neighbors(d.device_id): d.trust[n]=init
    def _interaction(self,src,nbr,traffic):
        attempts=10; drops=0; successes=0
        congestion=np.clip(abs(float(traffic.get('traffic_intensity',0)))/5,0,0.5); base_drop=0.02+0.08*congestion
        for _ in range(attempts):
            malicious=self.attacks.should_drop(nbr); benign=self.rng.random()<base_drop
            if malicious or benign: drops+=1
            else: successes+=1
        pdr=successes/attempts; delay_norm=float(np.clip(0.05+0.5*congestion+0.25*(1-pdr)+self.rng.normal(0,0.03),0,1)); qos=float(np.clip(0.7*pdr+0.3*(1-delay_norm),0,1))
        return successes,drops,pdr,delay_norm,qos
    def step_with_agent(self,agent,train=True,max_devices=None):
        self.attacks.update_states(self.topology.devices,self.t)
        if self.t>0 and self.t%10==0: self.mobility.step(self.topology.devices); self.topology.rebuild()
        traffic=self.replay.next_window(); records=[]; devices=self.topology.devices[:max_devices] if max_devices else self.topology.devices
        for src in devices:
            nbr_ids=self.topology.neighbors(src.device_id)
            if not nbr_ids: continue
            cand=[]
            for nid in nbr_ids:
                nbr=self.topology.devices[nid]; successes,drops,pdr,delay,qos=self._interaction(src,nbr,traffic); state=self.state_builder.build(src,nbr,nbr_ids,traffic,successes,drops,delay); a=agent.act(state,explore=train); old=src.trust.get(nid,self.cfg['state']['initial_trust']); delta=self.cfg['state']['trust_delta']*self.ACTION_DELTA[a]; new=float(np.clip(old+delta,0,1)); src.trust[nid]=new
                hist=list(src.reliability_history[nid]); expected=float(np.mean(hist[:-1])) if len(hist)>1 else float(state[0]); reward,parts=self.rewarder.compute(state,pdr,delay,expected); ns=state.copy(); ns[0]=float(np.clip(state[0]+self.rng.normal(0,.02),0,1))
                if hasattr(agent,'remember'): agent.remember(state,a,reward,ns,False)
                elif train: agent.update(state,a,reward,ns,False)
                risk=float(np.clip(0.7*state[2]+0.3*state[4],0,1)); score=self.router.score(new,qos,risk); cand.append((score,nid))
                true_mal=int(nbr.attack_active); pred_mal=int(new<self.cfg['state']['trusted_threshold'])
                rec={'t':self.t,'src':src.device_id,'nbr':nid,'cluster':src.cluster_id,'attack_type':nbr.attack_type,'attack_active':true_mal,'B':float(state[0]),'C':float(state[1]),'S':float(state[2]),'H':float(state[3]),'rho':float(state[4]),'trust_before':old,'action':a,'trust_after':new,'pdr':pdr,'delay_norm':delay,'qos':qos,'reward':reward,'reward_base':parts['base'],'gray_penalty':parts['gray'],'onoff_penalty':parts['onoff'],'collusion_penalty':parts['collusion'],'pred_malicious':pred_mal,'true_malicious':true_mal,'route_score':score}
                records.append(rec)
            if cand:
                best=max(cand)[1]
                for r in records[-len(cand):]: r['selected_next_hop']=best
        if train and hasattr(agent,'train_step'):
            for _ in range(max(1,self.cfg['fog']['train_updates_per_sync']//10)): agent.train_step()
        self.t+=1; self.logs.extend(records); return records
    def run(self,agent,steps=None,train=True,max_devices=None):
        n=steps or self.cfg['simulation']['episode_steps']
        for _ in range(n): self.step_with_agent(agent,train=train,max_devices=max_devices)
        return pd.DataFrame(self.logs)
