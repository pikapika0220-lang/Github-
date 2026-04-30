import mysql.connector

conn = mysql.connector.connect(
    host ="127.0.0.1", #どこのSQLに入るか
    user="root",#user名
    password="password",
    database="mydb" #どのdatabaseか(エクセルの表みたいな)
)
cursor = conn.cursor()# SQLを実行するための道具
name = "Kato"
age = 28
cursor.execute(f"INSERT INTO users (name, age) VALUES ('{name}', {age})")#SQLを実行する
cursor.execute("DELETE FROM users WHERE id != 7 AND name = 'Kato'")
conn.commit()#変更を確定

cursor.execute("SELECT * FROM users")
rows = cursor.fetchall()#結果を取得する
for row in rows:
    print(row)

conn.close()#接続を切る