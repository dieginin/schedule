from flet import Page, RouteChangeEvent

from views import *

routes = {
    "/": HomeView,
    "/manage": ManageView,
}


class Router:
    def __init__(self, page: Page):
        page.on_route_change = self.on_route_change

        self.initial_route(page)

    def initial_route(self, page):
        page.go("/")

    def on_route_change(self, e: RouteChangeEvent):
        e.page.views.clear()
        e.page.views.append(routes[e.route](e.page))
        e.page.update()
