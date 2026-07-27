import pandas as pd

print("Starting script...")

try:
    df = pd.read_csv("P2_all.csv")
    print("File loaded successfully!\n")

    print("First 5 rows:")
    print(df.head())

    print("\nColumn names:")
    print(list(df.columns))

    print("\nShape of dataset:")
    print(df.shape)

except Exception as e:
    print("Error occurred:")
    print(e)
