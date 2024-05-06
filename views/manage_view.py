from flet import Page, View


class ManageView(View):
    def __init__(self, page: Page):
        super().__init__()
        self.page: Page = page

        self.route = "/manage"
        self.controls = []
