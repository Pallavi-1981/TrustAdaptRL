TrustAdaptRL
GitHub Repository README
TrustAdaptRL: An Online Reinforcement Learning Framework for Attack-Resilient Trust Management in Fog-IoT Networks

TrustAdaptRL is a modular Python research framework for adaptive, attack-resilient trust management in Fog-enabled Internet of Things (Fog-IoT) networks. The framework combines reinforcement learning, attack-aware trust adaptation, Quality-of-Service-aware routing, fog-assisted hierarchical learning, cross-cluster policy transfer, and model-specific explainability.
The implementation supports both tabular Q-learning and Deep Q-Networks (DQN) and evaluates trust-management performance under grayhole, on-off, collusion, adaptive, coordinated, and reward-poisoning attacks.
The project follows a hybrid evaluation methodology in which public IoT security datasets provide realistic traffic and security characteristics, while Fog-IoT topology, neighbour relationships, packet-forwarding behaviour, trust states, and routing-specific adversarial behaviour are generated within a controlled simulation environment.
Key Features
•	Dynamic clustered Fog-IoT network simulation
•	Public traffic integration using TON_IoT, BoT-IoT, and IoT-23
•	Random Waypoint device mobility and dynamic neighbour discovery
•	Packet-forwarding and QoS simulation
•	Grayhole, on-off, collusion, adaptive, coordinated, and reward-poisoning attack scenarios
•	Five-dimensional RL trust state representation
•	Tabular Q-learning and PyTorch Deep Q-Network
•	Experience replay and target-network synchronization
•	Attack-aware reward shaping
•	Factorized neighbour-wise trust adaptation
•	Trust-QoS-security-aware next-hop routing
•	Fog-assisted hierarchical training and cluster-level experience aggregation
•	Policy synchronization and cross-cluster transfer learning
•	Classical trust-management baselines
•	Intrinsic Q-table explainability and SHAP/LIME-based DQN explainability
•	Ablation, scalability, statistical-significance, and reproducibility support
•	Automatic result logging and figure generation
Framework Overview
TON_IoT / BoT-IoT / IoT-23
            |
            v
Traffic Preprocessing
            |
            v
Traffic Observation Windows
            |
            v
Dynamic Fog-IoT Simulator
            |
      +-----+------+
      |            |
      v            v
Benign Nodes   Attack Injection
               |-- Grayhole
               |-- On-Off
               |-- Collusion
               |-- Adaptive
               |-- Coordinated
               `-- Reward Poisoning
      |            |
      +-----+------+
            |
            v
Neighbour Observations
            |
            v
State Construction
[B, C, S, H, rho]
            |
            v
TrustAdaptRL Agent
 |-- Tabular Q-Learning
 `-- Deep Q-Network
            |
            v
Trust Adjustment
            |
            v
Trust + QoS + Security Routing
            |
            v
Experience Collection
            |
            v
Fog-Level Training
            |
            v
Policy Synchronization
            |
            v
Evaluation / Transfer / XAI / Statistics
State Representation
For device i evaluating neighbour j at time t, TrustAdaptRL constructs:
s(i,j,t) = [B_j(t), C_j(t), S_j(t), H_j(t), rho_j(t)]
•	B_j(t) = forwarding reliability
•	C_j(t) = contextual network conditions
•	S_j(t) = traffic-security evidence
•	H_j(t) = temporal behavioural inconsistency
•	rho_j(t) = cross-neighbour behavioural correlation
This state is designed to distinguish benign network degradation from selective packet dropping, temporally adaptive attacks, and coordinated malicious behaviour.
Reinforcement Learning Actions
The RL agent applies one of three trust-adjustment actions independently to each candidate neighbour:
0 -> Decrease Trust
1 -> Maintain Trust
2 -> Increase Trust
Trust adaptation and routing are intentionally separated. First, the RL policy updates trust for each candidate neighbour. A second-stage routing module then selects the most suitable next hop using trust, QoS, and security information.
Attack-Aware Reward
TrustAdaptRL combines QoS performance with attack-specific penalties:
Reward =
    QoS Reward
    - Grayhole Penalty
    - On-Off Penalty
    - Collusion Penalty
A simplified implementation is:
R_base = w1 * pdr - w2 * normalized_delay

P_gray = max(
    0.0,
    expected_reliability - current_reliability - tau_gray
)

P_onoff = max(
    0.0,
    temporal_inconsistency - tau_onoff
)

P_collusion = (
    max(0.0, correlation - tau_collusion)
    * security_evidence
)

P_adv = (
    lambda_gray * P_gray
    + lambda_onoff * P_onoff
    + lambda_collusion * P_collusion
)

