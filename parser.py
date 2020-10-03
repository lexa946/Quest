import requests
from bs4 import BeautifulSoup


response = requests.get('https://quest-book.ru/forum/onlinebook.php?game=labirint&mode=book#66')
response.encoding = 'windows-1251'
soup = BeautifulSoup(response.text, 'html.parser')
all_paragraph = soup.select(".Section1 > p")[94:]
all_paragraph = [p.text for p in all_paragraph]
all_paragraph = list(filter(lambda x: len(x)>5, all_paragraph))

for paragraph in all_paragraph:
    print(paragraph)
print(response.text)