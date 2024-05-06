from flet import Page, RouteChangeEvent

from views import *

routes = {
    "/": HomeView,
    "/export": ExportView,
    "/manage": ManageView,
    "/set": SetView,
}


class Router:
    def __init__(self, page: Page):
        self.page: Page = page

        self.page.on_route_change = self.on_route_change

        self.initial_route()

    def initial_route(self):
        self.page.go("/")

    def on_route_change(self, e: RouteChangeEvent):
        self.page.views.clear()
        if self.page.client_storage.get("store_initials"):
            self.page.views.append(routes[e.route](self.page))
        else:
            self.page.views.append(routes["/manage"](self.page))
        self.page.update()
