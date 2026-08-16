import numpy as np
class AttackAwareReward:
    def __init__(self,cfg): self.c=cfg['reward']
    def compute(self,state,pdr,delay_norm,expected_B=None):
        B,C,S,H,rho=map(float,state); expected=B if expected_B is None else expected_B
        base=self.c['qos_pdr_weight']*pdr-self.c['qos_delay_weight']*delay_norm
        pgray=max(0.0,expected-B-self.c['tau_gray'])
        pon=max(0.0,H-self.c['tau_onoff'])
        pcoll=max(0.0,rho-self.c['tau_collusion'])*S
        adv=self.c['gray_weight']*pgray+self.c['onoff_weight']*pon+self.c['collusion_weight']*pcoll
        return float(base-adv), {'base':base,'gray':pgray,'onoff':pon,'collusion':pcoll,'adv':adv}
