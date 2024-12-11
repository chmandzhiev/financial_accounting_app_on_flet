import flet as ft


def main(page: ft.Page):
    page.vertical_alignment = ft.MainAxisAlignment.START
    rows = []

    def add_display_date(e):
        def display_date_of_expenses(e):
            txt_date_expenses.value = e.control.value.strftime("%d.%m.%Y")
            page.update()

        page.open(ft.DatePicker(date_picker_entry_mode="calendar",
                                on_change=display_date_of_expenses))

    def get_table_row(e: ft.ControlEvent):
        if e.control.selected is False:
            e.control.selected = True
        else:
            e.control.selected = False
        page.update()

    def add_record_to_table(e):
        rows.append(ft.DataRow(
                        on_select_changed=get_table_row,
                        cells=[
                           ft.DataCell(ft.Text(txt_date_expenses.value)),
                           ft.DataCell(ft.Text(dropdown_1.value)),
                           ft.DataCell(ft.Text("")),
                           ft.DataCell(ft.Text("User1")),
                           ft.DataCell(ft.Text(txt_summ_expenses.value)),
                           ft.DataCell(ft.Text(txt_notes.value)),
                        ],
                    ),)

        txt_date_expenses.value = ""
        txt_summ_expenses.value = ""
        txt_notes.value = ""
        dropdown_1.value = ""

        page.update()

    def del_record_in_table(e):
        new_rows = []
        for row in rows:
            if row.selected is False:
                new_rows.append(row)
        rows.clear()
        rows.extend(new_rows)

        page.update()

    btn_add_display_date = ft.ElevatedButton("Выбрать дату", icon=ft.icons.CALENDAR_MONTH, on_click=add_display_date)
    btn_add_record_to_table = ft.ElevatedButton("Добавить запись", on_click=add_record_to_table)
    btn_del_record_in_table = ft.ElevatedButton("Удалить запись", on_click=del_record_in_table)

    txt_date_expenses = ft.TextField(label="Дата расходов", read_only=True)
    txt_summ_expenses = ft.TextField(label="Сумма расходов", width=473)
    txt_notes = ft.TextField(label="Примечание", width=473, max_lines=3)

    dropdown_1 = ft.Dropdown(label="Статья расходов",
                             hint_text="Выбрать статью расходов",
                             options=[
                                 ft.dropdown.Option("ЖКХ"),
                                 ft.dropdown.Option("Продукты"),
                                 ft.dropdown.Option("Заправка авто"),
                                 ft.dropdown.Option("Кафе"),], width=473)

    data_table = ft.Container(ft.DataTable(
                                 border=ft.border.all(1, "black"),
                                 vertical_lines=ft.BorderSide(1, "black"),
                                 horizontal_lines=ft.BorderSide(1, "black"),
                                 heading_row_color=ft.colors.BLACK12,
                                 show_checkbox_column=True,
                                 columns=[
                                     ft.DataColumn(ft.Text("Дата")),
                                     ft.DataColumn(ft.Text("Статья расходов")),
                                     ft.DataColumn(ft.Text("Категория")),
                                     ft.DataColumn(ft.Text("Имя учетной записи")),
                                     ft.DataColumn(ft.Text("Сумма")),
                                     ft.DataColumn(ft.Text("Примечание")),
                                 ],
                                 rows=rows,), margin=ft.margin.only(top=10), expand=True,)

    row_1 = ft.Row([txt_date_expenses, btn_add_display_date], alignment=ft.MainAxisAlignment.CENTER)
    row_2 = ft.Row([dropdown_1], alignment=ft.MainAxisAlignment.CENTER)
    row_3 = ft.Row([txt_summ_expenses], alignment=ft.MainAxisAlignment.CENTER)
    row_4 = ft.Row([txt_notes], alignment=ft.MainAxisAlignment.CENTER)
    row_5 = ft.Row([btn_add_record_to_table, btn_del_record_in_table], alignment=ft.MainAxisAlignment.CENTER)
    row_6 = ft.Row([data_table])

    page.add(row_1, row_2, row_3, row_4, row_5, row_6)


ft.app(main)
