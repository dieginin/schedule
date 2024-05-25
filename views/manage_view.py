import flet as ft

import components as cp
from models import Member
from services import Database, show_snackbar


class DataTable(ft.DataTable):
    column_names = ["Name", "Initials", "Color", "Controls"]

    def __init__(self):
        super().__init__()
        self.horizontal_lines = ft.border.BorderSide(1, "primary")
        self.columns = [
            ft.DataColumn(ft.Text(i, color="tertiary")) for i in self.column_names
        ]
        self.update_table()

    def update_table(self):
        db = Database()
        self.rows.clear()
        for member in db.members:
            self.rows.append(
                ft.DataRow(
                    [
                        ft.DataCell(ft.Text(member.name)),
                        ft.DataCell(ft.Text(member.initials)),
                        ft.DataCell(
                            cp.ColorBtn(
                                member.color,
                                show_color=True,
                                callback=self.__edit_color,
                            ),
                            data=member,
                        ),
                        ft.DataCell(
                            ft.Row(
                                [
                                    ft.IconButton(
                                        "edit",
                                        on_click=self.__edit_member,
                                        style=ft.ButtonStyle(
                                            color="tertiary",
                                            overlay_color="tertiary,.1",
                                        ),
                                    ),
                                    ft.IconButton(
                                        "delete",
                                        on_click=self.__delete_member,
                                        style=ft.ButtonStyle(
                                            color="red", overlay_color="red,.1"
                                        ),
                                    ),
                                ],
                                data=member,
                            )
                        ),
                    ]
                )
            )

    def __edit_color(self, e: ft.ControlEvent, member: Member, color: str):
        if member.color != color:
            modify = member.modify(color=color)

            if "modified" in modify:
                show_snackbar(e.page, modify, "ontertiary", "tertiary")
                self.update_table()
                e.page.update()
                return True
            else:
                show_snackbar(e.page, modify, "onerror", "error")

    def __edit_member(self, e: ft.ControlEvent):
        member: Member = e.control.parent.data

        def edit(e: ft.ControlEvent):
            name_val = name.value.title().strip() if name.value else None
            initials_val = initials.value.strip() if initials.value else None

            if name_val or initials_val:
                dialog.close(e)
                modify = member.modify(name_val, initials_val)

                if "modified" in modify:
                    show_snackbar(e.page, modify, "ontertiary", "tertiary")
                    self.update_table()
                    e.page.update()
                else:
                    show_snackbar(e.page, modify, "onerror", "error")
            else:
                name.focus()

        name = cp.Field(
            member.name, capitalization="word", on_submit=edit, autofocus=True
        )
        initials = cp.Field(
            member.initials,
            capitalization="upper",
            width=80,
            max_length=5,
            on_submit=edit,
        )
        body = ft.Container(
            cp.CenteredColumn([name, initials]),
            height=115,
        )

        dialog = cp.Dialog("Edit", body, edit)
        e.page.dialog = dialog
        dialog.open = True
        e.page.update()

    def __delete_member(self, e: ft.ControlEvent):
        member: Member = e.control.parent.data

        def delete(e: ft.ControlEvent):
            dialog.close(e)
            delet = member.delete()

            if "deleted" in delet:
                show_snackbar(e.page, delet, "onprimary", "primary")
                self.update_table()
                e.page.update()

        dialog = cp.Dialog(
            "Delete", ft.Text(f"Do you really want to delete\n{member.name}?"), delete
        )
        e.page.dialog = dialog
        dialog.open = True
        e.page.update()


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

        self.__view_components()
        self.floating_action_button = self.home_btn
        self.padding = 0
        self.controls = [self.__store(), self.__members()]

    def __view_components(self):
        self.home_btn = cp.HomeBtn(
            visible=len(Database().members) > 0
            and bool(self.page.client_storage.get("store_initials"))
        )
        self.store_name = cp.Subtitle(
            value=f"{self.page.client_storage.get('store_initials')}"
        )
        self.member_name = cp.Field(
            "Name",
            capitalization="word",
            on_change=self.__suggest_initials,
            on_submit=self.__add_member,
        )
        self.member_initials = cp.Field(
            "Initials",
            capitalization="upper",
            width=80,
            max_length=5,
            on_submit=self.__add_member,
        )
        self.member_color = cp.ColorBtn()
        self.members_table = DataTable()

    def __store(self) -> Section:
        return Section(
            "Store",
            cp.CenteredRow(
                [
                    self.store_name,
                    cp.IconBtn(
                        "edit", tooltip="Edit name", on_click=self.__change_store
                    ),
                ]
            ),
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
                            cp.PrimaryBtn("Add", on_click=self.__add_member),
                        ]
                    ),
                    self.members_table,
                ]
            ),
            expand=True,
        )

    def __check_home_btn(self):
        self.home_btn.visible = len(Database().members) > 0 and bool(
            self.page.client_storage.get("store_initials")
        )
        self.home_btn.update()

    def __open_dialog(self, dialog: cp.Dialog):
        self.page.dialog = dialog
        dialog.open = True
        self.page.update()

    def __change_store(self, _):
        def change_name(e: ft.ControlEvent):
            store_name = new_name.value
            if store_name:
                dialog.close(e)
                e.page.client_storage.set("store_initials", store_name)
                self.store_name.value = store_name
                self.store_name.update()
                self.__check_home_btn()
            else:
                new_name.focus()

        new_name = cp.Field(
            self.store_name.value,
            autofocus=True,
            capitalization="upper",
            max_length=4,
            on_submit=change_name,
        )
        dialog = cp.Dialog("Change Store", new_name, on_confirm=change_name)

        self.__open_dialog(dialog)

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

    def __add_member(self, e: ft.ControlEvent):
        name = self.member_name.value
        initials = self.member_initials.value
        color = self.member_color.value

        if name and initials and color:
            db = Database()
            insert = db.insert_member(name.title().strip(), initials.strip(), color)
            if "inserted" in insert:
                show_snackbar(e.page, insert, "onprimary", "primary")
                self.members_table.update_table()
                self.member_color.generate_color()
            else:
                show_snackbar(e.page, insert, "onerror", "error")

            self.member_name.value = ""
            self.member_initials.value = ""
            self.__check_home_btn()

            e.page.update()
