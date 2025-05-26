import sqlite3

##Connect to sqlite3
connection = sqlite3.connect("student.db")

##create a Cursor object

cursor = connection.cursor()

## create the table

table_info="""
CREATE table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
MARKS INT)
"""

cursor.execute(table_info)

#Inserting records

cursor.execute('''Insert Into STUDENT values('Hari','ML',95)''')
cursor.execute('''Insert Into STUDENT values('Hemachandran','ML',98)''')
cursor.execute('''Insert Into STUDENT values('Jagadeesh','ML',100)''')
cursor.execute('''Insert Into STUDENT values('Geo','Data Science',95)''')
cursor.execute('''Insert Into STUDENT values('Rajesh','ML',92)''')
cursor.execute('''Insert Into STUDENT values('Irsath','Data Science',90)''')
cursor.execute('''Insert Into STUDENT values('Arun','Data Science',75)''')
cursor.execute('''Insert Into STUDENT values('Deva','CSE',65)''')

print("The inserted records are")
data = cursor.execute('''Select * from STUDENT''')
for row in data:
    print(row)



##commmit changes
connection.commit()
connection.close
