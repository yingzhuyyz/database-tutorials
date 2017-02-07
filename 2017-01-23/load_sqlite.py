import csv
import sqlite3
import sys
import os

sqlite_file = 'oshawa.sqlite3'

def create_table(db, tn, cn) :
	cur = db.cursor()
	cur.execute("""
	CREATE TABLE IF NOT EXISTS %s (%s);
	""" % (tn, cn))

	cur.execute("delete from %s" % tn)

	r = cur.execute('select * from %s;' % tn)
	names = [x[0] for x in r.description]
	print names

def insert_rows(db, tn, rows) :
	cur = db.cursor()
	for row in rows:
		fields = ','.join("?" for x in row)
		sql = "INSERT INTO %s VALUES (%s)" % (tn, fields)
		cur.execute(sql, row)

	r = cur.execute("select * from %s" % tn)
	print r.fetchone()

### Main ###

if sys.argv[1:]:
	datafile = sys.argv[1]
else:
	print "Usage: %s <datafile>" % sys.argv[0]
	sys.exit(0)

db = sqlite3.connect(sqlite_file)

tablename = os.path.splitext(os.path.basename(datafile))[0]
with open(datafile) as csvfile:
	reader = csv.reader(csvfile)
	rows = list(reader)
rows[0] = [unicode(x, errors="ignore") for x in rows[0]]
colnames = ','.join(rows[0])

print "creating table %s" % tablename;
create_table(db, tablename, colnames)
insert_rows(db, tablename, rows[1:])
db.commit()
