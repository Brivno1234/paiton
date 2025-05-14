from bs4 import BeautifulSoup 
import requests


url = input('Enter a URL (include `http://`): ')

response = requests.get(url)
html = response.text
soup = BeautifulSoup(html,"html.parser")


def upp ():
    for i in soup.find_all("h3"):
        for a in i.find_all("a"):
            Text = a.text.strip()
            print(Text)
upp()        
    
    

    