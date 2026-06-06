# Retail Sales ETL Pipeline

## Overview

This project demonstrates a simple ETL (Extract, Transform, Load) pipeline built using Python, Pandas, SQLite, and Matplotlib.

The pipeline extracts retail sales data from a CSV file, performs data cleaning and transformation, stores the processed data in a SQLite database, and generates sales reports and visualizations.

## Features

* Extract sales data from CSV files
* Clean and transform data using Pandas
* Calculate revenue for each transaction
* Remove duplicate records
* Handle missing values
* Store processed data in SQLite
* Generate revenue reports
* Create sales visualizations
* Log pipeline activities

## Technologies Used

* Python
* Pandas
* SQLite3
* Matplotlib
* Logging

## Project Structure

```text
retail-sales-etl-pipeline/
│
├── etl_pipeline.py
├── sales_data.csv
├── requirements.txt
├── .gitignore
└── README.md
```

## ETL Workflow

### 1. Extract

Reads raw sales data from a CSV file.

### 2. Transform

* Converts date column to datetime format
* Calculates revenue using:

Revenue = Price × Quantity

* Removes duplicate records
* Handles missing values

### 3. Load

* Saves cleaned data to a CSV file
* Loads transformed data into a SQLite database

### 4. Reporting

* Calculates total revenue
* Generates revenue by category
* Identifies top-performing products
* Produces data visualizations

## Installation

Clone the repository:

```bash
git clone https://github.com/Upendraadk/retail-sales-etl-pipeline.git
cd retail-sales-etl-pipeline
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the ETL pipeline:

```bash
python etl_pipeline.py
```

## Sample Output

The pipeline generates:

* Revenue reports
* Category-wise sales analysis
* Product performance insights
* Visualization charts

## Future Improvements

* Add exception handling
* Add data validation checks
* Schedule automatic pipeline execution
* Support multiple input file formats
* Generate PDF reports

## Author

Upendra Adhikari

GitHub: https://github.com/Upendraadk
