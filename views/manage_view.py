import flet as ft

from components import CenteredRow, HomeBtn, IconBtn, Subtitle, Title


class Section(ft.Column):
    def __init__(self, title: str, control: ft.Control, expand: bool | None = None):
        super().__init__()
        self.expand = expand
        self.controls = [
            CenteredRow([Title(title)]),
            ft.Divider(height=1),
            ft.Column(
                [control],
                expand=expand,
                scroll=ft.ScrollMode.AUTO,
            ),
        ]


class ManageView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page: ft.Page = page

        self.route = "/manage"

        self.floating_action_button = HomeBtn(visible=False)
        self.__view_components()
        self.controls = [self.__store(), self.__members()]

    def __view_components(self):
        self.store_name = Subtitle(f"{self.page.client_storage.get('store_initials')}")

    def __store(self) -> Section:
        return Section(
            "Store",
            CenteredRow([self.store_name, IconBtn("edit", tooltip="Edit name")]),
        )

    def __members(self) -> Section:
        return Section(
            "Members",
            ft.Container(bgcolor="red", height=1500),
            expand=True,
        )
