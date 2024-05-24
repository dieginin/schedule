import random

import flet as ft
from flet_contrib.color_picker import ColorPicker

from .layout import Dialog


class __ElevatedButton(ft.ElevatedButton):
    def __init__(self, text: str, icon: str | None = None, on_click=None):
        super().__init__()
        self.text = text
        self.icon = icon
        self.on_click = on_click


class PrimaryBtn(__ElevatedButton):
    def __init__(self, text: str, icon: str | None = None, on_click=None):
        super().__init__(text, icon, on_click)
        self.style = ft.ButtonStyle(
            color="primary",
            surface_tint_color="primary",
            overlay_color="primarycontainer",
        )


class SecondaryBtn(__ElevatedButton):
    def __init__(self, text: str, icon: str | None = None, on_click=None):
        super().__init__(text, icon, on_click)
        self.style = ft.ButtonStyle(
            color="secondary",
            surface_tint_color="secondary",
            overlay_color="secondarycontainer",
        )


class TertiaryBtn(__ElevatedButton):
    def __init__(self, text: str, icon: str | None = None, on_click=None):
        super().__init__(text, icon, on_click)
        self.style = ft.ButtonStyle(
            color="tertiary",
            surface_tint_color="tertiary",
            overlay_color="tertiarycontainer",
        )


class ColorBtn(ft.ElevatedButton):
    def __init__(self, value: str | None = None):
        super().__init__()
        self.value = value if value else "#%06x" % random.randint(0, 0xFFFFFF)
        self.tooltip = "Set Color"
        self.width = 25
        self.height = 25
        self.style = ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10), bgcolor=self.value
        )
        self.on_click = self._open_dialog

    def _open_dialog(self, e: ft.ControlEvent):
        self._picker = ColorPicker(self.value)
        self._dialog = Dialog(
            "Choose a Color", self._picker, on_confirm=self._update_button
        )

        e.page.dialog = self._dialog
        self._dialog.open = True
        e.page.update()

    def _update_button(self, e: ft.ControlEvent):
        self.value = self._picker.color
        self.bgcolor = self._picker.color
        self._dialog.open = False
        e.page.update()


class HomeBtn(ft.FloatingActionButton):
    def __init__(self, visible: bool | None = None):
        super().__init__()
        self.icon = "home"
        self.on_click = lambda e: e.page.go("/")
        self.visible = visible


class IconBtn(ft.IconButton):
    def __init__(self, icon: str, tooltip: str | None = None, on_click=None):
        super().__init__()
        self.icon = icon
        self.icon_color = "tertiary"
        self.highlight_color = "tertiary,.2"
        self.hover_color = "tertiary,.1"
        self.tooltip = tooltip
        self.on_click = on_click
