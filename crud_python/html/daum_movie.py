import requests
import lxml
from bs4 import BeautifulSoup

res = requests.get("http://ticket2.movie.daum.net/Movie/MovieRankList.aspx")
soup = BeautifulSoup(res.content,'lxml')
rankings = soup.find_all('strong', class_= 'tit_join')

for movie in rankings:
    m = movie.find('a')
    print(m.get_text().strip(), m['href'])
