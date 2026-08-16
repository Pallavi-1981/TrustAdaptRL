from trustadaptrl.utils.config import load_config
from trustadaptrl.datasets.preprocessing import synthetic_traffic
from trustadaptrl.simulation.environment import FogIoTTrustEnv
from trustadaptrl.agents.qlearning_agent import QLearningAgent

def test_smoke():
    cfg=load_config('configs/default.yaml'); env=FogIoTTrustEnv(cfg,synthetic_traffic(1000,11),11); agent=QLearningAgent(cfg,11); df=env.run(agent,steps=3,train=True,max_devices=5); assert len(df)>0; assert {'B','C','S','H','rho','reward','trust_after'}.issubset(df.columns)
