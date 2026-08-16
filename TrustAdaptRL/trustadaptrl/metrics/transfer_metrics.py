def retraining_reduction(n_scratch,n_transfer): return 100.0*(n_scratch-n_transfer)/max(1,n_scratch)
