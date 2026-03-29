from database_db.database import connetti_db


def esegui_deposito():
    print("\n ==== DEPOSITO ==== ")
    
    id_inserito= input ("\n Inserisci il tuo ID ")

    connessione = connetti_db()

    if connessione:
        try:
            cursor = connessione.cursor()
            
            query_select = "SELECT nome_titolare, saldo FROM conti WHERE id_conto = %s"
            cursor.execute(query_select, (id_inserito,))
            risultato = cursor.fetchone()
            
            if risultato:
                nome, saldo_attuale = risultato
                print(f"Salve {nome}, il saldo attuale è: {saldo_attuale} €")
                
                importo = float(input("Quanto vuoi depositare? "))
                
                if importo > 0:
                    nuovo_saldo = float(saldo_attuale) + importo
                    
                    query_update = "UPDATE conti SET saldo = %s WHERE id_conto = %s" #sempre la queri che richiama il DB
                    cursor.execute(query_update, (nuovo_saldo, id_inserito))
                    
                    # Conferma modifica
                    connessione.commit()
                    
                    print(f"✅ Deposito completato! Nuovo saldo: {nuovo_saldo} €")
                else:
                    print("❌ L'importo deve essere maggiore di zero.")
            else:
                print(f"❌ Errore: Nessun conto trovato con l'ID {id_inserito}")
                
        except ValueError:
            print("❌ Errore: Inserisci un numero valido per l'importo.")
        except Exception as e:
            print(f"❌ Errore durante l'operazione: {e}")
        finally:
            cursor.close()
            connessione.close()