import numpy as np, networkx as nx
from .device import Device

class Topology:
    def __init__(self,cfg,seed=11):
        self.cfg=cfg; self.rng=np.random.default_rng(seed); self.devices=[]; self.graph=nx.Graph(); self._init_devices(); self.rebuild()
    def _init_devices(self):
        s=self.cfg['simulation']; C=s['clusters']; n=s['devices_per_cluster']; frac=s.get('mobility_fraction',0.5)
        did=0
        for c in range(C):
            for _ in range(n):
                self.devices.append(Device(did,c,float(self.rng.uniform(0,s['area_width'])),float(self.rng.uniform(0,s['area_height'])),bool(self.rng.random()<frac))); did+=1
    def rebuild(self):
        r=self.cfg['simulation']['communication_range']; self.graph=nx.Graph(); self.graph.add_nodes_from(range(len(self.devices)))
        by_cluster={}
        for d in self.devices: by_cluster.setdefault(d.cluster_id,[]).append(d)
        for arr in by_cluster.values():
            for a_i,a in enumerate(arr):
                for b in arr[a_i+1:]:
                    if np.linalg.norm(a.pos()-b.pos())<=r: self.graph.add_edge(a.device_id,b.device_id)
        # ensure isolated nodes have at least nearest cluster neighbour
        for d in self.devices:
            if self.graph.degree[d.device_id]==0:
                cand=[x for x in by_cluster[d.cluster_id] if x.device_id!=d.device_id]
                if cand:
                    b=min(cand,key=lambda x:np.linalg.norm(x.pos()-d.pos())); self.graph.add_edge(d.device_id,b.device_id)
    def neighbors(self,did): return list(self.graph.neighbors(did))
