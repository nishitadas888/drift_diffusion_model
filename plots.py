# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv("P2_all.csv")

# # Convert ms to seconds if needed
# df["rt_sec"] = df["Response Time (ms)"] / 1000

# plt.hist(df["rt_sec"], bins=30)
# plt.xlabel("Reaction Time (seconds)")
# plt.ylabel("Frequency")
# plt.title("RT Distribution - P2")
# plt.show()

# accuracy = df.groupby("coh")["Correctness"].mean()

# plt.figure()
# plt.plot(accuracy.index, accuracy.values)
# plt.xlabel("Coherence")
# plt.ylabel("Accuracy")
# plt.title("Accuracy vs Coherence - P2")
# plt.show()


#UPDATED CODE WITH COMMENTS

# Reaction Time Distribution and Accuracy Analysis
# Participant: P2
# Purpose:
# This script performs exploratory data analysis on the
# behavioral dataset before fitting the Drift Diffusion Model.
# It visualizes:
# 1. Reaction Time Distribution
# 2. Accuracy as a function of stimulus coherence


# Import required libraries
import pandas as pd                  # Used for data loading and manipulation
import matplotlib.pyplot as plt      # Used for plotting graphs



# STEP 1: Load the dataset

# The dataset contains trial-level information including
# reaction time, stimulus coherence, and response correctness.

df = pd.read_csv("P2_all.csv")

print("Dataset loaded successfully.\n")



# STEP 2: Convert reaction time from milliseconds to seconds

# The dataset stores reaction times in milliseconds.
# Since most cognitive modeling frameworks (including DDM)
# use seconds, we convert the values accordingly.

df["rt_sec"] = df["Response Time (ms)"] / 1000

# STEP 3: Plot Reaction Time Distribution

# This histogram shows how participant reaction times are distributed across trials. It helps identify patterns such as skewness, slow responses, or outliers.

plt.hist(df["rt_sec"], bins=30)

plt.xlabel("Reaction Time (seconds)")     # X-axis label
plt.ylabel("Frequency")                   # Y-axis label
plt.title("Reaction Time Distribution - P2")  # Graph title

plt.show()   # Display the histogram



# STEP 4: Compute Accuracy for each Coherence Level

# The dataset contains different stimulus coherence levels.
# We group the trials by coherence and compute the mean correctness (accuracy) for each level.

accuracy = df.groupby("coh")["Correctness"].mean()



# STEP 5: Plot Accuracy vs Coherence

# This graph shows whether accuracy improves as coherence increases. In perceptual decision-making experiments, higher coherence usually makes the stimulus easier, resulting in higher accuracy.

plt.figure()   # Create a new figure

plt.plot(accuracy.index, accuracy.values)

plt.xlabel("Coherence Level")      # X-axis label
plt.ylabel("Accuracy")             # Y-axis label
plt.title("Accuracy vs Coherence - P2")  # Graph title

plt.show()   # Display the plot



# END OF SCRIPT

# Expected Outcome:
# 1. A histogram showing reaction time distribution.
# 2. A line graph showing how accuracy varies with coherence.
# These plots help validate the behavioral data before performing Drift Diffusion Model fitting.
