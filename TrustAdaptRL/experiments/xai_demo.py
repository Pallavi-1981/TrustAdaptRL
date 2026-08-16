"""Small SHAP-ready DQN explanation demo using synthetic traffic."""
import numpy as np
from trustadaptrl.utils.config import load_config
from trustadaptrl.agents.dqn_agent import DQNAgent
from trustadaptrl.explainability.explainers import shap_dqn
cfg=load_config('configs/default.yaml'); agent=DQNAgent(cfg,11); bg=np.random.rand(20,5).astype('float32'); xs=np.random.rand(5,5).astype('float32'); print(type(shap_dqn(agent,bg,xs)))
