import flet as ft
from flet_core.date_picker import DatePickerMode, DatePickerEntryMode


def main(page: ft.Page):
    def change_date(e):
        page.add(ft.Checkbox(label=f"Current date {date_picker.value}"))
        date_button.text = f"{date_picker.value}"
        page.update()

    date_picker = ft.DatePicker(
        on_change=change_date,
        date_picker_mode=DatePickerMode.YEAR,
        date_picker_entry_mode=DatePickerEntryMode.INPUT,
        hint_text="Say hello?",
    )

    page.overlay.append(date_picker)

    date_button = ft.ElevatedButton(
        "Pick date",
        icon=ft.icons.CALENDAR_MONTH,
        on_click=lambda _: date_picker.pick_date(),
    )

    page.add(date_button)


ft.app(target=main, view=ft.WEB_BROWSER, port=8550, host="0.0.0.0")