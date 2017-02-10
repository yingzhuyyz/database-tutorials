import sqlite3
import time
import random

def pause(n):
	time.sleep(n)  # n seconds

def setup():
	db = sqlite3.connect("shared.db")
	cur = db.cursor()
	cur.execute("create table if not exists T(value int)")
	cur.execute("delete from T")
	cur.execute("insert into T values (0), (1), (2)")
	db.commit()
	db.close()

def task1(n, transaction):
	db = sqlite3.connect("shared.db")
	cur = db.cursor()
	for i in range(n):

		if transaction:
			cur.execute("begin transaction")

		r = cur.execute("select max(value) from T")
		highest = r.fetchone()[0]
		pause(random.random())  # 0 to 1 seconds
		r = cur.execute("select min(value) from T")
		lowest = r.fetchone()[0]

		if transaction:
			db.commit()

		if lowest <= highest:
			print "Consistent (min = %d, max = %d)" % (lowest, highest)
		else:
			print "Inconsistent (min = %d, max = %d)" % (lowest, highest)

def task2(n):
	db = sqlite3.connect("shared.db")
	cur = db.cursor()
	for i in range(n):
		if i % 2 == 0:
			v = 0
		else:
			v = 1
		cur.execute("update T set value = ?", (v,))
		db.commit()
		pause(random.random())  # 0 to 1 seconds

if __name__ == '__main__':
	from multiprocessing import Process
	setup()
	p1 = Process(target=task1, args=(10, True))
	p2 = Process(target=task2, args=(10,))
	p1.start()
	p2.start()
	p1.join()
	p2.join()
