# If a peer returns 0 results, wait this many seconds before asking it for anything else
EMPTY_PEER_RESPONSE_PENALTY = 15.0

# Picked a reorg number that is covered by a single skeleton header request,
# which covers about 6 days at 15s blocks
MAX_SKELETON_REORG_DEPTH = 35000

# The maximum number of headers that the backfill can sync in one uninterrupted stretch.
# Depending on the lag, the job may get paused but will continue until the current stretch
# has processed this number of headers.
MAX_BACKFILL_HEADERS_AT_ONCE = 100_000

# Estimated time in between each block
PREDICTED_BLOCK_TIME = 13

# How many headers/blocks should we queue up waiting to be persisted?
# This buffer size is estimated using: NUM_BLOCKS_PERSISTED_PER_SEC * BUFFER_SECONDS * MARGIN
#
# NUM_BLOCKS_PERSISTED_PER_SEC = 200
#   (rough estimate from personal NVMe SSD, with small blocks on Ropsten)
#
# BUFFER_SECONDS = 30
#   (this should allow plenty of time for peers to fill in the buffer during db writes)
#
HEADER_QUEUE_SIZE_TARGET = 6000

# How many blocks to persist at a time
# Only need a few seconds of buffer on the DB write side.
BLOCK_QUEUE_SIZE_TARGET = 1000

# How many blocks to import at a time
# Only need a few seconds of buffer on the DB side
# This is specifically for blocks where execution happens locally.
# So each block might have a pretty significant execution time, on
#   the order of seconds.
# This is also used during Beam sync, to limit how many previews are emitted at once
# If you increase the number too high, then your I/O latency can skyrocket,
#   causing a massive slowdown.
# Every block gets previewed, and a block only enters the queue if another block import
#   is active. So a queue size of 3 means that up to 4 previews are happening at once.
BLOCK_IMPORT_QUEUE_SIZE = 31
# This metric seems hard to pin down, we may have to expose it as a command line flag,
#   until we have a better mechanism for backpressure related to slowness in I/O.
