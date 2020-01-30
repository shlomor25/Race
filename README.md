# Race
sqlite3


Hi, Yair

## createDB.py
create sqlite3 DB named race.db
every table has trigger on insert query

you can see schema diagram in SCHEMA:main.uml 

## insert.py
in input dir, I put json file (named file.json)
run insert.py to insert this json to files table

## fetch.py
simple select query on files table.



### notes:
i tried to use mongoDB
Dani wants events engine for horse race, 
mongo support events only in replica-set version (storing DB in cloud)
and this is a problem in elbit.systems 
