import PySimpleGUI as sg
import tkinter as tk
sg.theme('DarkAmber')

layout = [[sg.Text('hi')],
[[sg.Text('Another row')], sg.InputText()],
[sg.Button('ok'), sg.Button('cancel')] ]

window = sg.Window('hi', layout)
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED or event == 'cancel':
        break
    print('You entered', layout)

