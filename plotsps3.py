# import pandas as pd
# import matplotlib.pyplot as plt

# df = pd.read_csv("P3_all.csv")

# # Convert ms to seconds if needed
# df["rt_sec"] = df["Response Time (ms)"] / 1000

# plt.hist(df["rt_sec"], bins=30)
# plt.xlabel("Reaction Time (seconds)")
# plt.ylabel("Frequency")
# plt.title("RT Distribution - P3")
# plt.show()

# accuracy = df.groupby("coh")["Correctness"].mean()

# plt.figure()
# plt.plot(accuracy.index, accuracy.values)
# plt.xlabel("Coherence")
# plt.ylabel("Accuracy")
# plt.title("Accuracy vs Coherence - P3")
# plt.show()





# Reaction Time Distribution and Accuracy Analysis
# Participant: P3
# Purpose:
# This script performs exploratory data analysis on the
# behavioral dataset before fitting the Drift Diffusion Model.
# It visualizes:
# 1. Reaction Time Distribution
# 2. Accuracy as a function of stimulus coherence



# Import required libraries
import pandas as pd                  # Used for loading and manipulating dataset
import matplotlib.pyplot as plt      # Used for creating visualizations



# STEP 1: Load the dataset

# The dataset P3_all.csv contains trial-level data for
# Participant 3 including reaction time, coherence levels,
# and response correctness.

df = pd.read_csv("P3_all.csv")

print("Dataset loaded successfully.\n")



# STEP 2: Convert reaction time from milliseconds to seconds

# Reaction time values are recorded in milliseconds.
# For analysis and modeling purposes, they are converted
# into seconds.

df["rt_sec"] = df["Response Time (ms)"] / 1000



# STEP 3: Plot Reaction Time Distribution

# A histogram is used to visualize how reaction times are
# distributed across trials. This helps detect unusual
# response patterns or outliers in the dataset.

plt.hist(df["rt_sec"], bins=30)

plt.xlabel("Reaction Time (seconds)")      # Label for x-axis
plt.ylabel("Frequency")                    # Label for y-axis
plt.title("Reaction Time Distribution - P3")  # Graph title

plt.show()     # Display histogram



# STEP 4: Calculate Accuracy by Coherence Level

# The trials are grouped according to stimulus coherence.
# The mean of the "Correctness" column is calculated to
# determine accuracy for each coherence level.

accuracy = df.groupby("coh")["Correctness"].mean()



# STEP 5: Plot Accuracy vs Coherence

# This plot illustrates how participant accuracy changes
# with different stimulus coherence levels.
# Higher coherence typically results in higher accuracy.

plt.figure()   # Create a new figure for the plot

plt.plot(accuracy.index, accuracy.values)

plt.xlabel("Coherence Level")        # Label for x-axis
plt.ylabel("Accuracy")               # Label for y-axis
plt.title("Accuracy vs Coherence - P3")   # Graph title

plt.show()    # Display the plot



# END OF SCRIPT

# Expected Outputs:
# 1. Reaction Time Distribution Histogram
# 2. Accuracy vs Coherence Line Plot
#
# These visualizations provide a preliminary behavioral
# analysis before applying the Drift Diffusion Model (DDM).
