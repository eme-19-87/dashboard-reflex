"""Type definitions for data structures used in the application."""

from datetime import date
from typing import TypedDict
from numpy import double


class DimCustomerData(TypedDict):
    """Type definition for customer dimension"""
    customer_key:int
    customer_id: str
    customer_unique_id:str
    customer_city: str
    customer_state: str 
    customer_city_lat:double
    customer_city_lng:double
    
class DimSellerData(TypedDict):
    """Type definition for seller dimension"""
    seller_key:int
    seller_id: str
    seller_city: str
    seller_state: str 
    seller_city_lat:double
    seller_city_lng:double

class DimProductData(TypedDict):
    """Type definition for product dimension"""
    product_key:int
    product_id: str
    product_weight_g: int
    product_length_cm: int 
    product_heigth_cm:int
    product_width_cm:int
    product_category:str
    
    
class DimCalendarData(TypedDict):
    """Type definition for calendar dimension"""
    date_key:int
    date_ymd: date
    date_year: int
    date_month: int
    date_day: int
    month_name:str
    date_weekday:int
    weekday_iso_number:int
    weekday_of_year:int
    day_of_year:int
    quarter: int
    is_weekend:bool
    yyyymmdd:str
    yymm:str
    iso_date:str
    
class DimStatusData(TypedDict):
    """Type definition for status dimension"""
    status_key:int
    status:str
    status_group:str

class FactSalesData(TypedDict):
    """Type definition for fact sales"""
    order_key:int
    order_item_id:int
    customer_key:int
    seller_key:int
    product_key:int
    status_key:int
    date_purchase_key:int
    price: float
    freight_value:float
    total:float
    
class SalesForCustomersData(TypedDict):
    """Type definition for fact sales"""
    customer_key:int
    avg:float
    total:float
    
class SalesForStateCustomerData(TypedDict):
    """Type definition for fact sales where analize the states of Customers.
    Usuful to determinate the average and total sales for states where customers live."""
    customer_state:str
    avg_sales:float
    sum_sales:float
    std_sales:float
    count_items:int
    
class SalesForCitiesCustomerData(TypedDict):
    """Type definition for fact sales where analize the cities of Customers.
    Usuful to determinate the average and total sales for cities where customers live."""
    customer_city:str
    avg_sales:float
    sum_sales:float
    std_sales:float
    count_items:int
    
class SalesForCategoryCustomerData(TypedDict):
    """Type definition for fact sales where analize the category  of products purchased for Customers.
    Usuful to determinate the average and total sales for category"""
    product_category_name:str
    avg_sales:float
    sum_sales:float
    std_sales:float
    count_items:int



class SalesForStateSellerData(TypedDict):
    """Type definition for fact sales where analize the states of Sellers.
    Usuful to determinate the average and total sales for states where sellers works."""
    seller_key:int
    seller_state:str
    avg:float
    total:float
    
class SalesCustomerSitiesStateData(TypedDict):
    """Type definition for fact sales where analize the states of Sellers.
    Usuful to determinate the average and total sales for states where sellers works."""
    customer_state:int
    customer_city:str
    avg_sales:float
    sum_sales:float
    std_sales: float
    count_sales:int
