from flet import FontWeight, Paint, PaintLinearGradient, Text, TextStyle


class Title(Text):
    def __init__(self, value: str | None = None):
        super().__init__()
        self.value = value
        self.style = TextStyle(
            size=60,
            weight=FontWeight.W_100,
            letter_spacing=5,
            foreground=Paint(
                gradient=PaintLinearGradient(
                    (0, 135), (120, 20), ["primary", "tertiary"]
                ),
            ),
        )
