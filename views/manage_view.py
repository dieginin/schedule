from flet import Divider, MainAxisAlignment, Page, Row, View

from components import CenteredColumn, HomeBtn, IconBtn, Subtitle, Title


class ManageView(View):
    def __init__(self, page: Page):
        super().__init__()
        self.page: Page = page

        self.route = "/manage"

        self.floating_action_button = HomeBtn(visible=False)
        self.controls = [self.__store(), self.__members()]

    def __title_section(self, value: str | None = None) -> tuple:
        return Title(value), Divider()

    def __store(self) -> CenteredColumn:
        return CenteredColumn(
            [
                *self.__title_section("Store"),
                Row(
                    [
                        Subtitle(f"{self.page.client_storage.get('store_initials')}"),
                        IconBtn("edit", tooltip="Edit name"),
                    ],
                    alignment=MainAxisAlignment.CENTER,
                ),
            ]
        )

    def __members(self) -> CenteredColumn:
        return CenteredColumn(
            [
                *self.__title_section("Members"),
            ]
        )
