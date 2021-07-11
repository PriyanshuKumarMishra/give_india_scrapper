import requests
import json
op=open('git.json','w')
from bs4 import BeautifulSoup
url='https://www.giveindia.org/certified-indian-ngos'
page=requests.get(url)
soup=BeautifulSoup(page.text,'html.parser')
role=[]
namee=[]
place=[]
name,main = soup.find_all('div', class_='col'),soup.find_all('td', class_='jsx-697282504')
b=1
# for i in name:
#     n.append(i.text)
for i in main:
    if b==2:
        role.append(i.text)
    if b==1:
        namee.append(i.text)
    if b==3:
        place.append(i.text)
        b=0
    b+=1
be=[]
for i,j,k in zip(namee,role,place):
    a={}
    a['name']=i
    a['role']=j
    a['place']=k
    be.append(a)

json.dump(be,op,indent=4)