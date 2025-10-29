import sqlite3
 
clinica1 = sqlite3.connect('clínica.db')

cursor = clinica1.cursor()

#cursor.execute("CREATE TABLE clínica (Especialidades text, Médicos text, Consultas DATA, Pacientes text)")

cursor.execute("INSERT INTO clínica VALUES('Obstetra','Ana', '21/10/2025', 'Rebeca')")
cursor.execute("INSERT INTO clínica VALUES('Ginecologista','Sophia', '2/12/2025', 'Eduarda')")
cursor.execute("INSERT INTO clínica VALUES('Dermatologista','Isabelle', '25/11/2025', 'Mikaelly')")
cursor.execute("INSERT INTO clínica VALUES('Pediatra','Antônio','23/12/2025', 'Samira')")
cursor.execute("INSERT INTO clínica VALUES('Psiquiatra', 'Julia', '25/12/2025', 'Manuela')")

clinica1.commit()

cursor.execute("SELECT * FROM clínica")
print(cursor.fetchall())
