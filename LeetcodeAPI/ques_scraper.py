import requests
from bs4 import BeautifulSoup

response = requests.get("https://leetcode.com/problems/two-sum")
soup = BeautifulSoup(response.text, 'html.parser')

print(soup.text)

#Work in progress!!