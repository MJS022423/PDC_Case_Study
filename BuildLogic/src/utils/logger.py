"""
Logging configuration for the project.
"""

import logging
import logging.handlers
from pathlib import Path
from src.config import LOG_LEVEL, LOG_FORMAT


def setup_logger(name, log_file=None):
    """
    Configure and return a logger instance.
    
    Args:
        name: Logger name (typically __name__)
        log_file: Optional log file path
        
    Returns:
        logging.Logger: Configured logger instance
    """
    logger = logging.getLogger(name)
    logger.setLevel(LOG_LEVEL)
    
    # Console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(LOG_LEVEL)
    formatter = logging.Formatter(LOG_FORMAT)
    console_handler.setFormatter(formatter)
    logger.addHandler(console_handler)
    
    # File handler (optional)
    if log_file:
        log_path = Path(log_file)
        log_path.parent.mkdir(parents=True, exist_ok=True)
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(LOG_LEVEL)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)
    
    return logger
