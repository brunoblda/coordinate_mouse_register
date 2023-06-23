"""Importando modulos"""
import PySimpleGUI as sg
import logical_layer.return_position as rp
import gui_layer.gui as gui

if __name__ == "__main__":
    window_show = gui.make_window()
    while True:
        event, values = window_show.read()
        if event in (sg.WIN_CLOSED, 'Exit'):
            break
        if event == "Capturar":
            save_file = rp.write_on_file()
            window_show["texto_salvamento"].update(save_file)
    window_show.close()
    