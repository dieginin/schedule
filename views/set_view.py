from flet import Page, View


class SetView(View):
    def __init__(self, page: Page):
        super().__init__()
        self.page: Page = page

        self.route = "/set"
        self.controls = []
