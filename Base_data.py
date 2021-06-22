import sqlite3

conn = sqlite3.connect(':memory:')
cur = conn.cursor()

# create tables
cur.execute("""CREATE TABLE IF NOT EXISTS classes(
   class varchar(50) PRIMARY KEY,
   type varchar(2),
   country varchar(20),
   numGuns tinyint,
   bore REAL,
   displacement INT);
""")
conn.commit()


cur.execute(""" CREATE TABLE If NOT EXISTS ships(
    name varchar(50) PRIMARY KEY,
    class varchar(50) REFERENCES classes(class),
    launched int
)""")
conn.commit()


cur.execute(""" CREATE TABLE If NOT EXISTS Outcomes(
    ship varchar(50) PRIMARY KEY,
    battle varchar(20) REFERENCES Battles(name),
    result varchar(10) 
)""")
conn.commit()


cur.execute(""" CREATE TABLE If NOT EXISTS Battles(
    name varchar(20) PRIMARY KEY,
    [date] datetime 
)""")
conn.commit()

# add data

add_classes = [
    ('Bismarck', 'bb', 'Germany', 8, 15, 42000),
    ('Iowa', 'bb', 'USA', 9, 16, 46000),
    ('Kongo', 'bc', 'Japan' ,8, 14, 32000),
    ('North Carolina', 'bb', 'USA', 9, 16, 37000),
    ('Renown', 'bc', 'Gt. Britain', 6, 15, 32000),
    ('Revenge', 'bb', 'Gt. Britain', 8, 15, 29000),
    ('Tennessee', 'bb', 'USA', 12, 14, 32000),
    ('Yamato', 'bb', 'Japan', 9, 18, 65000)
]

add_ships = [
    ('Iowa', 'Iowa', 1943),
    ('Kongo', 'Kongo', 1913),
    ('North Carolina','North Carolina',1941),
    ('Renown','Renown',1916),
    ('Revenge','Revenge',1916),
    ('Tennessee','Tennessee',1920),
    ('Yamato','Yamato',1941),
    ('California','Tennessee',1921),
    ('Hiei','Kongo',1914),
    ('New Jersey','Iowa',1943),
    ('Washington','North Carolina',1941),
    ('Wisconsin','Iowa',1944)
]

add_Outcomes = [
    ('Bismarck','North Atlantic','sunk'),
    ('California','Suriago Strait','ok'),
    ('Duke of York','North Cape','ok'),
    ('Fuso','Suriago Strait','sunk'),
    ('Hood','North Atlantic','sunk'),
    ('King George V','North Atlantic','ok'),
    ('Kirishima','Guadalcanal','sunk'),
    ('Prince of Wales','North Atlantic','damaged'),
    ('Rodney','North Atlantic','ok'),
    ('Scharnhorst','North Cape','sunk'),
    ('South Dakota','Guadalcanal','damaged'),
    ('Tennessee','Suriago Strait','ok'),
    ('Washington','Guadalcanal','ok'),
    ('West Virginia','Suriago Strait','ok'),
    ('Yamashiro','Suriago Strait','sunk')
]

add_Battles = [
    ('North Atlantic', '1941-05-24'),
    ('Guadalcanal','1942-11-15'),
    ('North Cape','1943-02-26'),
    ('Suriago Strait','1944-10-25')
]

cur.executemany("INSERT INTO classes VALUES(?, ?, ?, ?, ?, ?);", add_classes)
cur.executemany("INSERT INTO ships VALUES(?, ?, ?);", add_ships)
cur.executemany("INSERT INTO Outcomes VALUES(?, ?, ?);", add_Outcomes)
cur.executemany("INSERT INTO Battles VALUES(?, ?);", add_Battles)
conn.commit()

# request

cur.execute("SELECT COUNTRY FROM CLASSES WHERE TYPE='bb' OR TYPE='bc'")

for v in cur.fetchall():
    print(v)


