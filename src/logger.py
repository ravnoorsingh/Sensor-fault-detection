# Loggging is for tracking events that happen when application run.
# it helps in debugging and monitoring the application.

import logging
import os
from datetime import datetime

LOG_FILE = f"{datetime.now().strftime('%m_%d_%Y_%H_%M_%S')}.log"

logs_path = os.path.join(os.getcwd(), "logs", LOG_FILE)

os.makedirs(logs_path, exist_ok=True)  # Create logs directory if it doesn't exist

LOG_FILE_PATH = os.path.join(logs_path, LOG_FILE)

logging.basicConfig(
    filename=LOG_FILE_PATH,
    format='[%(asctime)s] %(lineno)d - %(levelname)s - %(message)s',
    level=logging.INFO
)

# https://chatgpt.com/share/68787666-1980-800d-a211-cce255b28696