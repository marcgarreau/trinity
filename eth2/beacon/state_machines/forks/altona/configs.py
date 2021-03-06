from eth_utils import decode_hex

from eth2.beacon.constants import GWEI_PER_ETH
from eth2.beacon.typing import Gwei, Second, Version
from eth2.configs import Eth2Config

ALTONA_CONFIG = Eth2Config(
    # Misc
    MAX_COMMITTEES_PER_SLOT=2 ** 6,  # (= 64) committees
    TARGET_COMMITTEE_SIZE=2 ** 7,  # (= 128) validators
    MAX_VALIDATORS_PER_COMMITTEE=2 ** 11,  # (= 2,048) validators
    MIN_PER_EPOCH_CHURN_LIMIT=2 ** 2,
    CHURN_LIMIT_QUOTIENT=2 ** 16,
    SHUFFLE_ROUND_COUNT=90,
    HYSTERESIS_QUOTIENT=4,
    HYSTERESIS_DOWNWARD_MULTIPLIER=1,
    HYSTERESIS_UPWARD_MULTIPLIER=5,
    # Genesis
    MIN_GENESIS_ACTIVE_VALIDATOR_COUNT=640,
    MIN_GENESIS_TIME=1593433800,
    # Gwei values
    MIN_DEPOSIT_AMOUNT=Gwei(2 ** 0 * GWEI_PER_ETH),  # (= 1,000,000,000) Gwei
    MAX_EFFECTIVE_BALANCE=Gwei(2 ** 5 * GWEI_PER_ETH),  # (= 32,000,000,00) Gwei
    EJECTION_BALANCE=Gwei(2 ** 4 * GWEI_PER_ETH),  # (= 16,000,000,000) Gwei
    EFFECTIVE_BALANCE_INCREMENT=Gwei(2 ** 0 * GWEI_PER_ETH),  # (= 1,000,000,000) Gwei
    # Initial values
    GENESIS_FORK_VERSION=Version(b"\x00000121"),
    BLS_WITHDRAWAL_PREFIX=b"\x00",
    # Time parameters
    GENESIS_DELAY=Second(172800),
    SECONDS_PER_SLOT=Second(12),  # seconds
    MIN_ATTESTATION_INCLUSION_DELAY=2 ** 0,  # (= 1) slots
    SLOTS_PER_EPOCH=2 ** 5,  # (= 32) slots
    MIN_SEED_LOOKAHEAD=2 ** 0,  # (= 1) epochs
    MAX_SEED_LOOKAHEAD=2 ** 2,  # (= 4) epochs
    SLOTS_PER_HISTORICAL_ROOT=2 ** 13,  # (= 8,192) slots
    MIN_VALIDATOR_WITHDRAWABILITY_DELAY=2 ** 8,  # (= 256) epochs
    SHARD_COMMITTEE_PERIOD=2 ** 8,  # (= 256) epochs
    MIN_EPOCHS_TO_INACTIVITY_PENALTY=2 ** 2,
    # State list lengths
    EPOCHS_PER_ETH1_VOTING_PERIOD=32,
    EPOCHS_PER_HISTORICAL_VECTOR=2 ** 16,
    EPOCHS_PER_SLASHINGS_VECTOR=2 ** 13,
    HISTORICAL_ROOTS_LIMIT=2 ** 24,
    VALIDATOR_REGISTRY_LIMIT=2 ** 40,
    # Reward and penalty quotients
    BASE_REWARD_FACTOR=2 ** 6,  # (= 64)
    WHISTLEBLOWER_REWARD_QUOTIENT=2 ** 9,  # (= 512)
    PROPOSER_REWARD_QUOTIENT=2 ** 3,
    INACTIVITY_PENALTY_QUOTIENT=2 ** 24,  # (= 16,777,216)
    MIN_SLASHING_PENALTY_QUOTIENT=2 ** 5,
    # Max operations per block
    MAX_PROPOSER_SLASHINGS=2 ** 4,  # (= 16)
    MAX_ATTESTER_SLASHINGS=2 ** 1,  # (= 2)
    MAX_ATTESTATIONS=2 ** 7,  # (= 128)
    MAX_DEPOSITS=2 ** 4,  # (= 16)
    MAX_VOLUNTARY_EXITS=2 ** 4,  # (= 16)
    # Fork choice
    SAFE_SLOTS_TO_UPDATE_JUSTIFIED=8,
    # Deposit contract
    DEPOSIT_CONTRACT_ADDRESS=decode_hex(
        "0x1234567890123456789012345678901234567890"
    ),  # TBD
)
