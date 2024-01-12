from nicegui import native, ui, app

__version__ = 0.5

windowx, windowy = 500, 1000
upcomingList = []

app.native.window_args['resizable'] = False


def test(text, num):
    title.set_text(text)
    if num == 0:
        UpcomingCard.visible = True
        Quicklist.visible = False
    else:
        UpcomingCard.visible = False
        Quicklist.visible = True


def reminder_button():
    rem.props("text")


with ui.row().classes('w-full'):
    title = ui.label("Upcoming:").style('font-size: 400%; font-weight: 300')
    ui.space()
    with ui.button(icon='menu'):
        with ui.menu() as menu:
            ui.menu_item("Upcoming", on_click=lambda e: test("Upcoming:", 0))
            ui.menu_item("Quicklist", on_click=lambda e: test("Quick-List:", 1))
with ui.card().classes('w-full h-dvh') as UpcomingCard:
    with ui.column():
        for x in range(0, len(upcomingList)):
            ui.label(upcomingList[x])
with ui.card().classes("w-full h-dvh") as Quicklist:
    with ui.row():
        with ui.label("Todo").classes('w-full'):
            ui.textarea().props("autogrow")
        with ui.label("Reminder").classes('w-full'):
            rem = ui.textarea().props("autogrow")
    ui.button(text="Add Reminders To Upcoming")

Quicklist.set_visibility(False)
ui.run(native=True, reload=False, port=native.find_open_port(), window_size=(500, 500), title="Daily Planner")
