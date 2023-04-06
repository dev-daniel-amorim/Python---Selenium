'''
Instale as bibliotecas pelo terminal
pip install selenium
pip install webdriver-manager
'''

# Iniciando o chrome driver, selenium, e webdriver
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
servico = Service(ChromeDriverManager().install())

# Biblioteca que pega os elementos da página
from selenium.webdriver.common.by import By
# Biblioteca que envia comandos pras páginas
from selenium.webdriver.common.keys import Keys
# Biblioteca que realiza delays (tempo de atraso entre os comandos)
import time

# configurando o navegador com as opções maximizado e modo anonimo
opcoes = webdriver.ChromeOptions()
opcoes.add_argument("--start-maximized")
opcoes.add_argument("--incognito")
opcoes.add_argument("--enable-popup-blocking")
# opcao de nao fechar o navegador ao fim do código
opcoes.add_experimental_option("detach", True)

# iniciando o servico e passando as opções pro navegador
navegador = webdriver.Chrome(service=servico, options=opcoes)

# -- MINHAS VARIAVEIS
pagina = "https://www.google.com/"
minha_busca = "tv samsung"

atalho = "https://www.google.com/search?q=tv+samsung&source=lnms&tbm=shop&sa=X&ved=2ahUKEwjQkoOPlpT-AhX6q5UCHbr9BUIQ_AUoAXoECAEQAw&biw=1536&bih=700&dpr=1.25"

# -- INICIO

# abre a página do google
navegador.get(atalho)
time.sleep(5)

# #pega o elemento do campo input do google
# input_txt = navegador.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
# time.sleep(1)
# # digita no input o texto
# input_txt.send_keys(minha_busca)
# time.sleep(1)
# # envia um ENTER
# input_txt.send_keys(Keys.ENTER)
# time.sleep(2)
#
# aba_shopping = navegador.find_element(By.CSS_SELECTOR, '[data-hveid="CAEQAw"]')
# aba_shopping.click()

# pega cada painel da busca
paineis = navegador.find_elements(By.CLASS_NAME, "sh-dgr__gr-auto")

import pandas as pd
# para salvar excel em xlsx talvez seja necessario instalar o módulo: pip install openpyxl

def salvar_csv(lista_itens):

    produtos = pd.DataFrame(lista_itens, columns=["Produto", "Preços", "Link"])
    produtos.to_excel("lista de preços.xlsx", index=False)
    return


lista_itens = []

for item in paineis:

    preco = item.find_element(By.CLASS_NAME, "a8Pemb").text
    print(preco)

    nome_produto = item.find_element(By.CLASS_NAME, 'tAxDx').text
    print(nome_produto)

    # pegando um elemento pai atraves do filho
    elem_filho = item.find_element(By.CLASS_NAME, "aULzUe")
    elem_pai = elem_filho.find_element(By.XPATH, "..")
    link_produto = elem_pai.get_attribute('href')
    print(link_produto)

    lista_itens.append((nome_produto, preco, link_produto))
    salvar_csv(lista_itens)



