import reflex as rx

def certificates():
    return rx.box(
        rx.vstack(
            rx.heading(
                "Certificates",
                font_size="50px",
                text_align="center",
                margin_top="50px"
            ),
            rx.text(
                rx.fragment(
                    "Below you’ll find some of my programming certificates. I’ve taken courses in Git, GitHub, web development, HTML, CSS, JavaScript, PHP, Python, Django, Reflex, programming logic, and more. You can view my certificates in more detail at the following link: ",
                    rx.link(
                        "certificates",
                        href="https://drive.google.com/drive/folders/1fIZBZLCGIpGVvKLK1pKw70YrUWAuw39J?usp=drive_link",
                        color="cyan",
                        is_external=True
                    ),
                    "."
                ),
                text_align="center",
                margin_top="25px",
                max_width="1000px",
            ),
            align="center",
            justify="center",
        ),

        rx.center(
            rx.grid(
                *[
                    rx.card(
                        rx.image(
                            src=f"/{i}.jpg" if i != 2 else f"/{i}.png",
                            width="100%",
                            height="180px",
                            object_fit="cover",
                        ),
                        width="20vw",
                        height="200px",
                        padding="0.5em"
                    ) for i in range(1, 17)
                ],
                columns="4",
                spacing="7",
                margin_top="50px",
                max_width="90vw",
            ),
        ),
        width="100%",
        padding_bottom="60px",
        background_color="rgba(1, 11, 19, 0.5)",
        backdrop_filter="blur(10px)",             
        color="#F0FFFF",
        id="certificates"
        
    )
