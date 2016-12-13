import sqlite3, random
database = sqlite3.connect('personal.db')
print "Opened database successfully";
name = ['Paul', 'Jeff', 'Rosaline', 'Mabel']
state = ['Florida', 'Utah', 'Maine', 'South Dakota', 'Arkansas']

database.execute('''CREATE TABLE COMPANY
       (ID 			  INT     NOT NULL,
       NAME           TEXT    NOT NULL,
       AGE            INT     NOT NULL,
       ADDRESS        CHAR(50),
       SALARY         REAL);''')
print "Table created successfully";



def insertRandomRows():
	for i in range(0,4):
		randomAge = random.randrange(18, 47)
		randomState = random.randrange(0, 5)
		database.execute("INSERT INTO COMPANY (ID,NAME,AGE,ADDRESS,SALARY) \
      		VALUES (%i, '%s', %i, '%s', 20000.00 )" % (i, name[i], randomAge, state[randomState]));
		database.commit()	

insertRandomRows()

database.close()