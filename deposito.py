from conto_bancario import ContoBancario

def esegui_deposito(conti):
    print("\n ==== DEPOSITO ==== ")
    
    id_inserito= input ("\n Inserisci il tuo ID ")

    if id_inserito in conti:
        conto_trovato: ContoBancario = conti[id_inserito]
        print(f"Ciao {conto_trovato.nome}! Il tuo saldo attuale è: {conto_trovato.saldo} €")

    try: 
        importo_da_versare= float(input("Quanto vuoi Depositare? "))

        if importo_da_versare > 0:
            conto_trovato.saldo += importo_da_versare
            print(f"\nOperazione completata! Hai depositato {importo_da_versare} €.")
            print(f"Il tuo NUOVO SALDO è: {conto_trovato.saldo} €")
        else:
            print("\n Valore NON VALIDO per il Deposito")
    except ValueError:
        print("\n INSERISCI SOLO VALORI NUMERICI")
    
    else:
        print("Errore: Nessun conto trovato con questo ID. Riprova.")
