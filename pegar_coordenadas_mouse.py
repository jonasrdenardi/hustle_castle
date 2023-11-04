import time
import pyautogui
import keyboard

def print_mouse_position():
    x, y = pyautogui.position()
    print("Coordenadas do mouse:", x, y)

print("Pressione a tecla 'P' para imprimir as coordenadas do mouse.")
print("Pressione a tecla 'Esc' para sair do programa.")

while True:
    if keyboard.is_pressed('p'):
        print_mouse_position()
        time.sleep(2)
    
    if keyboard.is_pressed('esc'):
        print("Programa encerrado.")
        break
