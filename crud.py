import sqlite3

connect=sqlite3.connect('test.db')
cursor=connect.cursor()


def create_table():
	cursor.execute('CREATE TABLE IF NOT EXISTS user(id INTEGER PRIMARY KEY AUTOINCREMENT, name VARCHAR(255), email VARCHAR(255))')


def create_table2():
	cursor.execute('CREATE TABLE IF NOT EXISTS history( name VARCHAR(255), value VARCHAR(255), FOREIGN KEY(name) REFERENCES user(name) )')
	

def data_entry():
	#cursor.execute("INSERT INTO user(name,email) VALUES('alice','alice@example.com')")
	cursor.execute("INSERT INTO user(id,name,email) VALUES(3,'alex','alex@example.com')")
	connect.commit()

def data_entry2():
	#cursor.execute("INSERT INTO user(name,email) VALUES('alice','alice@example.com')")
	cursor.execute("INSERT INTO history(name,value) VALUES('alex','-4')")
	cursor.execute("INSERT INTO history(name,value) VALUES('alex','7')")
	connect.commit()



def read_from_db2():
	cursor.execute('SELECT * FROM history where value>1')
	# data=cursor.fetchall()
	# print(data)

	for row in cursor.fetchall():
		print(row)


def read_from_db():
	cursor.execute('SELECT * FROM user')
	# data=cursor.fetchall()
	# print(data)

	for row in cursor.fetchall():
		print(row)

def update():
	cursor.execute('SELECT * FROM user')
	[print(row) for row in cursor.fetchall()]
	cursor.execute("UPDATE user set email='john@example.com' WHERE name='john' ")
	connect.commit()
	print(60*'-')
	cursor.execute('SELECT * FROM user')
	[print(row) for row in cursor.fetchall()]


def delete():
	cursor.execute('SELECT * FROM user')
	[print(row) for row in cursor.fetchall()]
	cursor.execute("delete FROM user WHERE email='john@example.com' ")
	connect.commit()
	print(60*'-')
	cursor.execute('SELECT * FROM user')
	[print(row) for row in cursor.fetchall()]

#create_table()
#data_entry()
#create_table2()
#data_entry2()
#read_from_db()
read_from_db2()
#update()
#delete()
cursor.close()
connect.close()
