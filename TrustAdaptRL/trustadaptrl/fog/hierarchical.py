from copy import deepcopy
class ExperienceAggregator:
    def __init__(self): self.experiences=[]
    def add(self,items): self.experiences.extend(items)
    def clear(self): self.experiences.clear()
class PolicySynchronizer:
    @staticmethod
    def snapshot(agent):
        if hasattr(agent,'online'): return deepcopy(agent.online.state_dict())
        return deepcopy(agent.Q)
    @staticmethod
    def load(agent,state):
        if hasattr(agent,'online'):
            agent.online.load_state_dict(state); agent.target.load_state_dict(state)
        else: agent.Q=deepcopy(state)
class CrossClusterTransfer:
    @staticmethod
    def transfer(source_agent,target_agent):
        PolicySynchronizer.load(target_agent,PolicySynchronizer.snapshot(source_agent)); return target_agent
