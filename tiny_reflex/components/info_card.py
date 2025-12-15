import reflex as rx


def info_card(
    image_src: str,
    title: str,
    description: str,
    footer_text: str,
    footer_link: str,
) -> rx.Component:
    """Reusable information card component."""

    return rx.box(
        rx.hstack(
            # =========================
            # IMAGEN (IZQUIERDA)
            # =========================
            rx.image(
                src=image_src,
                width="180px",
                height="180px",
                object_fit="cover",
                border_radius="10px",
            ),

            # =========================
            # CONTENIDO (DERECHA)
            # =========================
            rx.vstack(
                rx.heading(title, size="4"),
                rx.text(
                    description,
                    font_size="1em",
                    color="gray.300",
                ),

                # =========================
                # PIE CON LINK
                # =========================
                rx.hstack(
                    rx.text(footer_text, font_size="0.9em", color="gray.400"),
                    rx.link(
                        "Ver más",
                        href=footer_link,
                        is_external=True,
                        color="blue.400",
                        font_size="0.9em",
                    ),
                    spacing="2",
                ),

                spacing="2",
                align="start",
            ),

            spacing="4",
            align="center",
        ),

        max_width="900px",
        width="100%",
        padding="1.5em",
        border_radius="12px",
        border="1px solid #2a2a2a",
        background_color="#111",
    )
