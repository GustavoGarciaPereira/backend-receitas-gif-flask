import requests
import json
import re

from bs4 import BeautifulSoup

url = 'http://www.calendario.com.br/feriados-santa-maria-rs.php?ano=2021'

page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

testo = soup.find_all("b")

dic = {}
dic2={}
lis = []

acha_data = re.compile(r"[0-9][0-9]/[0-9][0-9]/[0-9][0-9][0-9][0-9]")

#for i in range(len(testo)):
#    if acha_data.match(testo[i].text.strip()):
#        dic['data'] = testo[i+0].text.strip()
#        dic['tipo'] = testo[i+1].text.strip('[]')
#        dic['descricao'] = testo[i+2].text
#        lis.append(dic)
#        dic = {}
#


for i in range(len(testo)):
    if acha_data.match(testo[i].text.strip()):
        dic2['data'] = testo[i+0].text.strip()
        dic2['tipo'] = testo[i+1].text.strip('[]')
        dic2['descricao'] = testo[i+2].text
        dic[testo[i+0].text.strip()] = dic2
        lis.append(dic)
        #dic = {}
        dic2 = {}

#print(dic['07/09/2021'])