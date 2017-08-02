import _mysql

buffer = 1



def oneQuery():
	db = _mysql.connect(host="localhost",user="root",passwd="database22",db="hotsauces")
	db.query("""SELECT sauceName FROM sauces;""")
	stringQuery = db.store_result()
	nR = stringQuery.num_rows()
	while(nR > 0):
	    try:
		    print(stringQuery.fetch_row()[0][0])
		    nR = nR - 1
	    except IndexError:
		    break
	db.close()

def twoQuery():
	db = _mysql.connect(host="localhost",user="root",passwd="database22",db="hotsauces")
	db.query("""SELECT * FROM heat;""")
	r = db.store_result()
	nR = r.num_rows()
	while(nR > 0):
		print(r.fetch_row()[0][1])
		nR = nR - 1
	db.close()

def threeQuery():
	db = _mysql.connect(host="localhost",user="root",passwd="database22",db="hotsauces")
	db.query("""SELECT Count(heatID) FROM heat;""")
	r = db.store_result()
	print("""There are """ + str(r.fetch_row()[0][0]) + """ different heat ratings in the database.""")
	db.close()
	
while buffer:
	print("""
	0. Exit
	1. See hot sauces
	2. See heats
	3. See the number of individual heat ratings
	""")
	buffer=input("What would you like to do? ")
	if buffer == 1:
		oneQuery()
	if buffer == 2:
		twoQuery()
	if buffer == 3:
		threeQuery()