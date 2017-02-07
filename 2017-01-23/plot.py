import sqlite3

db = sqlite3.connect('./build/oshawa.sqlite3')
cur = db.cursor()
result = cur.execute("""
	with T(name, length) as (
		select rtrim(name, "ESWN"), shape_length
		from streets
	)
	select name, sum(length) as total
	from T
	group by name
	order by total desc;
""")

rows = result.fetchall()
for row in rows:
	print row
