# TrustAdaptRL

## TrustAdaptRL: Attack-Aware Trust, QoS, and Security Reinforcement Learning for Dynamic Fog-IoT Routing

TrustAdaptRL is a reinforcement-learning-based trust-aware routing framework designed for dynamic Fog-IoT environments. The framework integrates behavioural trust, contextual information, security/anomaly information, historical stability, and neighbour correlation into a compact state representation for adaptive next-hop decision-making.

The framework combines:

- Dynamic clustered Fog-IoT simulation
- Device mobility
- Trust-aware routing
- QoS-aware routing
- Security-aware routing
- Attack-aware reinforcement learning
- Q-learning
- Deep Q-Network (DQN)
- Grayhole attack modelling
- On-Off attack modelling
- Collusion attack modelling
- Advanced attack-robustness mechanisms
- Fog-level policy synchronization
- Cross-cluster knowledge transfer
- Explainable reinforcement learning
- Trust and routing baselines
- Statistical evaluation
- Computational efficiency analysis
- Public IoT traffic replay support
- Synthetic traffic generation
- Reproducible experiments

---

## 1. Overview

Modern Fog-IoT networks are dynamic, distributed, resource-constrained, and vulnerable to unreliable and malicious devices. Traditional routing mechanisms may not adequately adapt to changing node behaviour, mobility, Quality of Service (QoS), and coordinated attacks.

TrustAdaptRL addresses this problem by using reinforcement learning for adaptive trust management and routing decisions.

For device `i` evaluating neighbour `j` at time `t`, TrustAdaptRL constructs a five-dimensional state:

~~~text
s(i,j,t) = [B_ij(t), C_ij(t), S_ij(t), H_ij(t), ρ_ij(t)]
~~~

where:

~~~text
B = Behavioural Reliability
C = Contextual Information
S = Security / Anomaly Information
H = Historical Stability
ρ = Neighbour Correlation
~~~

The learned policy is combined with trust, QoS, and security risk to support adaptive next-hop routing.

---

## 2. Main Objective

The main objective of TrustAdaptRL is to develop an adaptive and attack-aware reinforcement-learning framework for secure and QoS-aware routing in dynamic Fog-IoT environments.

The framework aims to:

1. Model dynamic Fog-IoT network behaviour.
2. Represent neighbour trust using multiple behavioural and contextual features.
3. Detect and respond to malicious forwarding behaviour.
4. Adapt trust decisions using reinforcement learning.
5. Integrate QoS and security into routing decisions.
6. Improve resilience against Grayhole, On-Off, and Collusion attacks.
7. Support Fog-level policy learning.
8. Transfer learned knowledge between Fog clusters.
9. Provide explainability for learned decisions.
10. Compare the proposed approach with established trust and routing baselines.
11. Evaluate classification, convergence, statistical, and computational performance.

---

## 3. Key Features

~~~text
+---------------------------------------------------------------+
|                         TrustAdaptRL                          |
+---------------------------------------------------------------+
|                                                               |
| Dynamic Fog-IoT Simulation                                   |
|              |                                                |
|              v                                                |
| Device Mobility                                               |
|              |                                                |
|              v                                                |
| Attack Injection                                              |
|              |                                                |
|              v                                                |
| Trust / QoS / Security State Construction                     |
|              |                                                |
|              v                                                |
| Five-Dimensional State [B, C, S, H, ρ]                       |
|              |                                                |
|              v                                                |
| Attack-Aware Reward                                           |
|              |                                                |
|              v                                                |
| Reinforcement Learning                                        |
|          /           \                                        |
|         v             v                                       |
|   Q-Learning          DQN                                     |
|         \             /                                       |
|          v           v                                        |
| Trust-QoS-Security Routing                                    |
|              |                                                |
|              v                                                |
| Fog-Level Training                                             |
|              |                                                |
|              v                                                |
| Policy Synchronization                                        |
|              |                                                |
|              v                                                |
| Cross-Cluster Transfer                                        |
|              |                                                |
|              v                                                |
| Evaluation / Transfer / XAI / Statistical Analysis             |
|                                                               |
+---------------------------------------------------------------+
~~~

---

## 4. Framework Architecture

The complete TrustAdaptRL workflow is:

~~~text
                    Public IoT Traffic
                           |
                           v
              +-------------------------+
              | Dataset Loading /       |
              | Preprocessing           |
              +-------------------------+
                           |
                           v
              +-------------------------+
              | Dynamic Fog-IoT         |
              | Network Simulation      |
              +-------------------------+
                           |
                           v
              +-------------------------+
              | Mobility + Topology     |
              +-------------------------+
                           |
                           v
              +-------------------------+
              | Attack Manager          |
              | Grayhole / On-Off /     |
              | Collusion               |
              +-------------------------+
                           |
                           v
              +-------------------------+
              | State Builder           |
              | [B, C, S, H, ρ]        |
              +-------------------------+
                           |
                           v
              +-------------------------+
              | Attack-Aware Reward     |
              +-------------------------+
                           |
                           v
                 +-------------------+
                 | Reinforcement     |
                 | Learning          |
                 +-------------------+
                    /             \
                   v               v
            +-------------+   +-------------+
            | Q-Learning  |   | DQN         |
            +-------------+   +-------------+
                   \               /
                    \             /
                     v           v
              +-----------------------+
              | Trust-QoS-Security    |
              | Routing               |
              +-----------------------+
                           |
                           v
              +-----------------------+
              | Fog-Level Learning    |
              +-----------------------+
                           |
                           v
              +-----------------------+
              | Policy Synchronization|
              +-----------------------+
                           |
                           v
              +-----------------------+
              | Cross-Cluster Transfer|
              +-----------------------+
                           |
                           v
              +-----------------------+
              | Evaluation / XAI /    |
              | Statistical Analysis  |
              +-----------------------+
