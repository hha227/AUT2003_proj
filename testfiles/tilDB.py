
import mysql.connector as mariadb

mariadb_connection = mariadb.connect(user='student',password='student', database='projekt2003')
cursor = mariadb_connection.cursor()
Temperatur = 5
Gravity = 10
Prosent = 50
gkhu = 10


cursor.execute("INSERT INTO test (Temperatur, Gravity, Prosent,  gkhu) VALUES (%s,%s,%s,%s)",(Temperatur, Gravity, Prosent,  gkhu) )
mariadb_connection.commit()

#sudo apt-get install python3-mysql.connector
