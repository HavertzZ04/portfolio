import reflex as rx

def footer():
    return rx.box(
        rx.center(
            rx.divider(
                size="4",
                width="90%",
            )
        ),
        rx.vstack(
            rx.text(
                "Thanks for visiting — your time means everything.",
            ),
            align="center",
            justify="center",
            padding_top="25px"
        ),
        bg="#010B13",
        width="100%",
        padding_bottom="40px",
    )