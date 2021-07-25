import PySimpleGUI as sg
from Modules import DataBase

def Search():
    sg.theme('Reddit')

    layout = [
        [sg.Text('Busca Nome', size=(14,0)), sg.Input(size=(20,0), key='busca'), sg.Button('Buscar',size=(6,0),bind_return_key=True)],
        [sg.Text('Nome', size=(14,0)), sg.Text(size=(20,0), key='full_name', font=('Helvetica',10,'bold'))],
        [sg.Text('Login', size=(14,0)), sg.Text(size=(20,0), key='username', font=('Helvetica',10,'bold'))],
        [sg.Text('Senha', size=(14,0)), sg.Text(size=(20,0), key='password', font=('Helvetica',10,'bold'))],
        [sg.Multiline(size=(45,4), disabled=True, auto_refresh=True, reroute_stdout=True, reroute_cprint=True, write_only=True, key='-OUT-', autoscroll=True)],
        [sg.Button('Fechar',size=(10,1))]
    ]
    
    searchlogin = sg.Window('S.G.T.I. - Busca Login', layout, icon='Images/icon.ico', finalize=True)

    while True:
        evento, valores = searchlogin.read()
        if evento in (sg.WIN_CLOSED, 'Fechar'):
            break
        if evento == 'Buscar':
            if valores['busca'] == '':
                sg.popup_auto_close('Digite algum nome', auto_close_duration=2, no_titlebar=True, button_type=5, background_color='#8c8c8c', text_color='#ededed', font=('Arial Black',12))
                sg.cprint('')
            else:
                try:
                    DataBase.cursor.execute("SELECT name FROM logins WHERE name LIKE '%{}%'".format(valores['busca']))
                    first_name = DataBase.cursor.fetchall()
                    DataBase.cursor.execute("SELECT last_name FROM logins WHERE name LIKE '%{}%'".format(first_name[0][0]))
                    last_name = DataBase.cursor.fetchall()
                    resultado = first_name[0][0]+" "+ last_name[0][0]
                    sg.cprint("Nome: ",resultado)
                    searchlogin['full_name'].update(resultado)
                    DataBase.cursor.execute("SELECT username FROM logins WHERE name LIKE '%{}%'".format(first_name[0][0]))
                    resultado = DataBase.cursor.fetchall()
                    sg.cprint("Login: ",resultado[0][0])
                    searchlogin['username'].update(resultado[0][0])
                    DataBase.cursor.execute("SELECT password FROM logins WHERE name LIKE '%{}%'".format(first_name[0][0]))
                    resultado = DataBase.cursor.fetchall()
                    sg.cprint("Senha: ",resultado[0][0])
                    searchlogin['password'].update(resultado[0][0])
                except:
                    sg.popup_auto_close('Nome não localizado', auto_close_duration=2, no_titlebar=True, button_type=5, background_color='#8c8c8c', text_color='#ededed', font=('Arial Black',12))
    
    searchlogin.close()