from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome('./chromedriver')(C:\Users\Raísa\Downloads\testagem)

# Casos de teste 041 - 050
# Autor: Raísa Nunes Eça de Queiros

def CT_041():
    # Passo 1 - Acesso a URL
    driver.get("https://www.spotify.com/br/account/notifications/")
    driver.implicitly_wait(10)
    # Passo 2 - Solicitar a alteração das configurações de notificações
    elem = driver.find_element_by_xpath(
        "/html/body/div[4]/div/div[2]/div[1]/header/div[3]/div/div/form/input")
    def login():
    driver.get(
        "https://accounts.spotify.com/pt-BR/login?continue=https:%2F%2Fopen.spotify.com%2F")
    driver.implicitly_wait(10)
   
login()
    
    # Passo 3 - Inserir uma música valida
    # elem.send_keys("playlist")
    # Selecionar uma playist a partir dos resultados encontrados
    # elem_playlist = driver.find_element_by_xpath(
    # "//*[@id='searchPage']/div/div/section[1]/div[2]/div/div/div/div[4]")
    # elem_playlist.click()

    # Verificar resultados
    assert "Spotify – Buscar" in driver.title
    driver.close()

def CT_042():
    # Passo 1 - Acesso a URL
    driver.get("https://www.spotify.com/br/account/privacy/")
    driver.implicitly_wait(10)
    # Passo 2 - Solicitar a alteração das configurações de Privacidade
    elem = driver.find_element_by_xpath(
        "/html/body/div[4]/div/div[2]/div[1]/header/div[3]/div/div/form/input")
    def login():
    driver.get(
        "https://accounts.spotify.com/pt-BR/login?continue=https:%2F%2Fopen.spotify.com%2F")
    driver.implicitly_wait(10)

    login()
    
    # Passo 3 - Inserir uma música valida
    # elem.send_keys("playlist")
    # Selecionar uma playist a partir dos resultados encontrados
    # elem_playlist = driver.find_element_by_xpath(
    # "//*[@id='searchPage']/div/div/section[1]/div[2]/div/div/div/div[4]")
    # elem_playlist.click()

    # Verificar resultados
    assert "Spotify – Buscar" in driver.title
    driver.close()

def CT_043():
    # Passo 1 - Acesso a URL
    driver.get("https://www.spotify.com/br/account/subscription/receipt/")
    driver.implicitly_wait(10)
    # Passo 2 - Visualizar preços de pacotes Premium
    elem = driver.find_element_by_xpath(
        "/html/body/div[4]/div/div[2]/div[1]/header/div[3]/div/div/form/input")
    def login():
    driver.get(
        "https://accounts.spotify.com/pt-BR/login?continue=https:%2F%2Fopen.spotify.com%2F")
    driver.implicitly_wait(10)
   
login()
    
    # Passo 3 - Inserir uma música valida
    # elem.send_keys("playlist")
    # Selecionar uma playist a partir dos resultados encontrados
    # elem_playlist = driver.find_element_by_xpath(
    # "//*[@id='searchPage']/div/div/section[1]/div[2]/div/div/div/div[4]")
    # elem_playlist.click()

    # Verificar resultados
    assert "Spotify – Buscar" in driver.title
    driver.close()

    def CT_044():
    # Passo 1 - Acesso a URL
    driver.get("https://www.spotify.com/br/account/recover-playlists/")
    driver.implicitly_wait(10)
    # Passo 2 - Verificar se é possível e quais Playlists são permitidas a recuperação
    elem = driver.find_element_by_xpath(
        "/html/body/div[4]/div/div[2]/div[1]/header/div[3]/div/div/form/input")
    def login():
    driver.get(
        "https://accounts.spotify.com/pt-BR/login?continue=https:%2F%2Fopen.spotify.com%2F")
    driver.implicitly_wait(10)
   
login()
    
    # Passo 3 - Inserir uma música valida
    # elem.send_keys("playlist")
    # Selecionar uma playist a partir dos resultados encontrados
    # elem_playlist = driver.find_element_by_xpath(
    # "//*[@id='searchPage']/div/div/section[1]/div[2]/div/div/div/div[4]")
    # elem_playlist.click()

    # Verificar resultados
    assert "Spotify – Buscar" in driver.title
    driver.close()

     def CT_045():
    # Passo 1 - Acesso a URL
    driver.get("https://www.spotify.com/br/account/change-password/")
    driver.implicitly_wait(10)
    # Passo 2 - Verificar se a mudança de senha vai para e-mail ou aplicativo
    elem = driver.find_element_by_xpath(
        "/html/body/div[4]/div/div[2]/div[1]/header/div[3]/div/div/form/input")
    def login():
    driver.get(
        "https://accounts.spotify.com/pt-BR/login?continue=https:%2F%2Fopen.spotify.com%2F")
    driver.implicitly_wait(10)
   
