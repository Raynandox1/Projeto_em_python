from bs4 import BeautifulSoup
import requests

url = 'https://redecanais.la/alive-dublado-2020-1080p_34bae61d1.html'

#Criação da variável page com URL no método request.get
page = requests.get(url)

#coleta,analisa e configura como um objeto BeautifulSoup
soup = BeautifulSoup(page.text,'html.parser')
links = soup.find_all('iframe')

#retorna os todos os links do Junho de 2017 da página

for link in links:
    href= str(link)
    #print(href)
    if "Player" in href:
        href = href[href.find('src="')+5:href.find('" width="')]
        href = "https://sinalpublico.com"+href.replace(".php","hlb.php")    
        print(href)