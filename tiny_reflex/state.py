"""Application state management."""

import reflex as rx
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from tiny_reflex.types import (
    DimCustomerData,
    SalesForCustomersData,
    SalesForStateCustomerData
)
from tiny_reflex.queries import (
    load_customers_silver,
    load_sales_for_customers,
    load_sales_for_state_customers_query
)


class State(rx.State):
    """Global app state."""

    # ===========================
    # DATASETS PRINCIPALES
    # ===========================
    dim_customers_data: list[DimCustomerData] = []
    dim_seller_data: list[DimCustomerData] = []
    dim_products_data: list[DimCustomerData] = []
    

    # Importante: inicializar siempre
    sales_for_customers_data: list[SalesForCustomersData] = []
    sales_for_state_customers_data: list[SalesForStateCustomerData]=[]
    figure: go.Figure = px.line()
    fig_sales_for_state: go.Figure = px.line()
    
    # ===========================
    # FLAGS DE ESTADO
    # ===========================
    loading_customers: bool = False
    loading_orders: bool = False
    loading_statistics: bool = False
    loading_customers_silver: bool = False
    loading_sales_for_customers: bool = False
    loading_sales_for_state_customers: bool = False

    # ===========================
    # PROPIEDADES DERIVADAS
    # ===========================
    @rx.var
    def has_sales_customers_data(self) -> bool:
        return len(self.sales_for_customers_data) > 0

    @rx.var
    def has_customers_data_silver(self) -> bool:
        return len(self.dim_customers_data) > 0

    @rx.var
    def has_sales_for_state_customers(self) -> bool:
        return len(self.sales_for_state_customers_data) > 0

    # ===========================
    # EVENTOS
    # ===========================

    @rx.event
    def load_customers_silver(self):
        self.loading_customers_silver = True
        self.dim_customers_data = load_customers_silver()
        self.loading_customers_silver = False

    @rx.event
    def load_sales_customers_data(self):
        self.loading_sales_for_customers = True
        self.sales_for_customers_data = load_sales_for_customers()
        self.loading_sales_for_customers = False
        
    @rx.event
    def load_sales_for_state_customers(self):
        self.loading_sales_for_state_customers = True
        self.sales_for_state_customers_data = load_sales_for_state_customers_query()  # ESTA ERA LA LÍNEA MAL
        self.loading_sales_for_state_customers = False  # ESTA TAMBIÉN

    @rx.event
    def create_fig_bar_sales_customers(self):
        df=pd.DataFrame(self.sales_for_customers_data)
        df['customer_key'] = df['customer_key'].astype(str)
        self.figure = px.bar(
            df,
            x="customer_key",
            y="avg_sales",
            title="Ventas Por Clientes",
        )
        
    @rx.event
    def set_selected_customer_sales_metric(self, metric="avg_sales"):
        df=pd.DataFrame(self.sales_for_customers_data)
        #df['customer_key'] = df['customer_key'].astype(str)
        self.figure = px.bar(
            df,
            x="customer_key",
            y=f"{metric}",
            title="Ventas Por Clientes"
           
        )
        
    @rx.event
    def set_selected_sales_for_state_customers(self, metric="avg_sales"):
        df=pd.DataFrame(self.sales_for_state_customers_data)
        #df['customer_key'] = df['customer_key'].astype(str)
        self.fig_sales_for_state = px.bar(
            df,
            x="customer_state",
            y=f"{metric}",
            title="Ventas Por Estado Clientes",
            color=df["customer_state"].unique()
        )