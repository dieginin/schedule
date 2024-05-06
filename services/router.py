from flet import Page, RouteChangeEvent

from views import *

routes = {
    "/": HomeView,
    "/manage": ManageView,
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
        self.page.views.append(routes[e.route](self.page))
        self.page.update()
