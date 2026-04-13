"""ML-OPTIMIZED + FAST PARALLEL stock service (REALTIME SAFE)"""

from typing import List, Dict, Any
from data_processing.loaders import StockDataLoader
from models.ml_model import StockMLModel
from concurrent.futures import ThreadPoolExecutor
import logging

logger = logging.getLogger(__name__)


class StockService:
    """Ultra-fast stock service with ML + optimized parallel processing"""

    def __init__(self, loader: StockDataLoader):
        self.loader = loader

        self.stocks = self.loader.get_stocks_list()
        self.data = self.loader.stock_data

        # 🔥 worker control
        self.workers = 4

        # 🔥 TRAIN MODEL ONCE (CRITICAL FIX)
        self.model = StockMLModel()
        self._train_model()

    # ========================
    # ML TRAINING (ONCE ONLY)
    # ========================

    def _train_model(self):
        try:
            self.model.train(self.data)
            logger.info("✅ ML model trained ONCE (optimized)")
        except Exception as e:
            logger.error(f"ML training failed: {e}")

    # ========================
    # WORKER CONTROL
    # ========================

    def set_workers(self, workers: int):
        try:
            workers = int(workers)
            if workers <= 0:
                workers = 1
            self.workers = workers
            logger.info(f"⚡ Workers updated → {self.workers}")
        except Exception as e:
            logger.error(f"Invalid workers value: {e}")

    def get_workers(self) -> int:
        return self.workers

    # ========================
    # INTERNAL
    # ========================

    def _get_index(self, index, length):
        if index is not None:
            return min(max(index, 0), length - 1)
        return length - 1

    def _process_single_stock(self, stock, index):
        """🔥 FAST worker (NO TRAINING HERE)"""
        try:
            company = stock["company"]
            data = self.data.get(company)

            if not data:
                return None

            prices = data["prices"]
            length = data["length"]

            idx = self._get_index(index, length)
            current_price = prices[idx]

            start = max(0, idx - 10)
            relevant_prices = prices[start:idx + 1]

            # 🔥 USE PRETRAINED MODEL
            analysis = self.model.predict(relevant_prices)

            return {
                "company": company,
                "name": stock["name"],
                "price": round(current_price, 2),
                "confidence": analysis["confidence"],
                "action": analysis["action"]
            }

        except Exception as e:
            logger.error(f"Error processing stock {stock}: {e}")
            return None

    # ========================
    # PARALLEL CORE (FAST)
    # ========================

    def get_all_stocks(self, index: int = None) -> List[Dict[str, Any]]:
        """
        ⚡ FAST PARALLEL (THREAD-BASED, REALTIME SAFE)
        """

        with ThreadPoolExecutor(max_workers=self.workers) as executor:
            results = list(executor.map(
                lambda stock: self._process_single_stock(stock, index),
                self.stocks
            ))

        return [r for r in results if r is not None]

    # ========================
    # SINGLE STOCK
    # ========================

    def get_single_stock(self, company: str, index: int = None):
        data = self.data.get(company)
        if not data:
            return None

        prices = data["prices"]
        length = data["length"]

        idx = self._get_index(index, length)
        current_price = prices[idx]

        start = max(0, idx - 10)
        relevant_prices = prices[start:idx + 1]

        analysis = self.model.predict(relevant_prices)

        return {
            "company": company,
            "price": round(current_price, 2),
            "confidence": analysis["confidence"],
            "action": analysis["action"]
        }

    # ========================
    # HISTORY
    # ========================

    def get_stock_history(self, company: str, limit: int = 100, index: int = None):
        data = self.data.get(company)
        if not data:
            return []

        prices = data["prices"]
        length = data["length"]

        end = self._get_index(index, length)
        start = max(0, end - limit)

        return [
            {"index": i, "close": prices[i]}
            for i in range(start, end + 1)
        ]

    # ========================
    # PRICE
    # ========================

    def get_price_at_index(self, company: str, index: int) -> float:
        return self.loader.get_price_at_index(company, index)