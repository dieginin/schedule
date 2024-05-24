from typing import Literal

import flet as ft


class Field(ft.TextField):
    def __init__(
        self,
        hint_text: str | None = None,
        value: str | None = None,
        max_length: int | None = None,
        on_submit=None,
        on_change=None,
        capitalization: Literal["word", "upper"] | None = None,
        width: ft.OptionalNumber = None,
    ):
        super().__init__()
        self.hint_text = hint_text
        self.value = value
        self.max_length = max_length
        self.counter_text = " "
        self.on_submit = on_submit
        self.on_change = on_change
        self.capitalization = (
            ft.TextCapitalization.CHARACTERS
            if capitalization == "upper"
            else ft.TextCapitalization.WORDS if capitalization == "word" else None
        )  # type: ignore
        self.width = width
        self.border = ft.InputBorder.UNDERLINE
        self.text_align = ft.TextAlign.CENTER


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
