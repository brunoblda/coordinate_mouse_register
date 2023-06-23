""" Importa o pyautogui"""
import time
import os
import pyautogui

def get_mouse_postition():
    """Returns the mouse position"""

    x_position, y_position = pyautogui.position()
    return x_position,y_position

def write_on_file():
    """Write on the file the mouse position"""
    time.sleep(3)
    coordinates = get_mouse_postition()
    line = 1
    if os.path.exists("coordenadas_mouse.txt"):
        check_file = os.stat("coordenadas_mouse.txt").st_size
        if check_file != 0:
            with open("coordenadas_mouse.txt", encoding="utf-8") as f:
                line = len(f.readlines()) + 1
    with open("coordenadas_mouse.txt", "a", encoding="utf-8") as f:
        f.write(f"{line}. {coordinates}\n")
    response_text = f"Captura de nº {line} salva com sucesso."  
    return response_text
