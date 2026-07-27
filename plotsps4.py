# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv("P4_all.csv")

# # Convert ms to seconds if needed
# df["rt_sec"] = df["Response Time (ms)"] / 1000

# plt.hist(df["rt_sec"], bins=30)
# plt.xlabel("Reaction Time (seconds)")
# plt.ylabel("Frequency")
# plt.title("RT Distribution - P4")
# plt.show()

# accuracy = df.groupby("coh")["Correctness"].mean()

# plt.figure()
# plt.plot(accuracy.index, accuracy.values)
# plt.xlabel("Coherence")
# plt.ylabel("Accuracy")
# plt.title("Accuracy vs Coherence - P4")
# plt.show()




# Reaction Time Distribution and Accuracy Analysis
# Participant: P4
# Purpose:
# This script performs exploratory data analysis on the
# behavioral dataset before applying the Drift Diffusion Model.
# It visualizes:
# 1. Reaction Time Distribution
# 2. Accuracy as a function of stimulus coherence



# Import required libraries
import pandas as pd                  # Library for data loading and manipulation
import matplotlib.pyplot as plt      # Library for creating plots and visualizations



# STEP 1: Load the dataset

# The dataset P4_all.csv contains trial-level data for
# Participant 4, including reaction time, coherence level,
# and whether the response was correct.

df = pd.read_csv("P4_all.csv")

print("Dataset loaded successfully.\n")



# STEP 2: Convert reaction time from milliseconds to seconds

# Reaction times in the dataset are recorded in milliseconds.
# Since most behavioral analysis uses seconds, we convert them.

df["rt_sec"] = df["Response Time (ms)"] / 1000



# STEP 3: Plot Reaction Time Distribution

# A histogram is used to observe how reaction times are
# distributed across all trials for the participant.

plt.hist(df["rt_sec"], bins=30)

plt.xlabel("Reaction Time (seconds)")      # X-axis label
plt.ylabel("Frequency")                    # Y-axis label
plt.title("Reaction Time Distribution - P4")  # Graph title

plt.show()    # Display histogram



# STEP 4: Calculate Accuracy for each Coherence Level

# Trials are grouped based on stimulus coherence.
# The average of the "Correctness" column represents accuracy.

accuracy = df.groupby("coh")["Correctness"].mean()



# STEP 5: Plot Accuracy vs Coherence

# This graph shows how accuracy changes with stimulus
# coherence. Higher coherence usually leads to better accuracy.

plt.figure()   # Create a new figure window

plt.plot(accuracy.index, accuracy.values)

plt.xlabel("Coherence Level")          # X-axis label
plt.ylabel("Accuracy")                 # Y-axis label
plt.title("Accuracy vs Coherence - P4")   # Graph title

plt.show()   # Display the plot



# END OF SCRIPT

# Expected Output:
# 1. Histogram showing distribution of reaction times
# 2. Line plot showing relationship between coherence and accuracy

# These plots help verify behavioral patterns before
# fitting the Drift Diffusion Model.
