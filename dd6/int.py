import mysql.connector

db = mysql.connector.connect(host="localhost",port=3306, user="root", password="123456789", database="dbmsproj")
cursor = db.cursor()
# return the status of connection
def check_connection():
    if db.is_connected():
        return True
    else:
        return False
print(check_connection())


# print("Enter UserID")
# ch=int(input())
cursor = db.cursor()
query = "SELECT * FROM users"
cursor.execute(query)
cursor.close()


for row in cursor.fetchall():
    print(row)

with open('confl1.sql', 'r') as file:
    confl1 = file.read()
db.start_transaction()
cursor = db.cursor()
cursor.execute(confl1)
db.commit()
db.close()