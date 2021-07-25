import PySimpleGUI as sg
from Modules import DataBase

def Register():
    sg.theme('Reddit')

    layout = [
        [sg.Text('Nome Completo', size=(14,0)),sg.Input(size=(40,0),key='full_name')],
        [sg.Text('Função', size=(14,0)),sg.Input(size=(40,0),key='occupation')],
        [sg.Text('Local', size=(14,0)),sg.InputCombo(['VarejoCar','Carhill MGA','Carhill CAC'], readonly=True,default_value='',size=(38,0),key='place')],
        [sg.Text('E-mail', size=(14,0)),sg.Input(size=(40,0),key='email')],
        [sg.Text('Senha E-mail', size=(14,0)),sg.Input(size=(40,0),key='pass_email')],
        [sg.Text('Skype', size=(14,0)),sg.Input(size=(40,0),key='skype')],
        [sg.Text('Senha Skype', size=(14,0)),sg.Input(size=(40,0),key='pass_skype')],
        [sg.Text('Conta Google', size=(14,0)),sg.InputCombo(['Não','Sim'], readonly=True,default_value='Não',size=(5,0),key='google_account')],
        [sg.Text('Sistemas', size=(14,0)),sg.Checkbox('Autcom',key='autcom'),sg.Checkbox('SGR',key='sgr'),sg.Checkbox('Express',key='express')],
        [sg.Text('Login Sistemas', size=(14,0)),sg.Input(size=(40,0),key='login_systems')],
        [sg.Text('Senha Sistemas', size=(14,0)),sg.Input(size=(40,0),key='pass_systems')],
        [sg.Button('Cadastrar',size=(10,1)),sg.Button('Cancelar',size=(10,1))]
    ]
    registerusers = sg.Window("S.G.T.I. - Cadastrar Usuários", layout, resizable=False, icon='Images/icon.ico', finalize=True)

    while True:
        evento, valores = registerusers.read()
        if evento in (sg.WIN_CLOSED, 'Cancelar'):
            break
        if evento == 'Cadastrar':
            if valores['full_name'] == '' and valores['occupation'] == '' and valores['place'] == '':
                sg.popup_auto_close('Cadastro não efetuado','Preencha o Nome, a Função e o Local',auto_close_duration=4, no_titlebar=True, button_type=5, background_color='#8c8c8c', text_color='#ededed', font=('Arial Black',10))
            else:            
                sql = "INSERT INTO users (full_name, occupation, place, email, pass_email, skype, pass_skype, google_account, sistema_autcom, sistema_sgr, sistema_express, login_systems, pass_systems, inactive) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                val = valores['full_name'], valores['occupation'], valores['place'], valores['email'], valores['pass_email'], valores['skype'], valores['pass_skype'], valores['google_account'], valores['autcom'], valores['sgr'], valores['express'], valores['login_systems'], valores['pass_systems'], ['Não']
                DataBase.cursor.execute(sql, val)
                DataBase.con.commit()
                sg.popup_auto_close('Cadastro efetuado', auto_close_duration=2, no_titlebar=True, button_type=5, background_color='#8c8c8c', text_color='#ededed', font=('Arial Black',12))
    
    registerusers.close()