# Implementation Manifest

This repository maps the manuscript's implementation plan to executable modules.

1. Public traffic preparation: `trustadaptrl/datasets/`
2. Dynamic clustered Fog-IoT topology and mobility: `trustadaptrl/simulation/`
3. Grayhole/on-off/collusion plus advanced robustness helpers: `trustadaptrl/attacks/`
4. Five-part state construction `[B,C,S,H,rho]`: `trustadaptrl/features/state_builder.py`
5. Attack-aware reward: `trustadaptrl/rewards/attack_aware_reward.py`
6. Q-learning/DQN: `trustadaptrl/agents/`
7. Trust-QoS-security next-hop routing: `trustadaptrl/routing/`
8. Fog policy synchronization and transfer: `trustadaptrl/fog/`
9. Baselines: `trustadaptrl/baselines/`
10. Explainability: `trustadaptrl/explainability/`
11. Metrics/statistics/efficiency: `trustadaptrl/metrics/`
12. Reproduction and experiment scripts: `experiments/`, `train.py`, `reproduce_all.py`

The code intentionally includes a synthetic-traffic fallback so it is functional immediately. Real TON_IoT, BoT-IoT, or IoT-23 tabular exports can be passed through `--dataset` without changing the simulator-ground-truth logic.
