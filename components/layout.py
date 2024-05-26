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


class WeekTable(ft.DataTable):
    def __init__(self):
        super().__init__()
        self.horizontal_lines = ft.border.BorderSide(1, "primary")
        self.data_row_max_height = 45
        self.heading_row_height = 20
        self.columns = self.__generate_columns()
        self.rows = self.__generate_rows()

    @staticmethod
    def __generate_columns() -> list[ft.DataColumn]:
        column_names = [
            "Hours",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        return [ft.DataColumn(ft.Text(name, color="tertiary")) for name in column_names]

    @staticmethod
    def __generate_rows() -> list[ft.DataRow]:
        from .buttons import MemberBtn

        rows_names = [
            "07:00  \n  08:00",
            "08:00  \n  09:00",
            "09:00  \n  10:00",
            "10:00  \n  11:00",
            "11:00  \n  12:00",
            "12:00  \n  01:00",
            "01:00  \n  02:00",
            "02:00  \n  03:00",
            "03:00  \n  04:00",
            "04:00  \n  05:00",
            "05:00  \n  06:00",
            "06:00  \n  07:00",
            "07:00  \n  08:00",
            "08:00  \n  09:00",
            "09:00  \n  10:00",
            "10:00  \n  11:00",
            "11:00  \n  12:00",
        ]
        return [
            ft.DataRow(
                [
                    ft.DataCell(ft.Text(name, size=12)),
                    *[ft.DataCell(MemberBtn()) for _ in range(7)],
                ]
            )
            for name in rows_names
        ]
