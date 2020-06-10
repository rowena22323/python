import numpy as np
import requests
from bs4 import BeautifulSoup

URL = "http://ticket2.movie.daum.net/Movie/MovieRankList.aspx"

res = requests.get(URL)
soup = BeautifulSoup(res.content, 'lxml')
box = soup.find_all('div', class_="desc_boxthumb")

count = 0
data = [] # 출력용 리스트
for movie in box:  
    title, ranking = movie.find('strong', class_="tit_join"), movie.find('em', class_="emph_grade")
    movie, grade = title.get_text().strip(), ranking.get_text().strip()
    list = [movie, grade] # list에 집어넣을 값 결정
    data.append(list) # data에 list내용 집어넣기 (2차원)
    count += 1 # 반복자


d=np.array(data)
print(d.shape, d.ndim, d) # (20, 2) / 2 / data내용

