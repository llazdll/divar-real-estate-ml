# Divar Real Estate Price Prediction

An end-to-end machine learning project for analyzing Persian real-estate advertisements and predicting **asking prices**.

> Important: the target represents advertised/listed prices, not verified final transaction prices.

## Project scope
- Data acquisition and understanding
- Data quality assessment
- Exploratory data analysis
- Cleaning and feature engineering
- Baseline regression
- Model training, tuning, and evaluation
- Reproducible reporting

## Environment
- Kaggle Notebooks
- Python
- Pandas / NumPy
- Scikit-learn
- Matplotlib / Seaborn

## Repository structure
```text
.
├── configs/                 # Project configuration
├── data/                    # Local data only; not committed
│   ├── raw/
│   ├── interim/
│   └── processed/
├── notebooks/               # Ordered analysis workflow
├── reports/                 # Figures, tables, and reports
├── src/                     # Reusable project code
│   ├── data/
│   ├── features/
│   └── models/
├── tests/                   # Basic project tests
├── PROJECT_LOG.md
├── requirements.txt
└── README.md
```

## Dataset
Source: [Divar Real Estate Dataset (1M Persian Property Ads)](https://www.kaggle.com/datasets/valakhorasani/divar-real-estate-dataset1m-persian-property-ads)

Attach the dataset to a Kaggle Notebook using **Add Input**. Do not upload the raw dataset to this GitHub repository.

## Kaggle workflow
1. Create a Kaggle Notebook.
2. Add the dataset through **Add Input**.
3. Upload or clone this repository into the notebook environment.
4. Set `data.input_dir` in `configs/config.yaml` or pass the dataset directory to the loader.
5. Save generated outputs under `/kaggle/working/` and use **Save Version** to preserve notebook outputs.

## Target definition
The initial modeling task is regression for residential property sale advertisements. The exact target column, eligible listing types, currency/unit conventions, and filters must be confirmed during Phase 01 before modeling.

## Reproducibility
- Keep raw data unchanged.
- Record filtering and cleaning decisions.
- Split data before fitting preprocessing transformations.
- Fit imputers, encoders, and scalers on training data only.
- Avoid leakage from identifiers, post-publication fields, or target-derived features.
- Compare models against a simple baseline.

## Project status
Phase 00 — Project Initialization: scaffold created; environment and dataset paths must be verified in Kaggle.
