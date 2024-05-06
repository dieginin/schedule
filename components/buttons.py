from flet import ButtonStyle, ElevatedButton, colors


class _DefaultButton(ElevatedButton):
    def __init__(
        self,
        text: str | None = None,
        icon: str | None = None,
        on_click=None,
    ):
        super().__init__()
        self.text = text
        self.icon = icon
        self.on_click = on_click


class PrimaryButton(_DefaultButton):
    def __init__(self, text: str | None = None, icon: str | None = None, on_click=None):
        super().__init__(text, icon, on_click)
        self.style = ButtonStyle(
            color="primary",
            surface_tint_color="primary",
            overlay_color="primarycontainer",
        )


class SecondaryButton(_DefaultButton):
    def __init__(self, text: str | None = None, icon: str | None = None, on_click=None):
        super().__init__(text, icon, on_click)
        self.style = ButtonStyle(
            color="secondary",
            surface_tint_color="secondary",
            overlay_color="secondarycontainer",
        )


class TertiaryButton(_DefaultButton):
    def __init__(self, text: str | None = None, icon: str | None = None, on_click=None):
        super().__init__(text, icon, on_click)
        self.style = ButtonStyle(
            color="tertiary",
            surface_tint_color="tertiary",
            overlay_color="tertiarycontainer",
        )