~~~

---

## 5. State Representation

For device `i` evaluating neighbour `j` at time `t`, TrustAdaptRL constructs a five-dimensional state.

~~~text
s(i,j,t) = [B_ij(t), C_ij(t), S_ij(t), H_ij(t), ρ_ij(t)]
~~~

The state consists of:

~~~text
+--------+-------------------------+--------------------------------------+
| Symbol | Feature                 | Description                          |
+--------+-------------------------+--------------------------------------+
| B      | Behavioural Reliability  | Forwarding reliability of neighbour |
| C      | Contextual Information   | Context-dependent information       |
| S      | Security / Anomaly       | Anomaly-related information         |
| H      | Historical Stability     | Historical reliability variation    |
| ρ      | Correlation              | Correlation with other neighbours   |
+--------+-------------------------+--------------------------------------+
~~~

### 5.1 Behavioural Reliability

Behavioural reliability represents the forwarding success and drop behaviour of the evaluated neighbour.

The state builder uses forwarding outcomes and smoothing mechanisms to obtain a stable reliability representation.

~~~text
B = Smoothed Forwarding Reliability
~~~

### 5.2 Contextual Information

The contextual component incorporates network conditions such as:

- Delay
- Traffic conditions
- Contextual observations

The default context smoothing parameter is:

~~~yaml
context_smoothing: 0.7
~~~

### 5.3 Security / Anomaly Information

The security component represents anomaly-related information.

The implementation uses the anomaly score as part of the state representation:

~~~text
S = clipped anomaly_score
~~~

### 5.4 Historical Stability

Historical stability represents variation in the neighbour's reliability over the observation history.

The implementation uses the standard deviation of the reliability history:

~~~text
H = std(reliability_history)
~~~

### 5.5 Neighbour Correlation

The correlation component represents relationships between the evaluated neighbour and other neighbouring devices.

The implementation derives a non-negative correlation-related feature from available neighbour information.

~~~text
ρ >= 0
~~~

This component is particularly relevant when analysing coordinated or collusive behaviour.

---

## 6. Reinforcement Learning Actions

TrustAdaptRL uses three trust adaptation actions:

~~~text
+--------+---------------------------+
| Action | Meaning                   |
+--------+---------------------------+
|   0    | Decrease Trust            |
|   1    | Maintain Trust            |
|   2    | Increase Trust            |
+--------+---------------------------+
~~~

The reinforcement-learning agent observes:

~~~text
[B, C, S, H, ρ]
~~~

and selects one of the three actions.

---

## 7. Trust Adaptation

The framework maintains an initial trust value:

~~~text
initial_trust = 0.5
~~~

The trust adaptation magnitude is:

~~~text
trust_delta = 0.05
~~~

The trusted threshold is:

~~~text
trusted_threshold = 0.5
~~~

The conceptual trust adaptation process is:

~~~text
Action 0
   |
   v
Decrease Trust

Action 1
   |
   v
Maintain Trust

Action 2
   |
   v
Increase Trust
~~~

The resulting trust value is used by the routing component.

---

## 8. Attack Models

TrustAdaptRL explicitly models:

1. Grayhole attacks
2. On-Off attacks
3. Collusion attacks

The framework also contains advanced robustness utilities for adaptive and coordinated malicious behaviours.

---

## 9. Grayhole Attack

A Grayhole node selectively drops packets rather than continuously behaving maliciously.

The configured Grayhole drop probability is:

~~~yaml
grayhole_drop_probability: 0.45
~~~

The corresponding reward weight is:

~~~yaml
gray_weight: 0.7
~~~

The Grayhole threshold is:

~~~yaml
tau_gray: 0.10
~~~

The attack-aware reward uses these parameters to penalize routing decisions affected by suspicious packet-dropping behaviour.

---

## 10. On-Off Attack

An On-Off attacker alternates between benign and malicious behaviour.

The configured malicious duty cycle is:

~~~yaml
onoff_malicious_duty_cycle: 0.50
~~~

The reward weight is:

~~~yaml
onoff_weight: 0.7
~~~

The threshold is:

~~~yaml
tau_onoff: 0.12
~~~

This allows the framework to evaluate whether adaptive trust can respond to intermittent malicious behaviour.

---

## 11. Collusion Attack

Collusion attacks involve groups of malicious devices that coordinate their behaviour.

The configured collusion group size is:

~~~yaml
collusion_group_min: 3
collusion_group_max: 5
~~~

The reward weight is:

~~~yaml
collusion_weight: 0.8
~~~

The threshold is:

~~~yaml
tau_collusion: 0.65
~~~

Neighbour correlation information supports the analysis of coordinated behaviour.

---

## 12. Advanced Attack-Robustness Components

Advanced attack mechanisms are implemented in:

~~~text
trustadaptrl/attacks/advanced.py
~~~

The implementation includes:

~~~text
RewardPoisoner
AdaptiveGrayholeController
CoordinatedSchedule
~~~

These components support experimentation with:

- Reward manipulation
- Adaptive Grayhole behaviour
- Coordinated malicious schedules
- More challenging attack conditions

---

## 13. Attack Manager

Attack assignment and dynamic attack behaviour are managed by:

~~~text
trustadaptrl/attacks/attack_manager.py
~~~

The attack manager:

