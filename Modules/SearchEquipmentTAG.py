import PySimpleGUI as sg
from Modules import DataBase

def Search():
    sg.theme('Reddit')

    column1 = [
        [sg.Text('Busca TAG', size=(14,0)),sg.Input(size=(30,0),key='busca'),sg.Button('Buscar',size=(6,0),bind_return_key=True)],
        [sg.Text('Usuário', size=(14,0)),sg.Text(size=(40,0),key='user', font=('Helvetica',10,'bold'))],
        [sg.Text('Local', size=(14,0)),sg.Text(size=(12,0),key='place', font=('Helvetica',10,'bold'))],
        [sg.Text('Departamento', size=(14,0)),sg.Text(size=(12,0),key='department', font=('Helvetica',10,'bold'))],
        [sg.Text('Office', size=(14,0)),sg.Text(size=(30,0),key='office_license', font=('Helvetica',10,'bold'))],
        [sg.Text('Office Tipo', size=(14,0)),sg.Text(size=(12,0),key='office_type', font=('Helvetica',10,'bold'))],
        [sg.Text('Office Chave', size=(14,0)),sg.Text(size=(40,0),key='office_key', font=('Helvetica',10,'bold'))],
        [sg.Text('Windows', size=(14,0)),sg.Text(size=(30,0),key='windows_license', font=('Helvetica',10,'bold'))],
        [sg.Text('Windows Tipo', size=(14,0)),sg.Text(size=(12,0),key='windows_type', font=('Helvetica',10,'bold'))],
        [sg.Text('Windows Chave', size=(14,0)),sg.Text(size=(40,0),key='windows_key', font=('Helvetica',10,'bold'))],
        [sg.Text('Equipamento:',size=(14,0)),sg.Text(size=(8,0),key='equipment', font=('Helvetica',10,'bold'))],
        [sg.Text('Marca:',size=(14,0)),sg.Text(size=(12,0),key='manufacturer', font=('Helvetica',10,'bold'))],
        [sg.Text('TAG:',size=(14,0)),sg.Text(size=(10,0),key='id_equipment', font=('Helvetica',10,'bold'))],
        [sg.Text('Fornecedor', size=(14,0)),sg.Text(size=(20,0),key='provider', font=('Helvetica',10,'bold'))],
        [sg.Text('Nota Fiscal', size=(14,0)),sg.Text(size=(12,0),key='invoice', font=('Helvetica',10,'bold'))],
        [sg.Text('Chave Acesso', size=(14,0)),sg.Text(size=(40,0),key='access_key', font=('Helvetica',10,'bold'))],
        [sg.Button('Fechar',size=(6,0))]
    ]

    column2 = [
        [sg.Multiline(size=(60,16), disabled=True, auto_refresh=True, reroute_stdout=True, reroute_cprint=True, write_only=True, key='-OUT-', autoscroll=True)]
    ]
    
    layout = [
        [sg.Column(column1), sg.Column(column2)]
    ]

    searchequipmentuser = sg.Window('S.G.T.I. - Busca Equipamento Por TAG', layout, icon='Images/icon.ico', finalize=True)

    while True:
        evento, valores = searchequipmentuser.read()
        if evento in (sg.WIN_CLOSED, 'Fechar'):
            break
        if evento == 'Buscar':
            if valores['busca'] == '':
                sg.popup_auto_close('Digite alguma TAG', auto_close_duration=2, no_titlebar=True, button_type=5, background_color='#8c8c8c', text_color='#ededed', font=('Arial Black',12))
                sg.cprint('')
            else:
                try:
                    DataBase.cursor.execute("SELECT user FROM equipments WHERE id_equipment LIKE '%{}%'".format(valores['busca']))
                    resultado = DataBase.cursor.fetchall()
                    sg.cprint("Usuário: ",resultado[0][0])
                    searchequipmentuser['user'].update(resultado[0][0])
                    DataBase.cursor.execute("SELECT place FROM equipments WHERE id_equipment LIKE '%{}%'".format(valores['busca']))
                    resultado = DataBase.cursor.fetchall()
                    searchequipmentuser['place'].update(resultado[0][0])
                    sg.cprint("Local: ",resultado[0][0])
                    DataBase.cursor.execute("SELECT department FROM equipments WHERE id_equipment LIKE '%{}%'".format(valores['busca']))
                    resultado = DataBase.cursor.fetchall()
                    searchequipmentuser['department'].update(resultado[0][0])
                    sg.cprint("Departamento: ",resultado[0][0])
                    DataBase.cursor.execute("SELECT office_license FROM equipments WHERE id_equipment LIKE '%{}%'".format(valores['busca']))
                    resultado = DataBase.cursor.fetchall()
                    searchequipmentuser['office_license'].update(resultado[0][0])
                    sg.cprint("Office: ",resultado[0][0])
                    DataBase.cursor.execute("SELECT office_type FROM equipments WHERE id_equipment LIKE '%{}%'".format(valores['busca']))
                    resultado = DataBase.cursor.fetchall()
                    searchequipmentuser['office_type'].update(resultado[0][0])
                    sg.cprint("Office Tipo: ",resultado[0][0])
                    DataBase.cursor.execute("SELECT office_key FROM equipments WHERE id_equipment LIKE '%{}%'".format(valores['busca']))
                    resultado = DataBase.cursor.fetchall()
                    searchequipmentuser['office_key'].update(resultado[0][0])
                    sg.cprint("Office Chave: ",resultado[0][0])
                    DataBase.cursor.execute("SELECT windows_license FROM equipments WHERE id_equipment LIKE '%{}%'".format(valores['busca']))
                    resultado = DataBase.cursor.fetchall()
                    searchequipmentuser['windows_license'].update(resultado[0][0])
                    sg.cprint("Windows: ",resultado[0][0])
                    DataBase.cursor.execute("SELECT windows_type FROM equipments WHERE id_equipment LIKE '%{}%'".format(valores['busca']))
                    resultado = DataBase.cursor.fetchall()
                    searchequipmentuser['windows_type'].update(resultado[0][0])
                    sg.cprint("Windows Tipo: ",resultado[0][0])
                    DataBase.cursor.execute("SELECT windows_key FROM equipments WHERE id_equipment LIKE '%{}%'".format(valores['busca']))
                    resultado = DataBase.cursor.fetchall()
                    searchequipmentuser['windows_key'].update(resultado[0][0])
                    sg.cprint("Windows Chave: ",resultado[0][0])
                    DataBase.cursor.execute("SELECT equipment FROM equipments WHERE id_equipment LIKE '%{}%'".format(valores['busca']))
                    resultado = DataBase.cursor.fetchall()
                    searchequipmentuser['equipment'].update(resultado[0][0])
                    sg.cprint("Equipamento: ",resultado[0][0])
                    DataBase.cursor.execute("SELECT manufacturer FROM equipments WHERE id_equipment LIKE '%{}%'".format(valores['busca']))
                    resultado = DataBase.cursor.fetchall()
                    searchequipmentuser['manufacturer'].update(resultado[0][0])
                    sg.cprint("Marca: ",resultado[0][0])
                    DataBase.cursor.execute("SELECT id_equipment FROM equipments WHERE id_equipment LIKE '%{}%'".format(valores['busca']))
                    resultado = DataBase.cursor.fetchall()
                    searchequipmentuser['id_equipment'].update(resultado[0][0])
                    sg.cprint("TAG: ",resultado[0][0])
                    DataBase.cursor.execute("SELECT provider FROM equipments WHERE id_equipment LIKE '%{}%'".format(valores['busca']))
                    resultado = DataBase.cursor.fetchall()
                    searchequipmentuser['provider'].update(resultado[0][0])
                    sg.cprint("Fornecedor: ",resultado[0][0])
                    DataBase.cursor.execute("SELECT invoice FROM equipments WHERE id_equipment LIKE '%{}%'".format(valores['busca']))
                    resultado = DataBase.cursor.fetchall()
                    searchequipmentuser['invoice'].update(resultado[0][0])
                    sg.cprint("Nota Fiscal: ",resultado[0][0])
                    DataBase.cursor.execute("SELECT access_key FROM equipments WHERE id_equipment LIKE '%{}%'".format(valores['busca']))
                    resultado = DataBase.cursor.fetchall()
                    searchequipmentuser['access_key'].update(resultado[0][0])
                    sg.cprint("Chave Acesso: ",resultado[0][0])
                    searchequipmentuser['busca'].update('')
                except:
                    sg.popup_auto_close('TAG não localizada', auto_close_duration=2, no_titlebar=True, button_type=5, background_color='#8c8c8c', text_color='#ededed', font=('Arial Black',12))

    searchequipmentuser.close()