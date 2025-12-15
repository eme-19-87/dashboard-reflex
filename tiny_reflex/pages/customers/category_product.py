"""Category customers page component."""

import reflex as rx
from tiny_reflex.components.navbar import navbar
from tiny_reflex.state import State




# ============================================================
# PÁGINA PRINCIPAL
# ============================================================

def category_product_page() -> rx.Component:
    """Page displaying sales for city and states data."""

    return rx.box(
        rx.vstack(
            navbar(),
            rx.box(rx.heading("Ventas Por Categorias", font_size="2em",align="center")),
            # Botón para cargar datos
            rx.button(
                "Cargar Datos",
                on_click=lambda: State.load_sales_all_category_customers(
                    State.selected_sales_all_category_customers_metric,
                    State.num_category_to_show
                ),
                is_loading=State.loading_sales_all_category_customers,
            ),

            # Selector de métrica
            rx.hstack(
                rx.text("Metric:"),
                rx.select(
                    ["avg_sales", "sum_sales","std_sales"],
                    default_value="avg_sales",
                    on_change=State.set_selected_sales_for_all_category_customers,
                ),
                 # Selector de cantidad de estados
                rx.text("Categories to show:"),
                rx.select(
                    ["5","10","20","30","40","50"],
                    default_value=State.num_category_to_show,
                    on_change=State.set_num_category_to_show,
                ),
                spacing="4"
                
            ),

            # Contenido dinámico
            rx.cond(
                State.loading_sales_all_category_customers,
                rx.spinner(),
                rx.cond(
                    State.has_sales_all_category_customers,

                    # CONTENEDOR FULL WIDTH REAL
                    rx.box(
                        rx.plotly(
                            data=State.fig_sales_for_all_category,
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
