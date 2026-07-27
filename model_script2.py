# #submission 1
# import pandas as pd
# import pyddm
# from pyddm import Sample

# # Load data
# df = pd.read_csv("P2_all.csv")

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

# print("\nEstimated Parameters:")
# print(model.parameters())





# #UPDATED SUBMISSION, 07.03.2026, est. time taken overall: 23:13 - 03:27
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

# 0 - Anger  #old_neutral
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
# df = pd.read_csv("P2_all.csv")

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
#         choice_column_name="correct" #clarify
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
#             "B": (0.3, 3),     # decision boundary #above below middle starting point, does it mean its above the sp
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
#         if len(subset) < 10:   #check the trials, if running on both correct and incorrect
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
# results_list = []

# # Emotion results
# for key, val in emotion_results.items():
#     results_list.append({
#         "Participant": "P2",
#         "Condition_Type": "Emotion",
#         "Condition": key,
#         "Drift (v)": float(val['drift']['drift']),
#         "Boundary (a)": float(val['bound']['B']),
#         "Starting Point (z)": float(val['IC']['x0']),
#         "Non-Decision Time (Ter)": float(val['overlay']['nondectime'])
#     })

# # Difficulty results
# for key, val in difficulty_results.items():
#     results_list.append({
#         "Participant": "P2",
#         "Condition_Type": "Difficulty",
#         "Condition": key,
#         "Drift (v)": float(val['drift']['drift']),
#         "Boundary (a)": float(val['bound']['B']),
#         "Starting Point (z)": float(val['IC']['x0']),
#         "Non-Decision Time (Ter)": float(val['overlay']['nondectime'])
#     })

# # Interaction results
# for key, val in interaction_results.items():
#     results_list.append({
#         "Participant": "P2",
#         "Condition_Type": "Interaction",
#         "Condition": key,
#         "Drift (v)": float(val['drift']['drift']),
#         "Boundary (a)": float(val['bound']['B']),
#         "Starting Point (z)": float(val['IC']['x0']),
#         "Non-Decision Time (Ter)": float(val['overlay']['nondectime'])
#     })

# # Convert to DataFrame
# results_df = pd.DataFrame(results_list)

# # Save CSV
# results_df.to_csv("UPDATED_DDM_results_P2.csv", index=False)

# print("Updated CSV is ready")



# =============================================================
# Drift Diffusion Model Parameter Estimation (FINAL SUBMISSION)
# Author: Nishita Das
# Participant: P2
# =============================================================

"""
This script performs DDM analysis using PyDDM.

Tasks:
1. Baseline Model (All trials)
2. Emotion-based analysis
3. Difficulty-based analysis
4. Emotion × Difficulty interaction

Outputs:
- Clean CSV file for submission
"""

# =============================================================
# 1. IMPORT LIBRARIES
# =============================================================

import pandas as pd
import pyddm
from pyddm import Sample


# =============================================================
# 2. LOAD DATASET
# =============================================================

df = pd.read_csv("P2_all.csv")
print("Dataset loaded successfully.\n")


# =============================================================
# 3. PREPROCESS DATA
# =============================================================

# Rename columns for PyDDM compatibility
df = df.rename(columns={
    "Response Time (ms)": "rt",
    "Correctness": "correct"
})

# Convert RT from ms → seconds
df["rt"] = df["rt"] / 1000

# Display dataset info
print("Unique Face Emotion labels:")
print(df["Encoded Emotion"].unique(), "\n")

print("Unique difficulty levels:")
print(df["coh"].unique(), "\n")


# =============================================================
# 4. HELPER FUNCTION: FIT DDM MODEL
# =============================================================

def fit_ddm(dataframe, label):
    """
    Fits DDM model to given data subset
    """

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
            "d": (-5, 5),        # Drift rate
            "B": (0.3, 3),       # Boundary separation
            "x0": (-0.8, 0.8),   # Starting bias
            "ndt": (0, 0.5)      # Non-decision time
        }
    )

    print(f"Fitting DDM model for: {label}")
    model.fit(sample, verbose=False)

    print(f"Finished fitting: {label}\n")

    return model.parameters()


# =============================================================
# 5. BASELINE MODEL
# =============================================================

print("Running Baseline Model\n")
baseline_params = fit_ddm(df, "Baseline (All Trials)")


# =============================================================
# 6. EMOTION-BASED ANALYSIS
# =============================================================

print("Running Emotion-Based Analysis\n")

emotion_results = {}
emotions = df["Encoded Emotion"].unique()

for emotion in emotions:
    subset = df[df["Encoded Emotion"] == emotion]
    emotion_results[emotion] = fit_ddm(subset, f"Emotion: {emotion}")


# =============================================================
# 7. DIFFICULTY-BASED ANALYSIS
# =============================================================

print("Running Difficulty-Based Analysis\n")

difficulty_results = {}
difficulties = df["coh"].unique()

for diff in difficulties:
    subset = df[df["coh"] == diff]
    difficulty_results[diff] = fit_ddm(subset, f"Difficulty: {diff}")


# =============================================================
# 8. EMOTION × DIFFICULTY ANALYSIS
# =============================================================

print("Running Emotion × Difficulty Interaction Analysis\n")

interaction_results = {}

for emotion in emotions:
    for diff in difficulties:

        subset = df[
            (df["Encoded Emotion"] == emotion) &
            (df["coh"] == diff)
        ]

        # Skip small samples
        if len(subset) < 10:
            continue

        label = f"{emotion} | {diff}"
        interaction_results[label] = fit_ddm(subset, label)


# =============================================================
# 9. EXTRACT PARAMETERS (IMPORTANT FIX)
# =============================================================

def extract_params(val):
    """
    Converts PyDDM Fitted objects → float values
    (Fixes .value error issue)
    """
    return {
        "Drift (v)": float(val['drift']['drift']),
        "Boundary (a)": float(val['bound']['B']),
        "Starting Point (z)": float(val['IC']['x0']),
        "Non-Decision Time (Ter)": float(val['overlay']['nondectime'])
    }


# =============================================================
# 10. CREATE CLEAN CSV (SUBMISSION READY)
# =============================================================

results_list = []

# 🔹 Baseline
bp = extract_params(baseline_params)
results_list.append({
    "Participant": "P2",
    "Condition_Type": "Baseline",
    "Emotion": "All",
    "Difficulty": "All",
    **bp
})

# 🔹 Emotion
for key, val in emotion_results.items():
    params = extract_params(val)
    results_list.append({
        "Participant": "P2",
        "Condition_Type": "Emotion",
        "Emotion": key,
        "Difficulty": "-",
        **params
    })

# 🔹 Difficulty
for key, val in difficulty_results.items():
    params = extract_params(val)
    results_list.append({
        "Participant": "P2",
        "Condition_Type": "Difficulty",
        "Emotion": "-",
        "Difficulty": key,
        **params
    })

# 🔹 Interaction
for key, val in interaction_results.items():
    emotion, diff = key.split(" | ")
    params = extract_params(val)

    results_list.append({
        "Participant": "P2",
        "Condition_Type": "Interaction",
        "Emotion": emotion,
        "Difficulty": diff,
        **params
    })


# =============================================================
# 11. SAVE FINAL CSV
# =============================================================

results_df = pd.DataFrame(results_list)

results_df.to_csv("FINAL_DDM_RESULTS_P2.csv", index=False)

print("\nFINAL CSV READY: FINAL_DDM_RESULTS_P2.csv")