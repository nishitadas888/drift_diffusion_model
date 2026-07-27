import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# --- STEP 1: GATHERING THE DATA ---
# List the specific result files for participants P2, P3, and P4
files = ["UPDATED_DDM_results_P2.csv", "DDM_results_P3.csv", "DDM_results_P4.csv"]
all_dfs = []

for f in files:
    try:
        # Load each CSV into a DataFrame (digital table)
        temp_df = pd.read_csv(f)
        # Add the table to our list for merging
        all_dfs.append(temp_df)
    except Exception as e:
        # Error check in case a filename is misspelled or missing
        print(f"Error loading {f}: {e}")

# Combine all participants into one group table
df = pd.concat(all_dfs, ignore_index=True)

# --- STEP 2: ISOLATING AND NAMING THE EMOTIONS ---
# Filter for rows belonging to the 'Emotion' condition type
emo_df = df[df['Condition_Type'] == 'Emotion'].copy()

# Map numeric codes (0, 1, 2) to their actual emotion names
mapping = {0: 'Neutral', 1: 'Disgust', 2: 'Anger'}
# Create a new column for these labels to use on the X-axis
emo_df['Emotion_Name'] = emo_df['Condition'].astype(float).astype(int).map(mapping)

# --- STEP 3: CALCULATING THE AVERAGES ---
# Define the order of appearance: Neutral -> Disgust -> Anger
order = ['Neutral', 'Disgust', 'Anger']

# Calculate the group Mean (Average) for each emotion
means = emo_df.groupby('Emotion_Name')['Drift (v)'].mean().reindex(order)
# Calculate Standard Error (SEM) to show the variance whiskers
sems = emo_df.groupby('Emotion_Name')['Drift (v)'].std().reindex(order) / np.sqrt(3)

# --- STEP 4: CREATING THE VISUAL ---
plt.figure(figsize=(10, 7)) # Set the size of the plot window

# Assign specific colors for each category (Gray, Orange, Red)
colors = ['#B0BEC5', '#FFB74D', '#E57373']

# Draw the shaded bars representing the Group Average
# yerr=sems adds the vertical error bars
bars = plt.bar(means.index, means, yerr=sems, capsize=10, 
               color=colors, alpha=0.5, edgecolor='black', label='Group Average')

# Draw individual dots for P2, P3, and P4 to show inter-subject variability
sns.stripplot(data=emo_df, x='Emotion_Name', y='Drift (v)', 
              order=order, palette=colors, size=12, jitter=True, 
              edgecolor='black', linewidth=1)

# --- STEP 5: ADDING DATA LABELS ---
# Loop through bars to place the "Avg: X.XX" text for immediate readability
for i, bar in enumerate(bars):
    yval = bar.get_height()
    # Position text above for positive drift, below for negative drift
    va_type = 'bottom' if yval > 0 else 'top'
    plt.text(bar.get_x() + bar.get_width()/2, yval, 
             f'Avg: {round(yval, 2)}', ha='center', va=va_type, 
             fontweight='bold', fontsize=11)

# --- STEP 6: FINAL POLISHING ---
# Add a bold line at 0 to separate evidence accumulation directions
plt.axhline(0, color='black', linewidth=1.5)
plt.ylabel('Processing Speed (Average Drift Rate)', fontsize=12)
plt.title('Emotion-Wise Group Average vs. Individual Performance (P2, P3, P4)', fontsize=14, pad=20)
plt.grid(axis='y', linestyle=':', alpha=0.5) # Add faint grid lines
plt.tight_layout() # Prevent clipping of labels

# Show the final generated plot
plt.show()

# --- FINAL TAKEAWAY ---
# This plot indicates that the group was most efficient at processing 'Disgust' (positive drift), 
# while 'Neutral' and 'Anger' conditions showed negative drift rates, suggesting either 
# a bias toward the incorrect boundary or increased cognitive conflict during those trials.