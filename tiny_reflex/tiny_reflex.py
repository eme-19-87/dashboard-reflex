"""Main application file for Reflex app."""

import reflex as rx
from tiny_reflex.pages.index import index
from tiny_reflex.pages.customers.customers import customers_page
from tiny_reflex.pages.customers.states import states_page
from tiny_reflex.pages.customers.cities import cities_page
from tiny_reflex.pages.customers.category_product import category_product_page

# Create and configure the app
app = rx.App()

# Register all pages
app.add_page(index, route="/")
app.add_page(customers_page, route="/customers")
app.add_page(states_page, route="/customers/sales_by_state")
app.add_page(cities_page, route="/customers/sales_by_city")
app.add_page(category_product_page, route="/customers/sales_by_category")

