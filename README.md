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

## License

This project is licensed under the MIT License.

Author: Natnahom Asfaw
Date: 26/12/2024