1. Selects malicious devices.
2. Assigns attack categories.
3. Creates collusion groups.
4. Updates attack states.
5. Supports dynamic attack behaviour during simulation.

The default malicious-device ratio is:

~~~yaml
malicious_ratio: 0.20
~~~

---

## 14. Attack-Aware Reward

TrustAdaptRL uses an attack-aware reward instead of relying only on packet forwarding success.

The reward considers:

- Packet Delivery Ratio (PDR)
- Delay
- Grayhole behaviour
- On-Off behaviour
- Collusion behaviour

The reward configuration is:

~~~yaml
reward:
  qos_pdr_weight: 1.0
  qos_delay_weight: 0.35
  gray_weight: 0.7
  onoff_weight: 0.7
  collusion_weight: 0.8
  tau_gray: 0.10
  tau_onoff: 0.12
  tau_collusion: 0.65
~~~

The conceptual reward structure is:

~~~text
                  +------------------+
                  | Packet Delivery  |
                  | Ratio (PDR)      |
                  +------------------+
                           |
                           v
                  +------------------+
                  | Delay            |
                  +------------------+
                           |
                           v
        +------------------+------------------+
        |                  |                  |
        v                  v                  v
    Grayhole           On-Off            Collusion
     Penalty           Penalty             Penalty
        |                  |                  |
        +------------------+------------------+
                           |
                           v
                  Attack-Aware Reward
~~~

---

## 15. Reinforcement Learning Agents

TrustAdaptRL provides two reinforcement-learning agents:

~~~text
1. Q-Learning
2. Deep Q-Network (DQN)
~~~

Both agents use the same conceptual state representation and three trust adaptation actions.

---

## 16. Q-Learning Agent

Implementation:

~~~text
trustadaptrl/agents/qlearning_agent.py
~~~

The Q-learning agent uses:

- Discretized state representation
- Epsilon-greedy exploration
- Q-table
- Temporal-difference learning

Default configuration:

~~~yaml
qlearning:
  learning_rate: 0.10
  gamma: 0.95
  epsilon_start: 1.0
  epsilon_min: 0.05
  epsilon_decay: 0.995
  bins: 3
~~~

The five-dimensional continuous state is discretized into bins before being used by the Q-table.

---

## 17. Q-Learning Update

The Q-learning update is:

~~~text
Q(s,a) <- Q(s,a) +
          α [ r + γ max Q(s',a') - Q(s,a) ]
~~~

where:

~~~text
α = learning rate
γ = discount factor
r = reward
s = current state
a = selected action
s' = next state
~~~

---

## 18. Deep Q-Network

Implementation:

~~~text
trustadaptrl/agents/dqn_agent.py
~~~

The DQN uses a neural network to approximate the action-value function.

Default architecture:

~~~text
Input
  |
  v
5 State Features
  |
  v
64 neurons
  |
  v
64 neurons
  |
  v
32 neurons
  |
  v
3 Actions
~~~

Default configuration:

~~~yaml
dqn:
  learning_rate: 0.001
  gamma: 0.99
  batch_size: 32
  replay_capacity: 50000
  target_update: 20
  epsilon_start: 1.0
  epsilon_min: 0.05
  epsilon_decay: 0.995
  hidden_layers: [64, 64, 32]
~~~

The DQN implementation uses:

- PyTorch
- Experience replay
- Target network
- Epsilon-greedy exploration
- Mini-batch updates

---

## 19. Trust-QoS-Security Routing

The routing module is:

~~~text
trustadaptrl/routing/trust_qos_router.py
~~~

The routing score combines:

- Trust
- QoS
- Security risk

Default routing weights:

~~~yaml
routing:
  trust_weight: 0.5
  qos_weight: 0.35
  risk_weight: 0.15
~~~

The routing score is:

~~~text
Score =
    trust_weight × Trust
  + qos_weight × QoS
  - risk_weight × Risk
~~~

Therefore, a preferred neighbour should ideally provide:

~~~text
High Trust
    +
Good QoS
    +
Low Security Risk
~~~

---

## 20. Dynamic Fog-IoT Simulation

The simulation framework is implemented under:

~~~text
trustadaptrl/simulation/
~~~

The simulation components include:

~~~text
device.py
mobility.py
topology.py
environment.py
~~~

The environment models a clustered Fog-IoT network with configurable:

- Number of clusters
- Devices per cluster
- Area dimensions
- Communication range
- Episode length
- Observation window
- Mobility fraction

---

## 21. Default Simulation Configuration

~~~yaml
simulation:
  clusters: 5
  devices_per_cluster: 40
  area_width: 500.0
  area_height: 500.0
  communication_range: 100.0
  episode_steps: 1000
  observation_window: 10
  mobility_fraction: 0.5
~~~

This corresponds to:

~~~text
5 Fog clusters
40 devices per cluster
500 × 500 simulation area
100 communication range
1000 episode steps
10-step observation window
50% mobility fraction
~~~

---

## 22. Device Mobility

Mobility is implemented in:

~~~text
trustadaptrl/simulation/mobility.py
~~~

Default mobility configuration:

~~~yaml
mobility:
  min_speed: 0.5
  max_speed: 2.0
  pause_time: 5
~~~

The mobility model supports variable device movement with configurable speed and pause behaviour.

---

## 23. Fog-Level Learning

Fog-level learning is implemented in:

~~~text
trustadaptrl/fog/hierarchical.py
~~~

The main components include:

~~~text
ExperienceAggregator
PolicySynchronizer
CrossClusterTransfer
~~~

The workflow is:

~~~text
Local Device Experience
          |
          v
Fog Cluster
          |
          v
