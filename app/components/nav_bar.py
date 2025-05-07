import reflex as rx

def navbar_link(text: str, url: str):
    return rx.link(
        rx.text(text, size="4", weight="medium", color="#F0FFFF"), href=url
    )

def navbar():
    return rx.box(
        rx.desktop_only(
            rx.hstack(
                rx.hstack(
                    rx.heading(
                        "Hello World! 🌎", size="7", weight="bold", color="#F0FFFF"
                    ),
                    align_items="center",
                ),
                rx.hstack(
                    navbar_link("Home", "#home"),
                    navbar_link("Projects", "#projects"),
                    navbar_link("Certificates", "#certificates"),
                    navbar_link("Technologies", "#technologies"),
                    navbar_link("Goals", "#goals"),
                    justify="end",
                    spacing="5", 
                ),
                justify="between",
                align_items="center",
            ),
        ),
        rx.mobile_and_tablet(
            rx.hstack(
                rx.hstack(
                    rx.heading(
                        "Hello World! 🌎", size="6", weight="bold"
                    ),
                    align_items="center",
                ),
                rx.menu.root(
                    rx.menu.content(
                        rx.menu.item(rx.link("Home", href="#home")),
                        rx.menu.item(rx.link("Projects", href="#projects")),
                        rx.menu.item(rx.link("Certificates", href="#certificates")),
                        rx.menu.item(rx.link("Technologies", href="#technologies")),
                        rx.menu.item(rx.link("Goals", href="#goals")),
                    ),
                    justify="end",
                ),
                justify="between",
                align_items="center",
            ),
        ),
        bg="#010B13",
        padding="1em",
        width="100%",
        position="fixed",
        top="0",
        z_index="999",
    )
