import pandas as pd, argparse
from trustadaptrl.metrics.evaluation import classification
p=argparse.ArgumentParser(); p.add_argument('csv'); a=p.parse_args(); df=pd.read_csv(a.csv)
for atk in ['grayhole','onoff','collusion']:
    sub=df[(df.attack_type==atk)|(df.true_malicious==0)]
    print(atk, classification(sub.true_malicious,sub.pred_malicious))