Experience Aggregation
          |
          v
Fog-Level Training
          |
          v
Policy Synchronization
          |
          v
Cross-Cluster Transfer
~~~

---

## 24. Policy Synchronization

Policy synchronization allows knowledge learned at Fog level to be shared across the hierarchical network.

Configuration:

~~~yaml
fog:
  sync_interval_windows: 20
  train_updates_per_sync: 20
~~~

The synchronization process is controlled by:

~~~text
Synchronization Interval
+
Training Updates per Synchronization
~~~

---

## 25. Cross-Cluster Transfer

The framework contains:

~~~text
CrossClusterTransfer
~~~

to support transfer of learned knowledge between Fog clusters.

Conceptually:

~~~text
Cluster A
   |
   | Learned Policy
   v
Knowledge Transfer
   |
   v
Cluster B
   |
   v
Adapted Local Policy
~~~

---

## 26. Dataset Support

TrustAdaptRL supports synthetic traffic and public IoT traffic.

The dataset module is:

~~~text
trustadaptrl/datasets/
~~~

It contains:

~~~text
loaders.py
preprocessing.py
traffic_replay.py
~~~

Supported tabular formats include:

~~~text
CSV
Parquet
Pickle
~~~

---

## 27. Supported Public IoT Dataset Interfaces

The repository provides loader interfaces for:

~~~text
TON-IoT
BoT-IoT
IoT-23
~~~

The corresponding loader classes include:

~~~text
TONIoTLoader
BoTIoTLoader
IoT23Loader
~~~

These loaders use the common table-loading interface.

---

## 28. Dataset Preprocessing

The preprocessing pipeline supports common traffic features such as:

~~~text
packet_rate
byte_rate
mean_packet_size
flow_duration
inter_arrival
traffic_intensity
~~~

The preprocessing workflow is:

~~~text
Raw Traffic
    |
    v
Common Feature Extraction
    |
    v
Numeric Projection
    |
    v
Standardization
    |
    v
Anomaly Detection
    |
    v
RL Environment
~~~

The implementation uses:

~~~text
StandardScaler
IsolationForest
~~~

---

## 29. Synthetic Traffic

The project includes a synthetic-traffic fallback.

This allows the framework to execute without first downloading a large public IoT dataset.

~~~text
No Dataset
     |
     v
Synthetic Traffic
     |
     v
Fog-IoT Environment
     |
     v
RL Training
~~~

---

## 30. Dataset Usage

A dataset can be passed to the training script using:

~~~bash
python train.py --dataset path/to/dataset.csv
~~~

The training pipeline performs a train/test-style split before fitting the preprocessing transformation.

The workflow is:

~~~text
Dataset
   |
   v
70% Training Portion
   |
   v
Fit Preprocessor
   |
   v
30% Evaluation Portion
   |
   v
Transform Using Training Preprocessor
~~~

---

## 31. Explainability

Explainability components are implemented under:

~~~text
trustadaptrl/explainability/
~~~

The framework provides explanation utilities for:

- Q-table decisions
- DQN decisions

The implementation includes:

~~~text
Q-table explanation
SHAP-based DQN explanation
~~~

The DQN explanation helper is:

~~~text
shap_dqn
~~~

This allows learned routing decisions to be investigated instead of treating the reinforcement-learning model as a complete black box.

---

## 32. Baseline Methods

Baseline implementations are available under:

~~~text
trustadaptrl/baselines/methods.py
~~~

The repository includes:

~~~text
StaticWeightedTrust
BetaReputationTrust
DempsterShaferTrust
AnomalyThresholdTrust
QoSOnlyRouting
EigenTrustLite
~~~

These methods provide comparison points for evaluating TrustAdaptRL.

---

## 33. Baseline Categories

~~~text
+----------------------------+------------------------------+
| Baseline                   | Category                     |
+----------------------------+------------------------------+
| StaticWeightedTrust        | Weighted Trust               |
| BetaReputationTrust        | Reputation-based Trust       |
| DempsterShaferTrust        | Evidence-based Trust         |
| AnomalyThresholdTrust      | Anomaly-based Trust          |
| QoSOnlyRouting             | QoS-based Routing            |
| EigenTrustLite             | Reputation / Network Trust   |
+----------------------------+------------------------------+
~~~

---

## 34. Evaluation Metrics

Evaluation utilities are implemented under:

~~~text
trustadaptrl/metrics/
~~~

The module contains:

~~~text
evaluation.py
transfer_metrics.py
efficiency.py
~~~

The framework supports evaluation of:

- Accuracy
- Precision
- Recall
- F1-score
- Convergence time
- Paired statistical comparisons
- Transfer performance
- Computational efficiency

---

## 35. Transfer Metrics

Transfer-specific metrics are implemented in:

~~~text
trustadaptrl/metrics/transfer_metrics.py
~~~

These metrics support evaluation of knowledge transfer between Fog clusters and comparison of performance before and after transfer.

---

## 36. Computational Efficiency

The efficiency module is:

~~~text
trustadaptrl/metrics/efficiency.py
~~~

It provides measurement utilities for:

~~~text
Latency
Memory usage
CPU usage
Estimated energy consumption
~~~

---

## 37. Statistical Analysis

The evaluation utilities include paired statistical analysis.

The reproduction workflow generates:

~~~text
paired_statistics.csv
~~~

This supports comparison of different methods across common experimental conditions.

---

## 38. Experiment Scripts

The repository contains:

~~~text
experiments/
├── xai_demo.py
├── transfer.py
├── attack_specific.py
├── baseline_comparison.py
├── ablation.py
└── statistics.py
~~~

