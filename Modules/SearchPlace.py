import PySimpleGUI as sg
from Modules import DataBase

def Search():
    sg.theme('Reddit')

    layout = [
        [sg.Text('Busca Local', size=(12,0)), sg.Input(size=(20,0), key='busca'), sg.Button('Buscar',size=(6,0),bind_return_key=True)],
        [sg.Text('Local', size=(12,0)), sg.Text(size=(20,0), key='place', font=('Helvetica',10,'bold'))],
        [sg.Button('Fechar',size=(10,1))]
    ]
    
    searchplace = sg.Window('S.G.T.I. - Busca Local', layout, icon='Images/icon.ico', finalize=True)

    while True:
        evento, valores = searchplace.read()
        if evento in (sg.WIN_CLOSED, 'Fechar'):
            break
        if evento == 'Buscar':
            if valores['busca'] == '':
                sg.popup_auto_close('Digite algum local', auto_close_duration=2, no_titlebar=True, button_type=5, background_color='#8c8c8c', text_color='#ededed', font=('Arial Black',12))
                sg.cprint('')
            else:
                try:
                    DataBase.cursor.execute("SELECT place FROM places WHERE place LIKE '%{}%'".format(valores['busca']))
                    resultado = DataBase.cursor.fetchall()
                    sg.cprint("Local: ",resultado[0][0])
                    searchplace['place'].update(resultado[0][0])
                except:
                    sg.popup_auto_close('Local não localizado', auto_close_duration=2, no_titlebar=True, button_type=5, background_color='#8c8c8c', text_color='#ededed', font=('Arial Black',12))
    
    searchplace.close()