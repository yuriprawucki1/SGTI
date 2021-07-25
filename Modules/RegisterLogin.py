import PySimpleGUI as sg
from Modules import DataBase

def Register():
    sg.theme('Reddit')

    layout = [
        [sg.Text('Primeiro Nome', size=(14,0)), sg.Input(size=(20,0), key='first_name')],
        [sg.Text('Último Nome', size=(14,0)), sg.Input(size=(20,0), key='last_name')],
        [sg.Text('Login', size=(14,0)), sg.Input(key='login', size=(20,0), readonly=True)],
        [sg.Text('Senha', size=(14,0)), sg.Input(size=(20,0), key='password')],
        [sg.Button('Cadastrar',size=(10,1)),sg.Button('Fechar',size=(10,1))]
    ]

    registerlogin = sg.Window("S.G.T.I. - Cadastrar Login", layout, resizable=False, icon='Images/icon.ico', finalize=True)

    while True:
        evento, valores = registerlogin.read()
        if evento in (sg.WIN_CLOSED, 'Fechar'):
            break
        if evento == 'Cadastrar':
            if valores['first_name'] == '' and valores['last_name'] == '' and valores['password'] == '':
                sg.popup_auto_close('Cadastro não efetuado','Preencha o Nome, o Sobrenome e a Senha', auto_close_duration=4, no_titlebar=True, button_type=5, background_color='#8c8c8c', text_color='#ededed', font=('Arial Black',10))
            else:
                username = valores['first_name'].lower()+"."+valores['last_name'].lower()
                sql = "INSERT INTO logins (name, last_name, username, password) VALUES (%s, %s, %s, %s)"
                val = valores['first_name'], valores['last_name'], username, valores['password']
                DataBase.cursor.execute(sql, val)
                DataBase.con.commit()
                registerlogin['login'].update(username)
                sg.popup_auto_close('Cadastro efetuado', auto_close_duration=2, no_titlebar=True, button_type=5, background_color='#8c8c8c', text_color='#ededed', font=('Arial Black',12))

    registerlogin.close()