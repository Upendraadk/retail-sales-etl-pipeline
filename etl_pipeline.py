import pandas as pd
import sqlite3
import logging
import time
import matplotlib.pyplot as plt


# Logging Setup
logging.basicConfig(
    filename="pipeline.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)


# Extract
def extract(file_path):
    logging.info("Extracting data...")
    return pd.read_csv(file_path)


# Transform
def transform(df):
    logging.info("Transforming data...")
    
    df['date'] = pd.to_datetime(df['date'])
    df['revenue'] = df['price'] * df['quantity']
    
    df = df.drop_duplicates()
    df = df.fillna(0)
    
    return df


# Load to CSV + Database
def load(df):
    logging.info("Loading data...")
    
    # Save cleaned CSV
    df.to_csv("cleaned_sales_data.csv", index=False)
    
    # Load into SQLite DB
    conn = sqlite3.connect("retail.db")
    df.to_sql("sales", conn, if_exists="replace", index=False)
    conn.close()


# Generate Report
def generate_report():
    logging.info("Generating report...")
    
    conn = sqlite3.connect("retail.db")
    df = pd.read_sql("SELECT * FROM sales", conn)
    
    total_revenue = df['revenue'].sum()
    category_sales = df.groupby('category')['revenue'].sum()
    top_products = df.groupby('product')['revenue'].sum().sort_values(ascending=False)
    
    print("\n===== REPORT =====")
    print("Total Revenue:", total_revenue)
    print("\nRevenue by Category:\n", category_sales)
    print("\nTop Products:\n", top_products)
    
    # Visualization
    category_sales.plot(kind='bar')
    plt.title("Revenue by Category")
    plt.xlabel("Category")
    plt.ylabel("Revenue")
    plt.tight_layout()
    plt.savefig("revenue_by_category.png")
    plt.close()
    
    conn.close()


# Main Pipeline
def run_pipeline():
    logging.info("Pipeline started")
    
    df = extract("sales_data.csv")
    df = transform(df)
    load(df)
    generate_report()
    
    logging.info("Pipeline completed")


# Scheduler 
if __name__ == "__main__":
    run_pipeline()
    
    # Uncomment below to run daily automatically
    """
    while True:
        run_pipeline()
        time.sleep(86400)  # 24 hours
    """