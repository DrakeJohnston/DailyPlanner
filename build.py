import os
import subprocess
from pathlib import Path
import nicegui

cmd = [
    'python',
    '-m', 'PyInstaller',
    'main.py', # your main file with ui.run()
    '--name', 'myapp', # name of your app
    '--onefile',
    #'--hidden-import', '__future__',
    #'--hidden-import', 'asyncio',
    #'--hidden-import', 'typing',
    '--paths', 'C:\\Users\\ironb\\PycharmProjects\\DailyPlanner\\.venv\\Lib\\site-packages',
    '--windowed', # prevent console appearing, only use with ui.run(native=True, ...)
    '--add-data', f'{Path(nicegui.__file__).parent}{os.pathsep}nicegui'
]
subprocess.call(cmd)