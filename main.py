from flet import Page, app

from services import Router


class Main:
    def __init__(self, page: Page):
        super().__init__()

        self.__init_config__(page)
        self.__init_window__(page)

    def __init_config__(self, page):
        page.title = "SBM Schedule"
        Router(page)

    def __init_window__(self, page):
        page.window_height = page.window_min_height = 600
        page.window_width = page.window_min_width = 800
        page.window_center()


app(Main)
