import reflex as rx

images = [
    {"src": "https://cdn4.iconfinder.com/data/icons/iconsimple-programming/512/html-512.png", "alt": "html5"},
    {"src": "https://static-00.iconduck.com/assets.00/file-type-css-icon-1806x2048-r5fwjl3p.png", "alt": "css3"},
    {"src": "https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg", "alt": "javascript"},
    {"src": "https://miro.medium.com/v2/resize:fit:1024/1*9HanDsRU11ZMsgDGJwN96w.png", "alt": "bootstrap"},
    {"src": "https://www.vikingsoftware.com/wp-content/uploads/2024/02/Python.png", "alt": "python"},
    {"src": "https://cdn.worldvectorlogo.com/logos/django.svg", "alt": "django"},
    {"src": "https://raw.githubusercontent.com/devicons/devicon/master/icons/php/php-original.svg", "alt": "php"},
    {"src": "https://www.manualweb.net/img/logos/flask.png", "alt": "flask"},
    {"src": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/35/Tux.svg/1727px-Tux.svg.png", "alt": "linux"},
    {"src": "https://upload.wikimedia.org/wikipedia/commons/thumb/3/34/Windows_logo_-_2012_derivative.svg/1200px-Windows_logo_-_2012_derivative.svg.png", "alt": "windows"},
    {"src": "https://avatars.githubusercontent.com/u/18133?s=280&v=4", "alt": "git"},
    {"src": "https://cdn-icons-png.freepik.com/512/4494/4494756.png", "alt": "github"},
    {"src": "https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Visual_Studio_Code_1.35_icon.svg/512px-Visual_Studio_Code_1.35_icon.svg.png?20210804221519", "alt": "visual"},
    {"src": "https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/PyCharm_Icon.svg/2048px-PyCharm_Icon.svg.png", "alt": "Py Charm"},
    {"src": "https://www.svgrepo.com/show/331760/sql-database-generic.svg", "alt": "SQL"},
    {"src": "https://upload.wikimedia.org/wikipedia/commons/thumb/2/2f/Google_Apps_Script.svg/2048px-Google_Apps_Script.svg.png", "alt": "Apps Script"},
    {"src": "https://avatars.githubusercontent.com/u/104714959?s=200&v=4", "alt": "Reflex"},
    {"src": "https://cdn.pixabay.com/photo/2023/05/08/00/43/chatgpt-7977357_1280.png", "alt": "Chat GPT"},
]

def technologies():
    return rx.box(
        rx.vstack(
            rx.heading(
                "Technologies",
                font_size="50px",
                text_align="center",
                margin_top="30px",
            ),
            rx.text(
                "Over the years, creating projects has shaped me into a full-stack developer, helping me appreciate the beauty of both frontend and backend. While I now focus on Python for task automation at work, I’m confident starting new projects with the following technologies, frameworks, libraries, and digital tools I've gained experience with.",
                text_align="center",
                margin_top="25px",
                max_width="1000px"
            ),
            align="center",
            justify="center",
        ),
        rx.center(
            rx.grid(
                rx.foreach(
                    images,
                    lambda img: rx.image(
                        src=img["src"],
                        alt=img["alt"],
                        width="80px",
                        height="80px",
                        margin="auto",
                    )
                ),
                columns="9",
                spacing="6",
                width="100%",
                justify_items="center",
                padding_top="50px",
                padding_right="25px",
                padding_left="25px",
                max_width="1000px"
            )
        )
        ,
        bg="#010B13",
        width="100%",
        padding_top="25px",
        padding_bottom="50px",
        id="technologies"
        
    )
