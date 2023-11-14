import requests
import pandas as pd
from bs4 import BeautifulSoup
url = 'https://www.espncricinfo.com/rankings/content/page/211271.html'
response = requests.get(url)

soup = BeautifulSoup(response.text, "html.parser")
x = soup.find_all(class_='StoryengineTable')[1]
y = x.find_all('tr')
df3 = []
for i in y:
  temp = []
  for j in i.find_all('td'):
    #  print(j.text,end=" ")
    temp.append(j.text)
  df3.append(temp)
df3=pd.DataFrame(df3)
print(df3)
