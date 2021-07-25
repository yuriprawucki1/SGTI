import PySimpleGUI as sg
from Modules import DataBase

def Register():
    sg.theme('Reddit')

    layout = [
        [sg.Text('Local', size=(18,0)),sg.InputCombo(DropdownPlace(), readonly=True,default_value='',size=(38,0),key='place')],
        [sg.Text('Departamento', size=(18,0)),sg.Input(size=(40,0),key='department')],
        [sg.Text('Usuário', size=(18,0)),sg.Input(size=(40,0),key='user')],
        [sg.Text('Office - Licença', size=(18,0)),sg.Input(size=(40,0),key='office_license')],
        [sg.Text('Office - Tipo', size=(18,0)),sg.InputCombo(['ESD','FPP','OEM','OPEN','-'], readonly=True,default_value='',size=(38,0),key='office_type')],
        [sg.Text('Office - Chave', size=(18,0)),sg.Input(size=(40,0),key='office_key')],
        [sg.Text('Windows - Licença', size=(18,0)),sg.Input(size=(40,0),key='windows_license')],
        [sg.Text('Windows - Tipo', size=(18,0)),sg.InputCombo(['ESD','FPP','OEM','OPEN','-'], readonly=True,default_value='',size=(38,0),key='windows_type')],
        [sg.Text('Windows - Chave', size=(18,0)),sg.Input(size=(40,0),key='windows_key')],
        [sg.Text('Equipamento', size=(18,0)),sg.InputCombo(['Desktop','Notebook'], readonly=True,default_value='',size=(38,0),key='equipment')],
        [sg.Text('Marca', size=(18,0)),sg.InputCombo(['Acer','Apple','Asus','Dell','HP','Lenovo','LG','Samsung','Outros'], readonly=True,default_value='',size=(38,0),key='manufacturer')],
        [sg.Text('ID', size=(18,0)),sg.Input(size=(40,0),key='id_equipment')],
        [sg.Text('Nota Fiscal', size=(18,0)),sg.Input(size=(40,0),key='invoice')],
        [sg.Text('Chave de Acesso', size=(18,0)),sg.Input(size=(40,0),key='access_key')],
        [sg.Text('Empresa', size=(18,0)),sg.Input(size=(40,0),key='provider')],
        [sg.Button('Cadastrar',size=(10,1)),sg.Button('Cancelar',size=(10,1))]
    ]
    registerequipments = sg.Window("S.G.T.I. - Cadastrar Equipamentos", layout, resizable=False, icon='Images/icon.ico', finalize=True)

    while True:
        evento, valores = registerequipments.read()
        if evento in (sg.WIN_CLOSED, 'Cancelar'):
            break
        if evento == 'Cadastrar':
            if valores['place'] == '' and valores['equipment'] == '' and valores['id_equipment'] == '':
                sg.popup_auto_close('Cadastro não efetuado','Preencha o Local, o Equipamento e o ID',auto_close_duration=4, no_titlebar=True, button_type=5, background_color='#8c8c8c', text_color='#ededed', font=('Arial Black',10))
            else:            
                sql = "INSERT INTO equipments (place, department, user, office_license, office_type, office_key, windows_license, windows_type, windows_key, equipment, manufacturer, id_equipment, invoice, access_key, provider) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
                val = valores['place'], valores['department'], valores['user'], valores['office_license'], valores['office_type'], valores['office_key'], valores['windows_license'], valores['windows_type'], valores['windows_key'], valores['equipment'], valores['manufacturer'], valores['id_equipment'], valores['invoice'], valores['access_key'], valores['provider']
                DataBase.cursor.execute(sql, val)
                DataBase.con.commit()
                sg.popup_auto_close('Cadastro efetuado', auto_close_duration=2, no_titlebar=True, button_type=5, background_color='#8c8c8c', text_color='#ededed', font=('Arial Black',12))
    
    registerequipments.close()

def DropdownPlace():
    DataBase.cursor.execute("SELECT place FROM places")
    lista = DataBase.cursor.fetchall()
    lista = [i for sub in lista for i in sub]
    return sorted(lista)