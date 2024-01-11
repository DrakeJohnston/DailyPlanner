from nicegui import native, ui

ui.label('Hello from PyInstaller')

ui.run(native=True, reload=False, port=native.find_open_port())
