from flet import ButtonStyle, ElevatedButton, FloatingActionButton, IconButton


class __ElevatedButton(ElevatedButton):
    def __init__(self, text: str, icon: str | None = None, on_click=None):
        super().__init__()
        self.text = text
        self.icon = icon
        self.on_click = on_click


class PrimaryBtn(__ElevatedButton):
    def __init__(self, text: str, icon: str | None = None, on_click=None):
        super().__init__(text, icon, on_click)
        self.style = ButtonStyle(
            color="primary",
            surface_tint_color="primary",
            overlay_color="primarycontainer",
        )


class SecondaryBtn(__ElevatedButton):
    def __init__(self, text: str, icon: str | None = None, on_click=None):
        super().__init__(text, icon, on_click)
        self.style = ButtonStyle(
            color="secondary",
            surface_tint_color="secondary",
            overlay_color="secondarycontainer",
        )


class TertiaryBtn(__ElevatedButton):
    def __init__(self, text: str, icon: str | None = None, on_click=None):
        super().__init__(text, icon, on_click)
        self.style = ButtonStyle(
            color="tertiary",
            surface_tint_color="tertiary",
            overlay_color="tertiarycontainer",
        )


class HomeBtn(FloatingActionButton):
    def __init__(self, visible: bool | None = None):
        super().__init__()
        self.icon = "home"
        self.on_click = lambda e: e.page.go("/")
        self.visible = visible


class IconBtn(IconButton):
    def __init__(self, icon: str, tooltip: str | None = None, on_click=None):
        super().__init__()
        self.icon = icon
        self.icon_color = "tertiary"
        self.highlight_color = "tertiary,.2"
        self.hover_color = "tertiary,.1"
        self.tooltip = tooltip
        self.on_click = on_click
