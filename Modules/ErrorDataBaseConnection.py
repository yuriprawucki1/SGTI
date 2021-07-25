from configparser import Error
import PySimpleGUI as sg

def ErrorConnection():
    sg.theme('Reddit')
    column1 = [
        [sg.Image(filename='Images/error_database.png')]
    ]
    column2 = [
        [sg.Text('Falha ao se conectar no banco de dados', font=('Helvetica',10,'bold'))],
        [sg.Text('Favor verifique a conexão\nou se o servidor está iniciado', font=('Helvetica',10,'bold'))]
    ]
    layout = [
        [sg.Column(column1), sg.Column(column2, element_justification='c')]
    ]
    errordatabaseconnection = sg.Window('S.G.T.I. - Banco de Dados',layout,resizable=False,icon='Images/icon.ico',disable_minimize=True,finalize=True)
    errordatabaseconnection.TKroot.focus_force()

    while True:
        evento, valores = errordatabaseconnection.read()
        if evento == sg.WIN_CLOSED:
            break
    
    errordatabaseconnection.close()