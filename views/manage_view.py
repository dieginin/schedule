import flet as ft

import components as cp


class DataTable(ft.DataTable):
    column_names = ["Name", "Initials", "Color", "Controls"]

    def __init__(self):
        super().__init__()
        self.expand = True
        self.border_radius = 8
        self.border = ft.border.all(2, "red")
        self.horizontal_lines = ft.border.BorderSide(1, "primary")
        self.columns = [
            ft.DataColumn(ft.Text(i, color="tertiary")) for i in self.column_names
        ]


class Section(ft.Column):
    def __init__(self, title: str, control: ft.Control, expand: bool | None = None):
        super().__init__()
        self.expand = expand
        self.controls = [
            cp.CenteredRow([cp.Title(title)]),
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

        self.floating_action_button = cp.HomeBtn(visible=False)
        self.__view_components()
        self.controls = [self.__store(), self.__members()]

    def __view_components(self):
        self.store_name = cp.Subtitle(
            value=f"{self.page.client_storage.get('store_initials')}"
        )
        self.member_name = cp.Field(
            "Name", capitalization="word", on_change=self.__suggest_initials
        )
        self.member_initials = cp.Field(
            "Initials", capitalization="upper", width=80, max_length=5
        )
        self.member_color = ft.Container(height=40, width=40, bgcolor="red")
        self.members_table = DataTable()

    def __store(self) -> Section:
        return Section(
            "Store",
            cp.CenteredRow([self.store_name, cp.IconBtn("edit", tooltip="Edit name")]),
        )

    def __members(self) -> Section:
        return Section(
            "Members",
            cp.CenteredColumn(
                [
                    cp.CenteredRow(
                        [
                            self.member_name,
                            self.member_initials,
                            self.member_color,
                            cp.PrimaryBtn("Add"),
                        ]
                    ),
                    self.members_table,
                ]
            ),
            expand=True,
        )

    def __suggest_initials(self, e: ft.ControlEvent):
        name_splited = e.control.value.split()
        initials_suggested = ""
        if len(name_splited) > 1:
            for w in name_splited[:5]:
                initials_suggested += w[0]
        else:
            try:
                initials_suggested = name_splited[0][:2].upper()
            except:
                initials_suggested = initials_suggested

        self.member_initials.value = initials_suggested
        self.member_initials.update()
