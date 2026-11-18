# Notebook execution order

Run notebooks in numerical order. Each notebook should state its objective, inputs, outputs, decisions, and validation checks.

1. `00_project_setup.ipynb` — environment and dataset discovery
2. `01_data_understanding.ipynb` — files, schema, data dictionary, target feasibility
3. `02_data_quality.ipynb` — missingness, duplicates, invalid values, outliers
4. `03_eda.ipynb` — univariate and bivariate analysis
5. `04_data_cleaning.ipynb` — reproducible cleaning pipeline
6. `05_feature_engineering.ipynb` — leakage-aware features
7. `06_train_test_split.ipynb` — split strategy and leakage checks
8. `07_baseline_model.ipynb` — baseline regression
9. `08_model_training.ipynb` — candidate models and tuning
10. `09_model_evaluation.ipynb` — final evaluation and error analysis
