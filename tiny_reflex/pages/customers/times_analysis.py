"""Cities and States page component."""

import reflex as rx
import pandas as pd
from tiny_reflex.components.navbar import navbar
from tiny_reflex.state import State



# ============================================================
# PÁGINA PRINCIPAL
# ============================================================
def times_analysis() -> rx.Component:
    """Page displaying sales for day, month and year"""

    return rx.box(
        rx.toast.provider(),
        rx.vstack(
            navbar(),
            rx.box(rx.heading("Ventas Por Día, Meses y Años", font_size="2em",align="center")),
            # Botón para cargar datos
            rx.button(
                "Cargar Datos",
                on_click=lambda: State.init_data_time_analysis(),
                is_loading=State.loading_sales_for_year,
            ),


            # Contenido dinámico
            rx.cond(
                State.loading_sales_for_year,
                rx.spinner(),
                rx.cond(
                    State.has_sales_for_year,

                    # CONTENEDOR FULL WIDTH REAL
                    rx.box(
                        rx.plotly(
                            data=State.fig_sales_for_year,
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
        rx.hstack(
        rx.vstack(
            rx.text("Fecha desde"),
            rx.input(
                type="date",
                value=State.start_date,
                on_change=State.set_start_date,
            ),
        ),
        rx.vstack(
            rx.text("Fecha hasta"),
            rx.input(
                type="date",
                value=State.end_date,
                on_change=State.set_end_date,
            ),
        ),
        spacing="4",
        align="end",
    ),
        rx.vstack(
             rx.cond(
                State.loading_sales_for_year_month,
                rx.spinner(),
                rx.cond(
                    State.has_sales_for_year_month,
                    # CONTENEDOR FULL WIDTH REAL
                    rx.box(
                        rx.plotly(
                            data=State.fig_sales_for_month_year,

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
                )
             )
        ),
        rx.hstack(
        rx.vstack(
            rx.text("Fecha desde"),
            rx.input(
                type="date",
                value=State.start_date_ymd,
                on_change=State.set_start_date_ymd,
            ),
        ),
        rx.vstack(
            rx.text("Fecha hasta"),
            rx.input(
                type="date",
                value=State.end_date_ymd,
                on_change=State.set_end_date_ymd,
            ),
        ),
        spacing="4",
        align="end",
    ),
         rx.vstack(
             rx.cond(
                State.loading_sales_for_year_month_day,
                rx.spinner(),
                rx.cond(
                    State.has_sales_for_year_month_day,
                    # CONTENEDOR FULL WIDTH REAL
                    rx.box(
                        rx.plotly(
                            data=State.fig_sales_for_day_month_year,
                            on_mount=State.set_selected_sales_for_year_month_day,
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
                )
             )
        ),
        width="100vw",
        padding="0",
        margin="0",
    )

