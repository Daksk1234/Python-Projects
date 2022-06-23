import requests
from bs4 import BeautifulSoup

user_input = input("Enter The Word: ")
web = requests.get('https://www.lexico.com/definition/'+user_input)
data = web.content
soup = BeautifulSoup(data, features="html.parser")
tag = soup.find_all("span", "ind")
a = 1
# print(tag)

for i in tag:
    print(a, ".", i.text)
    a = a + 1