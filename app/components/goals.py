import reflex as rx

def goals():
    return rx.box(
        rx.center(
            rx.divider(
                size="4",
                width="90%",
            )
        ),
        rx.vstack(
            rx.heading(
                "Goals",
                font_size="50px",
                text_align="center",
                margin_top="55px"
            ),
            rx.list(
                rx.list_item("🚀 Build a technology that transforms and improves humanity."),
                rx.list_item("🎓 Earn a degree in computer science and become an inspiring professor."),
                rx.list_item("💻 Work as a developer for top-tier companies like Google."),
                margin_top="25px",
                max_width="1000px",
                text_align="center",
                font_size="20px",
            ),
            rx.image(
                src="/gorilla.svg",
                width="80px",
                height="80px",
                margin_top="25px"
            ),
            align="center",
            justify="center",
        ),
        bg="#010B13",
        width="100%",
        padding_top="25px",
        padding_bottom="50px",
        id="goals"
        
    )