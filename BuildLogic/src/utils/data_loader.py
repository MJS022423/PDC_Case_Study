"""
Data loading utilities for BuildConnect Logistics datasets.
"""

import pandas as pd
from pathlib import Path
import logging

logger = logging.getLogger(__name__)


class DataLoader:
    """Load and basic preprocessing of BuildConnect data files."""
    
    def __init__(self, data_dir):
        """
        Initialize DataLoader with data directory path.
        
        Args:
            data_dir: Path to directory containing CSV files
        """
        self.data_dir = Path(data_dir)
    
    def load_transactions(self):
        """Load transactions.csv file."""
        path = self.data_dir / "transactions.csv"
        logger.info(f"Loading transactions from {path}")
        return pd.read_csv(path)
    
    def load_branches(self):
        """Load branches.csv file."""
        path = self.data_dir / "branches.csv"
        logger.info(f"Loading branches from {path}")
        return pd.read_csv(path)
    
    def load_products(self):
        """Load products.csv file."""
        path = self.data_dir / "products.csv"
        logger.info(f"Loading products from {path}")
        return pd.read_csv(path)
    
    def load_trucks(self):
        """Load trucks.csv file."""
        path = self.data_dir / "trucks.csv"
        logger.info(f"Loading trucks from {path}")
        return pd.read_csv(path)
    
    def load_inventory(self):
        """Load inventory.csv file."""
        path = self.data_dir / "inventory.csv"
        logger.info(f"Loading inventory from {path}")
        return pd.read_csv(path)
    
    def load_delivery_logs(self):
        """Load delivery_logs.csv file."""
        path = self.data_dir / "delivery_logs.csv"
        logger.info(f"Loading delivery logs from {path}")
        return pd.read_csv(path)
    
    def load_all(self):
        """Load all CSV files into a dictionary."""
        return {
            'transactions': self.load_transactions(),
            'branches': self.load_branches(),
            'products': self.load_products(),
            'trucks': self.load_trucks(),
            'inventory': self.load_inventory(),
            'delivery_logs': self.load_delivery_logs(),
        }
