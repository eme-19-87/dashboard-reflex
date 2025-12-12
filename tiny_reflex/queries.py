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

def load_sales_for_state_customers()->list[SalesForStateCustomerData]:
    """Load average and total sales for states of customers"""
    try:
        engine=get_engine()
        query="Select fs.customer_state, avg(total) AS avg_sales_state, sum(total) AS total_sales_state from gold.fact_sales fs inner join gold.dim_customers dm on fs.customer_key=dm.customer_key group by customer_state limit 10"
        df=pd.read_sql(query,engine)
        records=df.to_dict("records")
        return cast(list[SalesForStateCustomerData],records)
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
    
