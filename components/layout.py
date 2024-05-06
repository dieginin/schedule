from flet import Column, Control, CrossAxisAlignment, Divider, MainAxisAlignment, Row

from .text import Title


class CenteredColumn(Column):
    def __init__(self, controls: list[Control] | None = None):
        super().__init__()
        self.controls = controls
        self.horizontal_alignment = CrossAxisAlignment.CENTER


class CenteredRow(Row):
    def __init__(self, controls: list[Control] | None = None):
        super().__init__()
        self.controls = controls
        self.alignment = MainAxisAlignment.CENTER


class Section(CenteredColumn):
    def __init__(self, title: str, control: Control | None = None):
        super().__init__()
        self.controls = self.__controls(title, control)

    def __controls(self, title: str, control: Control | None = None) -> list[Control]:
        controls = [Title(title), Divider()]
        if control:
            controls.append(control)
        return controls
