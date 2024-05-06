from flet import Page, View


class ExportView(View):
    def __init__(self, page: Page):
        super().__init__()
        self.page: Page = page

        self.route = "/export"
        self.controls = []
