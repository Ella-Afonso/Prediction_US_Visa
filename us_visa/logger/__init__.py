import logging
import os
from from_root import from_root
from datetime import datetime

# Generate a log file name based on the current date and time
LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

# Directory where logs will be stored
log_dir = 'logs'

# Complete path for the log file
logs_path = os.path.join(from_root(), log_dir, LOG_FILE)

# Ensure the directory exists
os.makedirs(os.path.join(from_root(), log_dir), exist_ok=True)

# Configure the logging
logging.basicConfig(
    filename=logs_path,
    format="[ %(asctime)s ] %(name)s - %(levelname)s - %(message)s",
    level=logging.DEBUG,
)

# Create a logger instance for testing
logger = logging.getLogger(__name__)
logger.info("Logger has been configured and is ready to use.")
