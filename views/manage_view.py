from flet import Divider, Page, View

from components import CenteredColumn, CenteredRow, HomeBtn, IconBtn, Section, Subtitle


class ManageView(View):
    def __init__(self, page: Page):
        super().__init__()
        self.page: Page = page

        self.route = "/manage"

        self.floating_action_button = HomeBtn(visible=False)
        self.__view_controls()
        self.controls = [self.__store(), self.__members()]

    def __view_controls(self):
        self.name = Subtitle(f"{self.page.client_storage.get('store_initials')}")

    def __store(self) -> CenteredColumn:
        return Section(
            "Store",
            CenteredRow(
                [
                    self.name,
                    IconBtn(
                        "edit", tooltip="Edit name"
                    ),  # TODO crear popup/dialog para cambiar nombre de tienda
                ]
            ),
        )

    def __members(self) -> CenteredColumn:
        return Section("Members")  # TODO members section
