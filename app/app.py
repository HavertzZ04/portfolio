import reflex as rx

from app.components.nav_bar import navbar
from app.components.home import home
from app.components.projects import projects
from app.components.certificates import certificates
from app.components.technologies import technologies
from app.components.goals import goals
from app.components.footer import footer

def index():
    return rx.box(
        navbar(),
        rx.box(
            home(),
            projects(),
            certificates(),
            technologies(),
            goals(),
            footer(),
            padding_top="4.4em"
        ),
        rx.script("""
            document.documentElement.style.scrollBehavior = 'smooth';
        """
        ),

        style={
            "backgroundColor": "#FFE0C4",
            "backgroundImage": (
                "url(\"data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' width='100%25' height='100%25' "
                "viewBox='0 0 1200 800'%3E%3Cdefs%3E%3CradialGradient id='a' cx='0' cy='800' r='800' "
                "gradientUnits='userSpaceOnUse'%3E%3Cstop offset='0' stop-color='%23c435a2'/%3E%3Cstop offset='1' "
                "stop-color='%23c435a2' stop-opacity='0'/%3E%3C/radialGradient%3E%3CradialGradient id='b' "
                "cx='1200' cy='800' r='800' gradientUnits='userSpaceOnUse'%3E%3Cstop offset='0' stop-color='%23d0ffcb'"
                "/%3E%3Cstop offset='1' stop-color='%23d0ffcb' stop-opacity='0'/%3E%3C/radialGradient%3E%3CradialGradient "
                "id='c' cx='600' cy='0' r='600' gradientUnits='userSpaceOnUse'%3E%3Cstop offset='0' "
                "stop-color='%233768c9'/%3E%3Cstop offset='1' stop-color='%233768c9' stop-opacity='0'/%3E%3C/radialGradient%3E"
                "%3CradialGradient id='d' cx='600' cy='800' r='600' gradientUnits='userSpaceOnUse'%3E%3Cstop offset='0' "
                "stop-color='%23FFE0C4'/%3E%3Cstop offset='1' stop-color='%23FFE0C4' stop-opacity='0'/%3E%3C/radialGradient%3E"
                "%3CradialGradient id='e' cx='0' cy='0' r='800' gradientUnits='userSpaceOnUse'%3E%3Cstop offset='0' "
                "stop-color='%2314141B'/%3E%3Cstop offset='1' stop-color='%2314141B' stop-opacity='0'/%3E%3C/radialGradient%3E"
                "%3CradialGradient id='f' cx='1200' cy='0' r='800' gradientUnits='userSpaceOnUse'%3E%3Cstop offset='0' "
                "stop-color='%23D2F0FF'/%3E%3Cstop offset='1' stop-color='%23D2F0FF' stop-opacity='0'/%3E%3C/radialGradient%3E"
                "%3C/defs%3E%3Crect fill='url(%23a)' width='1200' height='800'/%3E%3Crect fill='url(%23b)' width='1200' "
                "height='800'/%3E%3Crect fill='url(%23c)' width='1200' height='800'/%3E%3Crect fill='url(%23d)' "
                "width='1200' height='800'/%3E%3Crect fill='url(%23e)' width='1200' height='800'/%3E%3Crect "
                "fill='url(%23f)' width='1200' height='800'/%3E%3C/svg%3E\")"
            ),
            "backgroundAttachment": "fixed",
            "backgroundSize": "cover",
            "minHeight": "100vh",
        }
    )

app = rx.App()
app.add_page(index, route="/", title="HavertzZ Portfolio")
