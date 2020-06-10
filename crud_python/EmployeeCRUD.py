import os
import cx_Oracle
import time

DB_ID = "scott"
DB_PWD = "1234"
DB_URL = "localhost/company"

def get_conn():
    os.putenv("NLS_LANG", ".UTF8")
    conn = cx_Oracle.connect(DB_ID,DB_PWD,DB_URL)
    print(conn.version)
    return conn

def get_all_rows(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employee")
    for row in cursor:
        print(row)
    cursor.close()
    return cursor

def get_rows_key(conn, key):
    cursor = conn.cursor()
    str_sql = "select*from employee where id =: id"
    cursor.execute(str_sql, {'id' : key})
    row = cursor.fetchall()
    print(row)
    cursor.close()

def insert_row(conn, id, name, email):
    cursor = conn.cursor()
    str_sql = "insert into employee values(:id,: name,: email)"
    cursor.execute(str_sql, {'id' : id , 'name' : name , 'email': email})
    conn.commit()
    cursor.close()

def update_row(conn, id, name, email):
    cursor = conn.cursor()
    str_sql = "update employee set name=:name, "+\
        "email =:email where id =: id"
    cursor.execute(str_sql, {'id' : id,'name': name, 'email':email})
    conn.commit()
    cursor.close()

def delete_row(conn, id):
    cursor = conn.cursor()
    str_sql = "delete from employee where id =: id"
    cursor.execute(str_sql, {'id':id})
    conn.commit()
    cursor.close()

while True:
    print("########사원관리#######")
    print(" 1. 전체               ")
    print(" 2. 검색               ")
    print(" 3. 추가               ")
    print(" 4. 수정               ")
    print(" 5. 삭제               ")
    print(" 6. 종료               ")
    print("#######################")
    num = input("번호를 입력해주세요.[1-6]: ")
    if num == "1":
        conn = get_conn()
        get_all_rows(conn)
        conn.close()
    elif num == "2":
        key = int(input("사번을 입력해 주세요 : "))
        conn = get_conn()
        get_rows_key(conn,key)
        conn.close() 
    elif num == "3":
        id = int(input("사번을 입력하세요 : "))
        name = input("이름을 입력하세요 : ")
        email = input("이메일을 입력하세요 : ")
        conn = get_conn()
        insert_row(conn, id, name, email)
        conn.close()
    elif num == "4":
        id = int(input("사번을 입력하세요 : "))
        name = input("이름을 입력하세요 : ")
        email = input("이메일을 입력하세요 : ")
        conn = get_conn()
        update_row(conn, id, name, email)
        conn.close()
    elif num == "5":
        id = int(input("사번을 입력하세요 : "))
        conn = get_conn()
        delete_row(conn, id)
        conn.close()
    elif num == "6":
        print("종료되었습니다. 감사합니다. 안녕히 가십시요.")
        time.sleep(1)
        break
    else:
        os.system("cls")
