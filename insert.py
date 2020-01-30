import sqlite3
import json
import os
from createDB import db_name


# trigger function
def alert(message):
    print('insert: %s' % message)


if __name__ == '__main__':
    #files = os.listdir('input')
    files = ['file.json']
    db = sqlite3.connect(db_name)
    db.create_function("alert", 1, alert)
    try:
        cur = db.cursor()
        for file in files:
            with open('input/%s' % file) as f:
                data = json.load(f)
            #todo change table name
            # insert all field to file table
            sql = 'INSERT INTO files ({}) VALUES ({})'.format(
                ','.join(data.keys()),
                ','.join(['?'] * len(data)))
            cur.execute(sql, tuple(data.values()))
            db.commit()
            print("one record added successfully")
    except Exception as e:
        print('error in operation, %s' % e)
        db.rollback()
    db.close()
