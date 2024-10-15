import sqlite3

# Conectando ao banco de dados
conexao = sqlite3.connect("meu_banco.db")
cursor = conexao.cursor()

# Criando uma tabela
cursor.execute("CREATE TABLE IF NOT EXISTS pessoas (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER)")

# Inserindo dados
cursor.execute("INSERT INTO pessoas (nome, idade) VALUES (?, ?)", ("Vitor", 20))
cursor.execute("INSERT INTO pessoas (nome, idade) VALUES (?, ?)", ("San", 22))
conexao.commit()

# Consultando dados
cursor.execute("SELECT * FROM pessoas")
pessoas = cursor.fetchall()
print("Pessoas:", pessoas)

# Fechando a conexão
conexao.close()
