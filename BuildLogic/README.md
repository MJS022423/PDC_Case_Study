# BuildConnect Logistics - Parallel and Distributed Computing Case Study

A comprehensive solution for optimizing operations of BuildConnect Logistics using parallel and distributed computing techniques.

## Project Overview

This project addresses Challenge 3: **Fraud Detection in High-Volume Transactions** (with infrastructure for Challenges 1 & 2) from the PDC Finals Case Study.

### Challenge 3: Fraud Detection System
Detects fraudulent transactions in high-volume data using distributed machine learning, considering:
- Transaction frequency and patterns
- Transaction amounts relative to history
- Time of day anomalies
- Customer behavior analysis

## Project Structure

```
Project_2/
├── src/
│   ├── challenge3_fraud/          # Fraud detection implementation
│   ├── challenge1_inventory/      # Inventory optimization (structure ready)
│   ├── challenge2_routing/        # Route optimization (structure ready)
│   ├── parallel/                  # Parallel computing implementations
│   └── utils/                     # Shared utilities
├── notebooks/                     # Jupyter notebooks for analysis
├── data/                          # CSV datasets
├── docs/                          # Documentation
├── tests/                         # Unit and integration tests
├── scripts/                       # Execution scripts
└── reports/                       # Results and benchmark reports
```

## Setup Instructions

### Prerequisites
- Python 3.8+
- pip or conda

### Installation

1. Clone or navigate to the project directory
2. Install dependencies:
```bash
pip install -r requirements.txt
```

3. Configure paths in `src/config.py` as needed

## Usage

### Running Fraud Detection
```bash
python scripts/run_challenge3.py
```

### Running Notebooks
```bash
jupyter notebook notebooks/
```

### Running Tests
```bash
pytest tests/
```

## Key Features

- **Scalable Fraud Detection**: Handles 50,000+ transactions daily
- **Distributed Processing**: Support for Dask, Spark, and Ray
- **Real-time Scoring**: Near real-time fraud risk assessment
- **Comprehensive Logging**: Full audit trail and debugging
- **Performance Benchmarks**: Speedup and resource utilization metrics

## Technologies Used

- **Python 3.x**
- **scikit-learn**: Machine learning
- **Dask/PySpark/Ray**: Distributed computing
- **Pandas**: Data processing
- **Matplotlib/Plotly**: Visualization
- **Joblib**: Model serialization

## Files

- `fraud_detection_train_model.ipynb` - Model training and evaluation
- `forecast_train_model.ipynb` - Demand forecasting (Challenge 1)
- `src/challenge3_fraud/fraud_detector.py` - Main fraud detection implementation
- `src/outputs/models/fraud_model.pkl` - Trained model artifact

## Documentation

See the `docs/` directory for detailed documentation:
- `CASE_STUDY_DOCUMENTATION.md` - Full case study requirements
- `TECHNICAL_REPORT.md` - Design and findings
- `DESIGN_DOCUMENT.md` - Architecture details

## Team & Contributions

(To be updated with team member names and roles)

## Performance Results

(Benchmarks and results to be populated in `reports/`)

---

**Course**: Parallel and Distributed Computing (PDC)  
**Institution**: [Your Institution]  
**Duration**: 2 weeks
