from PySimpleGUI import PySimpleGUI as sg
import requests

def app():
    layout = [
        [sg.Text('Digite o cep: '), sg.Input(key='cep')],
        [sg.Button('verificar')],
        [sg.Text('', key='resposta')],
        [sg.Text('', key='dados')]
    ]

    window = sg.Window('Busca CEP', layout=layout)
    while True:
        evento, valores = window.read()
        if evento == sg.WIN_CLOSED:
            break

        elif evento == "verificar":
            cep = valores['cep']
            if cep > "8":
                window["resposta"].update("Isso não é um cep!")
                exit()
            elif cep <= "8":
                req = requests.get(f"https://viacep.com.br/ws/{cep}/json/")
                dd = req.json()
                window['resposta'].update('Cep encontrado.')
                window['dados'].update(f'cep: {dd["cep"]}\nlogradouro: {dd["cep"]}\ncomplemento: {dd["complemento"]}\nbairro: {dd["bairro"]}\nlocalidade: {dd["localidade"]}\nuf: {dd["uf"]}\nddd: {dd["ddd"]}')
app()