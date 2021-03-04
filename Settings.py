# DATASET_NAME = "Artificial_Cos"
# ARTIFICIAL_DATA = True
DATASET_NAME = "BA"
ARTIFICIAL_DATA = False

# Flags for the current algo being used
_DQN_ = 0
_AC_ = 0
_PPO_ = 1

# MAX_EPISODES = 1_000_000
MAX_EPISODES = 200_000

# Tensorboard logging
TENSORBOARD_SAVE = True
# TENSORBOARD_UPDATE = MAX_EPISODES/100
TENSORBOARD_UPDATE = 1000

# Output logging
LOG_OUTPUTS = True

# Evaluation
# EVALUATE_EVERY_N_EPISODES = MAX_EPISODES/100
EVALUATE_EVERY_N_EPISODES = TENSORBOARD_UPDATE

# Save model checkpoints during training
SAVE_CHECKPOINTS = False
CHECKPOINT_STEP = MAX_EPISODES/10

# Load existing model checkpoint
LOAD_MODEL = False
MODEL_TO_LOAD = "checkpoints/TestDQN_30d_EAS=False_RAPC=False03-02-2021_19-07-39/TestDQN_30d_EAS=False_RAPC=False03-02-2021_19-07-39_200.pth"

# Current state will have data for N-1 days before the current day (SND)
STATE_N_DAYS = 7

# Environment starting date after reset
RANDOM_START_TRAINING_DATE = 1
RANDOM_START_VAL_DATE = 1

# End current episode after selling a stock (EAS)
END_AFTER_SELL = 0

# Number of days until episode ends (EL)
EPISODE_LENGTH = 20

# Update reward on price change (RAPC)
REWARD_AFTER_PRICE_CHANGE = 1

REWARD_BUY = 0
REWARD_SELL_MULTIPLIER = 100
REWARD_HOLD_ACTIVE_MULTIPLIER = 10
REWARD_HOLD_INACTIVE_PRICE_UP = -0.02
REWARD_HOLD_INACTIVE_PRICE_DOWN = 0
REWARD_INVALID = 0

# Dataset
# RUN_FOLDER = "runs/"
# RUN_NAME = "TestPPO_JNJ"
# TRAIN_DATA = "data/JNJ_2000-2019.csv"
# VAL_DATA = "data/JNJ_2020.csv"
# RUN_FOLDER = "runs_artificial/"
# RUN_NAME = "PPO_Handcrafted_15d"
# TRAIN_DATA = "data/Artificial_Handcrafted_15d.csv"
# VAL_DATA = "data/Artificial_Handcrafted_15d.csv"

# Algorithms
DQN = "DQN"
AC = "AC"
PPO = "PPO"

if _DQN_ == 1:
	ALGO_NAME = DQN
if _AC_ == 1:
	ALGO_NAME = AC
if _PPO_ == 1:
	ALGO_NAME = PPO

RUN_NAME = "{}_{}".format(ALGO_NAME, DATASET_NAME)

if ARTIFICIAL_DATA:
	RUN_FOLDER = "runs_artificial/"
	TRAIN_DATA = "data/{}.csv".format(DATASET_NAME)
	VAL_DATA = "data/{}.csv".format(DATASET_NAME)
else:
	RUN_FOLDER = "runs/"
	TRAIN_DATA = "data/{}_2000-2019.csv".format(DATASET_NAME)
	VAL_DATA = "data/{}_2020.csv".format(DATASET_NAME)

# Actions
ACTION_HOLD = 0
ACTION_BUY = 1
ACTION_SELL = 2

# DQN Settings
DQN_GAMMA = 0.99
DQN_TAU = 0.001
DQN_BATCH_SIZE = 8
DQN_EXPERIENCE_BUFFER_SIZE = 10000
DQN_EXPERIENCE_START_SIZE = 1000
DQN_LEARNING_RATE = 0.001
DQN_SOFT_UPDATE = True
# DQN_SYNC_TARGET = 1000
DQN_SYNC_TARGET = 100
DQN_EPSILON_DECAY_LAST_FRAME = 10**5
DQN_EPSILON_START = 1.0
DQN_EPSILON_FINAL = 0.02

# AC Settings
AC_LEARNING_RATE = 0.0005

# PPO Settings
# PPO_LEARNING_RATE = 0.003 # max
PPO_LEARNING_RATE = 0.001
# PPO_LEARNING_RATE = 0.000005 # min
PPO_GAMMA = 0.99
PPO_CLIP = 0.2
PPO_STEPS_PER_BATCH = EPISODE_LENGTH * 32
PPO_N_UPDATES_PER_ITERATION = 5

if _DQN_ == 1:
	LEARNING_RATE = DQN_LEARNING_RATE
if _AC_ == 1:
	LEARNING_RATE = AC_LEARNING_RATE
if _PPO_ == 1:
	LEARNING_RATE = PPO_LEARNING_RATE