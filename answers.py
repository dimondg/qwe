#Укорачиваем старый фильм
def get_result(name):
    import sqlite3
    con = sqlite3.connect(name)
    cur = con.cursor()
    result = cur.execute('''UPDATE films 
    SET duration = int(duration) / 3
    WHERE year = 1973''')
    con.commit()
    con.close()
#Длинная старая фантастика
def get_result(name):
    import sqlite3
    con = sqlite3.connect(name)
    cur = con.cursor()
    result = cur.execute('''DELETE from films where year < 2000 AND duration > 90 
    AND genre=(SELECT id FROM genres WHERE title = 'фантастика')''').fetchall()
    con.commit()
    con.close()
#Длинные комедии
import sqlite3
f1 = input()
con = sqlite3.connect(f1)
cur = con.cursor()
result = cur.execute("""SELECT title FROM Films WHERE (genre=(SELECT id FROM genres
            WHERE title = 'комедия')) AND duration >= 60""").fetchall()
for elem in result:
    print(elem[0])
con.close()
#Список песен
import sqlite3
nnn = input()
con = sqlite3.connect("music_db.sqlite")
cur = con.cursor()
result = cur.execute("""SELECT DISTINCT Track.Name 
FROM Track
LEFT JOIN album ON track.albumId = album.albumId 
LEFT JOIN artist ON artist.ArtistId = album.ArtistId 
WHERE artist.Name = ? 
ORDER BY track.Name""", (nnn,)).fetchall()
for elem in result:
    print(elem[0])
con.close()
#короткие фильмы
import sqlite3
f1 = input()
con = sqlite3.connect(f1)
cur = con.cursor()
result = cur.execute('''SELECT title FROM films WHERE (duration <= 85)''').fetchall()
for elem in result:
    print(elem[0])

con.close()
#список исполнителей
import sqlite3

a = []
genre = input()
db = sqlite3.connect("music_db.sqlite")
cur = db.cursor()
result = cur.execute(f"""SELECT DISTINCT
  a.name
FROM 
  genre g,
  track t,
  album al,
  artist a
WHERE
  t.genreid = g.genreid 
AND
  t.albumid = al.albumid
AND
  al.artistid = a.artistid
AND
  g.name = '{genre}'
ORDER BY a.name;""")
for i in result:
    if i[0] not in a:
        a.append(i[0])
for i in a:
    print(i)
db.close()
