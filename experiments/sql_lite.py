import sqlite3
import itertools
import random

dbpath = "test.sqlite"
conn = sqlite3.connect(dbpath)

cur = conn.cursor()
iter_cnt = itertools.count(1)

cur.executescript("""

DROP TABLE IF EXISTS items;

CREATE TABLE items(
    item_id INTEGER PRIME KEY,
    name TEXT,
    price flaot UNIQUE
);



INSERT INTO items(item_id, name, price)VALUES(201,'Apple', 800);
INSERT INTO items(item_id, name, price)VALUES(202,'Orange', 780);
""")


conn.commit()


for i in range(20):
    num = random.random()
    cur.execute("INSERT INTO items(item_id, name, price)VALUES({}, 'test', {})".format(next(iter_cnt),  num))

conn.commit()
cur = conn.cursor()
cur.execute("SELECT item_id,name,price FROM items where item_id = 15")
item_list = cur.fetchall()

for it in item_list:
    print(it)

conn.close()