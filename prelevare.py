from conto_bancario import ContoBancario

def esegui_prelievo(conti):
    print("\n ==== PRELEVA ==== ")
    
    id_inserito= input ("\n Inserisci il tuo ID ")

    if id_inserito in conti:
        conto_trovato: ContoBancario = conti[id_inserito]
        print(f"Ciao {conto_trovato.nome}! Il tuo saldo attuale è: {conto_trovato.saldo} €")

        try: 
            importo_da_prelevare= float(input("Quanto vuoi Prelevare? "))

            if 0 < importo_da_prelevare <= conto_trovato.saldo:
                conto_trovato.saldo -= importo_da_prelevare #aggiunto funzione per il calcolo matematico della sottrazione
                print(f"\nOperazione completata! Hai prelevato {importo_da_prelevare} €.")
                print(f"Il tuo NUOVO SALDO è: {conto_trovato.saldo} €")

            elif importo_da_prelevare > conto_trovato.saldo:
                print("Errore: Fondi insufficienti. Non hai abbastanza soldi sul conto!")
            else:
                print("Errore: L'importo deve essere maggiore di zero.")
                    
        except ValueError:
            print("Errore: Devi inserire un numero valido. Operazione annullata.")
    else:
        # Questo scatta se l'ID inserito all'inizio non esiste
        print("Errore: Nessun conto trovato con questo ID. Riprova.")
            