These scripts correspond to different experimental aspects of TrustAdaptRL.

---

## 39. XAI Demonstration

The XAI demonstration is:

~~~text
experiments/xai_demo.py
~~~

The explainability workflow is:

~~~text
State Features
      |
      v
Learned Policy
      |
      v
Selected Action
      |
      v
Explanation
~~~

---

## 40. Transfer Experiment

The transfer experiment is:

~~~text
experiments/transfer.py
~~~

The workflow is:

~~~text
Source Fog Cluster
        |
        v
Learned Policy
        |
        v
Transfer
        |
        v
Target Fog Cluster
        |
        v
Adaptation / Evaluation
~~~

---

## 41. Attack-Specific Experiment

The attack-specific experiment is:

~~~text
experiments/attack_specific.py
~~~

It supports evaluation under:

~~~text
Grayhole
On-Off
Collusion
~~~

---

## 42. Baseline Comparison

The baseline comparison experiment is:

~~~text
experiments/baseline_comparison.py
~~~

It is used to compare TrustAdaptRL against the implemented baseline methods.

---

## 43. Ablation Study

The ablation experiment is:

~~~text
experiments/ablation.py
~~~

The purpose is to evaluate the importance of individual components of the framework.

Potential components include:

~~~text
Behavioural information
Context information
Security information
Historical information
Correlation information
Attack-aware reward
Trust component
QoS component
Security-risk component
~~~

---

## 44. Statistical Experiment

The statistical experiment is:

~~~text
experiments/statistics.py
~~~

It supports statistical comparison of experimental results.

---

## 45. Training

The main training entry point is:

~~~text
train.py
~~~

Q-learning:

~~~bash
python train.py --agent qlearning
~~~

DQN:

~~~bash
python train.py --agent dqn
~~~

Training with a dataset:

~~~bash
python train.py --agent qlearning --dataset path/to/dataset.csv
~~~

DQN with a dataset:

~~~bash
python train.py --agent dqn --dataset path/to/dataset.csv
~~~

---

## 46. Training Arguments

The main training arguments are:

~~~text
--config
--agent
--dataset
--steps
--max-devices
--seed
~~~

Example:

~~~bash
python train.py --agent dqn --steps 1000 --max-devices 30 --seed 11
~~~

---

## 47. Evaluation

The evaluation entry point is:

~~~text
evaluate.py
~~~

Example:

~~~bash
python evaluate.py path/to/results.csv
~~~

---

## 48. Complete Reproduction

The complete reproduction script is:

~~~text
reproduce_all.py
~~~

The reproduction workflow evaluates multiple:

~~~text
Malicious ratios
Random seeds
RL methods
~~~

Malicious ratios:

~~~text
0.00
0.10
0.20
0.33
~~~

Seeds:

~~~text
11
22
33
44
55
~~~

Methods:

~~~text
Q-Learning
DQN
~~~

---

## 49. Reproduction Command

Run:

~~~bash
python reproduce_all.py
~~~

The reproduction workflow generates:

~~~text
outputs/tables/all_runs.csv
outputs/tables/paired_statistics.csv
~~~

---

## 50. Output Files

The repository contains interaction-log outputs such as:

~~~text
outputs/
├── dqn_interaction_log.csv
└── qlearning_interaction_log.csv
~~~

The complete reproduction workflow generates:

~~~text
outputs/tables/all_runs.csv
outputs/tables/paired_statistics.csv
~~~

---

## 51. Interaction Logs

Interaction logs record reinforcement-learning interaction information.

The logged information includes state/action/reward/trust-related information generated during execution.

Important fields include:

~~~text
B
C
S
H
rho
reward
trust_after
~~~

---

## 52. Configuration

The main configuration file is:

~~~text
configs/default.yaml
~~~

The configuration contains:

~~~text
seed
simulation
mobility
attacks
state
reward
routing
qlearning
dqn
fog
evaluation
~~~

---

## 53. Complete Default Configuration

~~~yaml
seed: 11

simulation:
  clusters: 5
  devices_per_cluster: 40
  area_width: 500.0
  area_height: 500.0
  communication_range: 100.0
  episode_steps: 1000
  observation_window: 10
  mobility_fraction: 0.5

mobility:
  min_speed: 0.5
  max_speed: 2.0
  pause_time: 5

attacks:
  malicious_ratio: 0.20
  grayhole_drop_probability: 0.45
  onoff_malicious_duty_cycle: 0.50
  collusion_group_min: 3
  collusion_group_max: 5

state:
  history_window: 10
  context_smoothing: 0.7
  additive_smoothing: 1.0
  trust_delta: 0.05
  initial_trust: 0.5
  trusted_threshold: 0.5

reward:
  qos_pdr_weight: 1.0
  qos_delay_weight: 0.35
  gray_weight: 0.7
  onoff_weight: 0.7
  collusion_weight: 0.8
  tau_gray: 0.10
  tau_onoff: 0.12
  tau_collusion: 0.65

routing:
  trust_weight: 0.5
  qos_weight: 0.35
  risk_weight: 0.15

qlearning:
  learning_rate: 0.10
  gamma: 0.95
  epsilon_start: 1.0
  epsilon_min: 0.05
  epsilon_decay: 0.995
  bins: 3

dqn:
  learning_rate: 0.001
  gamma: 0.99
  batch_size: 32
  replay_capacity: 50000
  target_update: 20
  epsilon_start: 1.0
  epsilon_min: 0.05
  epsilon_decay: 0.995
  hidden_layers: [64, 64, 32]

