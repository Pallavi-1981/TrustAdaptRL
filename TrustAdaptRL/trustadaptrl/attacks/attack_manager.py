import numpy as np
class AttackManager:
    def __init__(self,cfg,seed=11): self.cfg=cfg; self.rng=np.random.default_rng(seed); self.malicious=set(); self.groups={}
    def assign(self,devices):
        ratio=self.cfg['attacks']['malicious_ratio']; n=int(round(len(devices)*ratio)); ids=self.rng.choice(len(devices),size=n,replace=False) if n else []
        self.malicious=set(map(int,ids)); kinds=['grayhole','onoff','collusion']
        coll=[]
        for idx,did in enumerate(sorted(self.malicious)):
            d=devices[did]; d.attack_type=kinds[idx%3]
            if d.attack_type=='collusion': coll.append(did)
        gmin=self.cfg['attacks']['collusion_group_min']; gmax=self.cfg['attacks']['collusion_group_max']; gid=0; i=0
        while i<len(coll):
            size=int(self.rng.integers(gmin,gmax+1)); grp=coll[i:i+size]
            if len(grp)>=2:
                self.groups[gid]=grp
                for did in grp: devices[did].collusion_group=gid
                gid+=1
            i+=size
    def update_states(self,devices,t):
        duty=self.cfg['attacks']['onoff_malicious_duty_cycle']
        for d in devices:
            if d.device_id not in self.malicious: d.attack_active=False; continue
            if d.attack_type=='grayhole': d.attack_active=True
            elif d.attack_type=='onoff': d.attack_active=((t//50)%2==0) if abs(duty-0.5)<1e-9 else ((t%100)<int(100*duty))
            else: d.attack_active=((t//75)%2==0)
    def should_drop(self,device):
        if not device.attack_active: return False
        if device.attack_type=='grayhole': p=self.cfg['attacks']['grayhole_drop_probability']
        elif device.attack_type=='onoff': p=0.7
        elif device.attack_type=='collusion': p=0.55
        else: p=0.0
        return bool(self.rng.random()<p)
