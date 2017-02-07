build:
		mkdir -p ./build
		gunzip --stdout < ../datasets/Oshawa_Streets.csv.gz > ./build/streets.csv

run:
		python load_sqlite.py build/streets.csv

clean:
		rm -rf ./build
