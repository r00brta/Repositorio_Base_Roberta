import sqlite3

biblioteca1 = sqlite3.connect('biblioteca.db')

cursor = biblioteca1.cursor()

#cursor.execute("CREATE TABLE biblioteca(Autores text, Livros text, Alunos text, Empréstimos date)")

cursor.execute("INSERT INTO biblioteca VALUES('Peneloppe Douglas','Corrupt','Mika', '20/10')")
cursor.execute("INSERT INTO biblioteca VALUES('Larissa Abreu','Judas','Isa', '2/12')")
cursor.execute("INSERT INTO biblioteca VALUES('JK.Rowling','Harry Potter', 'Manu', '25/11')")
cursor.execute("INSERT INTO biblioteca VALUES('Larissa Abreu','Anticristo','Mika', '23/12')")
cursor.execute("INSERT INTO biblioteca VALUES('leonor Carvalho','Incipt','Isa', '25/12')")

biblioteca1.commit()

cursor.execute("SELECT * FROM biblioteca")
print(cursor.fetchall())