reward = R_base - P_adv
Fog-Assisted Hierarchical Learning
TrustAdaptRL separates lightweight device-side inference from computationally intensive fog-side learning.
IoT Device Responsibilities
•	Local feature extraction
•	RL state construction
•	Trust-policy inference
•	Neighbour trust adjustment
•	Next-hop selection
•	Experience generation
Fog Node Responsibilities
•	Experience aggregation
•	Replay-buffer management
•	Q-learning or DQN optimization
•	Target-network synchronization
•	Policy redistribution
•	Cross-cluster policy sharing
This design reduces computational requirements at constrained IoT devices while allowing devices within a cluster to benefit from collective learning.
Supported RL Models
Tabular Q-Learning
Default configuration:
Learning rate:     0.10
Discount factor:   0.95
Initial epsilon:   1.00
Minimum epsilon:   0.05
The continuous trust-state features are discretized into compact categorical states.
Deep Q-Network
The DQN is implemented using PyTorch. Typical architecture:
Input: 5 state features
        |
Dense Layer
        |
ReLU
        |
Dense Layer
        |
ReLU
        |
Dense Layer
        |
ReLU
        |
Output: 3 Q-values
Output:
Q(Decrease Trust)
Q(Maintain Trust)
Q(Increase Trust)
Default configuration:
Optimizer:             Adam
Learning rate:         1e-3
Discount factor:       0.99
Mini-batch size:       32
Replay-buffer size:    50,000
Target update:         Every 20 training steps
Initial epsilon:       1.0
Minimum epsilon:       0.05
Public Datasets
TON_IoT
Used for realistic:
•	IoT/IIoT traffic characteristics
•	Telemetry behaviour
•	Protocol patterns
•	Temporal traffic variation
•	Security indicators
BoT-IoT
Used primarily for high-volume adversarial traffic such as:
•	DDoS
•	DoS
•	Scanning
•	Data exfiltration
IoT-23
Used for heterogeneous, temporally varying benign and malware-related IoT traffic patterns.
Important Dataset Note
The datasets are not treated as native trust-management datasets.
They do not directly provide:
•	Per-neighbour trust values
•	Dynamic Fog-IoT routing topology
•	Neighbour forwarding histories
•	Routing-specific grayhole attacks
•	Routing-specific on-off attacks
•	Collusion trust attacks
The public datasets provide realistic traffic characteristics, while the simulator independently generates:
•	Topology
•	Neighbour interactions
•	Forwarding successes and failures
•	Attack states
•	Trust ground truth
Traffic Security Evidence
The security feature S_j(t) is supporting evidence, not the true trust label.
Traffic Features
      |
      v
Security / Anomaly Model
      |
      v
Probability or Anomaly Score
      |
      v
Normalized Security Evidence S_j(t)
The native dataset attack label should not be directly supplied to the RL agent as trust ground truth.
Attack Models
Grayhole
Grayhole nodes selectively drop packets while forwarding others normally. Typical drop probability:
0.30 - 0.60
On-Off
On-off attackers alternate between benign and malicious behaviour. Default malicious duty cycle:
50%
Collusion
Collusion involves coordinated malicious neighbours. Typical group size:
3 - 5 malicious devices
The feature rho_j(t) is intended to capture cross-neighbour behavioural correlation.
Reward Poisoning
Optional experiments can corrupt rewards:
poisoned_reward = -reward
or:
poisoned_reward = reward + noise
Adaptive Attack
Adaptive attackers modify malicious intensity based on their trust status:
High trust
   ->
Increase malicious behaviour

Low trust
   ->
Temporarily behave benignly
Default Simulation Configuration
Fog clusters:                   5
Fog nodes per cluster:          1
IoT devices per cluster:       40
Total IoT devices:             200

Area per cluster:               500 m x 500 m
Communication range:           100 m

Mobility model:                 Random Waypoint
Mobility speed:                 0.5-2.0 m/s
Pause time:                     5 s

Episode length:                 1,000 time steps
Observation window:             10 time steps

Malicious-node ratios:
0%
10%
20%
33%

Grayhole drop probability:
0.30-0.60

On-off malicious duty cycle:
50%

Collusion group size:
3-5 nodes

