"""Graphical User Interface module"""
import textwrap
import PySimpleGUI as sg

def make_window(theme=None):
    """Create the Graphical User Interface"""

    sg.theme(theme)

    text_1 = "Salva coordenadas capturadas no arquivo coordenadas_mouse.txt"
    text_2 = ("Ao clickar em capturar, o sistema irá registrar a posição que " 
            "o mouse estará ao se passar 3 segundos.")

    layout_l = [
                [sg.Button('Capturar', font='_14', pad=(150,10))],
                [sg.T('', key="texto_salvamento", font=("", 16), justification='c', pad=(0,5))]
            ]
    # Note - LOCAL Menu element is used (see about for how that's defined)
    layout = [
                [sg.T(textwrap.fill(text_1, 40)
                    ,pad=(0,5), font='_ 16', justification='c', expand_x=False)],
                [sg.T(textwrap.fill(text_2, 40)
                    ,pad=(0,5) , font='_ 16', justification='c', expand_x=False)],
                [sg.Col(layout_l, p=0)]
            ]

    window = sg.Window('Salvar Coordenadas do Mouse', layout, finalize=True,
                       right_click_menu=sg.MENU_RIGHT_CLICK_EDITME_VER_EXIT, keep_on_top=True
                       , element_justification='c', size=(500,250))

    return window
