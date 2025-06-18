
import sqlite3

## Connect to sqlite3
connection = sqlite3.connect("student.db")

## Create a cursor object to insert record, create table, retrive data
cursor = connection.cursor()

## create the table
table_info = """
Create table STUDENT(NAME VARCHAR(25), CLASS VARCHAR(25),SECTION VARCHAR(25), MARKS INT);
"""

cursor.execute(table_info)

## Insert records
cursor.execute("""
INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES
('Alice', 'Math', 'B', 85),
('Bob', 'English', 'A', 78),
('Charlie', 'Science', 'C', 92),
('David', 'History', 'B', 82),
('Emily', 'Art', 'A', 98),
('Finn', 'Music', 'C', 75),
('Grace', 'Computer Science', 'B', 89),
('Henry', 'Geography', 'A', 68),
('Isabella', 'Biology', 'C', 95),
('Jack', 'Chemistry', 'B', 80),
('Olivia', 'Physics', 'A', 100),
('William', 'French', 'C', 72),
('Sophia', 'Spanish', 'B', 87),
('Lucas', 'German', 'A', 90),
('Mia', 'Italian', 'C', 84),
('Ethan', 'Latin', 'B', 79),
('Aaliyah', 'Literature', 'A', 99),
('Benjamin', 'Philosophy', 'C', 71),
('Charlotte', 'Psychology', 'B', 86),
('Daniel', 'Sociology', 'A', 93),
('Elijah', 'Anthropology', 'C', 69),
('Evelyn', 'Economics', 'B', 81),
('Ava', 'Accounting', 'A', 97),
('James', 'Marketing', 'C', 70),
('Isabella', 'Finance', 'B', 83),
('Mason', 'Business', 'A', 91),
('Amelia', 'Statistics', 'C', 77),
('Michael', 'Calculus', 'B', 88),
('Jennifer', 'Linear Algebra', 'A', 96),
('Noah', 'Differential Equations', 'C', 74),
('Ashley', 'Discrete Mathematics', 'B', 82),
('Matthew', 'Probability Theory', 'A', 94),
('Madison', 'Logic', 'C', 67),
('Daniel', 'Algorithms', 'B', 78),
('Chloe', 'Data Structures', 'A', 92),
('Christopher', 'Computer Architecture', 'C', 73),
('Samantha', 'Operating Systems', 'B', 80),
('Jackson', 'Networking', 'A', 90),
('Abigail', 'Database Systems', 'C', 76),
('David', 'Software Engineering', 'B', 89),
('Elizabeth', 'Artificial Intelligence', 'A', 98),
('Logan', 'Machine Learning', 'C', 71),
('Sarah', 'Computer Graphics', 'B', 84),
('Joseph', 'Web Development', 'A', 97),
('Emily', 'Mobile Development', 'C', 75),
('Gabriel', 'Game Development', 'B', 86),
('Luna', 'Cybersecurity', 'A', 95),
('William', 'Cloud Computing', 'C', 70);

""")

## Display all records
print("The inserted records are")
data = cursor.execute("SELECT * FROM STUDENT")

for row in data:
    print(row)

## CLose the connection
connection.commit()
connection.close()
