#Projekt na przedmiot Bazy Danych, semestr letni 2022/2023
#Wykonał: Mateusz Gałęziewski 319433

#Prosta baza danych sprzedaży nieruchomości

import sqlite3

#Let's connect to the database
db = sqlite3.connect('galeziewski_mateusz_projekt.db')

#Creating a cursor
cursor = db.cursor()

#Creating tables
sql_statements = [
    '''CREATE TABLE Building(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        adress VARCHAR NOT NULL,
        postal_code VARCHAR (6) NOT NULL,
        city VARCHAR (50) NOT NULL,
        built_year INTEGER (4),
        lift_inside BOOLEAN NOT NULL,
        total_floors INTEGER DEFAULT 1 NOT NULL 
    )''',
    '''CREATE TABLE Owner(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (40) NOT NULL,
        surname VARCHAR (40) NOT NULL,
        owner_adress VARCHAR NOT NULL,
        phone INTEGER (9) NOT NULL,
        mail VARCHAR (60) NOT NULL
    )''',
    '''CREATE TABLE Client(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (40) NOT NULL,
        surname VARCHAR (40) NOT NULL,
        client_adress VARCHAR NOT NULL,
        phone INTEGER (9) NOT NULL,
        mail VARCHAR (60) NOT NULL
    )''',
    '''CREATE TABLE Agent(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        name VARCHAR (40) NOT NULL,
        surname VARCHAR (40) NOT NULL,
        agent_adress VARCHAR NOT NULL,
        phone INTEGER (9) NOT NULL,
        mail VARCHAR (60) NOT NULL
    )''',
    '''CREATE TABLE prop_category(
        id INTEGER PRIMARY KEY,
        category TEXT (20)
    )''',
    '''CREATE TABLE Property(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    price REAL NOT NULL,
    surface REAL NOT NULL,
    local VARCHAR (6) NOT NULL,
    floor_nr INTEGER NOT NULL,
    rooms INTEGER NOT NULL,
    building_id INTEGER NOT NULL REFERENCES Building(id),
    prop_category_id INTEGER NOT NULL REFERENCES prop_category(id)
    )''',
    '''CREATE TABLE Deal(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        date DATE NOT NULL,
        total_price REAL NOT NULL,
        property_id INTEGER NOT NULL REFERENCES Property(id),
        owner_id INTEGER NOT NULL REFERENCES Owner(id),
        client_id INTEGER NOT NULL REFERENCES Client(id),
        agent_id INTEGER NOT NULL REFERENCES Agent(id)
    )''',
    '''CREATE TABLE Service(
        id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        serivce_name VARCHAR (40) NOT NULL,
        service_price REAL NOT NULL,
        service_description VARCHAR (100) NOT NULL
    )''',
    '''CREATE TABLE INT_Deal_Service(
        int_deal_service_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
        deal_id INTEGER NOT NULL REFERENCES Deal(id),
        service_id INTEGER NOT NULL REFERENCES Service(id)
    )''',
    '''INSERT INTO prop_category (id, category) 
        VALUES 
            (1, 'low standard'),
            (2, 'standard'),
            (3, 'high standard'),
            (4, 'luxury')'''
]

#Executing the queries
cursor.execute('BEGIN')
for sql in sql_statements:
    cursor.execute(sql)
cursor.execute('COMMIT')

#save changes to the database

cursor.close()
db.close()