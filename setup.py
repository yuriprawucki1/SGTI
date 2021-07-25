import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable('Program.py', base=base, icon='Images/icon.ico', target_name='SGTI.exe')
]

buildOptions = dict(
        packages = ['Modules'],
        includes = ['PySimpleGUI', 'mysql.connector', 'platform'],
        include_files = ['Images/', 'config.ini'],
        excludes = [],
        include_msvcr = True
)

setup(
    name = "SGTI",
    version = "1.0.0.0",
    author = "Yuri Prawucki",
    description = "Sistema de Gestão da Tecnologia da Informação",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
