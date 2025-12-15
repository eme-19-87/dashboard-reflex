"""Database query functions."""

import pandas as pd
from typing import cast
from tiny_reflex.db_connection import get_engine
from tiny_reflex.types import DimCustomerData, SalesForCategoryCustomerData, SalesForCitiesCustomerData,SalesForCustomersData, SalesForStateCustomerData

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

def load_sales_for_city_customers_query(metric: str = "avg_sales",
                                         limit: str = "5"
                                        ) -> list[SalesForCitiesCustomerData]:
    """
        Permite obtener las ventas para los clientes por ciudades
        
        Parámetros:
        
        metric: Define la métrica que se mostrará que podra ser el promedio, suma, desvío estándar
        o cantidad.
        
        limit: Define la cantidad de registros que se mostrará
        
        Retorno:
        
        Retorna una lista de tipos SalesForCitiesCustomerData que contendrá la información de las
        ventas por ciudad de los clientes
    """

    # Seguridad: evitar SQL injection
    allowed_metrics = {"avg_sales", "sum_sales","std_sales","count_sales"}
    if metric not in allowed_metrics:
        metric = "avg_sales"

    try:
        engine = get_engine()
        query = f"""
            SELECT 
                dm.customer_city,
                ROUND(AVG(fs.total),2) AS avg_sales,
                ROUND(SUM(fs.total),2) AS sum_sales,
                ROUND(STDDEV(fs.total),2) AS std_sales,
                COUNT(fs.order_key) AS count_items
            FROM gold.fact_sales fs
            INNER JOIN gold.dim_customers dm 
                ON fs.customer_key = dm.customer_key
            GROUP BY dm.customer_city
            ORDER BY {metric} DESC
            LIMIT {limit}::INT
        """
        df = pd.read_sql(query, engine)
        return cast(list[SalesForCitiesCustomerData], df.to_dict("records"))
    except Exception as e:
        print(f"Error loading data for customers sales: {e}")
        return []
    
def load_sales_for_all_category_customers_query(metric: str = "avg_sales",
                                         limit: str = "5"
                                        ) -> list[SalesForCategoryCustomerData]:
    """
        Permite obtener las ventas para los clientes por categoria de productos comprados
        
        Parámetros:
        
        metric: Define la métrica que se mostrará que podra ser el promedio, suma, desvío estándar
        o cantidad.
        
        limit: Define la cantidad de registros que se mostrarán
        
        Retorno:
        
        Retorna una lista de tipos SalesForCategoryCustomerData que contendrá la información de las
        ventas por categoria de producto para los clientes
    """

    # Seguridad: evitar SQL injection
    allowed_metrics = {"avg_sales", "sum_sales","std_sales","count_sales"}
    if metric not in allowed_metrics:
        metric = "avg_sales"

    try:
        engine = get_engine()
        query = f"""
            SELECT 
                dp.product_category_name,
                ROUND(AVG(fs.total),2) AS avg_sales,
                ROUND(SUM(fs.total),2) AS sum_sales,
                ROUND(STDDEV(fs.total),2) AS std_sales,
                COUNT(dp.product_category_name) AS count_items
            FROM gold.fact_sales fs
            INNER JOIN gold.dim_products dp 
                ON fs.product_key = dp.product_key
            GROUP BY dp.product_category_name
            ORDER BY {metric} DESC
            LIMIT {limit}::INT
        """
        df = pd.read_sql(query, engine)
        return cast(list[SalesForCitiesCustomerData], df.to_dict("records"))
    except Exception as e:
        print(f"Error loading data for customers sales: {e}")
        return []
    
def load_sales_for_state_cities_customers_query(metric: str = "avg_sales",
                                         limit: str = "5"
                                        ) -> list[SalesForStateCustomerData]:
    """
        Permite obtener los datos de las ventas de las ciudades por estado para mostrarlos
        en un gráfico agrupado.
        
        Parámetros:
        metric: Define qué metrica se mostrará: promedio, suma, desvío estándar, conteo
        limit: Define la cantidad de registros que se mostrarán
        
        Retorno:
        Retorna una lista de tipo SalesCustomerSitiesStateData que es el tipo de dato que guarda la
        información de las ventas para las ciudades agrupadas por estado
    """

    # Seguridad: evitar SQL injection
    allowed_metrics = {"avg_sales", "sum_sales","avg_sales","count_sales"}
    if metric not in allowed_metrics:
        metric = "avg_sales"

    try:
        engine = get_engine()
        query = f"""
            SELECT 
                dm.customer_state,
                dm.customer_city,
                ROUND(AVG(fs.total),2) AS avg_sales,
                ROUND(SUM(fs.total),2) AS sum_sales,
                ROUND(STDDEV(fs.total),2) AS std_sales,
                COUNT(fs.order_key) AS count_items
            FROM gold.fact_sales fs
            INNER JOIN gold.dim_customers dm 
                ON fs.customer_key = dm.customer_key
            GROUP BY dm.customer_state DESC,customer_city DESC
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
    
