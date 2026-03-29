import random
from database_db.database import connetti_db

def crea_utente_conto():
    print("CREAZIONE NUOVO CONTO")
    nome = input("\nINSERISCI l'INTESTATARIO DEL CONTO ")
    id_conto= str(random.randint(100,999))
    saldo_iniziale = 1000 

    connessione= connetti_db()
        

    if connessione:
        try:
            cursor = connessione.cursor()
            query = "INSERT INTO conti (id_conto, nome_titolare, saldo) VALUES (%s, %s, %s) "
            valori = (id_conto, nome, saldo_iniziale)

            cursor.execute (query, valori)
            connessione.commit()

            print(f"\nConto creato con successo! Benvenuto {nome}.")
            print(f"IL TUO NUMERO IDENTIFICATIVO (ID) ASSEGNATO È: {id_conto}")
            print("Conservalo con cura, ti servirà per le prossime operazioni!")
        except Exception as e:
            print(f"ERRORE DURANTE LA CREAZIONE{e}: ")
        finally:
            cursor.close()
            connessione.close()
    else:
        print("🔴 Errore: Impossibile collegarsi al database. Riprova più tardi.")

