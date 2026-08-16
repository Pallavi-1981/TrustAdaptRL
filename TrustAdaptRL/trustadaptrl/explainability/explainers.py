import numpy as np
FEATURES=['B','C','S','H','rho']
def explain_qtable(agent,state,action,reward_components,trust_before,trust_after):
    return {'state':dict(zip(FEATURES,map(float,state))),'q_values':agent.values(state).astype(float).tolist(),'selected_action':int(action),'reward_components':{k:float(v) for k,v in reward_components.items()},'trust_before':float(trust_before),'trust_after':float(trust_after)}
def shap_dqn(agent,background,samples):
    try:
        import shap, torch
        model=agent.online; model.eval(); bg=torch.tensor(np.asarray(background),dtype=torch.float32); xs=torch.tensor(np.asarray(samples),dtype=torch.float32); exp=shap.DeepExplainer(model,bg); return exp.shap_values(xs)
    except Exception as e:
        return {'warning':f'SHAP unavailable or failed: {e}'}
