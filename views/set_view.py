from datetime import date, datetime, timedelta

import flet as ft

import components as cp


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
        return cp.Subtitle(f"{date.today()}")

    def __Buttons(self) -> ft.Control:
        return cp.CenteredRow(
            [cp.PrimaryBtn("Set Schedule"), cp.SecondaryBtn("Cancel")]
        )

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
