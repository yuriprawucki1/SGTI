import PySimpleGUI as sg
from Modules import DataBase

def Register():
    sg.theme('Reddit')

    layout = [
        [sg.Text('Local', size=(6,0)), sg.Input(size=(20,0), key='place')],
        [sg.Button('Cadastrar',size=(10,1)),sg.Button('Fechar',size=(10,1))]
    ]

    registerplace = sg.Window("S.G.T.I. - Cadastrar Local", layout, resizable=False, icon='Images/icon.ico', finalize=True)

    while True:
        evento, valores = registerplace.read()
        if evento in (sg.WIN_CLOSED, 'Fechar'):
            break
        if evento == 'Cadastrar':
            if valores['place'] == '':
                sg.popup_auto_close('Cadastro não efetuado','Preencha o Local', auto_close_duration=4, no_titlebar=True, button_type=5, background_color='#8c8c8c', text_color='#ededed', font=('Arial Black',10))
            else:
                sql = "INSERT INTO places (place) VALUES (%s)"
                val = valores['place'],
                DataBase.cursor.execute(sql, val)
                DataBase.con.commit()
                sg.popup_auto_close('Cadastro efetuado', auto_close_duration=2, no_titlebar=True, button_type=5, background_color='#8c8c8c', text_color='#ededed', font=('Arial Black',12))

    registerplace.close()