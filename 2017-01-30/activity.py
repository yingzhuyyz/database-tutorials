import sqlite3

def setup():
	db = sqlite3.connect("shared.db")
	cur = db.cursor()
	cur.execute("create table if not exists T(value int)")
	cur.execute("delete from T")
	cur.execute("insert into T values (0)")
	db.commit()
	db.close()

def task1():
	db = sqlite3.connect("shared.db")
	cur = db.cursor()
	r = cur.execute("select value from T")
	print r.fetchone()

def task2():
	db = sqlite3.connect("shared.db")
	cur = db.cursor()

setup()
task1()
