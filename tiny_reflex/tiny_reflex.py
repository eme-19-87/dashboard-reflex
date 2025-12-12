"""Main application file for Reflex app."""

import reflex as rx
from tiny_reflex.pages.index import index
from tiny_reflex.pages.customers import customers_page

# Create and configure the app
app = rx.App()

# Register all pages
app.add_page(index, route="/")
app.add_page(customers_page, route="/customers")

