"""Warm-start cross-cluster transfer demonstration."""
from trustadaptrl.utils.config import load_config
from trustadaptrl.datasets.preprocessing import synthetic_traffic
from trustadaptrl.simulation.environment import FogIoTTrustEnv
from trustadaptrl.agents.dqn_agent import DQNAgent
from trustadaptrl.fog.hierarchical import CrossClusterTransfer
from trustadaptrl.metrics.evaluation import classification
cfg=load_config('configs/default.yaml'); traffic=synthetic_traffic(5000,11)
source=DQNAgent(cfg,11); src_env=FogIoTTrustEnv(cfg,traffic,11); src_env.run(source,steps=60,train=True,max_devices=30)
target=DQNAgent(cfg,99); CrossClusterTransfer.transfer(source,target); tgt_env=FogIoTTrustEnv(cfg,synthetic_traffic(5000,99),99); df=tgt_env.run(target,steps=30,train=False,max_devices=30)
print(classification(df.true_malicious,df.pred_malicious))
