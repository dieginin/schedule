from flet import Column, Control, CrossAxisAlignment


class CenteredColumn(Column):
    def __init__(self, controls: list[Control] | None = None):
        super().__init__()
        self.controls = controls
        self.horizontal_alignment = CrossAxisAlignment.CENTER
