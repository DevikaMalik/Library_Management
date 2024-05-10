import sqlite3
con = sqlite3.connect('LMS.db')
cur = con.cursor()
book=cur.execute("SELECT * FROM books").fetchall()
for i in book:
    print(i)
member =cur.execute("SELECT * from member").fetchall()
print("Members are")
for j in member:
    print(j)