This is week-2 project

# Insurance EDA Project

This project focuses on exploratory data analysis of insurance policy data from Feb 2014 to Aug 2015.

## Structure

- `data/`: Raw data files
- `notebooks/`: Jupyter notebooks for analysis
- `src/`: Source code for data processing and analysis
- `.github/`: CI/CD workflows

## Getting Started

1. Clone the repo
2. Install dependencies: `pip install -r requirements.txt`
3. Run analysis scripts from the `src` directory.

## Task 2: Data Version Control (DVC)
# Overview
In this task, we implemented Data Version Control (DVC) to manage our datasets efficiently. DVC helps in tracking changes in data files, ensuring reproducibility, and facilitating collaboration among team members.

Steps Implemented
DVC Installation
Installed DVC using pip:
bash

pip install dvc
DVC Initialization
Initialized DVC in the project directory:
bash

dvc init
Local Remote Storage Setup
Created a local storage directory for DVC:
bash

mkdir /path/to/your/local/storage
Configured the local storage as the default DVC remote:
bash

dvc remote add -d localstorage /path/to/your/local/storage
Data Tracking
Added the dataset (data.csv) to DVC for tracking:
bash

dvc add data.csv
Version Control
Committed the changes, including the .dvc files, to the Git repository:
bash

git add data.csv.dvc .gitignore
git commit -m "Track data.csv with DVC"
Data Push
Pushed the tracked data to the local remote storage:
bash

dvc push
# Benefits of Using DVC
Versioning: Keeps track of different versions of datasets, allowing for easy rollback and comparison.
Reproducibility: Ensures that all team members can access the same data versions and processing environments.
Collaboration: Facilitates collaborative work by managing data separately from code.
Usage
To retrieve the data and recreate the environment, clone the repository and run:

git clone <repository-url>
cd <repository-directory>
dvc pull

## Task 3: A/B Hypothesis Testing
# Overview
In this task, we conducted A/B hypothesis testing to analyze the impact of various features on risk and profit margins. This involves formulating null hypotheses and using statistical tests to validate them.

# Null Hypotheses
H0: There are no risk differences across provinces.
H0: There are no risk differences between zip codes.
H0: There are no significant margin (profit) differences between zip codes.
H0: There are no significant risk differences between Women and Men.
# Steps Implemented
Data Segmentation: The dataset was segmented into control and test groups based on client features (e.g., IsVATRegistered).
Statistical Testing:
Chi-Squared Test: Used to analyze categorical data and test risk differences across provinces.
T-Test: Used to compare profit margins between different groups.
Analysis and Reporting: Results were documented, and findings were summarized to provide insights into the hypotheses.
Benefits of A/B Testing
Data-Driven Decisions: Helps in making informed decisions based on statistical evidence.
Performance Evaluation: Evaluates the effectiveness of different strategies or features.
Risk Management: Identifies potential risks associated with different client demographics or features.

## Task 4: Model Evaluation and Performance Metrics

### Overview
In this task, we focused on evaluating the performance of our models used in the insurance data analysis. This includes assessing how well the models predict outcomes based on various features within the dataset.

### Objectives
1. **Model Selection:** Choose appropriate models for predicting outcomes such as claims and premium amounts.
2. **Performance Metrics:** Define and compute key performance metrics to evaluate model effectiveness.

### Steps Implemented
1. **Data Preparation:**
   - Cleaned and preprocessed the dataset to handle missing values and categorical variables.
   - Split the dataset into training and testing sets to ensure unbiased model evaluation.

2. **Model Training:**
   - Trained multiple models, such as:
     - Linear Regression for predicting premium amounts.
     - Decision Trees for classifying claims.
     - Random Forest for improved accuracy and robustness.

3. **Model Evaluation:**
   - Used metrics such as:
     - **Accuracy:** To evaluate classification performance.
     - **Precision and Recall:** To understand the trade-off between false positives and false negatives.
     - **Mean Absolute Error (MAE) and Root Mean Squared Error (RMSE):** For regression performance evaluation.

4. **Model Comparison:**
   - Compared the performance of different models using cross-validation to determine the best-performing model based on the defined metrics.

5. **Hyperparameter Tuning:**
   - Conducted hyperparameter tuning using Grid Search or Random Search to optimize model performance.

### Benefits of Model Evaluation
- **Improved Decision Making:** Better understanding of model performance aids in making informed decisions regarding policy and risk assessments.
- **Enhanced Accuracy:** Identifying the best model leads to more accurate predictions and insights.
- **Resource Optimization:** Efficiently allocates resources by understanding which models work best for specific tasks.

### Conclusion
This task emphasizes the importance of rigorous model evaluation in achieving reliable and actionable insights from the insurance dataset. By utilizing the right metrics and models, we can significantly enhance our predictive capabilities.

## License

This project is licensed under the MIT License.

Author: Natnahom Asfaw
Date: 26/12/2024