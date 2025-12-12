"""Cities and States page component."""

import reflex as rx
import plotly.graph_objects as go
from tiny_reflex.state import State




# ============================================================
# PÁGINA PRINCIPAL
# ============================================================

def customers_page() -> rx.Component:
    """Page displaying customers data."""
    return rx.fragment(
        rx.vstack(
            rx.heading("Cities And States", font_size="2em"),
            rx.link("← Back to Home", href="/", style={"text_decoration": "none"}),

            rx.button(
                "Load Cities And States",
                on_click=State.load_sales_customers_data,
                is_loading=State.loading_sales_for_customers,
            ),
            rx.select(
                ["avg_sales", "sum_sales"],
                default_value="avg_sales",
                on_change=State.set_selected_customer_sales_metric,
            ),
            rx.cond(
                State.loading_sales_for_customers,
                rx.spinner(),
                rx.cond(
                    State.has_sales_customers_data,
                     rx.plotly(
                            data=State.figure,
                            on_mount=State.set_selected_customer_sales_metric,
                        ),
                    rx.text("No data loaded. Click 'Load Customers' to fetch data."),
                ),
            ),

            spacing="1",
            padding="2em",
            width="100%",
        )
    )