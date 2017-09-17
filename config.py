
# Ports for your workers
STRATUM_HOST = "0.0.0.0"
STRATUM_PORT = 8080

# Coin address where money goes. If you mine direct to the exchange, you MUST specify payment_id together with wallet of exchange.
WALLET = '47C6Q3YPA3BP4K33mS9imSF9P4igydxp9C845omejofSbgwegQrUXCaSmqLKMMzuFdHm2M7AwonzY8GmgmUk6aqDLyTHe8R'
# Only if you mine direct to the exchange
PAYMENT_ID = ''

# It's useful for individually monitoring and statistic.
# In your workers you have to use any number as username (without wallet!)
ENABLE_WORKER_ID = True
WORKER_ID_FROM_IP = False

# On DwarfPool you have option to monitor your workers via email.
# If WORKER_ID is enabled, you can monitor every worker/rig separately.
MONITORING = True
MONITORING_EMAIL = 'di4n007@gmail.com'

# Main pool
POOL_HOST = 'mine.moneropool.com'
POOL_PORT = 3333

# Failover pool
POOL_FAILOVER_ENABLE = True
POOL_HOST_FAILOVER = 'mine.moneropool.com'
POOL_PORT_FAILOVER = 8080

# ERROR, INFO, DEBUG
LOGLEVEL = 'DEBUG'
DEBUG = True
LOGFILE = "logfile.log"
