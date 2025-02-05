
import pandas as pd

file_name = input("Enter the CSV file name: ")

try:
    data = pd.read_csv(file_name)
    print("\nFirst 5 rows of the CSV file:")
    print(data.head())
    
except FileNotFoundError:
    print(f"Error: The file '{file_name}' was not found.")
