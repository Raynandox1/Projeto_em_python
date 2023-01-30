from bs4 import BeautifulSoup
import requests

url = 'https://sinalpublico.com/player3/download.php?vid=carretelmentolado.gq/d/MP4/RedeCanais/RedeCanais/RCFServer5/ondemand/DRESTNHONMLTVSODLCRALEG.mp4?mu3zAQc9HC3GbwJq=shlLRx08reUBj7nJhL7ryQ&3U1G7qaTxrPbalZnEx=1674426919'

#Criação da variável page com URL no método request.get
page = requests.get(url)

#coleta,analisa e configura como um objeto BeautifulSoup
soup = BeautifulSoup(page.text,'html.parser')
links = soup.find_all('body')

#retorna os todos os links do Junho de 2017 da página

for link in links:
    href= str(link)
    print(href)
    
    