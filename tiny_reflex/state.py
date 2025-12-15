"""Application state management."""

import reflex as rx
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
from tiny_reflex.types import (
    DimCustomerData,
    SalesForCitiesCustomerData,
    SalesForCustomersData,
    SalesForStateCustomerData,
    SalesForCategoryCustomerData
)
from tiny_reflex.queries import (
    load_customers_silver,
    load_sales_for_customers,
    load_sales_for_state_customers_query,
    load_sales_for_city_customers_query,
    load_sales_for_all_category_customers_query
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
    sales_for_city_customers_data: list[SalesForCitiesCustomerData]=[]
    sales_for_all_category_customers_data: list[SalesForCategoryCustomerData]=[]
    
    #Variables para las figuras
    figure: go.Figure = px.line()
    fig_sales_for_state: go.Figure = px.line()
    fig_sales_for_city: go.Figure = px.line()
    fig_sales_for_all_category: go.Figure = px.line()
    fig_funel_sales_for_state: go.Figure=px.line()
    
    #Variables para los select
    selected_sales_metric: str = "avg_sales"
    num_states_to_show: str = "5"
    selected_sales_city_metric: str = "avg_sales"
    num_cities_to_show: str = "5"
    selected_sales_all_category_customers_metric: str = "avg_sales"
    num_category_to_show: str = "5"
    option_states:list[str]=[]
    # ===========================
    # FLAGS DE ESTADO
    # ===========================
    loading_customers: bool = False
    loading_orders: bool = False
    loading_statistics: bool = False
    loading_customers_silver: bool = False
    loading_sales_for_customers: bool = False
    loading_sales_for_state_customers: bool = False
    loading_sales_for_city_customers: bool = False
    loading_sales_for_city_customers: bool = False
    loading_sales_all_category_customers: bool = False
    
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
    
    @rx.var
    def has_sales_for_city_customers(self) -> bool:
        return len(self.sales_for_city_customers_data) > 0
    
    @rx.var
    def has_sales_all_category_customers(self) -> bool:
        return len(self.sales_for_all_category_customers_data) > 0

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
        self.sales_for_state_customers_data = load_sales_for_state_customers_query()  
        self.loading_sales_for_state_customers = False 
    
    @rx.event
    def load_sales_for_city_customers(self):
        self.loading_sales_for_city_customers = True
        self.sales_for_city_customers_data = load_sales_for_city_customers_query()  
        self.loading_sales_for_city_customers = False   
    
    @rx.event
    def load_sales_all_category_customers(self):
        self.loading_sales_all_category_customers = True
        self.sales_for_all_category_customers_data = load_sales_for_all_category_customers_query() 
        self.loading_sales_all_category_customers= False  
    
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
        self.selected_sales_metric = metric
        self.sales_for_state_customers_data = load_sales_for_state_customers_query(
            metric=self.selected_sales_metric,
            limit=self.num_states_to_show
        )

        df = pd.DataFrame(self.sales_for_state_customers_data)

       
        # =========================
        # PLOT CHART
        # =========================
        self.fig_funel_sales_for_state = px.bar(
            df,
            x=metric,
            y="customer_state",
            text_auto='.2s',
            title=f"Ventas por Estado (Top {self.num_states_to_show})"
        )

        self.fig_funel_sales_for_state.update_layout(
            autosize=True
        )
        
    @rx.event
    def set_selected_sales_for_city_customers(self, metric="avg_sales"):
        self.selected_sales_city_metric = metric
        self.sales_for_city_customers_data= load_sales_for_city_customers_query(
            metric=self.selected_sales_city_metric,
            limit=self.num_cities_to_show
        )

        df = pd.DataFrame(self.sales_for_city_customers_data)

       
        # =========================
        # PLOT CHART
        # =========================
        self.fig_sales_for_city = px.bar(
            df,
            x=metric,
            y="customer_city",
            text_auto='.2s',
            title=f"Ventas por Ciudades (Top {self.num_cities_to_show})"
        )

        self.fig_funel_sales_for_state.update_layout(
            autosize=True
        )

    @rx.event
    def set_selected_sales_for_all_category_customers(self, metric="avg_sales"):
        self.selected_sales_all_category_customers_metric = metric
        self.sales_for_all_category_customers_data= load_sales_for_all_category_customers_query(
            metric=self.selected_sales_all_category_customers_metric,
            limit=self.num_category_to_show
        )

        df = pd.DataFrame(self.sales_for_all_category_customers_data)

       
        # =========================
        # PLOT CHART
        # =========================
        self.fig_sales_for_all_category= px.bar(
            df,
            x=metric,
            y="product_category_name",
            text_auto='.2s',
            title=f"Ventas por Categorias(Top {self.num_cities_to_show})"
        )

        self.fig_funel_sales_for_state.update_layout(
            autosize=True
        )

    @rx.event
    def set_num_cities_to_show(self, value: str):
        """Update number of citiess and reload from the database."""
        try:
            self.num_cities_to_show = str(max(5, int(value)))
        except:
            self.num_cities_to_show = 5

        self.set_selected_sales_for_city_customers(self.selected_sales_city_metric)
        
    @rx.event
    def set_num_states_to_show(self, value: str):
        """Update number of states and reload from the database."""
        try:
            self.num_states_to_show = str(max(5, int(value)))
        except:
            self.num_states_to_show = 5

        self.set_selected_sales_for_state_customers(self.selected_sales_metric)
    
    @rx.event
    def set_num_category_to_show(self, value: str):
        """Update number of category and reload from the database."""
        try:
            self.num_category_to_show = str(max(5, int(value)))
        except:
            self.num_category_to_show = 5

        self.set_selected_sales_for_all_category_customers(self.selected_sales_all_category_customers_metric)
