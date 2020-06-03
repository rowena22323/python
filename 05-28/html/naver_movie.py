import os
import cx_Oracle
import requests
from bs4 import BeautifulSoup

DB_ID = "scott"
DB_PWD = "1234"
DB_URL = "localhost/company"

def get_conn():
    os.putenv("NLS_LANG", ".UTF8")
    conn = cx_Oracle.connect(DB_ID,DB_PWD,DB_URL)
    print(conn.version)
    return conn

def insert_row(conn, TITLE, LINK):
    cursor = conn.cursor()
    str_sql = "insert into movies_ranks values(TITLE,LINK)"
    cursor.execute(str_sql, {'TITLE' : TITLE , 'LINK': LINK})
    conn.commit()
    cursor.close()

def get_rows_key(conn, key):
    cursor = conn.cursor()
    str_sql = "select*from movies_ranks where NO =: NO"
    cursor.execute(str_sql, {'NO' : key})
    row = cursor.fetchall()
    print(row)
    cursor.close()

res = requests.get("https://movie.naver.com/movie/sdb/rank/rmovie.nhn")
soup = BeautifulSoup(res.content, 'lxml')
rankings = soup.find_all('table', class_= "list_ranking")
movies = rankings[0].find_all('div',class_="tit3")

conn = get_conn()
i=0
for movie in movies : 
    m = movie.find('a')
    i+=1
    insert_row(conn, m.get_text(), m['href'])

conn.close()

while True:
    print("########무비무비#######")
    print(" 1. 전체               ")
    print(" 2. 순위               ")
    print("#######################")
    num = input("번호를 입력해주세요.[1-2]: ")
    if num == "1":
        conn = get_conn()
        get_all_rows(conn)
        conn.close()
    elif num == "2":
        key = int(input("순위를 입력해 주세요 : "))
        conn = get_conn()
        get_rows_key(conn,key)
        conn.close()



