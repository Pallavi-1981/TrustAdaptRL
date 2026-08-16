from dataclasses import dataclass, field
from collections import defaultdict, deque
import numpy as np

@dataclass
class Device:
    device_id:int
    cluster_id:int
    x:float
    y:float
    mobile:bool=True
    trust:dict=field(default_factory=dict)
    reliability_history:dict=field(default_factory=lambda:defaultdict(lambda:deque(maxlen=50)))
    context_smoothed:dict=field(default_factory=dict)
    attack_type:str='none'
    attack_active:bool=False
    collusion_group:int|None=None
    def pos(self): return np.array([self.x,self.y],dtype=float)
