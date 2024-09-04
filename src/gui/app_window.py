import flet as ft


def main_page(page:ft.Page):
    page.window.height = 650
    page.window.width = 800
    page.title = "Wifi Speed Test"
    page.horizontal_alignment = ft.MainAxisAlignment.START

    frame = ft.Container(
            margin=0,
            padding=0,
            height=630,
            width=200,
            bgcolor="grey",
            border_radius=10
    )

    page.add(frame)

ft.app(main_page)