#old submission reported at 17.02.2026
# import pandas as pd
# import pyddm
# from pyddm import Sample

# # Load data
# df = pd.read_csv("P4_all.csv")

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







#UPDATED SUBMISSION, 10.03.2026, est. time taken overall: 10:23 - 01:34













#24.03.2026, 03:34
# UPDATED SUBMISSION FOR P4
"""
Drift Diffusion Model Parameter Estimation
Author: Nishita Das
Participant: P4

Outputs:
- Clean CSV file for submission
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

df = pd.read_csv("P4_all.csv")

print("Dataset loaded successfully.\n")


# ==============================
# 3. PREPROCESS DATA
# ==============================

df = df.rename(columns={
    "Response Time (ms)": "rt",
    "Correctness": "correct"
})

df["rt"] = df["rt"] / 1000  # convert ms → seconds

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
        "Participant": "P4",
        "Condition_Type": "Emotion",
        "Condition": key,
        **extract(val)
    })

# Difficulty
for key, val in difficulty_results.items():
    results_list.append({
        "Participant": "P4",
        "Condition_Type": "Difficulty",
        "Condition": key,
        **extract(val)
    })

# Interaction
for key, val in interaction_results.items():
    results_list.append({
        "Participant": "P4",
        "Condition_Type": "Interaction",
        "Condition": key,
        **extract(val)
    })


# ==============================
# 11. SAVE CSV
# ==============================

results_df = pd.DataFrame(results_list)
results_df.to_csv("DDM_results_P4.csv", index=False)

print("\nCSV for P4 is READY")