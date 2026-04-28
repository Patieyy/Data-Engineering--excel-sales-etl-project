# Excel Sales ETL Project

- Project Overview

This project demonstrates a simple ETL (Extract, Transform, Load) pipeline using Excel and Python.

The goal was to take messy sales data, clean it, and transform it into a structured format for analysis.

---

- Process

### 1. Extract

* Raw data stored in Excel (`raw_sales_data.xlsx`)

### 2. Transform

* Removed duplicates
* Cleaned text using TRIM
* Standardized regions
* Handled missing values
* Recalculated total sales
* Used Python (pandas) for final transformation

### 3. Load

* Exported final dataset as CSV (`final_sales_data.csv`)

---

-Tools Used

* Excel (Data Cleaning)
* Python (pandas)
* Git & GitHub

---

- Project Structure

data/

* raw_sales_data.xlsx
* cleaned_sales_data.xlsx
* final_sales_data.csv

scripts/

* etl_process.py

---

- How to Run

```bash
pip install pandas openpyxl
python scripts/etl_process.py
```

---

- Key Skills Demonstrated

* Data Cleaning
* ETL Pipeline Design
* Python (pandas)
* Data Validation
* Git Version Control
