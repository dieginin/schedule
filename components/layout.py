import flet as ft


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
