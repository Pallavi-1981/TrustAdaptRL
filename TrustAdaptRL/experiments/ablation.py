"""Feature/reward ablation helper. Uses logged interactions to derive simple diagnostic summaries."""
import pandas as pd, argparse
p=argparse.ArgumentParser(); p.add_argument('csv'); a=p.parse_args(); df=pd.read_csv(a.csv)
for f in ['B','C','S','H','rho']:
    print(f, 'corr_with_true_malicious=', round(df[f].corr(df.true_malicious),4))