fog:
  sync_interval_windows: 20
  train_updates_per_sync: 20

evaluation:
  seeds: [11, 22, 33, 44, 55]
  malicious_ratios: [0.0, 0.10, 0.20, 0.33]
~~~

---

## 54. Repository Structure

The actual project structure is:

~~~text
TrustAdaptRL/
│
├── configs/
│   └── default.yaml
│
├── experiments/
│   ├── xai_demo.py
│   ├── transfer.py
│   ├── attack_specific.py
│   ├── baseline_comparison.py
│   ├── ablation.py
│   └── statistics.py
│
├── tests/
│   └── test_smoke.py
│
├── outputs/
│   ├── dqn_interaction_log.csv
│   └── qlearning_interaction_log.csv
│
├── trustadaptrl/
│   │
│   ├── __init__.py
│   │
│   ├── utils/
│   │   ├── seed.py
│   │   ├── config.py
│   │   └── __init__.py
│   │
│   ├── fog/
│   │   ├── hierarchical.py
│   │   └── __init__.py
│   │
│   ├── explainability/
│   │   ├── explainers.py
│   │   └── __init__.py
│   │
│   ├── routing/
│   │   ├── trust_qos_router.py
│   │   └── __init__.py
│   │
│   ├── features/
│   │   ├── state_builder.py
│   │   └── __init__.py
│   │
│   ├── simulation/
│   │   ├── device.py
│   │   ├── mobility.py
│   │   ├── topology.py
│   │   ├── environment.py
│   │   └── __init__.py
│   │
│   ├── attacks/
│   │   ├── advanced.py
│   │   ├── attack_manager.py
│   │   └── __init__.py
│   │
│   ├── agents/
│   │   ├── qlearning_agent.py
│   │   ├── dqn_agent.py
│   │   └── __init__.py
│   │
│   ├── datasets/
│   │   ├── traffic_replay.py
│   │   ├── preprocessing.py
│   │   ├── loaders.py
│   │   └── __init__.py
│   │
│   ├── rewards/
│   │   ├── attack_aware_reward.py
│   │   └── __init__.py
│   │
│   ├── metrics/
│   │   ├── transfer_metrics.py
│   │   ├── efficiency.py
│   │   ├── evaluation.py
│   │   └── __init__.py
│   │
│   └── baselines/
│       ├── methods.py
│       └── __init__.py
│
├── train.py
├── evaluate.py
├── reproduce_all.py
└── IMPLEMENTATION_MANIFEST.md
~~~

---

## 55. Module Responsibilities

~~~text
+------------------------------+------------------------------------------+
| Module                       | Responsibility                           |
+------------------------------+------------------------------------------+
| datasets/                    | Traffic loading and preprocessing        |
| simulation/                  | Fog-IoT topology, devices, mobility      |
| attacks/                     | Attack generation and robustness         |
| features/                   | Five-dimensional state construction      |
| rewards/                     | Attack-aware reward calculation          |
| agents/                      | Q-learning and DQN                       |
| routing/                     | Trust-QoS-security routing               |
| fog/                         | Fog learning and policy transfer         |
| baselines/                   | Comparison methods                        |
| explainability/              | RL decision explanation                  |
| metrics/                     | Evaluation and efficiency                |
| experiments/                 | Research experiments                     |
| utils/                       | Configuration and random seeds           |
+------------------------------+------------------------------------------+
~~~

---

## 56. Implementation Manifest

The repository contains:

~~~text
IMPLEMENTATION_MANIFEST.md
~~~

The implementation covers:

~~~text
1. Public traffic preparation
2. Dynamic clustered Fog-IoT topology
3. Mobility
4. Grayhole attacks
5. On-Off attacks
6. Collusion attacks
7. Advanced robustness helpers
8. Five-part state representation
9. Attack-aware reward
10. Q-learning
11. DQN
12. Trust-QoS-security routing
13. Fog policy synchronization
14. Cross-cluster transfer
15. Baselines
16. Explainability
17. Metrics
18. Statistical analysis
19. Computational efficiency
20. Reproduction experiments
~~~

---

## 57. Testing

The repository contains:

~~~text
tests/test_smoke.py
~~~

The smoke test validates the integration between:

~~~text
Configuration
Synthetic Traffic
Fog-IoT Environment
Q-Learning Agent
~~~

Run:

~~~bash
pytest -q
~~~

Expected result:

~~~text
1 passed
~~~

---

## 58. Random Seed Management

Seed handling is implemented in:

~~~text
trustadaptrl/utils/seed.py
~~~

Default seed:

~~~yaml
seed: 11
~~~

Evaluation seeds:

~~~text
11
22
33
44
55
~~~

Multiple seeds help reduce dependence on a single random initialization.

---

## 59. Reproducibility

TrustAdaptRL supports reproducible experiments through:

- Configuration files
- Explicit random seeds
- Multiple evaluation seeds
- Reproduction scripts
- Interaction logging
- Standardized evaluation

Main reproduction command:

~~~bash
python reproduce_all.py
~~~

---

## 60. End-to-End Workflow

