"""Cities and States page component."""

import reflex as rx
import pandas as pd
from tiny_reflex.state import State



def sales_for_state_table() -> rx.Component:
    """Table showing the same data used in the funnel chart."""

    return rx.cond(
                State.loading_sales_for_state_customers,
                rx.spinner(),
                rx.cond(
                    State.has_sales_for_state_customers,
                    rx.data_table(
                        data=State.sales_for_state_customers_data,
                        columns=[
                            "customer_state",
                            "avg_sales",
                            "sum_sales",
                            "std_sales",
                            "count_items"
                        ],
                        pagination=True,
                        search=True,
                        sort=True,
                    ),
                    rx.text("No data loaded. Click 'Load Customers' to fetch data."),
                ),
            )



# ============================================================
# PÁGINA PRINCIPAL
# ============================================================
def cities_page() -> rx.Component:
    """Page displaying sales for city and states data."""

    return rx.box(
        rx.vstack(
            rx.heading("Cities And States", font_size="2em"),
            rx.link("← Back to Home", href="/", style={"text_decoration": "none"}),

            # Botón para cargar datos
            rx.button(
                "Load Cities And States",
                on_click=lambda: State.load_sales_for_state_customers(
                    State.selected_sales_metric,
                    State.num_states_to_show
                ),
                is_loading=State.loading_sales_for_state_customers,
            ),

            # Selector de métrica
            rx.hstack(
                rx.text("Metric:"),
                rx.select(
                    ["avg_sales", "sum_sales","std_sales"],
                    default_value="avg_sales",
                    on_change=State.set_selected_sales_for_state_customers,
                ),
                spacing="4",
            ),

            # Selector de cantidad de estados
            rx.hstack(
                rx.text("States to show:"),
                rx.select(
                    ["5","10","20","30","40","50"],
                    default_value=State.num_states_to_show,
                    on_change=State.set_num_states_to_show,
                ),
                spacing="4",
            ),

            # Contenido dinámico
            rx.cond(
                State.loading_sales_for_state_customers,
                rx.spinner(),
                rx.cond(
                    State.has_sales_for_state_customers,

                    # CONTENEDOR FULL WIDTH REAL
                    rx.box(
                        rx.plotly(
                            data=State.fig_funel_sales_for_state,
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

                    rx.text("No data loaded. Click 'Load Cities And States' to fetch data."),
                ),
            ),
            sales_for_state_table(),
            spacing="1",
            width="100%",
        ),
        
        width="100vw",
        padding="0",
        margin="0",
    )

