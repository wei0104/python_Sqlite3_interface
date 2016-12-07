#!/usr/bin/python
import sqlite3
conn = sqlite3.connect('test.db')

c = conn.cursor()
c.execute('''CREATE TABLE Grades
(
	ID int NOT NULL,
	last_name varchar(20),
	first_name varchar(20),
	attendance decimal(8,2),
	quiz int,
	midterm int,
	final decimal(8,2),
	e_credit int
	)''')
c.execute("INSERT INTO Grades VALUES (140104001,'Tom','Wang',93.33,68,82,64.44,5)")
c.execute("INSERT INTO Grades VALUES (140106004,'Bob','Huang',100.00,80,100,47.77,3)")
c.execute("INSERT INTO Grades VALUES (140106006,'Mary','Lee',92.31,64,90,86.66,5)")
c.execute("INSERT INTO Grades VALUES (140303002,'Alice','Lin',86.67,48,66,84.44,6)")
c.execute("INSERT INTO Grades VALUES (140306005,'Joe','Hu',93.33,48,66,84.44,6)")
c.execute("ALTER TABLE Grades ADD COLUMN overall_percent decimal(8,2)")
c.execute('''
		  UPDATE Grades
       	  SET overall_percent = (
				attendance * 0.1 + quiz * 0.1 +
				midterm * 0.4 + final *0.4 + e_credit)
		  ''')
c.execute("ALTER TABLE Grades ADD COLUMN grade varchar(4)")
c.execute("UPDATE Grades SET grade = 'A' WHERE overall_percent >= 90.00")
c.execute("UPDATE Grades SET grade = 'B' WHERE overall_percent >= 80.00 and overall_percent< 90.00")
c.execute("UPDATE Grades SET grade = 'C' WHERE overall_percent >= 70.00 and overall_percent< 80.00")
c.execute("UPDATE Grades SET grade = 'D' WHERE overall_percent >= 60.00 and overall_percent< 70.00")
c.execute("UPDATE Grades SET grade = 'F' WHERE overall_percent < 60.00")
for row in c.execute("SELECT * FROM Grades ORDER BY grade"):
    print row

conn.commit()
conn.close()
