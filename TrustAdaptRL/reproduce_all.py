from pathlib import Path
import copy, pandas as pd
from trustadaptrl.utils.config import load_config
from trustadaptrl.datasets.preprocessing import synthetic_traffic
from trustadaptrl.simulation.environment import FogIoTTrustEnv
from trustadaptrl.agents.qlearning_agent import QLearningAgent
from trustadaptrl.agents.dqn_agent import DQNAgent
from trustadaptrl.metrics.evaluation import classification, paired_stats

def run(method,cfg,seed,ratio,steps=120,max_devices=30):
    c=copy.deepcopy(cfg); c['attacks']['malicious_ratio']=ratio; traffic=synthetic_traffic(6000,seed); agent=QLearningAgent(c,seed) if method=='qlearning' else DQNAgent(c,seed); env=FogIoTTrustEnv(c,traffic,seed); df=env.run(agent,steps=steps,train=True,max_devices=max_devices); m=classification(df.true_malicious,df.pred_malicious); m.update(method=method,seed=seed,malicious_ratio=ratio,pdr=df.pdr.mean(),delay=df.delay_norm.mean(),reward=df.reward.mean()); return m

def main():
    cfg=load_config('configs/default.yaml'); rows=[]
    # Reproducible compact research run; increase steps/devices in config for full paper-scale experiments.
    for ratio in cfg['evaluation']['malicious_ratios']:
        for seed in cfg['evaluation']['seeds']:
            for method in ['qlearning','dqn']: rows.append(run(method,cfg,seed,ratio))
    out=Path('outputs/tables'); out.mkdir(parents=True,exist_ok=True); df=pd.DataFrame(rows); df.to_csv(out/'all_runs.csv',index=False)
    stats=[]
    for ratio in cfg['evaluation']['malicious_ratios']:
        q=df[(df.method=='qlearning')&(df.malicious_ratio==ratio)].sort_values('seed').accuracy.values; d=df[(df.method=='dqn')&(df.malicious_ratio==ratio)].sort_values('seed').accuracy.values; s=paired_stats(d,q); s['malicious_ratio']=ratio; s['comparison']='DQN-vs-Qlearning'; stats.append(s)
    pd.DataFrame(stats).to_csv(out/'paired_statistics.csv',index=False); print(df.groupby(['method','malicious_ratio'])[['accuracy','detection_rate','pdr','delay']].mean()); print('Saved outputs/tables/all_runs.csv and paired_statistics.csv')
if __name__=='__main__': main()
