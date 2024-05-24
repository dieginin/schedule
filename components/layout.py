from typing import Literal

import flet as ft


class Field(ft.TextField):
    def __init__(
        self,
        hint_text: str | None = None,
        max_length: int | None = None,
        on_submit=None,
        on_change=None,
        autofocus: bool | None = None,
        capitalization: Literal["word", "upper"] | None = None,
        width: ft.OptionalNumber = None,
    ):
        super().__init__()
        self.hint_text = hint_text
        self.max_length = max_length
        self.counter_text = " "
        self.on_submit = on_submit
        self.on_change = on_change
        self.autofocus = autofocus
        self.capitalization = (
            ft.TextCapitalization.CHARACTERS
            if capitalization == "upper"
            else ft.TextCapitalization.WORDS if capitalization == "word" else None
        )  # type: ignore
        self.width = width
        self.border = ft.InputBorder.UNDERLINE
        self.text_align = ft.TextAlign.CENTER


class Dialog(ft.AlertDialog):
    def __init__(
        self,
        title: str | None = None,
        content: ft.Control | None = None,
        on_confirm=None,
    ):
        super().__init__()
        self.title = ft.Text(title) if title else None
        self.content = content
        self.actions = [
            ft.TextButton("Confirm", on_click=on_confirm),
            ft.TextButton(
                "Cancel",
                on_click=self.close,
                style=ft.ButtonStyle(color="red", overlay_color="red,.1"),
            ),
        ]

    def close(self, e: ft.ControlEvent):
        self.open = False
        e.page.update()


class CenteredColumn(ft.Column):
    def __init__(self, controls: list[ft.Control] | None = None):
        super().__init__()
        self.controls = controls
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER


class CenteredRow(ft.Row):
    def __init__(self, controls: list[ft.Control] | None = None):
        super().__init__()
        self.controls = controls
        self.alignment = ft.MainAxisAlignment.CENTER
