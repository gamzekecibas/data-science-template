# data-science-template
Template repo for data science projects

```bash
project_name/
│
├── data/
│   ├── raw/
│   │   ├── dataset.csv          # Original data
│   │   └── ...
│   ├── processed/
│   │   ├── clean_data.csv      # Processed data
│   │   └── ...
│
├── notebooks/
│   ├── exploratory_data_analysis.ipynb
│   ├── data_preprocessing.ipynb
│   ├── modeling.ipynb
│   └── ...
│
├── src/
│   ├── __init__.py
│   ├── data/
│   │   ├── __init__.py
│   │   ├── data_loading.py     # Functions for loading data
│   │   ├── data_preprocessing.py
│   │   └── ...
│   ├── models/
│   │   ├── __init__.py
│   │   ├── model.py            # Machine learning models
│   │   └── ...
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── helpers.py          # Helper functions
│   │   └── ...
│
├── requirements.txt            # Project dependencies
├── README.md                   # Project documentation
├── config.yaml                 # Configuration file
├── pre-commit-config.yaml      # Pre-commit configuration file for organized commits
├── .gitignore                  # Git ignore file
├── LICENSE                     # License information
```
