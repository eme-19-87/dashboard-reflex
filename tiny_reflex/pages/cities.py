"""Cities and States page component."""

import reflex as rx
import plotly.graph_objects as go
from tiny_reflex.state import State




# ============================================================
# PÁGINA PRINCIPAL
# ============================================================

def cities_page() -> rx.Component:
    """Page displaying sales for city and states data."""
    return rx.fragment(
        rx.vstack(
            rx.heading("Cities And States", font_size="2em"),
            rx.link("← Back to Home", href="/", style={"text_decoration": "none"}),

            rx.button(
                "Load Cities And States",
                on_click=State.load_sales_for_state_customers,
                is_loading=State.loading_sales_for_state_customers,
            ),
            rx.select(
                ["avg_sales", "sum_sales"],
                default_value="avg_sales",
                on_change=State.set_selected_sales_for_state_customers,
            ),

            rx.cond(
                State.loading_sales_for_state_customers,
                rx.spinner(),
                rx.cond(
                    State.has_sales_for_state_customers,

                    # =============================
                    # GRÁFICO A PANTALLA COMPLETA
                    # =============================
                    rx.box(
                        rx.plotly(
                            data=State.fig_sales_for_state,
                            on_mount=State.set_selected_sales_for_state_customers,
                            style={"width": "100%", "height": "100%"},
                        ),
                        width="100%",
                        height="100vh",     # Alto completo de pantalla
                        padding="0",
                        margin="0",
                    ),

                    rx.text("No data loaded. Click 'Load Cities And States' to fetch data."),
                ),
            ),

            spacing="1",
            padding="2em",
            width="100%",
        )
    )