Independent random seeds:
5
Repository Structure
TrustAdaptRL/
|
|-- configs/
|   |-- default.yaml
|   |-- qlearning.yaml
|   |-- dqn.yaml
|   |-- attacks.yaml
|   `-- experiments.yaml
|
|-- data/
|   |-- raw/
|   |   |-- ton_iot/
|   |   |-- bot_iot/
|   |   `-- iot23/
|   |-- processed/
|   `-- cache/
|
|-- trustadaptrl/
|   |-- datasets/
|   |-- simulation/
|   |-- attacks/
|   |-- features/
|   |-- rewards/
|   |-- agents/
|   |-- routing/
|   |-- baselines/
|   |-- fog/
|   |-- explainability/
|   |-- metrics/
|   `-- utils/
|
|-- experiments/
|-- notebooks/
|
|-- outputs/
|   |-- logs/
|   |-- checkpoints/
|   |-- tables/
|   |-- figures/
|   |-- explanations/
|   `-- statistics/
|
|-- train.py
|-- evaluate.py
|-- reproduce_all.py
|-- requirements.txt
`-- README.md
Installation
Clone the repository:
git clone https://github.com/your-username/TrustAdaptRL.git
cd TrustAdaptRL
Create a virtual environment:
python -m venv venv
Windows
venv\Scripts\activate
Linux/macOS
source venv/bin/activate
Install dependencies:
pip install -r requirements.txt
Quick Start
The repository includes a synthetic traffic fallback, so the framework can be tested without downloading the public datasets.
Run Q-learning:
python train.py --agent qlearning --steps 100 --max-devices 40
Run DQN:
python train.py --agent dqn --steps 100 --max-devices 40
Run the experimental pipeline:
python reproduce_all.py
Running with Public Traffic Data
Place the datasets under:
data/raw/ton_iot/
data/raw/bot_iot/
data/raw/iot23/
Example:
python train.py     --agent dqn     --dataset data/raw/ton_iot/ton_iot.csv
The preprocessing layer maps dataset-specific fields into a common traffic representation before their use by the simulator.
Configuration
Most experiment settings are controlled through YAML files. Example:
simulation:
  clusters: 5
  devices_per_cluster: 40
  area_width: 500
  area_height: 500
  communication_range: 100
  episode_steps: 1000
  observation_window: 10

mobility:
  model: random_waypoint
  min_speed: 0.5
  max_speed: 2.0
  pause_time: 5

attacks:
  malicious_ratios:
    - 0.0
    - 0.10
    - 0.20
    - 0.33

  grayhole:
    drop_probability: 0.45

  onoff:
    malicious_duty_cycle: 0.50

  collusion:
    min_group: 3
    max_group: 5

qlearning:
  learning_rate: 0.10
  gamma: 0.95

dqn:
  learning_rate: 0.001
  gamma: 0.99
  batch_size: 32
  replay_capacity: 50000
  target_update: 20

exploration:
  epsilon_start: 1.0
  epsilon_min: 0.05

evaluation:
  seeds:
    - 11
    - 22
    - 33
    - 44
    - 55
Baseline Methods
TrustAdaptRL includes representative comparison methods:
•	Static Weighted Trust
•	Beta-Reputation Trust
•	EigenTrust
•	Dempster-Shafer Trust
•	Anomaly Detection + Trust Threshold
•	QoS-Only Routing
For fair evaluation, all methods should use identical topology, traffic replay, attack schedules, malicious-node selection, random seeds, and evaluation metrics.
Evaluation Metrics
Trust Management
•	Trust Accuracy
•	Precision
•	Recall
•	F1-Score
•	False Positive Rate
•	False Negative Rate
Attack Resilience
•	Grayhole Detection Rate
•	On-Off Detection Rate
•	Collusion Detection Rate
•	Adaptive Attack Detection Rate
•	Coordinated Attack Detection Rate
Quality of Service
•	Packet Delivery Ratio
•	End-to-End Latency
•	Throughput
•	Jitter
Trust Stability
•	Temporal trust variance
•	Convergence time
•	Trust trajectory
Default convergence criterion:
Trust-change tolerance = 0.01
Consecutive stable windows = 5
Computational Efficiency
•	Decision latency
•	Inference latency
•	CPU utilization
•	Memory consumption
•	Simulated energy per decision
•	Fog offloading latency
•	Fog training time
Cross-Cluster Generalization
Compare:
Training from Scratch
        vs.
