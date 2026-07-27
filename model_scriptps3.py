# import pandas as pd
# import pyddm
# from pyddm import Sample

# # Load data
# df = pd.read_csv("P3_all.csv")

# # Rename columns
# df = df.rename(columns={
#     "Response Time (ms)": "rt",
#     "Correctness": "correct"
# })

# # Create Sample object
# sample = Sample.from_pandas_dataframe(
#     df,
#     rt_column_name="rt",
#     choice_column_name="correct"
# )

# print("Sample created successfully!")

# # Define model with FREE parameters
# model = pyddm.gddm(
#     drift="d",
#     bound="B",
#     starting_position="x0",
#     nondecision="ndt",
#     noise=1,
#     parameters={
#         "d": (-5, 5),
#         "B": (0.3, 3),
#         "x0": (-0.8, 0.8),
#         "ndt": (0, 0.5)
#     }
# )

# print("Fitting model...")

# # Fit model
# model.fit(sample, verbose=False)

# print("\nModel fitted successfully!\n")

# # print("\nEstimated Parameters:")
# # print(model.parameters())






# #UPDATED SUBMISSION, 08.03.2026, est. time taken overall: 10:23 - 02:47

# """
# Drift Diffusion Model Parameter Estimation
# Author: Nishita Das
# Project: Effects of Emotions and Anxiety on Visual Perceptual Decision Making

# This script performs DDM parameter estimation using PyDDM.

# Steps included:
# 1. Data preprocessing
# 2. Baseline model fitting
# 3. Emotion-based parameter estimation
# 4. Difficulty-based parameter estimation
# 5. Emotion × Difficulty interaction analysis

# Parameters estimated:
# - Drift rate (v)
# - Boundary separation (a)
# - Starting point bias (z)
# - Non-decision time (t0)

# Encoded Emotion values represent the following emotional conditions:

# 0 - Anger #old_neutral
# 1 - Disgust
# 2 - Neutral #old_anger
# """

# """
# DDM_Parameter_Estimation.py
# -------------------------------------------------------------
# Drift Diffusion Model (DDM) Parameter Estimation using PyDDM

# This script performs cognitive modelling on behavioural
# reaction time data using the Drift Diffusion Model.

# Structure of the script:
# 1. Import Libraries
# 2. Load Dataset
# 3. Preprocess Data
# 4. Baseline Model (All Trials)
# 5. Task A - Emotion-based Analysis
# 6. Task B - Difficulty-based Analysis
# 7. Task C - Emotion × Difficulty Analysis
# 8. Print / Store Results

# """


# # 1. IMPORT LIBRARIES


# import pandas as pd
# import pyddm
# from pyddm import Sample


# # 2. LOAD DATASET


# # Load behavioural dataset for participant
# df = pd.read_csv("P3_all.csv")

# print("Dataset loaded successfully.\n")


# # 3. PREPROCESS DATA


# # Rename columns so they match PyDDM requirements
# df = df.rename(columns={
#     "Response Time (ms)": "rt",
#     "Correctness": "correct"
# })

# # Convert reaction time from milliseconds to seconds
# # (DDM models typically assume seconds)
# df["rt"] = df["rt"] / 1000

# # Check emotion labels present in dataset
# print("Unique Face Emotion labels:")
# print(df["Encoded Emotion"].unique(), "\n")

# # Check difficulty labels
# print("Unique difficulty levels:")
# print(df["coh"].unique(), "\n")


# # Helper Function: Fit DDM Model


# def fit_ddm(dataframe, label):
#     """
#     Fits a Drift Diffusion Model to the provided dataframe.

#     Parameters
#     ----------
#     dataframe : pandas.DataFrame
#         Subset of behavioural trials
#     label : str
#         Condition name (for reporting)

#     Returns
#     -------
#     dict
#         Estimated DDM parameters
#     """

#     # Convert dataframe to PyDDM Sample object
#     sample = Sample.from_pandas_dataframe(
#         dataframe,
#         rt_column_name="rt",
#         choice_column_name="correct"
#     )

