from database_db.database import connetti_db

def verifica():
    print("\n====Verifica Saldo=====")

    id_inserito= input("\n Inserisci il tuo ID ")

    connessione = connetti_db()

    if connessione:
        try:
            cursor = connessione.cursor()
            query = "SELECT nome_titolare, saldo FROM conti WHERE id_conto = %s"
            cursor.execute(query, (id_inserito,))

            risultato = cursor.fetchone()

            if risultato:
                nome, saldo = risultato
                print(f"\n--- Riepilogo Conto ---")
                print(f"Titolare: {nome}")
                print(f"Saldo Attuale: {saldo} €")
            else:
                print(f"Errore: Nessun conto trovato con l'ID {id_inserito}")

        except Exception as e:
            print(f" Errore durante la lettura: {e}")

        finally:
            cursor.close()
            connessione.close()