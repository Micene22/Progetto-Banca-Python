# Creo un DB con PhpMyAdmin
import mysql.connector
from mysql.connector import Error

def connetti_db():
    try:
        connessione = mysql.connector.connect(
            host='localhost',
            database='banca_python',
            user='root',
            password='root',
            port=8889
        )

        if connessione.is_connected():
            print("🟢 SUCCESS: Connesso al database 'banca_Micene'!")
            return connessione
            
    except Error as e:
        print(f"🔴 ERRORE: Impossibile connettersi al database. Dettagli: {e}")
        return None

if __name__ == "__main__":
    connetti_db()