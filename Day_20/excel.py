import pandas as pd

# Load both sheets
df1 = pd.read_excel("file.xlsx", sheet_name="Sheet1")
df2 = pd.read_excel("file.xlsx", sheet_name="Sheet2")

# Compare dataframes
differences = df1.compare(df2)

# Save differences to a new Excel file
differences.to_excel("differences.xlsx")

print("Comparison complete. Check differences.xlsx for results.")