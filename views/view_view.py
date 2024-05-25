import flet as ft

import components as cp


class ViewView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page: ft.Page = page

        self.route = "/view"
        self.floating_action_button = cp.HomeBtn()
        self.padding = 0
        self.controls = []
