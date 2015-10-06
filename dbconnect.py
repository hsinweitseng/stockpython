import MySQLdb
import time

conn = MySQLdb.connect("hsinweitseng.mysql.pythonanywhere-services.com","hsinweitseng","9954hsin","hsinweitseng$default")

c = conn.cursor()

username = 'hsinweitseng'
tweet = 'man is cool'

c. execute("INSERT INTO taula (time, username, tweet) VALUES (%s,%s,%s)",(time.time(), username, tweet))

conn.commit()

c.execute("SELECT * FROM taula")

rows = c.fetchall()

for eachRow in rows:
    print eachRow
