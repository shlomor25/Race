import sqlite3
db_name = 'race.db'

# SQL create table scripts
create_sensor = '''CREATE TABLE IF NOT EXISTS sensors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    sensor_name TEXT (20) NOT NULL,
    sensor_type NUMERIC,
    platform INTEGER,
    description TEXT (200),
    location NUMERIC ,
    sensor_status INTEGER,
    update_date_time NUMERIC,
    direction REAL,
    coverage INTEGER,
    frequency TEXT (50)
    );'''

create_person = '''CREATE TABLE IF NOT EXISTS persons (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    person_name TEXT (20) NOT NULL,
    description TEXT (200),
    update_date_time NUMERIC,
    location TEXT (50),
    address TEXT (50),
    language INTEGER,
    gender INTEGER,
    age INTEGER,
    speaker_id INTEGER
    );'''

create_device = '''CREATE TABLE IF NOT EXISTS devices (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    external_id INTEGER NOT NULL,
    device_type INTEGER ,
    model TEXT (20),
    name TEXT (20) NOT NULL,
    description TEXT (200), 
    SSID TEXT (20), --add table for many SSIDs
    SSID_password TEXT (10),
    mac_id TEXT (20),
    vendor NUMERIC,
    imsi TEXT (15),
    imei TEXT (15),
    ip TEXT (15),
    location TEXT (100),
    address TEXT (100),
    update_date_time NUMERIC,
    freqency TEXT (50),
    network_hierarchy INTEGER,
    language INTEGER,
    gender INTEGER ,
    age INTEGER ,
    keywords INTEGER , --many?
    with_gun NUMERIC ,
    key_logger NUMERIC ,
    linked_devices INTEGER , --many
    sensor_id INTEGER REFERENCES sensors(sensor_id),
    person_id INTEGER REFERENCES persons(person_id),
    --FOREIGN KEY(sensor_id) REFERENCES sensors(sensor_id),
    --FOREIGN KEY(person_id) REFERENCES persons(person_id)
    -- speaker_id
    -- number of speakers?
    );'''

create_device_linked_devices = """CREATE TABLE IF NOT EXIST device_linked_devices (
    source_id INTEGER NOT NULL ,
    target_id INTEGER NOT NULL ,
    FOREIGN KEY (source_id) REFERENCES devices(source_id), 
    FOREIGN KEY (target_id) REFERENCES devices(target_id),
    UNIQUE (source_id, target_id)
    );"""

create_file = '''CREATE TABLE IF NOT EXISTS files (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    external_id INTEGER ,
    file_name TEXT (20) NOT NULL,
    file_type INTEGER,
    description TEXT (200),
    update_date_time NUMERIC,
    file_path TEXT (50) NOT NULL,
    language INTEGER,
    gender INTEGER,
    age INTEGER 
    speaker_id INTEGER,
    number_of_speaker INTEGER,
    keywords INTEGER,
    with_gun NUMERIC ,
    device_id INTEGER,
    FOREIGN KEY(device_id) REFERENCES devices(device_id)
    );'''

create_cyber_insight = '''CREATE TABLE IF NOT EXISTS cyber_insights (
    insight_id INTEGER PRIMARY KEY AUTOINCREMENT,
    insight_type INTEGER,
    description TEXT (200),
    update_date_time NUMERIC,
    linked_devices TEXT (50), -- many
    location TEXT (50), -- many
    address TEXT (50), -- many
    synopsis TEXT (50),
    people NUMERIC,
    number_of_people NUMERIC,
    combat_vs_non TEXT (10),
    activity NUMERIC,
    device_id INTEGER, -- ?
    FOREIGN KEY(device_id) REFERENCES devices(device_id)
    );'''

create_cyber_attack = '''CREATE TABLE IF NOT EXISTS cyber_attacks (
    attack_id INTEGER PRIMARY KEY AUTOINCREMENT,
    access_vectors INTEGER,
    description TEXT (200),
    attack_name TEXT (50),
    linked_devices TEXT (50), -- many
    synopsis TEXT (50),
    msisdn TEXT (10),
    ip TEXT (15),
    attack_status INTEGER,
    update_date_time NUMERIC,
    device_id INTEGER, -- ?
    FOREIGN KEY(device_id) REFERENCES devices(device_id)
    );'''

# SQL create trigger script
# now on insertion, print description field
trigger = """CREATE TRIGGER if not exists {}
                AFTER INSERT ON {}
                BEGIN
                SELECT alert(NEW.description); 
                END;"""

# tables
tables = ["sensors", "persons", "devices", 'files', "cyber_insights", "cyber_attacks"]
queries = [create_sensor, create_person, create_device, create_file, create_cyber_insight, create_cyber_attack]
triggers = [trigger.format('t_'+table, table) for table in tables]


if __name__ == '__main__':
    db = sqlite3.connect(db_name)
    try:
        cur = db.cursor()
        for i in range(len(tables)):
            # create table and trigger
            cur.execute(queries[i])
            print('table %s created successfully' % tables[i])
            cur.execute(triggers[i])
            print('\ttrigger added successfully')
    except Exception as e:
        print('error in operation, %s' % e)
        db.rollback()
    db.close()
