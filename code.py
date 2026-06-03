import sqlite3

Roll_no = int(input("Enter your roll_no:"))
Name = input("Enter your name:")
Sub1 = int(input("Enter sub1 marks:"))
Sub2 = int(input("Enter sub2 marks:"))
Sub3 = int(input("Enter sub3 marks:"))

if Sub1 > 100 or Sub2 > 100 or Sub3 > 100:
    print("Marks cannot be greater than 100")
else:
    total = Sub1+Sub2+Sub3
    percentage = (total)/3

    if percentage >= 90:
        grade = "A+"
    
    elif percentage >= 75:
        grade = "A"

    elif percentage >= 60:
        grade = "B"

    elif percentage >= 40:
        grade = "C"

    else:
        grade = "Fail"



print("\n----- STUDENT RESULT -----")
print("Roll No :", Roll_no)
print("Name :", Name)
print("Total Marks :", total)
print("Percentage :", percentage)
print("Grade :", grade)

conn = sqlite3.connect("student.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
    roll_no INTEGER PRIMARY KEY,
    name TEXT,
    sub1 INTEGER,
    sub2 INTEGER,
    sub3 INTEGER,
    total INTEGER,
    percentage REAL,
    grade TEXT
)
""")

try:
    cursor.execute("""
    INSERT INTO students
    (roll_no,name,sub1,sub2,sub3,total,percentage,grade)
    VALUES (?,?,?,?,?,?,?,?)
    """,
    (Roll_no, Name, Sub1, Sub2, Sub3, total, percentage, grade))

    conn.commit()
    print("Record inserted successfully")

except sqlite3.IntegrityError:
    print("This Roll Number already exists")
    
    
choice = input("\n Do you want to search a student record?(yes/no):")

if choice.lower() == "yes":
    search_roll = int(input("Enter Roll_no to search:"))
    
    cursor.execute(
        "SELECT*FROM students WHERE roll_no=?",(search_roll,)
    )
    record = cursor.fetchone()
    
    if record:
        print("\n----- STUDENT RECORD -----")
        print("Roll No :", record[0])
        print("Name :", record[1])
        print("Sub1 :", record[2])
        print("Sub2 :", record[3])
        print("Sub3 :", record[4])
        print("Total :", record[5])
        print("Percentage :", record[6])
        print("Grade :", record[7])
    else:
        print("Student not found")

else:
    print("Thank You!")

conn.close()

