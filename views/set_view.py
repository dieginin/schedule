from datetime import datetime, timedelta

import flet as ft

import components as cp


class DataTable(ft.DataTable):

    def __init__(self):
        super().__init__()
        self.horizontal_lines = ft.border.BorderSide(1, "primary")
        self.data_row_max_height = 45
        self.heading_row_height = 20
        self.columns = self.__generate_columns()
        self.rows = self.__generate_rows()

    @staticmethod
    def __generate_columns() -> list[ft.DataColumn]:
        column_names = [
            "Hours",
            "Monday",
            "Tuesday",
            "Wednesday",
            "Thursday",
            "Friday",
            "Saturday",
            "Sunday",
        ]
        return [ft.DataColumn(ft.Text(name, color="tertiary")) for name in column_names]

    @staticmethod
    def __generate_rows() -> list[ft.DataRow]:
        rows_names = [
            "07:00  \n  08:00",
            "08:00  \n  09:00",
            "09:00  \n  10:00",
            "10:00  \n  11:00",
            "11:00  \n  12:00",
            "12:00  \n  01:00",
            "01:00  \n  02:00",
            "02:00  \n  03:00",
            "03:00  \n  04:00",
            "04:00  \n  05:00",
            "05:00  \n  06:00",
            "06:00  \n  07:00",
            "07:00  \n  08:00",
            "08:00  \n  09:00",
            "09:00  \n  10:00",
            "10:00  \n  11:00",
            "11:00  \n  12:00",
        ]
        return [
            ft.DataRow(
                [
                    ft.DataCell(ft.Text(name, size=12)),
                    *[ft.DataCell(cp.MemberBtn()) for _ in range(7)],
                ]
            )
            for name in rows_names
        ]


class SetView(ft.View):
    def __init__(self, page: ft.Page):
        super().__init__()
        self.page: ft.Page = page

        self.route = "/set"

        self.__view_config()
        self.__view_components()
        self.controls = [self.__Date(), self.__Week(), self.__Buttons()]

    def __view_config(self):
        self.padding = 0
        self.floating_action_button = cp.HomeBtn()
        self.vertical_alignment = ft.MainAxisAlignment.SPACE_EVENLY
        self.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def __view_components(self):
        today = datetime.now()
        next_monday = self.__get_next_monday(today)
        self.first_day = cp.Subtitle(next_monday.strftime("%d %B %Y"))
        self.picker = ft.DatePicker(
            value=next_monday,
            date_picker_entry_mode=ft.DatePickerEntryMode.CALENDAR_ONLY,
            help_text="Set week",
            on_change=self.__change_date,
        )
        self.page.overlay.append(self.picker)

    def __Date(self) -> ft.Control:
        return cp.CenteredRow(
            [
                self.first_day,
                cp.IconBtn(
                    "edit",
                    tooltip="Edit date",
                    on_click=lambda _: self.picker.pick_date(),
                ),
            ]
        )

    def __Week(self) -> ft.Control:
        return DataTable()

    def __Buttons(self) -> ft.Control:
        return cp.PrimaryBtn("Set Schedule")

    def __get_next_monday(self, date: datetime):
        return date + timedelta(days=(7 - date.weekday()) % 7)

    def __change_date(self, e: ft.ControlEvent):
        if self.picker.value:
            if self.picker.value.weekday() != 0:
                self.picker.value = self.__get_next_monday(self.picker.value)
                self.picker.pick_date()
            else:
                self.first_day.value = self.picker.value.strftime("%d %B %Y")
                self.update()
