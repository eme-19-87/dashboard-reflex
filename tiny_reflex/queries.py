"""Database query functions."""

import pandas as pd
from typing import cast
from tiny_reflex.db_connection_local import get_engine
from tiny_reflex.types import DimCustomerData,SalesForCustomersData, SalesForStateCustomerData

def load_sales_for_customers()->list[SalesForCustomersData]:
    """Load average and total sales for customers"""
    try:
        engine=get_engine()
        query="Select fs.customer_key::TEXT,avg(fs.total) AS avg_sales,sum(fs.total) AS sum_sales from gold.fact_sales fs inner join gold.dim_customers dc on fs.customer_key=dc.customer_key group by fs.customer_key order by avg_sales ASC,sum_sales ASC limit 10"
        df=pd.read_sql(query,engine)
        records=df.to_dict("records")
        return cast(list[SalesForCustomersData],records)
    except Exception as e:
        print(f"Error loading data for customers sales: {e}")
        return []  

def load_sales_for_state_customers_query(metric: str = "avg_sales",
                                         limit: str = "5"
                                        ) -> list[SalesForStateCustomerData]:
    """Load top-N states ordered by metric (avg or sum)"""

    # Seguridad: evitar SQL injection
    allowed_metrics = {"avg_sales", "sum_sales","avg_sales"}
    if metric not in allowed_metrics:
        metric = "avg_sales"

    try:
        engine = get_engine()
        query = f"""
            SELECT 
                dm.customer_state,
                ROUND(AVG(fs.total),2) AS avg_sales,
                ROUND(SUM(fs.total),2) AS sum_sales,
                ROUND(STDDEV(fs.total),2) AS std_sales,
                COUNT(fs.order_key) AS count_items
            FROM gold.fact_sales fs
            INNER JOIN gold.dim_customers dm 
                ON fs.customer_key = dm.customer_key
            GROUP BY dm.customer_state
            ORDER BY {metric} DESC
            LIMIT {limit}::INT
        """
        df = pd.read_sql(query, engine)
        return cast(list[SalesForStateCustomerData], df.to_dict("records"))
    except Exception as e:
        print(f"Error loading data for customers sales: {e}")
        return []

     
          
def load_customers_silver() -> list[DimCustomerData]:
    """Load customers data from database."""
    try:
        engine = get_engine()
        query = "SELECT customer_id, customer_city, customer_state FROM silver.olist_customers ORDER BY customer_id LIMIT 100"
        df = pd.read_sql(query, engine)
        records = df.to_dict("records")
        return cast(list[DimCustomerData], records)
    except Exception as e:
        print(f"Error loading customers: {e}")
        return []
    
