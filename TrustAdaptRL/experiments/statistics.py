import argparse,pandas as pd
from trustadaptrl.metrics.evaluation import paired_stats
p=argparse.ArgumentParser(); p.add_argument('csv'); p.add_argument('--a',default='dqn'); p.add_argument('--b',default='qlearning'); p.add_argument('--metric',default='accuracy'); a=p.parse_args(); df=pd.read_csv(a.csv)
for ratio,g in df.groupby('malicious_ratio'):
    va=g[g.method==a.a].sort_values('seed')[a.metric].values; vb=g[g.method==a.b].sort_values('seed')[a.metric].values
    print(ratio,paired_stats(va,vb))
