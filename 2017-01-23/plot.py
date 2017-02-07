import sqlite3
import matplotlib
matplotlib.use('Agg')
from matplotlib import pylab as pl

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
pl.hist([float(x[1]) for x in rows], bins=100)
pl.savefig('./build/lengths.png')
