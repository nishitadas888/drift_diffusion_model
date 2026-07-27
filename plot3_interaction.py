import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# --- STEP 1: LOADING DATA ---
# List the exact filenames for P2, P3, and P4 to gather the group data
files = ["UPDATED_DDM_results_P2.csv", "DDM_results_P3.csv", "DDM_results_P4.csv"]
all_dfs = []

for f in files:
    try:
        # pd.read_csv reads the spreadsheet into a DataFrame (digital table)
        temp_df = pd.read_csv(f)
        # Append each table into a list for merging
        all_dfs.append(temp_df)
    except Exception as e:
        # Safety check for missing files or typos
        print(f"Error loading {f}: {e}")

# pd.concat merges the three individual tables into one giant "Group" table
df = pd.concat(all_dfs, ignore_index=True)

# --- STEP 2: FLEXIBLE FILTERING ---
# Convert 'Condition' to text (string) to search for specific difficulty levels
df['Condition_Str'] = df['Condition'].astype(str)

# Search for rows containing '0.25' (Hard) or '0.7' (Easy) inside the text strings
mask = df['Condition_Str'].str.contains('0.25') | df['Condition_Str'].str.contains('0.7')
# Create a sub-table containing only these interaction "Extremes"
extreme_df = df[mask].copy()

# --- STEP 3: CLEANUP & LABELING ---
def make_label(val):
    """Turns complex CSV strings into clean labels for the graph."""
    # Remove extra spaces for consistent matching
    v = str(val).replace(" ", "")
    # Map numbers to Emotion names (0=Neu, 1=Dis, 2=Ang)
    v = v.replace('0|', 'Neu ').replace('1|', 'Dis ').replace('2|', 'Ang ')
    # Map Coherence values to Difficulty names
    v = v.replace('0.25', 'Hard').replace('0.7', 'Easy')
    return v

# Apply the labeling function to create the X-axis names
extreme_df['Final_Label'] = extreme_df['Condition_Str'].apply(make_label)

# --- STEP 4: CALCULATING AVERAGES ---
# Define the logical order: Neutral -> Disgust -> Anger (Hard vs. Easy for each)
order = ['Neu Hard', 'Neu Easy', 'Dis Hard', 'Dis Easy', 'Ang Hard', 'Ang Easy']

# Calculate Mean (Average) and SEM (Standard Error) for each of the 6 categories
stats = extreme_df.groupby('Final_Label')['Drift (v)'].agg(['mean', 'sem']).reindex(order)

# --- STEP 5: PLOTTING ---
plt.figure(figsize=(12, 7)) # Set the size of the plot window

# Assign colors: Gray for Neutral, Orange for Disgust, Red for Anger
colors = ['#B0BEC5', '#78909C', '#FFCC80', '#FB8C00', '#EF9A9A', '#E53935']

# Draw the shaded bars for the Group Average
# yerr adds the vertical whiskers (Standard Error)
bars = plt.bar(stats.index, stats['mean'], yerr=stats['sem'], capsize=8, 
               color=colors, alpha=0.6, edgecolor='black')

# Draw individual dots (P2, P3, P4) on top to show the distribution of scores
sns.stripplot(data=extreme_df, x='Final_Label', y='Drift (v)', order=order, 
              palette=colors, size=10, jitter=True, edgecolor='black', linewidth=1)

# Add the "Avg: X.XX" text labels to each bar for immediate clarity
for bar in bars:
    y = bar.get_height()
    if not np.isnan(y):
        # Position text above for positive drift, below for negative drift
        plt.text(bar.get_x() + bar.get_width()/2, y, f'{round(y, 2)}', 
                 ha='center', va='bottom' if y > 0 else 'top', fontweight='bold', fontsize=10)

# --- STEP 6: FINAL POLISHING ---
# Add a bold line at 0 to separate positive and negative accumulation directions
plt.axhline(0, color='black', linewidth=1.5)
plt.title("Interaction: Group Average (P2, P3, P4)") # Main title
plt.ylabel("Drift Rate (Processing Speed)") # Y-axis label
plt.grid(axis='y', linestyle=':', alpha=0.5) # Faint grid lines
plt.tight_layout() # Ensure labels don't get cut off

# Show the final generated plot
plt.show()

# --- FINAL TAKEAWAY ---
# This interaction plot demonstrates how emotional valence modulates the effect of task 
# difficulty. By comparing the 'Hard' and 'Easy' extremes, we can observe whether 
# certain emotions (like Disgust) maintain a stable processing speed regardless of 
# clarity, or if others (like Anger) become significantly more difficult under blur.