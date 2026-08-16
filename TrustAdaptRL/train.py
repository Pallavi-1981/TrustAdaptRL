import argparse, json
from pathlib import Path
import pandas as pd
from trustadaptrl.utils.config import load_config
from trustadaptrl.utils.seed import set_seed
from trustadaptrl.datasets.preprocessing import synthetic_traffic, UnifiedTrafficPreprocessor
from trustadaptrl.datasets.loaders import load_table
from trustadaptrl.simulation.environment import FogIoTTrustEnv
from trustadaptrl.agents.qlearning_agent import QLearningAgent
from trustadaptrl.agents.dqn_agent import DQNAgent
from trustadaptrl.metrics.evaluation import classification

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('--config',default='configs/default.yaml'); ap.add_argument('--agent',choices=['qlearning','dqn'],default='qlearning'); ap.add_argument('--dataset'); ap.add_argument('--steps',type=int,default=100); ap.add_argument('--max-devices',type=int,default=40); ap.add_argument('--seed',type=int); args=ap.parse_args()
    cfg=load_config(args.config); seed=args.seed or cfg.get('seed',11); set_seed(seed)
    if args.dataset:
        raw=load_table(args.dataset); split=max(1,int(.7*len(raw))); p=UnifiedTrafficPreprocessor(seed); traffic=pd.concat([p.fit_transform(raw.iloc[:split]),p.transform(raw.iloc[split:])],ignore_index=True)
    else: traffic=synthetic_traffic(max(5000,args.steps*5),seed)
    agent=QLearningAgent(cfg,seed) if args.agent=='qlearning' else DQNAgent(cfg,seed)
    env=FogIoTTrustEnv(cfg,traffic,seed); df=env.run(agent,args.steps,train=True,max_devices=args.max_devices); out=Path('outputs'); out.mkdir(exist_ok=True); df.to_csv(out/f'{args.agent}_interaction_log.csv',index=False)
    m=classification(df['true_malicious'],df['pred_malicious']); print(json.dumps(m,indent=2)); print(f'Wrote {len(df):,} interaction records to {out}')
if __name__=='__main__': main()
