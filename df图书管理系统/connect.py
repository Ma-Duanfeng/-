import pymysql

# 连接数据库
def connect():
    conn = pymysql.connect(host='127.0.0.1', user='root', password='633901', database='library')
    cursor = conn.cursor()
    return cursor, conn
