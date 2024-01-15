from nicegui import native, ui, app

__version__ = 0.5

windowx, windowy = 500, 1000
todoList = []

with ui.card().classes("mx-auto w-full h-max") as mainCard:
    with ui.row():
        ui.label("Todo: ").style("font-size: 300%")
        ui.card().classes("w-full")
        with ui.row():
            ui.button("Add")
            ui.button("Remove")

ui.run(native=True, reload=False, port=native.find_open_port(), window_size=(500, 500), title="Daily Planner")
