import mysql.connector
import pandas as pd

# Conexão do meu Banco de dados
def conectar_banco():
    try:
        cns = mysql.connector.connect(
            user='root', 
            password='enzoeric',
            host='localhost',
            database='acoes'
        )
        mycursor = cns.cursor()
        return cns, mycursor
    
    except mysql.connector.Error as err:
        print(f"Erro na conexão com o Banco de Dados: {err}")
        return None, None

# Criação do DataBase
def criar_database(cns,mycursor):
    try:
        mycursor.execute("CREATE DATABASE IF NOT EXISTS acoes")
        # print("Banco de dados 'acoes' criado ou já existente.")
        mycursor.execute("USE acoes")
        # print("Usando o banco de dados 'acoes'.")
    except mysql.connector.Error as err:
        print(f"Erro ao criar ou selecionar o banco: {err}")


# Criacao das minhas tabelas
def criar_tabelas(cns, mycursor):
    try:
        # Criar a tabela `ativos`
        mycursor.execute("""
            CREATE TABLE IF NOT EXISTS ativos (
                id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                Ticker VARCHAR(50) NOT NULL,
                Ticker_id INT NOT NULL UNIQUE
            )
        """)
        # print("Tabela 'ativos' criada ou já existente.")

        # Criar a tabela `historico`
        mycursor.execute("""
            CREATE TABLE IF NOT EXISTS historico (
                id INT NOT NULL AUTO_INCREMENT PRIMARY KEY,
                Date VARCHAR(200) NOT NULL,
                Open DECIMAL(10,2) NOT NULL,
                High DECIMAL(10,2) NOT NULL,
                Low DECIMAL(10,2) NOT NULL,
                Close DECIMAL(10,2) NOT NULL,
                Ativo_id INT NOT NULL,
                FOREIGN KEY (Ativo_id) REFERENCES ativos(Ticker_id)
            )
        """)
        # print("Tabela 'historico' criada ou já existente.")
    except mysql.connector.Error as err:
        print(f"Erro ao criar as tabelas: {err}")


# BUILDING -------------------------------
def obter_dados(cns):
    try:
        query = "SELECT * FROM historico"
        df = pd.read_sql(query, con=cns) # Aqui o pandas está lendo meu DB, estou passando parâmetro e conexão
        return df
    
    except Exception as e:
        print(f"Erro ao executar a consulta: {e}")
        return None
# BUILDING -------------------------------


cns, mycursor = conectar_banco()

# Executa se conexão e conector não forem None
if cns and mycursor:
    criar_database(cns, mycursor) 
    criar_tabelas(cns, mycursor)
