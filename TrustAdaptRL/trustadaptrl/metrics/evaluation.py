import numpy as np
from sklearn.metrics import accuracy_score,precision_score,recall_score,f1_score,confusion_matrix
from scipy import stats

def classification(y_true,y_pred):
    y_true=np.asarray(y_true); y_pred=np.asarray(y_pred); tn,fp,fn,tp=confusion_matrix(y_true,y_pred,labels=[0,1]).ravel()
    return {'accuracy':accuracy_score(y_true,y_pred),'precision':precision_score(y_true,y_pred,zero_division=0),'recall':recall_score(y_true,y_pred,zero_division=0),'f1':f1_score(y_true,y_pred,zero_division=0),'fpr':fp/(fp+tn+1e-9),'fnr':fn/(fn+tp+1e-9),'detection_rate':tp/(tp+fn+1e-9)}
def convergence_time(trust,eps=.01,K=5):
    x=np.asarray(trust,float)
    for t in range(K,len(x)):
        if np.all(np.abs(np.diff(x[t-K:t+1]))<eps): return t
    return len(x)
def paired_stats(a,b):
    a=np.asarray(a,float); b=np.asarray(b,float); diff=a-b; sd=np.std(diff,ddof=1); dz=np.mean(diff)/(sd+1e-12); t=stats.ttest_rel(a,b)
    try: w=stats.wilcoxon(a,b)
    except ValueError: w=type('X',(object,),{'statistic':0.0,'pvalue':1.0})()
    ci=stats.t.interval(.95,len(a)-1,loc=np.mean(a),scale=stats.sem(a)) if len(a)>1 else (a[0],a[0])
    return {'mean':float(np.mean(a)),'sd':float(np.std(a,ddof=1)),'ci95_low':float(ci[0]),'ci95_high':float(ci[1]),'paired_t_p':float(t.pvalue),'wilcoxon_p':float(w.pvalue),'cohen_dz':float(dz)}
