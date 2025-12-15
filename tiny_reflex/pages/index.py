"""Home page component."""

import reflex as rx
from tiny_reflex.components.navbar import navbar
from tiny_reflex.components.info_card import info_card

def index() -> rx.Component:
    """Main index page with navigation."""
    return rx.vstack(
        navbar(),
        rx.vstack(
            rx.heading("Trabajo Final Data Analytics. Devligth 2025", font_size="2em"),
            rx.box("Análisis Base De Datos Olist Ecommerce Brazil", font_size="1.2em"),
            rx.vstack(
                rx.box("Presentación"),
                spacing="2",
            ),
            rx.vstack(
                info_card(
                image_src="/assets/favicon.ico",
                title="Espinoza Enrique Manuel",
                description=(
                    "Estudiante de Licenciatura En Sistemas De Información 4º Año."
                    "Analista Programador Universitario."
                ),
                footer_text="Linkedin:",
                footer_link="https://www.linkedin.com/in/enrique-espinoza-948157224",
                
            ),
                spacing="2",
            ),
            spacing="2",
            padding_top="10%",
            align="center",
        ),
        width="100%",
        align="center"
    )
