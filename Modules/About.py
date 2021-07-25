import PySimpleGUI as sg
import platform

def About():
    sg.theme('Reddit')
    pysgversion = sg.version
    layout = [
        [sg.Text('Versão deste programa: 1.0')],
        [sg.Text('Versão do Python: '+platform.python_version())],
        [sg.Text('Versão do PySimpleGUI:')],
        [sg.Text(pysgversion)]
    ]
    about = sg.Window('Sobre',layout,resizable=False,icon='Images/icon.ico',disable_minimize=True,finalize=True)
    about.TKroot.focus_force()