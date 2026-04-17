
#!/usr/bin/env python
"""
BuildConnect Logistics - Fraud Detection System
Main entry point for Challenge 3 execution
"""

import sys
from pathlib import Path

# Add src to path
sys.path.insert(0, str(Path(__file__).parent / "src"))

from src.utils.logger import setup_logger
from src.challenge3_fraud.fraud_detector import FraudDetector, FeatureEngineer
from src.utils.data_loader import DataLoader
from src.config import RAW_DATA_DIR, FRAUD_MODEL_PATH, FRAUD_THRESHOLD

logger = setup_logger(__name__)


def main():
    """Main execution function for fraud detection system."""
    logger.info("=" * 80)
    logger.info("BuildConnect Logistics - Fraud Detection System")
    logger.info("=" * 80)
    
    try:
        # Load data
        logger.info("Loading transaction data...")
        loader = DataLoader(RAW_DATA_DIR)
        transactions_df = loader.load_transactions()
        logger.info(f"Loaded {len(transactions_df):,} transactions")
        
        # Feature engineering
        logger.info("Extracting temporal features...")
        df = FeatureEngineer.extract_temporal_features(transactions_df)
        
        logger.info("Encoding categorical features...")
        df, _ = FeatureEngineer.encode_categorical_features(df)
        
        logger.info("Creating fraud labels...")
        df = FeatureEngineer.create_fraud_labels(df)
        
        # Load or train model
        detector = FraudDetector()
        if FRAUD_MODEL_PATH.exists():
            logger.info("Loading pre-trained model...")
            detector.load_model(FRAUD_MODEL_PATH)
        else:
            logger.info("Training fraud detection model...")
            features = [
                'branch_encoded', 'product_encoded', 'customer_encoded',
                'quantity', 'total_amount', 'hour', 'dayofweek', 'month'
            ]
            df_clean = df[['transaction_id'] + features + ['fraud']].dropna()
            detector.train(df_clean)
            FRAUD_MODEL_PATH.parent.mkdir(parents=True, exist_ok=True)
            detector.save_model(FRAUD_MODEL_PATH)
            logger.info(f"Model saved to {FRAUD_MODEL_PATH}")
        
        # Score transactions
        logger.info("Scoring transactions for fraud risk...")
        features = [
            'branch_encoded', 'product_encoded', 'customer_encoded',
            'quantity', 'total_amount', 'hour', 'dayofweek', 'month'
        ]
        df_clean = df[['transaction_id'] + features + ['fraud']].dropna()
        X = df_clean[features]
        fraud_scores = detector.predict(X)
        
        # Report
        logger.info("\n" + "=" * 80)
        logger.info("FRAUD DETECTION SUMMARY")
        logger.info("=" * 80)
        fraud_count = (fraud_scores > FRAUD_THRESHOLD).sum()
        logger.info(f"Transactions analyzed: {len(fraud_scores):,}")
        logger.info(f"Flagged as fraudulent: {fraud_count:,} ({fraud_count/len(fraud_scores)*100:.2f}%)")
        logger.info(f"Fraud threshold: {FRAUD_THRESHOLD}")
        logger.info("=" * 80 + "\n")
        
        return 0
        
    except Exception as e:
        logger.error(f"Error: {str(e)}", exc_info=True)
        return 1


if __name__ == "__main__":
    sys.exit(main())