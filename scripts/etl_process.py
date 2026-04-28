import pandas as pd

# Extract: read cleaned Excel file
df = pd.read_excel("../data/cleaned_sales_data.xlsx")

# Transform: clean column names
df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")

# Recalculate total sales to make sure it is correct
df["total_sales"] = df["quantity"] * df["unit_price"]

# Load: save final CSV file
df.to_csv("../data/final_sales_data.csv", index=False)

print("ETL process completed successfully!")