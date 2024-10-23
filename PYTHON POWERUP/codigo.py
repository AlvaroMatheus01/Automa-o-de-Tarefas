#Passo 1 : Entrar no site da empresa
# Link: https://dlp.hashtagtreinamentos.com.python/intensivao/login
#Passo 2 : Fazer o login
#Passo 3 : Pegar/importar a base de dados
#Passo 4 : Cadastrar o produto
#Passo 5 : repetir o passo 4 até cadastrar todos os produtos

from os import write
import pyautogui
import time


#### LEMBRETES ####
#pyautogui.click - clicar com o mouse
#pyautogui.write - escrever um texto
#pyautogui.press - apertar a tecla
#pyautogui.hotkey - combinação de teclas (Ctrl C)
#pyautogui.scroll - rolar a tela para cima ou para baixo
#### LEMBRETES ####

pyautogui.PAUSE = 0.5
# - Entrar no sistema
# - Abrir o navegador
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# - entrar no link https://dlp.hashtagtreinamentos.com.python/intensivao/login

pyautogui.write("dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(1)

# - Fazer o Login no Sistema
pyautogui.click(x=893, y=379)
pyautogui.write("matheuscristoaguiar@hotmail.com")
pyautogui.click(x=877, y=469)
pyautogui.write("123456")
pyautogui.press("enter")



#Importar Base de Dados
import pandas

tabela = pandas.read_csv("produtos.csv")

print(tabela)

# 4- Cadastrar os Produtos
#para cada linha da tabela:

for linha in tabela.index:
    #- Código;
    pyautogui.click(x = 876, y = 256)
    codigo = str(tabela.loc[linha,"codigo"]) #String=texto
    pyautogui.write(codigo)
    
    # Marca;
    pyautogui.press("tab")
    marca = str(tabela.loc[linha,"marca"])
    pyautogui.write(marca)
    
    # Tipo;
    pyautogui.press("tab")
    tipo = str(tabela.loc[linha,"tipo"])
    pyautogui.write(tipo)
    
    # Categoria;
    pyautogui.press("tab")
    categoria = str(tabela.loc[linha,"categoria"])
    pyautogui.write(categoria)
    
    # Preço;
    pyautogui.press("tab")
    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)
    
    # Custo;
    pyautogui.press("tab")
    custo = str (tabela.loc[linha, "custo"])
    pyautogui.write(custo)
    
    # Observação
    pyautogui.press("tab")
    obs = str(tabela.loc[linha,"obs"])
    if obs!= "nan":
        pyautogui.write(obs)

    # Clicar no botao de enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

    # Voltar para o inicio da Pagina para cadastrar novamente
    pyautogui.scroll(-2000)
    time.sleep(1)
    pyautogui.scroll(5000)

    # Repetir para todas os produtos - para todas as linhas da tabela