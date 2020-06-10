import os
import cx_Oracle
import time
import requests
from bs4 import BeautifulSoup

DB_ID = "scott"
DB_PWD = "1234"
DB_URL = "localhost/company"

def get_conn():
    os.putenv("NLS_LANG", ".UTF8")
    conn = cx_Oracle.connect(DB_ID,DB_PWD,DB_URL)
    return conn

def insert_row(conn, no, title, link):
    cursor = conn.cursor()
    str_sql = "INSERT INTO MOVIES_RANKS(NO, TITLE, LINK) " \
        " VALUES(:no, :title, :link)"
    cursor.execute(str_sql, \
        {'no': no, 'title' : title, 'link':link})
    conn.commit()
    cursor.close()

URL = "http://ticket2.movie.daum.net/Movie/MovieRankList.aspx"

res = requests.get(URL)
soup = BeautifulSoup(res.content, 'lxml')
rankings = soup.find_all('strong', class_="tit_join")

def get_rows_count(conn):
    cursor = conn.cursor()
    str_sql = "select nvl(max(no),1) from movies_ranks"
    cursor.execute(str_sql)
    row = cursor.fetchone()
    # print(row) (1,)
    cursor.close()
    return row[0]

conn = get_conn()
no = get_rows_count(conn)
if no == 1:
    pass
else:
    no = no + 1

for movie in rankings:
    m = movie.find('a')
    # print(m.get_text().strip(), m['href'])
    title, link = m.get_text().strip(), m['href']
    conn = get_conn()
    insert_row(conn, no, title, link)
    no += 1

conn.close()
print("Successed!!")


