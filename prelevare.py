from database_db.database import connetti_db

def esegui_prelievo(): # Rimosso (conti)
    print("\n ==== PRELIEVO ==== ")
    id_inserito = input("\n Inserisci il tuo ID: ")

    connessione = connetti_db()

    if connessione:
        try:
            cursor = connessione.cursor()
            
            query_select = "SELECT nome_titolare, saldo FROM conti WHERE id_conto = %s"
            cursor.execute(query_select, (id_inserito,))
            risultato = cursor.fetchone()
            
            if risultato:
                nome, saldo_attuale = risultato
                saldo_attuale = float(saldo_attuale)
                
                print(f"Salve {nome}, il tuo saldo attuale è: {saldo_attuale} €")
                importo = float(input("Quanto vuoi prelevare? "))
                
                #Controllo disponibilità di SALDO
                if 0 < importo <= saldo_attuale:
                    nuovo_saldo = saldo_attuale - importo
                    
                  
                    query_update = "UPDATE conti SET saldo = %s WHERE id_conto = %s"
                    cursor.execute(query_update, (nuovo_saldo, id_inserito))
                    connessione.commit()
                    
                    print(f"✅ Operazione completata! Hai prelevato {importo} €.")
                    print(f"Il tuo NUOVO SALDO è: {nuovo_saldo} €")
                else:
                    print("❌ Errore: Fondi insufficienti o importo non valido.")
            else:
                print(f"❌ Errore: ID non trovato.")
                
        except ValueError:
            print("❌ Errore: Inserisci un numero valido.")
        finally:
            cursor.close()
            connessione.close()