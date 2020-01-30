# Race
sqlite3


Hi, Yair

## createDB.py
create sqlite3 DB named race.db

every table has trigger on insert query

you can see schema diagram in SCHEMA.uml 

## insert.py
in 'input' directory, I put json file (named file.json)

run insert.py to insert this json to files table

## fetch.py
simple select query on files table.


### notes:
Dani suggest to use mongodb

i tried this idea, but mongodb supports events engine only in replica-set version (storing DB in cloud)

and this is a problem in elbit.systems 

we need this event engine to run horse race flow.

please look at schema design and verify that its OK.