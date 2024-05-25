from flet import Page, Theme, app

from services import Router


class Main:
    def __init__(self, page: Page):
        super().__init__()
        self.page: Page = page

        self.__init_config__()
        self.__init_window__()

    def __init_config__(self):
        self.page.title = "SBM Schedule"
        self.page.theme = Theme(color_scheme_seed="bluegrey")
        Router(self.page)

    def __init_window__(self):
        self.page.window_height = self.page.window_min_height = 1000
        self.page.window_width = self.page.window_min_width = 900
        self.page.window_center()


app(Main)
