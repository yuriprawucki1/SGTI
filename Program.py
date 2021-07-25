import PySimpleGUI as sg
import os
from Modules import *

def Login():
    sg.theme('Reddit')
    column1 = [
        [sg.Image(filename='Images/login.png')]
    ]
    column2 = [
        [sg.Text('Usuário', font=('Helvetica',10,'bold'),size=(10,0)),sg.InputCombo(DropdownLogin(),key='user_login',size=(18,0), readonly=True)],
        [sg.Text('Senha', font=('Helvetica',10,'bold'),size=(10,0)),sg.Input(size=(20,0),key='pass_login', password_char='*')],
        [sg.Button('Entrar', font=('Helvetica',10,'bold'),size=(8,0),bind_return_key=True),sg.Text('  '),sg.Text(key='text_login', font=('Helvetica',10,'bold'), text_color='#b31212', size=(18,0))]
    ]
    layout = [
        [sg.Column(column1), sg.Column(column2)]
    ]
    loginscreen = sg.Window("S.G.T.I. - Login", layout, icon='Images/icon.ico', return_keyboard_events=True, disable_minimize=True)
    
    while True:
        eventos, valores = loginscreen.read()
        if eventos == sg.WINDOW_CLOSED:
            break
        if eventos == 'Entrar':
            DataBase.cursor.execute("SELECT username FROM logins WHERE username ='{}'".format(valores['user_login']))
            user_login_db = DataBase.cursor.fetchall()
            DataBase.cursor.execute("SELECT password FROM logins WHERE username ='{}'".format(valores['user_login']))
            pass_login_db = DataBase.cursor.fetchall()
            if valores['user_login'] == user_login_db[0][0] and valores['pass_login'] == pass_login_db[0][0]:
                loginscreen.close()
                HomeScreen()
            else:
                loginscreen['text_login'].update('Dados incorretos !')
    loginscreen.close()

def DropdownLogin():
    DataBase.cursor.execute("SELECT username FROM logins")
    lista = DataBase.cursor.fetchall()
    lista = [i for sub in lista for i in sub]
    return sorted(lista)

def HomeScreen():
    sg.theme('Reddit')

    menu_def = [['&Geral', ['Cadastrar Usuário', 'Buscar Usuário','Cadastrar Local', 'Buscar Local']],
            ['&Usuários', ['Cadastrar Logins', 'Busca por Nome', 'Busca por E-mail', 'Busca por Skype']],
            ['&Equipamentos', ['Cadastrar Equipamentos', 'Busca por Usuário', 'Busca por TAG'], ['Busca por ID']],
            ['&Ajuda', 'Sobre']]

    layout = [
        [sg.Menu(menu_def)],
        [sg.Image(filename='Images/background.png')]
    ]
    homescreen = sg.Window("S.G.T.I. - Sistema de Gestão da Tecnologia da Informação", layout, size=(800,500), resizable=True, element_justification='c', icon='Images/icon.ico', finalize=True)
    homescreen.TKroot.focus_force()    

    while True:
        evento, valores = homescreen.read()
        if evento == sg.WIN_CLOSED:
            break
        elif evento == 'Cadastrar Usuário':
            RegisterLogin.Register()
        elif evento == 'Buscar Usuário':
            SearchLogin.Search()
        elif evento == 'Cadastrar Local':
            RegisterPlace.Register()
        elif evento == 'Buscar Local':
            SearchPlace.Search()
        elif evento == 'Cadastrar Logins':
            RegisterUsers.Register()
        elif evento == 'Busca por Nome':
            SearchUserName.Search()
        elif evento == 'Busca por E-mail':
            SearchUserEmail.Search()
        elif evento == 'Busca por Skype':
            SearchUserSkype.Search()
        elif evento == 'Cadastrar Equipamentos':
            RegisterEquipments.Register()
        elif evento == 'Busca por Usuário':
            SearchEquipmentUser.Search()
        elif evento == 'Busca por TAG':
            SearchEquipmentTAG.Search()
        elif evento == 'Sobre':
            About.About()
            homescreen.reappear()
        
    homescreen.close()

if __name__ == '__main__':
    Login()