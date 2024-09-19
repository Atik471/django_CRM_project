import pymysql , os


database = pymysql.connect(
    host = 'localhost',
    user = 'root',
    passwd = '12345678'
)

cursorObj  = database.cursor()

cursorObj.execute("CREATE DATABASE db_crm")

# print(cursorObj)