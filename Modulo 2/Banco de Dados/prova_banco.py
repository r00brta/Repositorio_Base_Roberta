import sqlite3
banco = sqlite3.connect('escola.db')
cursor = banco.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS Alunos (id INTEGER PRIMARY KEY AUTOINCREMENT, Nome text, Idade integer, Email text)")
#cursor.execute("INSERT INTO Alunos (Nome, Idade, Email) VALUES ('Renata', 16, 'renata@gmail.com')")
#cursor.execute("INSERT INTO Alunos (Nome, Idade, Email) VALUES ('Felipe', 17, 'felipe@gmail.com')")
#cursor.execute("INSERT INTO Alunos (Nome, Idade, Email) VALUES ('Larisa', 15, 'larissa@gmail.com')")

#banco.commit()

#cursor.execute("SELECT * FROM Alunos")
#cursor.execute("SELECT * FROM Alunos WHERE id = 2")
#cursor.execute("UPDATE Alunos SET Nome = 'Ana' WHERE id = 2")
#banco.commit()
#cursor.execute("DELETE FROM Alunos WHERE id = 3")
#banco.commit()
print(cursor.fetchall())