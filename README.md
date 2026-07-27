# Drift Diffusion Model Analysis

This repository contains Python scripts for analyzing behavioral reaction-time data using a Drift Diffusion Model (DDM) approach.

## What is included

- Data inspection and preprocessing scripts
- DDM model fitting scripts for different experimental conditions
- Plotting scripts for emotion, difficulty, and interaction effects
- A basic test script for the PyDDM dependency

## Privacy note

The raw research data files in this workspace are intentionally excluded from GitHub by the repository ignore rules. The CSV files remain on your local machine only and are not pushed to the remote repository.

If you want to run the scripts locally, keep your private CSV files in the project root with the expected names, such as:

- P2_all.csv
- P3_all.csv
- P4_all.csv
- UPDATED_DDM_results_P2.csv

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run the scripts locally:

```bash
python inspect_data.py
python model_script2.py
```

## Repository structure

- inspect_data.py: basic inspection of the input dataset
- model_script2.py: main DDM analysis script
- plot1_emotion.py, plot2_difficulty.py, plot3_interaction.py: visualization scripts
- test_pyddm.py: basic PyDDM sanity check

## Publishing to GitHub

After initializing the repository locally, push it to GitHub using:

```bash
git branch -M main
git remote add origin <your-github-repo-url>
git push -u origin main
```
