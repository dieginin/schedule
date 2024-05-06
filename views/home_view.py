from flet import Page, View


class HomeView(View):
    def __init__(self, page: Page):
        super().__init__()
        self.page = page

        self.route = "/"
        self.controls = []
