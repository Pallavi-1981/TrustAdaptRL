import argparse, json, pandas as pd
from trustadaptrl.metrics.evaluation import classification
p=argparse.ArgumentParser(); p.add_argument('csv'); a=p.parse_args(); df=pd.read_csv(a.csv); print(json.dumps(classification(df.true_malicious,df.pred_malicious),indent=2))
