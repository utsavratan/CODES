import pandas as pd
file_name = "data.csv"
try:
    df = pd.read_csv(file_name)
    print("First 5 rows of the CSV file:")
    print(df.head())
except FileNotFoundError:
    print(f"File '{file_name}' not found. Please check the file path.")