~~~text
                     START
                       |
                       v
              Load Configuration
                       |
                       v
             Load Public Dataset
                    /     \
                   /       \
                  v         v
             Dataset      Synthetic
                  \         /
                   \       /
                    v     v
               Preprocessing
                       |
                       v
              Build Fog-IoT Network
                       |
                       v
                Device Mobility
                       |
                       v
                Attack Injection
                       |
                       v
               Observe Neighbours
                       |
                       v
             Build State [B,C,S,H,ρ]
                       |
                       v
              Select RL Action
                  /    |    \
                 /     |     \
                v      v      v
           Decrease  Maintain Increase
             Trust     Trust     Trust
                \       |       /
                 \      |      /
                  v     v     v
                Calculate Reward
                       |
                       v
             Update RL Policy
                  /        \
                 v          v
            Q-Learning      DQN
                 \          /
                  \        /
                   v      v
              Routing Decision
                       |
                       v
              Fog-Level Learning
                       |
                       v
             Policy Synchronization
                       |
                       v
             Cross-Cluster Transfer
                       |
                       v
          Evaluation / XAI / Statistics
                       |
                       v
                      END
~~~

---

## 61. Research Evaluation Dimensions

### Security

~~~text
Grayhole resilience
On-Off attack resilience
Collusion resilience
Anomaly awareness
~~~

### Routing

~~~text
Trust-aware routing
QoS-aware routing
Security-aware routing
Adaptive next-hop selection
~~~

### Learning

~~~text
Q-learning
DQN
Convergence
Policy adaptation
~~~

### Transfer

~~~text
Fog-level learning
Policy synchronization
Cross-cluster transfer
~~~

### Explainability

~~~text
Q-table explanations
SHAP-based DQN explanations
~~~

### Efficiency

~~~text
Latency
CPU
Memory
Estimated energy
~~~

---

## 62. Proposed Framework Summary

TrustAdaptRL integrates:

~~~text
                 TrustAdaptRL
                      |
       +--------------+--------------+
       |              |              |
       v              v              v
    Trust            QoS          Security
       |              |              |
       +--------------+--------------+
                      |
                      v
             Five-Dimensional State
                  [B,C,S,H,ρ]
                      |
                      v
             Attack-Aware Reward
                      |
                      v
          Reinforcement Learning
             /              \
            v                v
       Q-Learning            DQN
            \                /
             \              /
              v            v
              Adaptive Routing
                      |
                      v
               Fog-Level Learning
                      |
                      v
              Policy Synchronization
                      |
                      v
              Cross-Cluster Transfer
                      |
                      v
              Explainable Decisions
                      |
                      v
           Statistical Evaluation
~~~

---

## 63. Installation

Create a Python virtual environment:

~~~bash
python -m venv .venv
~~~

### Windows

~~~bash
.venv\Scripts\activate
~~~

### Linux / macOS

~~~bash
source .venv/bin/activate
~~~

Install the required Python packages used by the project:

~~~bash
pip install numpy pandas pyyaml scikit-learn torch pytest shap
~~~

---

## 64. Quick Start

Run Q-learning:

~~~bash
python train.py --agent qlearning
~~~

Run DQN:

~~~bash
python train.py --agent dqn
~~~

Specify training steps:

~~~bash
python train.py --agent dqn --steps 1000
~~~

Limit simulated devices:

~~~bash
python train.py --agent dqn --max-devices 30
~~~

Specify a seed:

~~~bash
python train.py --agent dqn --seed 11
~~~

---

## 65. Dataset-Based Quick Start

For a supported IoT dataset:

~~~bash
python train.py --agent dqn --dataset path/to/dataset.csv --steps 1000
~~~

The workflow is:

~~~text
Load Dataset
     |
     v
Preprocess Traffic
     |
     v
Build Environment
     |
     v
Run DQN
     |
     v
Generate Interaction Log
~~~

---

## 66. Complete Experiment Execution

Run:

~~~bash
python reproduce_all.py
~~~

The workflow evaluates:

~~~text
Methods:
    Q-Learning
    DQN

Malicious Ratios:
    0.00
    0.10
    0.20
    0.33

Seeds:
    11
    22
    33
    44
    55
~~~

---

## 67. Research Contributions

The implementation provides an integrated framework combining:

1. Multi-dimensional trust representation.
2. Attack-aware reinforcement learning.
3. Dynamic Fog-IoT simulation.
4. Mobility-aware network modelling.
5. Grayhole attack modelling.
6. On-Off attack modelling.
7. Collusion attack modelling.
8. Trust-QoS-security routing.
9. Q-learning-based trust adaptation.
10. DQN-based trust adaptation.
11. Fog-level policy synchronization.
12. Cross-cluster policy transfer.
13. Explainable reinforcement-learning decisions.
14. Multiple trust and routing baselines.
15. Statistical comparison.
16. Computational efficiency analysis.
17. Reproducible multi-seed evaluation.

---

## 68. Important Design Principles

### Multi-Dimensional Trust

Trust is represented using:

~~~text
Trust State = [B, C, S, H, ρ]
~~~

rather than relying on a single behavioural measurement.

### Attack Awareness

The reward explicitly incorporates attack-related penalties:

~~~text
Normal QoS
     +
Security Awareness
     +
Attack Penalties
     =
Attack-Aware Learning
~~~

### Adaptive Decision Making

~~~text
Observe
   |
   v
Evaluate
   |
   v
Learn
   |
   v
Adapt
   |
   v
Route
~~~

### Fog-Level Intelligence

~~~text
Local Experience
      |
      v
Fog Aggregation
      |
      v
Policy Synchronization
      |
      v
Cross-Cluster Transfer
~~~

---

## 69. Limitations and Scope

The repository provides a research implementation and experimental framework.

The implementation includes a synthetic-traffic fallback so that the main framework can be executed without requiring an external dataset.

When public IoT datasets are used, they should be converted into a supported tabular representation and their traffic attributes should be mapped to the preprocessing pipeline.

Experimental results depend on:

