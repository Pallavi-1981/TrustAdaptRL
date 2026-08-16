class TrustQoSRouter:
    def __init__(self,cfg): self.c=cfg['routing']
    def score(self,trust,qos,risk): return self.c['trust_weight']*trust+self.c['qos_weight']*qos-self.c['risk_weight']*risk
