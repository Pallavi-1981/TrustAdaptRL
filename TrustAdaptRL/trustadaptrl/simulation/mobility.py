import numpy as np
class RandomWaypointLite:
    def __init__(self,cfg,seed=11): self.cfg=cfg; self.rng=np.random.default_rng(seed)
    def step(self,devices):
        s=self.cfg['simulation']; m=self.cfg['mobility']
        for d in devices:
            if not d.mobile: continue
            speed=float(self.rng.uniform(m['min_speed'],m['max_speed'])); ang=float(self.rng.uniform(0,2*np.pi))
            d.x=float(np.clip(d.x+speed*np.cos(ang),0,s['area_width'])); d.y=float(np.clip(d.y+speed*np.sin(ang),0,s['area_height']))
