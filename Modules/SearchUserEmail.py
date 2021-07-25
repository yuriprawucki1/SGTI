import PySimpleGUI as sg
from Modules import DataBase

def Search():
    sg.theme('Reddit')

    column1 = [
        [sg.Text('Busca Nome', size=(14,0)),sg.Input(size=(30,0),key='busca'),sg.Button('Buscar',size=(6,0),bind_return_key=True)],
        [sg.Text('Nome Completo', size=(14,0)),sg.Text(size=(40,0),key='full_name', font=('Helvetica',10,'bold'))],
        [sg.Text('Função', size=(14,0)),sg.Text(size=(40,0),key='occupation', font=('Helvetica',10,'bold'))],
        [sg.Text('Local', size=(14,0)),sg.Text(size=(40,0),key='place', font=('Helvetica',10,'bold'))],
        [sg.Text('E-mail', size=(14,0)),sg.Text(size=(40,0),key='email', font=('Helvetica',10,'bold'))],
        [sg.Text('Senha E-mail', size=(14,0)),sg.Text(size=(40,0),key='pass_email', font=('Helvetica',10,'bold'))],
        [sg.Text('Skype', size=(14,0)),sg.Text(size=(40,0),key='skype', font=('Helvetica',10,'bold'))],
        [sg.Text('Senha Skype', size=(14,0)),sg.Text(size=(40,0),key='pass_skype', font=('Helvetica',10,'bold'))],
        [sg.Text('Conta Google', size=(14,0)),sg.Text(size=(40,0),key='google_account', font=('Helvetica',10,'bold'))],
        [sg.Text('Sistemas',size=(14,0)),sg.Text('Autcom:',size=(7,0)),sg.Text(size=(4,0),key='autcom', font=('Helvetica',10,'bold')),sg.Text('SGR:',size=(4,0)),sg.Text(size=(4,0),key='sgr', font=('Helvetica',10,'bold')),sg.Text('Express:',size=(8,0)),sg.Text(size=(4,0),key='express', font=('Helvetica',10,'bold'))],
        [sg.Text('Login Sistemas', size=(14,0)),sg.Text(size=(40,0),key='login_systems', font=('Helvetica',10,'bold'))],
        [sg.Text('Senha Sistemas', size=(14,0)),sg.Text(size=(40,0),key='pass_systems', font=('Helvetica',10,'bold'))],
        [sg.Text('Inativo', size=(14,0)),sg.Text(size=(40,0),key='inactive', font=('Helvetica',10,'bold'))],
        [sg.Button('Fechar',size=(6,0))]
    ]

    column2 = [
        [sg.Multiline(size=(45,15), disabled=True, auto_refresh=True, reroute_stdout=True, reroute_cprint=True, write_only=True, key='-OUT-', autoscroll=True)]
    ]
    
    layout = [
        [sg.Column(column1), sg.Column(column2)]
    ]

    searchuseremail = sg.Window('S.G.T.I. - Busca Usuários Por E-mail', layout, icon='Images/icon.ico', finalize=True)

    while True:
        evento, valores = searchuseremail.read()
        if evento in (sg.WIN_CLOSED, 'Fechar'):
            break
        if evento == 'Buscar':
            if valores['busca'] == '':
                sg.popup_auto_close('Digite algum e-mail', auto_close_duration=2, no_titlebar=True, button_type=5, background_color='#8c8c8c', text_color='#ededed', font=('Arial Black',12))
                sg.cprint('')
            else:
                try:
                    DataBase.cursor.execute("SELECT full_name FROM users WHERE email LIKE '%{}%'".format(valores['busca']))
                    resultado = DataBase.cursor.fetchall()
                    sg.cprint("Nome: ",resultado[0][0])
                    searchuseremail['full_name'].update(resultado[0][0])
                    DataBase.cursor.execute("SELECT occupation FROM users WHERE email LIKE '%{}%'".format(valores['busca']))
                    resultado = DataBase.cursor.fetchall()
                    searchuseremail['occupation'].update(resultado[0][0])
                    sg.cprint("Função: ",resultado[0][0])
                    DataBase.cursor.execute("SELECT place FROM users WHERE email LIKE '%{}%'".format(valores['busca']))
                    resultado = DataBase.cursor.fetchall()
                    searchuseremail['place'].update(resultado[0][0])
                    sg.cprint("Local: ",resultado[0][0])
                    DataBase.cursor.execute("SELECT email FROM users WHERE email LIKE '%{}%'".format(valores['busca']))
                    resultado = DataBase.cursor.fetchall()
                    searchuseremail['email'].update(resultado[0][0])
                    sg.cprint("E-mail: ",resultado[0][0])
                    DataBase.cursor.execute("SELECT pass_email FROM users WHERE email LIKE '%{}%'".format(valores['busca']))
                    resultado = DataBase.cursor.fetchall()
                    searchuseremail['pass_email'].update(resultado[0][0])
                    sg.cprint("Senha E-mail: ",resultado[0][0])
                    DataBase.cursor.execute("SELECT skype FROM users WHERE email LIKE '%{}%'".format(valores['busca']))
                    resultado = DataBase.cursor.fetchall()
                    searchuseremail['skype'].update(resultado[0][0])
                    sg.cprint("Skype: ",resultado[0][0])
                    DataBase.cursor.execute("SELECT pass_skype FROM users WHERE email LIKE '%{}%'".format(valores['busca']))
                    resultado = DataBase.cursor.fetchall()
                    searchuseremail['pass_skype'].update(resultado[0][0])
                    sg.cprint("Senha Skype: ",resultado[0][0])
                    DataBase.cursor.execute("SELECT google_account FROM users WHERE email LIKE '%{}%'".format(valores['busca']))
                    resultado = DataBase.cursor.fetchall()
                    searchuseremail['google_account'].update(resultado[0][0])
                    sg.cprint("Conta Google: ",resultado[0][0])
                    DataBase.cursor.execute("SELECT sistema_autcom FROM users WHERE email LIKE '%{}%'".format(valores['busca']))
                    resultado = DataBase.cursor.fetchall()
                    resultado = resultado[0][0]
                    if resultado == 0:
                        searchuseremail['autcom'].update("Não")
                        sg.cprint("Autcom: Não")
                    else:
                        searchuseremail['autcom'].update("Sim")
                        sg.cprint("Autcom: Sim")
                    DataBase.cursor.execute("SELECT sistema_sgr FROM users WHERE email LIKE '%{}%'".format(valores['busca']))
                    resultado = DataBase.cursor.fetchall()
                    resultado = resultado[0][0]
                    if resultado == 0:
                        searchuseremail['sgr'].update("Não")
                        sg.cprint("SGR: Não")
                    else:
                        searchuseremail['sgr'].update("Sim")
                        sg.cprint("SGR: Sim")
                    DataBase.cursor.execute("SELECT sistema_express FROM users WHERE email LIKE '%{}%'".format(valores['busca']))
                    resultado = DataBase.cursor.fetchall()
                    resultado = resultado[0][0]
                    if resultado == 0:
                        searchuseremail['express'].update("Não")
                        sg.cprint("Express: Não")
                    else:
                        searchuseremail['express'].update("Sim")
                        sg.cprint("Express: Sim")
                    DataBase.cursor.execute("SELECT login_systems FROM users WHERE email LIKE '%{}%'".format(valores['busca']))
                    resultado = DataBase.cursor.fetchall()
                    searchuseremail['login_systems'].update(resultado[0][0])
                    sg.cprint("Login Sistemas: ",resultado[0][0])
                    DataBase.cursor.execute("SELECT pass_systems FROM users WHERE email LIKE '%{}%'".format(valores['busca']))
                    resultado = DataBase.cursor.fetchall()
                    searchuseremail['pass_systems'].update(resultado[0][0])
                    sg.cprint("Senha Sistemas: ",resultado[0][0])
                    DataBase.cursor.execute("SELECT inactive FROM users WHERE email LIKE '%{}%'".format(valores['busca']))
                    resultado = DataBase.cursor.fetchall()
                    searchuseremail['inactive'].update(resultado[0][0])
                    sg.cprint("Inativo: ",resultado[0][0])
                    searchuseremail['busca'].update('')
                except:
                    sg.popup_auto_close('E-mail não localizado', auto_close_duration=2, no_titlebar=True, button_type=5, background_color='#8c8c8c', text_color='#ededed', font=('Arial Black',12))

    searchuseremail.close()