import sqlite3
database = sqlite3.connect('personal.db')
print "Opened database successfully";

database.execute('''CREATE TABLE COMPANY
       (ID 			  INT     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')
print "Table created successfully";
name = ['Paul', 'Jeff', 'Rosaline', 'Mabel']

def insertRandomRows():
	for i in range(0,4):
		database.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      		VALUES (%i, '%s', 32, 'California', 20000.00 )" % (i, name[i]));
		database.commit()	

insertRandomRows()

database.close()