#     # Define generalized DDM model with free parameters
#     model = pyddm.gddm(
#         drift="d",
#         bound="B",
#         starting_position="x0",
#         nondecision="ndt",
#         noise=1,
#         parameters={
#             "d": (-5, 5),      # drift rate
#             "B": (0.3, 3),     # decision boundary
#             "x0": (-0.8, 0.8), # starting bias
#             "ndt": (0, 0.5)    # non-decision time
#         }
#     )

#     print(f"Fitting DDM model for: {label}")

#     # Fit model
#     model.fit(sample, verbose=False)

#     params = model.parameters()

#     print(f"Finished fitting: {label}\n")

#     return params


# # 4. BASELINE MODEL (ALL TRIALS)

# print("Running Baseline Model (All Trials)\n")

# baseline_params = fit_ddm(df, "Baseline (All Trials)")


# # 5. TASK A – EMOTION-BASED ANALYSIS


# print("Running Emotion-Based Analysis\n")

# emotion_results = {}

# emotions = df["Encoded Emotion"].unique()

# for emotion in emotions:

#     subset = df[df["Encoded Emotion"] == emotion]

#     params = fit_ddm(subset, f"Emotion: {emotion}")

#     emotion_results[emotion] = params



# # 6. TASK B – DIFFICULTY-BASED ANALYSIS


# print("Running Difficulty-Based Analysis\n")

# difficulty_results = {}

# difficulties = df["coh"].unique()

# for diff in difficulties:

#     subset = df[df["coh"] == diff]

#     params = fit_ddm(subset, f"Difficulty: {diff}")

#     difficulty_results[diff] = params



# # 7. TASK C – EMOTION × DIFFICULTY ANALYSIS

# print("Running Emotion × Difficulty Interaction Analysis\n")

# interaction_results = {}

# for emotion in emotions:
#     for diff in difficulties:

#         subset = df[
#             (df["Encoded Emotion"] == emotion) &
#             (df["coh"] == diff)
#         ]

#         # Skip empty conditions
#         if len(subset) < 10:
#             continue

#         label = f"{emotion} | {diff}"

#         params = fit_ddm(subset, label)

#         interaction_results[label] = params



# # 8. PRINT / STORE ALL RESULTS


# print("\n===================================================")
# print("FINAL DDM PARAMETER ESTIMATES")
# print("===================================================\n")

# print("Baseline Model:")
# print(baseline_params, "\n")

# print("Emotion-Based Results:")
# for k, v in emotion_results.items():
#     print(k, ":", v)
# print()

# print("Difficulty-Based Results:")
# for k, v in difficulty_results.items():
#     print(k, ":", v)
# print()

# print("Emotion × Difficulty Results:")
# for k, v in interaction_results.items():
#     print(k, ":", v)
# print()

# # Optional: Save results to CSV
# results_df = []

# for key, val in emotion_results.items():
#     row = {"Condition": f"Emotion-{key}", **val}
#     results_df.append(row)

# for key, val in difficulty_results.items():
#     row = {"Condition": f"Difficulty-{key}", **val}
#     results_df.append(row)

# for key, val in interaction_results.items():
#     row = {"Condition": f"Interaction-{key}", **val}
#     results_df.append(row)

# results_df = pd.DataFrame(results_df)

# results_df.to_csv("DDM_results_summary.csv", index=False)

# print("Results saved to: DDM_results_summary.csv")

















#24-03-2026, 02:47
# UPDATED SUBMISSION FOR P3
"""
Drift Diffusion Model Parameter Estimation
Author: Nishita Das
Participant: P3

This script performs DDM parameter estimation using PyDDM.

Outputs:
- Clean CSV file for submission (NO errors)
- Parameters: Drift (v), Boundary (a), Starting Point (z), Non-decision Time (Ter)
"""

# ==============================
# 1. IMPORT LIBRARIES
# ==============================

