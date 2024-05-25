import flet as ft

from components import CenteredColumn, PrimaryBtn, SecondaryBtn, TertiaryBtn, Title
from services.database import Database


class HomeView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page: ft.Page = page

        self.route = "/"

        self.vertical_alignment = ft.MainAxisAlignment.SPACE_EVENLY
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

        self.controls = [self.__title(), self.__buttons()]

    def __title(self) -> CenteredColumn:
        return CenteredColumn(
            [
                ft.Image("logo.png", width=500),
                Title(f"Welcome to {self.page.client_storage.get('store_initials')}!"),
            ]
        )

    def __buttons(self) -> CenteredColumn:
        disabled = not (
            self.page.client_storage.get("store_initials")
            and len(Database().members) > 0
        )
        return CenteredColumn(
            [
                PrimaryBtn(
                    "Set Schedule",
                    icon="calendar_month_rounded",
                    on_click=lambda _: self.page.go("/set"),
                    disabled=disabled,
                ),
                TertiaryBtn(
                    "View Schedule",
                    icon="bar_chart_rounded",
                    on_click=lambda _: self.page.go("/view"),
                    disabled=disabled,
                ),
                SecondaryBtn(
                    "Manage Store",
                    icon="settings_rounded",
                    on_click=lambda _: self.page.go("/manage"),
                ),
            ]
        )
