import random

import flet as ft
from flet_contrib.color_picker import ColorPicker

from .layout import Dialog


class __ElevatedButton(ft.ElevatedButton):
    def __init__(
        self,
        text: str,
        icon: str | None = None,
        on_click=None,
        disabled: bool | None = None,
    ):
        super().__init__()
        self.text = text
        self.icon = icon
        self.on_click = on_click
        self.disabled = disabled


class PrimaryBtn(__ElevatedButton):
    def __init__(
        self,
        text: str,
        icon: str | None = None,
        on_click=None,
        disabled: bool | None = None,
    ):
        super().__init__(text, icon, on_click, disabled)
        self.style = ft.ButtonStyle(
            color="grey" if disabled else "primary",
            surface_tint_color="primary",
            overlay_color="primarycontainer",
        )


class SecondaryBtn(__ElevatedButton):
    def __init__(
        self,
        text: str,
        icon: str | None = None,
        on_click=None,
        disabled: bool | None = None,
    ):
        super().__init__(text, icon, on_click, disabled)
        self.style = ft.ButtonStyle(
            color="grey" if disabled else "secondary",
            surface_tint_color="secondary",
            overlay_color="secondarycontainer",
        )


class TertiaryBtn(__ElevatedButton):
    def __init__(
        self,
        text: str,
        icon: str | None = None,
        on_click=None,
        disabled: bool | None = None,
    ):
        super().__init__(text, icon, on_click, disabled)
        self.style = ft.ButtonStyle(
            color="grey" if disabled else "tertiary",
            surface_tint_color="tertiary",
            overlay_color="tertiarycontainer",
        )


class ColorBtn(ft.ElevatedButton):
    def __init__(
        self, value: str | None = None, show_color: bool = False, callback=None
    ):
        super().__init__()
        self.value = value if value else "#%06x" % random.randint(0, 0xFFFFFF)
        self.tooltip = self.value if show_color else "Set Color"
        self.width = 25
        self.height = 25
        self.style = ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=10), bgcolor=self.value
        )
        self.on_click = self._open_dialog
        self.__callback = callback

    def generate_color(self) -> str:
        self.value = "#%06x" % random.randint(0, 0xFFFFFF)
        self.style = ft.ButtonStyle(bgcolor=self.value)
        return self.value

    def _open_dialog(self, e: ft.ControlEvent):
        self._picker = ColorPicker(self.value)
        self._dialog = Dialog(
            "Choose a Color", self._picker, on_confirm=self._update_button
        )

        e.page.dialog = self._dialog
        self._dialog.open = True
        e.page.update()

    def _update_button(self, e: ft.ControlEvent):
        if self.__callback:
            if self.__callback(e, self.parent.data, self._picker.color):  # type: ignore
                self.value = self._picker.color
                self.bgcolor = self._picker.color
        else:
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


class MemberBtn(ft.ElevatedButton):
    def __init__(self):
        super().__init__()
        self.on_click = self.change_member
        self.on_long_press = self.close_day
        self.current_member_index = -1
        self.width = 50
        self.height = 27
        self.update_button_style("primary")

    def update_button_style(self, color: str):
        self.style = ft.ButtonStyle(
            color=color,
            surface_tint_color=color,
            overlay_color=f"{color},.1",
            padding=0,
            shape=ft.RoundedRectangleBorder(radius=10),
        )

    def change_member(self, _):
        from services import Database

        members = Database().members
        self.current_member_index = (self.current_member_index + 1) % (len(members) + 1)
        if self.current_member_index == len(members):
            self.text = ""
            self.update_button_style("primary")
        else:
            next_member = members[self.current_member_index]
            self.text = next_member.initials
            self.update_button_style(members[self.current_member_index].color)
        self.update()

    def close_day(self, _):
        self.text = "CLSD"
        self.update_button_style("error")
        self.update()
