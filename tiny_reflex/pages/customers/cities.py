"""Customers page component."""

import reflex as rx
from tiny_reflex.components.navbar import navbar
from tiny_reflex.state import State




# ============================================================
# PÁGINA PRINCIPAL
# ============================================================

def cities_page() -> rx.Component:
    """Page displaying sales for city and states data."""

    return rx.box(
        rx.vstack(
            navbar(),
            rx.box(rx.heading("Ventas Por Ciudades", font_size="2em",align="center")),
            # Botón para cargar datos
            rx.button(
                "Cargar Datos",
                on_click=lambda: State.load_sales_for_city_customers(
                    State.selected_sales_city_metric,
                    State.num_cities_to_show
                ),
                is_loading=State.loading_sales_for_city_customers,
            ),

            # Selector de métrica
            rx.hstack(
                rx.text("Metric:"),
                rx.select(
                    ["avg_sales", "sum_sales","std_sales"],
                    default_value="avg_sales",
                    on_change=State.set_selected_sales_for_city_customers,
                ),
                 # Selector de cantidad de estados
                rx.text("States to show:"),
                rx.select(
                    ["5","10","20","30","40","50"],
                    default_value=State.num_cities_to_show,
                    on_change=State.set_num_cities_to_show,
                ),
                spacing="4"
                
            ),

            # Contenido dinámico
            rx.cond(
                State.loading_sales_for_city_customers,
                rx.spinner(),
                rx.cond(
                    State.has_sales_for_city_customers,

                    # CONTENEDOR FULL WIDTH REAL
                    rx.box(
                        rx.plotly(
                            data=State.fig_sales_for_city,
                            layout={
                                "autosize": True
                                
                            },
                            style={
                                "width": "100vw",
                                "height": "80vh",
                            },
                        ),
                        width="100vw",
                        height="80vh",
                        padding="0",
                    ),

                    rx.text("No data loaded. Click 'Load Data' to fetch data."),
                ),
            ),
            spacing="1",
            width="100%",
        ),
        
        width="100vw",
        padding="0",
        margin="0",
    )
