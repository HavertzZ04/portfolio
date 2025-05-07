import reflex as rx

def home():
    return rx.center(
        rx.card(
            rx.flex(
                rx.inset(
                    rx.box(
                        background="center/cover url('/logo.png')",
                        width="380px",
                        height="380px",
                    ),
                    width="100%",
                    height="380px",
                ),
                rx.vstack(
                    rx.heading(
                        "This is Havertzz",
                        font_size="50px",
                        text_align="center",
                    ),
                    rx.text(
                        "I'm a self-taught Colombian developer passionate about automation, AI, and new technologies. I build my own tools to simplify life—this portfolio is where I express programming as art and purpose.",
                        text_align="center",
                        padding_top="20px",
                    ),
                    align="center",
                    justify="center",
                ),
                direction="row",
            ),
            max_width="1000px",
            margin_top="100px",
            background_color="rgba(1, 11, 19, 0.4)",
            backdrop_filter="blur(10px)",             
            border="1px solid rgba(255, 255, 255, 0.2)",
            border_radius="20px",
            color="#F0FFFF",
        ),
        id="home"
    )
