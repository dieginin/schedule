from flet import CrossAxisAlignment, Image, MainAxisAlignment, Page, View

from components import CenteredColumn, PrimaryBtn, SecondaryBtn, TertiaryBtn, Title


class HomeView(View):
    def __init__(self, page: Page):
        super().__init__()
        self.page: Page = page

        self.route = "/"

        self.vertical_alignment = MainAxisAlignment.SPACE_EVENLY
        self.horizontal_alignment = CrossAxisAlignment.CENTER

        self.controls = [self.__title(), self.__buttons()]

    def __title(self) -> CenteredColumn:
        return CenteredColumn(
            [
                Image("logo.png", width=500),
                Title(f"Welcome to {self.page.client_storage.get('store_initials')}!"),
            ]
        )

    def __buttons(self) -> CenteredColumn:
        return CenteredColumn(
            [
                PrimaryBtn(
                    "Set Schedule",
                    icon="calendar_month_rounded",
                    on_click=lambda _: self.page.go("/set"),
                ),
                TertiaryBtn(
                    "Export Schedule",
                    icon="download_rounded",
                    on_click=lambda _: self.page.go("/export"),
                ),
                SecondaryBtn(
                    "Manage Store",
                    icon="settings_rounded",
                    on_click=lambda _: self.page.go("/manage"),
                ),
            ]
        )
