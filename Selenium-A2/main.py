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
minha_busca = "Biblioteca selenium"

# -- INICIO

# abre a página do google
navegador.get(pagina)
time.sleep(3)

#pega o elemento do campo input do google
input_txt = navegador.find_element(By.XPATH, "/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")

# digita no input o texto
input_txt.send_keys(minha_busca)
time.sleep(1)
# envia um ENTER
input_txt.send_keys(Keys.ENTER)
time.sleep(2)