login()
    
    # Passo 3 - Inserir uma música valida
    # elem.send_keys("playlist")
    # Selecionar uma playist a partir dos resultados encontrados
    # elem_playlist = driver.find_element_by_xpath(
    # "//*[@id='searchPage']/div/div/section[1]/div[2]/div/div/div/div[4]")
    # elem_playlist.click()

    # Verificar resultados
    assert "Spotify – Buscar" in driver.title
    driver.close()

    def CT_046():
    # Passo 1 - Acesso a URL
    driver.get("https://www.spotify.com/br/redeem/")
    driver.implicitly_wait(10)
    # Passo 2 - Inserir o PIN que está no verso do seu cartão presente ou o código Premium do seu recibo de compra.
    elem = driver.find_element_by_xpath(
        "/html/body/div[4]/div/div[2]/div[1]/header/div[3]/div/div/form/input")
    def login():
    driver.get(
        "https://accounts.spotify.com/pt-BR/login?continue=https:%2F%2Fopen.spotify.com%2F")
    driver.implicitly_wait(10)
   
login()
    
    # Passo 3 - Inserir uma música valida
    # elem.send_keys("playlist")
    # Selecionar uma playist a partir dos resultados encontrados
    # elem_playlist = driver.find_element_by_xpath(
    # "//*[@id='searchPage']/div/div/section[1]/div[2]/div/div/div/div[4]")
    # elem_playlist.click()

    # Verificar resultados
    assert "Spotify – Buscar" in driver.title
    driver.close()

      def CT_047():
    # Passo 1 - Acesso a URL
    driver.get("https://www.spotify.com/br/account/apps/")
    driver.implicitly_wait(10)
    # Passo 2 - Inserir o PIN que está no verso do seu cartão presente ou o código Premium do seu recibo de compra.
    elem = driver.find_element_by_xpath(
        "/html/body/div[4]/div/div[2]/div[1]/header/div[3]/div/div/form/input")
    def login():
    driver.get(
        "https://accounts.spotify.com/pt-BR/login?continue=https:%2F%2Fopen.spotify.com%2F")
    driver.implicitly_wait(10)
   
login()
    
    # Passo 3 - Inserir uma música valida
    # elem.send_keys("playlist")
    # Selecionar uma playist a partir dos resultados encontrados
    # elem_playlist = driver.find_element_by_xpath(
    # "//*[@id='searchPage']/div/div/section[1]/div[2]/div/div/div/div[4]")
    # elem_playlist.click()

    # Verificar resultados
    assert "Spotify – Buscar" in driver.title
    driver.close()

      def CT_048():
    # Passo 1 - Acesso a URL
    driver.get("https://www.spotify.com/br/account/notifications/")
    driver.implicitly_wait(10)
    # Passo 2 - Verificar se atualizações do Spotify são automáticas, e por onde elas serão enviadas, se por e-mail ou por outro meio
    elem = driver.find_element_by_xpath(
        "/html/body/div[4]/div/div[2]/div[1]/header/div[3]/div/div/form/input")
    def login():
    driver.get(
        "https://accounts.spotify.com/pt-BR/login?continue=https:%2F%2Fopen.spotify.com%2F")
    driver.implicitly_wait(10)
   
login()
    
    # Passo 3 - Inserir uma música valida
    # elem.send_keys("playlist")
    # Selecionar uma playist a partir dos resultados encontrados
    # elem_playlist = driver.find_element_by_xpath(
    # "//*[@id='searchPage']/div/div/section[1]/div[2]/div/div/div/div[4]")
    # elem_playlist.click()

    # Verificar resultados
    assert "Spotify – Buscar" in driver.title
    driver.close()

    def CT_049():
    # Passo 1 - Acesso a URL
    driver.get("https://www.spotify.com/br/account/notifications/")
    driver.implicitly_wait(10)
    # Passo 2 - Verificar se notícias e ofertas do Spotify são obrigatórias ou o usuário pode optar por não recebê-las
    elem = driver.find_element_by_xpath(
        "/html/body/div[4]/div/div[2]/div[1]/header/div[3]/div/div/form/input")
    def login():
    driver.get(
        "https://accounts.spotify.com/pt-BR/login?continue=https:%2F%2Fopen.spotify.com%2F")
    driver.implicitly_wait(10)
   
login()
    
    # Passo 3 - Inserir uma música valida
    # elem.send_keys("playlist")
    # Selecionar uma playist a partir dos resultados encontrados
    # elem_playlist = driver.find_element_by_xpath(
    # "//*[@id='searchPage']/div/div/section[1]/div[2]/div/div/div/div[4]")
    # elem_playlist.click()

    # Verificar resultados
    assert "Spotify – Buscar" in driver.title
    driver.close()

     def CT_050():
    # Passo 1 - Acesso a URL
    driver.get("https://www.spotify.com/br/account/privacy/")
    driver.implicitly_wait(10)
    # Passo 2 - Testagem de processo de coleta de dados
    elem = driver.find_element_by_xpath(
        "/html/body/div[4]/div/div[2]/div[1]/header/div[3]/div/div/form/input")
    def login():
    driver.get(
        "https://accounts.spotify.com/pt-BR/login?continue=https:%2F%2Fopen.spotify.com%2F")
    driver.implicitly_wait(10)
   
login()
    
    # Passo 3 - Inserir uma música valida
    # elem.send_keys("playlist")
    # Selecionar uma playist a partir dos resultados encontrados
    # elem_playlist = driver.find_element_by_xpath(
    # "//*[@id='searchPage']/div/div/section[1]/div[2]/div/div/div/div[4]")
    # elem_playlist.click()

    # Verificar resultados
    assert "Spotify – Buscar" in driver.title
    driver.close()  