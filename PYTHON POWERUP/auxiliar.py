import pyautogui
import time


#código vai esperar 5 segundos para capturar a posição correta do mouse.
time.sleep(5)
#mostrar a posição do mouse na tela
print(pyautogui.position())


# Voltar para o inicio da Pagina para cadastrar novamente
pyautogui.scroll(-1000)