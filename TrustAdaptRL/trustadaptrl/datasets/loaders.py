from pathlib import Path
import pandas as pd

def load_table(path):
    p=Path(path)
    if p.suffix.lower()=='.csv': return pd.read_csv(p)
    if p.suffix.lower() in {'.parquet','.pq'}: return pd.read_parquet(p)
    if p.suffix.lower() in {'.pkl','.pickle'}: return pd.read_pickle(p)
    raise ValueError(f'Unsupported dataset format: {p.suffix}')

class TONIoTLoader: 
    def load(self,path): return load_table(path)
class BoTIoTLoader:
    def load(self,path): return load_table(path)
class IoT23Loader:
    def load(self,path): return load_table(path)
