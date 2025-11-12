import sqlite3
banco = sqlite3.connect('fabrica_programadores.db')
cursor = banco.cursor()

#cursor.execute("CREATE TABLE Alunos (id INTEGER PRIMARY KEY AUTOINCREMENT,nome Text,idade INTEGER,cidade TEXT)")
# cursor.execute("INSERT INTO Alunos (nome, idade, cidade) VALUES ('Isabelle Luísa', 16, 'Itapevi')")
# cursor.execute("INSERT INTO Alunos (nome, idade, cidade) VALUES ('Arthur Félix', 16, 'Rio de Janeiro')")
# cursor.execute("INSERT INTO Alunos (nome, idade, cidade) VALUES ('Roberta Mikaelly', 15, 'Guarulhos')")
# cursor.execute("INSERT INTO Alunos (nome ,idade, cidade) VALUES ('Davi Antenor', 16, 'Rio Grande do Sul')")
# cursor.execute("INSERT INTO Alunos (nome, idade, cidade) VALUES ('Ezequiel', 15, 'São Paulo')")
# cursor.execute("INSERT INTO Alunos (nome, idade, cidade) VALUES ('Gustavo Souza', 16, 'Osasco')")
# cursor.execute("INSERT INTO Alunos (nome, idade, cidade) VALUES ('Isáac', 15, 'Barueri')")
# cursor.execute("INSERT INTO Alunos (nome, idade, cidade) VALUES ('José', 15, 'Osasco')")
# cursor.execute("INSERT INTO Alunos (nome, idade, cidade) VALUES ('Juan Pedro', 15, 'Carapicuíba')")
# cursor.execute("INSERT INTO Alunos (nome, idade, cidade) VALUES ('Kaua Vinícius', 15, 'Pernambuco')")
# cursor.execute("INSERT INTO Alunos (nome, idade, cidade) VALUES ('Kethleen', 16, 'Minas Gerais')")
# cursor.execute("INSERT INTO Alunos (nome, idade, cidade) VALUES ('Pedro Henrique', 15, 'Barueri')")
# cursor.execute("INSERT INTO Alunos (nome, idade, cidade) VALUES ('Rebeca', 16, 'Cururuquára')")
# cursor.execute("INSERT INTO Alunos (nome, idade, cidade) VALUES ('Vitória', 16, 'Barueri')")
# cursor.execute("INSERT INTO Alunos (nome, idade, cidade) VALUES ('Stefany', 15, 'Barueri')")
# cursor.execute("INSERT INTO Alunos (nome, idade, cidade) VALUES ('Gustavo Alessandro', 16, 'Barueii')")
# cursor.execute("INSERT INTO Alunos (nome, idade, cidade) VALUES ('Maisa', 16, 'Osasco')")
# 
#cursor.execute("CREATE TABLE Professores (id INTEGER PRIMARY KEY AUTOINCREMENT, nome text, idade INTEGER, cidade TEXT)")
#cursor.execute("INSERT INTO Professores (nome, idade, cidade) VALUES ('Ricardo', 25, 'São Paulo')")


#cursor.execute("CREATE TABLE Cursos (id INTEGER PRIMARY KEY AUTOINCREMENT,nome text, carga_horaria integer, preco REAL)")
#cursor.execute("INSERT INTO Cursos (nome, carga_horaria, preco) VALUES ('Python', 100, 600.00)")
#cursor.execute("INSERT INTO Cursos (nome, carga_horaria, preco) VALUES ('Java', 120, 1500.00)")
#cursor.execute("INSERT INTO Cursos (nome, carga_horaria, preco) VALUES ('HTML', 200, 900.00)")
#cursor.execute("INSERT INTO Cursos (nome, carga_horaria, preco) VALUES ('CSS', 140, 1000.00)")
#cursor.execute("INSERT INTO Cursos (nome, carga_horaria, preco) VALUES ('Programacao de computador avancado', 600, 5000.00)")
#cursor.execute("INSERT INTO Cursos (nome, carga_horaria, preco) VALUES ('Banco de dados', 90, 200.00)")
#banco.commit()

cursor.execute("CREATE TABLE Matricula (id INTEGER PRIMARY KEY AUTOINCREMENT, id_aluno INTEGER, id_curso INTEGER, data TEXT, FOREIGN KEY (id_aluno) REFERENCES Alunos (id), FOREIGN KEY (id_curso) REFERENCES Cursos (id))")
banco.commit()


# cursor.execute("SELECT cidade FROM alunos")
# cursor.execute("SELECT carga_horaria >=40 FROM Cursos")

# print(cursor.fetchall())