import pandas as pd
import pyddm
from pyddm import Sample


# ==============================
# 2. LOAD DATASET
# ==============================

df = pd.read_csv("P3_all.csv")   # <-- change only filename

print("Dataset loaded successfully.\n")


# ==============================
# 3. PREPROCESS DATA
# ==============================

df = df.rename(columns={
    "Response Time (ms)": "rt",
    "Correctness": "correct"
})

df["rt"] = df["rt"] / 1000  # ms → seconds

print("Unique Face Emotion labels:")
print(df["Encoded Emotion"].unique(), "\n")

print("Unique difficulty levels:")
print(df["coh"].unique(), "\n")


# ==============================
# 4. HELPER FUNCTION
# ==============================

def fit_ddm(dataframe, label):

    sample = Sample.from_pandas_dataframe(
        dataframe,
        rt_column_name="rt",
        choice_column_name="correct"
    )

    model = pyddm.gddm(
        drift="d",
        bound="B",
        starting_position="x0",
        nondecision="ndt",
        noise=1,
        parameters={
            "d": (-5, 5),
            "B": (0.3, 3),
            "x0": (-0.8, 0.8),
            "ndt": (0, 0.5)
        }
    )

    print(f"Fitting DDM model for: {label}")
    model.fit(sample, verbose=False)

    print(f"Finished fitting: {label}\n")

    return model.parameters()


# ==============================
# 5. BASELINE MODEL
# ==============================

print("Running Baseline Model\n")
baseline_params = fit_ddm(df, "Baseline")


# ==============================
# 6. EMOTION ANALYSIS
# ==============================

print("Running Emotion-Based Analysis\n")

emotion_results = {}
emotions = df["Encoded Emotion"].unique()

for emotion in emotions:
    subset = df[df["Encoded Emotion"] == emotion]
    emotion_results[emotion] = fit_ddm(subset, f"Emotion: {emotion}")


# ==============================
# 7. DIFFICULTY ANALYSIS
# ==============================

print("Running Difficulty-Based Analysis\n")

difficulty_results = {}
difficulties = df["coh"].unique()

for diff in difficulties:
    subset = df[df["coh"] == diff]
    difficulty_results[diff] = fit_ddm(subset, f"Difficulty: {diff}")


# ==============================
# 8. INTERACTION ANALYSIS
# ==============================

print("Running Emotion × Difficulty Analysis\n")

interaction_results = {}

for emotion in emotions:
    for diff in difficulties:

        subset = df[
            (df["Encoded Emotion"] == emotion) &
            (df["coh"] == diff)
        ]

        if len(subset) < 10:
            continue

        label = f"{emotion} | {diff}"
        interaction_results[label] = fit_ddm(subset, label)


# ==============================
# 9. EXTRACT VALUES (FIXED)
# ==============================

def extract(val):
    return {
        "Drift (v)": val['drift']['drift'].real,
        "Boundary (a)": val['bound']['B'].real,
        "Starting Point (z)": val['IC']['x0'].real,
        "Non-Decision Time (Ter)": val['overlay']['nondectime'].real
    }


# ==============================
# 10. CREATE CSV OUTPUT
# ==============================

results_list = []

# Emotion
for key, val in emotion_results.items():
    results_list.append({
        "Participant": "P3",
        "Condition_Type": "Emotion",
        "Condition": key,
        **extract(val)
    })

# Difficulty
for key, val in difficulty_results.items():
    results_list.append({
        "Participant": "P3",
        "Condition_Type": "Difficulty",
        "Condition": key,
        **extract(val)
    })

# Interaction
for key, val in interaction_results.items():
    results_list.append({
        "Participant": "P3",
        "Condition_Type": "Interaction",
        "Condition": key,
        **extract(val)
    })


# ==============================
# 11. SAVE CSV
# ==============================

results_df = pd.DataFrame(results_list)
results_df.to_csv("DDM_results_P3.csv", index=False)

print("\nCSV for P3 is READY")