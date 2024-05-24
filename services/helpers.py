import flet as ft


def show_snackbar(
    page: ft.Page,
    message: str | None = None,
    message_color: str | None = None,
    bgcolor: str | None = None,
):
    page.snack_bar = ft.SnackBar(ft.Text(message, color=message_color), bgcolor=bgcolor)
    page.snack_bar.open = True
