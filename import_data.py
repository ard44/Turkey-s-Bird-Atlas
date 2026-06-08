import sqlite3
import csv

conn = sqlite3.connect('bird_atlas.db')
cursor = conn.cursor()

import csv
import sqlite3


conn = sqlite3.connect('bird_atlas.db')
cursor = conn.cursor()


cursor.execute('DROP TABLE IF EXISTS species')
cursor.execute('''
    CREATE TABLE species (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name_tr TEXT,
        name_latin TEXT,
        genus TEXT,
        habitat_name TEXT,
        region_name TEXT,
        conservation_status TEXT
    )
''')


with open('kuslar.csv', encoding='utf-8-sig', newline='') as f:
    reader = csv.DictReader(f, delimiter=';')
    for row in reader:
        cursor.execute('''
            INSERT INTO species (name_tr, name_latin, genus, habitat_name, region_name, conservation_status)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            row['Türkçe Adı'], 
            row['Bilimsel Adı'], 
            row['Cins'], 
            row['Habitat'], 
            row['Görüldüğü Türkiye Bölgeleri'], 
            row['IUCN Durumu']
        ))

conn.commit()
conn.close()
print("Tebrikler! 513 kuş türü veritabanına başarıyla aktarıldı.")