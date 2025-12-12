"""Home page component."""

import reflex as rx


def index() -> rx.Component:
    """Main index page with navigation."""
    return rx.fragment(
        rx.vstack(
            rx.heading("Northwind Database Explorer", font_size="2em"),
            rx.box("Explore data from the Northwind database", font_size="1.2em"),
            rx.hstack(
                rx.link(
                    rx.button("View Customers"),
                    href="/customers",
                    style={"text_decoration": "none"},
                ),
               
                spacing="2",
            ),
            spacing="2",
            padding_top="10%",
            align="center",
        ),
    )