Transferred Policy Initialization
•	Transfer accuracy
•	Convergence steps
•	Retraining-time reduction
Explainability
Q-Learning
Tabular Q-learning is interpreted intrinsically using:
•	Current state
•	Available actions
•	Q-values
•	Selected action
•	Reward components
•	Trust before action
•	Trust after action
DQN
SHAP is used as the primary DQN explanation method. Features analyzed:
B -> Behavioural Reliability
C -> Context
S -> Security Evidence
H -> Temporal Inconsistency
rho -> Cross-Neighbour Correlation
LIME can additionally be used for representative local explanations.
Ablation Studies
Supported variants can include:
Full TrustAdaptRL
TrustAdaptRL without Context C
TrustAdaptRL without Security Evidence S
TrustAdaptRL without Temporal Feature H
TrustAdaptRL without Correlation rho
TrustAdaptRL without Attack-Aware Penalties
TrustAdaptRL with QoS-Only Reward
TrustAdaptRL without Fog-Level Aggregation
Scalability Experiments
Typical network sizes:
50 devices
100 devices
200 devices
300 devices
500 devices
Measure:
•	Decision latency
•	DQN inference time
•	Fog training cost
•	CPU usage
•	Memory usage
•	Throughput
•	Detection performance
Statistical Evaluation
Principal experiments should be repeated over multiple independent seeds. Recommended reporting:
•	Mean
•	Standard Deviation
•	95% Confidence Interval
•	Paired t-test
•	Wilcoxon Signed-Rank Test
•	Cohen's d_z
Statistical tests should use per-seed values rather than aggregated means.
Reproducibility
The framework records:
•	Configuration files
•	Random seeds
•	Topology configuration
•	Attack parameters
•	Dataset replay order
•	RL hyperparameters
•	Model checkpoints
•	Trust trajectories
•	Per-run metrics
•	Statistical results
Typical output structure:
outputs/
|
|-- logs/
|-- checkpoints/
|-- tables/
|-- figures/
|-- explanations/
`-- statistics/
Typical output files:
overall_metrics.csv
attack_metrics.csv
qos_metrics.csv
stability_metrics.csv
efficiency_metrics.csv
transfer_metrics.csv
ablation_results.csv
sensitivity_results.csv
statistical_tests.csv
Typical Visualizations
•	Trust accuracy comparisons
•	Attack-specific detection rates
•	Packet delivery ratio comparisons
•	Latency comparisons
•	Trust evolution curves
•	Q-learning convergence curves
•	DQN loss curves
•	Reward evolution curves
•	Scalability analysis
•	Malicious-node-ratio sensitivity
•	Cross-cluster transfer results
•	Ablation plots
•	SHAP feature-importance plots
•	Temporal attribution plots
•	Trust stability plots
Recommended Experimental Workflow
1.	Validate dataset preprocessing
2.	Validate topology and mobility
3.	Validate packet forwarding and QoS
4.	Validate grayhole attacks
5.	Validate on-off attacks
6.	Validate collusion attacks
7.	Validate B, C, S, H, and rho features
8.	Validate attack-aware reward
9.	Run static trust baselines
10.	Train Q-learning
11.	Train DQN
12.	Perform baseline comparison
13.	Evaluate individual attacks
14.	Vary malicious-node proportion
15.	Test adaptive and poisoning attacks
16.	Perform scalability analysis
17.	Perform ablation analysis
18.	Perform cross-cluster transfer
19.	Generate explainability results
20.	Perform multi-seed statistical testing
Important Experimental Considerations
Avoid Trust-Label Leakage
Do not use:
security_evidence = true_attack_label
Instead, S_j(t) should come from imperfect traffic-derived security or anomaly evidence. Simulator attack states should be reserved for evaluation ground truth.
Validate Attacks Before Training
Confirm that:
Grayhole
    -> forwarding reliability decreases

On-Off
    -> temporal inconsistency increases

Collusion
    -> cross-neighbour correlation increases
Keep Train and Test Scenarios Separate
Training and testing should use distinct:
•	Attack schedules
•	Topology realizations
•	Traffic windows
•	Replay order
•	Target clusters
Dependencies
Major packages include:
Python
NumPy
Pandas
PyTorch
Scikit-learn
NetworkX
Gymnasium
SciPy
Statsmodels
Matplotlib
SHAP
LIME
PyYAML
psutil
See requirements.txt for the complete dependency specification.
Hardware
The framework is software-based and does not require physical IoT devices or fog hardware. A GPU is recommended for large DQN experiments but is not mandatory for Q-learning or small-scale validation.
Research Scope
•	Fog-IoT security
•	Adaptive trust management
•	Reinforcement-learning-based cybersecurity
•	Attack-resilient routing
•	Explainable reinforcement learning
•	Distributed intelligence
•	Fog-assisted machine learning
•	Non-stationary adversarial environments
•	Trust-aware network optimization
Citation
If you use this implementation in academic work, cite the corresponding TrustAdaptRL research paper.
@article{TrustAdaptRL,
  title   = {TrustAdaptRL: An Online Reinforcement Learning Framework for Attack-Resilient Trust Management in Fog-IoT Networks},
  author  = {Authors},
  journal = {Journal},
  year    = {Year}
}
Replace the placeholder publication information after the paper is formally published.
License
Add the license selected for the repository, such as:
MIT License
Apache License 2.0
BSD 3-Clause License
Disclaimer
This repository is intended primarily for academic research and experimental evaluation. The Fog-IoT environment, routing-specific attacks, neighbour interactions, and trust labels are simulated under controlled conditions. Public network-security datasets are used to provide realistic traffic characteristics and should not be interpreted as containing native Fog-IoT trust-management annotations.
Results from the framework therefore represent controlled, public-traffic-driven Fog-IoT simulation experiments and should not automatically be interpreted as equivalent to performance in physical production deployments.
