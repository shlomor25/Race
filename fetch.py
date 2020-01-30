import sqlite3
from createDB import db_name

db = sqlite3.connect(db_name)
# todo change table name
sql = "SELECT * from files;"
cur = db.cursor()
cur.execute(sql)
while True:
    record = cur.fetchone()
    if record is None:
        break
    print(record)
db.close()
