import reflex as rx


def navbar() -> rx.Component:
    """Reusable navigation bar with Customers dropdown."""
    return rx.hstack(
        rx.heading("Brazil Ecommerce Explorer", size="5"),

        rx.spacer(),

        rx.link("Home", href="/"),

        # =========================
        # Customers (Dropdown)
        # =========================
        rx.menu.root(
            rx.menu.trigger(
                rx.text("Customers ▾", cursor="pointer")
            ),
            rx.menu.content(
                 rx.menu.item(
                    rx.link("General Sales", href="/customers")
                ),
                rx.menu.item(
                    rx.link("Sales By State", href="/customers/sales_by_state")
                ),
                rx.menu.item(
                    rx.link("Sales By City", href="/customers/sales_by_city")
                ),
                rx.menu.item(
                    rx.link("Sales By Category", href="/customers/sales_by_category")
                ),
                 rx.menu.item(
                    rx.link("Sales By Time", href="/customers/time_analysis")
                )
            ),
        ),

        padding="1em",
        width="100%",
        border_bottom="1px solid #333",
        align="center",
        spacing="4",
    )

