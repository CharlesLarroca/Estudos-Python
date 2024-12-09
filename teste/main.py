# import mysql.connector

# conn = mysql.connector.connect(host='localhost',
# user='root',
# password='sua_senha')

# if conn.is_connected():
#   print('Connected.')
# else:
#   print('Fail.')

import pymysql

conn = pymysql.connect(host='localhost', user='root', password='Drl4rr0c4#')

print(conn)