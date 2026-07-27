import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# --- STEP 1: GATHERING THE DATA ---
# Identify the 3 result files for P2, P3, and P4
files = ["UPDATED_DDM_results_P2.csv", "DDM_results_P3.csv", "DDM_results_P4.csv"]
all_dfs = []

for f in files:
    try:
        # Load the CSV into a DataFrame (digital table)
        temp_df = pd.read_csv(f)
        all_dfs.append(temp_df)
    except Exception as e:
        print(f"Error loading {f}: {e}")

# Merge all three participants into one group-level table
df = pd.concat(all_dfs, ignore_index=True)

# --- STEP 2: ISOLATING THE DIFFICULTY DATA ---
# Filter for rows belonging to the 'Difficulty' condition type
diff_df = df[df['Condition_Type'] == 'Difficulty'].copy()

# --- STEP 3: PREPARING THE X-AXIS ---
# Convert 'Condition' to numbers (floats) so they sort logically (0.25 to 0.70)
diff_df['Condition'] = diff_df['Condition'].astype(float)
order = sorted(diff_df['Condition'].unique())

# --- STEP 4: CALCULATING GROUP STATS ---
# Calculate the group Mean (Average) for each coherence level
means = diff_df.groupby('Condition')['Drift (v)'].mean().sort_index()
# Calculate Standard Error (SEM) for the error bar whiskers
sems = diff_df.groupby('Condition')['Drift (v)'].std().sort_index() / np.sqrt(3)

# --- STEP 5: CREATING THE VISUAL ---
plt.figure(figsize=(10, 7))

# Use a blue gradient to represent the levels of coherence
colors = ['#E3F2FD', '#90CAF9', '#42A5F5', '#1E88E5'] 

# Create the shaded bars for the Group Average
bars = plt.bar([str(x) for x in means.index], means, yerr=sems, capsize=10, 
               color=colors, alpha=0.5, edgecolor='black', label='Group Average')

# Draw individual dots for P2, P3, and P4 to show the raw data points
sns.stripplot(data=diff_df, x='Condition', y='Drift (v)', 
              palette=colors, size=12, jitter=True, 
              edgecolor='black', linewidth=1)

# Add "Avg: X.XX" labels directly on the bars for clarity
for i, bar in enumerate(bars):
    yval = bar.get_height()
    va_type = 'bottom' if yval > 0 else 'top'
    plt.text(bar.get_x() + bar.get_width()/2, yval, 
             f'Avg: {round(yval, 2)}', ha='center', va=va_type, 
             fontweight='bold', fontsize=11)

# --- STEP 6: FINAL POLISHING (UPDATED PER LAB FEEDBACK) ---
plt.axhline(0, color='black', linewidth=1.5)

# UPDATED: X-axis label set to "Coherence Levels"
plt.xlabel('Coherence Levels', fontsize=12)

# UPDATED: Title set to "How Coherence Levels Affect Drift Rate"
plt.title('How Coherence Levels Affect Drift Rate', fontsize=14, pad=20)

plt.ylabel('Processing Speed (Drift Rate)', fontsize=12)
plt.grid(axis='y', linestyle=':', alpha=0.5)
plt.tight_layout()

# Show the final generated plot
plt.show()

# --- FINAL TAKEAWAY ---
# This plot confirms that as Coherence Levels increase, the drift rate generally follows an upward trend, indicating faster evidence accumulation when the motion stimulus is more coherent and signal-to-noise ratio is higher.