~~~text
Dataset
+
Dataset Preprocessing
+
Simulation Configuration
+
Attack Configuration
+
Random Seed
+
RL Configuration
~~~

---

## 70. Reproducibility Checklist

Before reporting experimental results, record:

~~~text
[ ] Dataset
[ ] Dataset preprocessing
[ ] Random seed
[ ] Number of Fog clusters
[ ] Devices per cluster
[ ] Communication range
[ ] Mobility parameters
[ ] Malicious-device ratio
[ ] Attack type
[ ] Attack parameters
[ ] RL algorithm
[ ] RL hyperparameters
[ ] Reward configuration
[ ] Routing weights
[ ] Fog synchronization interval
[ ] Transfer configuration
[ ] Number of evaluation runs
~~~

---

## 71. Recommended Experiment Matrix

~~~text
                 Attack Ratio
              0%   10%   20%   33%
               |    |     |     |
               v    v     v     v
           +------------------------+
           | Q-Learning             |
           +------------------------+
                      |
                      v
           +------------------------+
           | DQN                    |
           +------------------------+
                      |
                      v
           +------------------------+
           | Baselines              |
           +------------------------+
                      |
                      v
           +------------------------+
           | Statistical Analysis   |
           +------------------------+
                      |
                      v
           +------------------------+
           | Efficiency Analysis    |
           +------------------------+
~~~

---

## 72. Comparison Framework

The proposed methods can be compared against:

~~~text
TrustAdaptRL-Q-Learning
TrustAdaptRL-DQN
StaticWeightedTrust
BetaReputationTrust
DempsterShaferTrust
AnomalyThresholdTrust
QoSOnlyRouting
EigenTrustLite
~~~

Comparison dimensions include:

~~~text
Accuracy
Precision
Recall
F1-score
Convergence
Transfer Performance
Latency
Memory
CPU
Estimated Energy
~~~

---

## 73. Project Status

The repository contains an executable research implementation covering:

~~~text
✓ Dynamic Fog-IoT simulation
✓ Device mobility
✓ Multiple attack models
✓ Five-dimensional state construction
✓ Attack-aware reward
✓ Q-learning
✓ DQN
✓ Trust-QoS-security routing
✓ Fog-level learning
✓ Policy synchronization
✓ Cross-cluster transfer
✓ Baseline methods
✓ Explainability
✓ Evaluation metrics
✓ Efficiency metrics
✓ Statistical analysis
✓ Reproduction scripts
✓ Smoke testing
~~~

---

## 74. Citation

If this repository is used in academic research, cite the corresponding TrustAdaptRL research work.

Add the final publication metadata when available:

~~~bibtex
@article{trustadaptrl,
  title   = {TrustAdaptRL: Attack-Aware Trust and Reinforcement Learning for Dynamic Fog-IoT Routing},
  author  = {Author Name},
  journal = {Journal Name},
  year    = {2026},
  volume  = {},
  number  = {},
  pages   = {},
  doi     = {}
}
~~~

---

## 75. License

Add the project license information according to the license selected for the repository.

For example:

~~~text
This project is intended for research and academic purposes.
Please refer to the LICENSE file for the applicable terms and conditions.
~~~

---

## 76. Acknowledgement

This repository uses concepts and technologies from:

~~~text
Fog Computing
Internet of Things
Trust Management
Reinforcement Learning
Deep Reinforcement Learning
Network Security
Anomaly Detection
QoS-aware Routing
Explainable Artificial Intelligence
~~~

---

## 77. Final Summary

TrustAdaptRL provides an integrated research framework for adaptive and attack-aware trust management and routing in dynamic Fog-IoT networks.

The framework combines:

~~~text
Dynamic Fog-IoT Simulation
            +
Mobility
            +
Trust Representation
            +
Security / Anomaly Detection
            +
Attack Modelling
            +
Attack-Aware Reward
            +
Q-Learning
            +
DQN
            +
QoS-Aware Routing
            +
Fog-Level Learning
            +
Policy Synchronization
            +
Cross-Cluster Transfer
            +
Explainable AI
            +
Baseline Comparison
            +
Statistical Analysis
            +
Efficiency Evaluation
~~~

The central state representation is:

~~~text
s(i,j,t) = [B_ij(t), C_ij(t), S_ij(t), H_ij(t), ρ_ij(t)]
~~~

The reinforcement-learning actions are:

~~~text
0 → Decrease Trust
1 → Maintain Trust
2 → Increase Trust
~~~

The routing decision combines trust, QoS, and security risk:

~~~text
Routing Score =
    Trust Contribution
  + QoS Contribution
  - Security Risk Contribution
~~~

The complete framework workflow is:

~~~text
IoT Traffic
    |
    v
Preprocessing
    |
    v
Dynamic Fog-IoT Network
    |
    v
Mobility
    |
    v
Attack Modelling
    |
    v
State [B,C,S,H,ρ]
    |
    v
Attack-Aware Reward
    |
    v
Q-Learning / DQN
    |
    v
Trust Adaptation
    |
    v
Trust-QoS-Security Routing
    |
    v
Fog-Level Training
    |
    v
Policy Synchronization
    |
    v
Cross-Cluster Transfer
    |
    v
XAI
    |
    v
Baseline Comparison
    |
    v
Statistical Analysis
    |
    v
Efficiency Evaluation
    |
    v
Reproducible Results
~~~

---

# TrustAdaptRL

~~~text
Adaptive Trust
      +
QoS Awareness
      +
Security Awareness
      +
Reinforcement Learning
      +
Fog-Level Intelligence
      +
Explainability
      =
TrustAdaptRL
~~~
