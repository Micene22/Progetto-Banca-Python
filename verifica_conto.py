from conto_bancario import ContoBancario

def verifica(conti):
    print("\n====Verifica Saldo=====")

    id_inserito= input("\n Inserisci il tuo ID")

    if id_inserito in conti:
        conto_trovato: ContoBancario= conti[id_inserito] #per aiutare con l'editor ma capire il perchè
        print(f"Utente trovato: {conto_trovato.nome}")
        print(f"Il tuo saldo attuale è di: {conto_trovato.saldo} €")
    else:
        print("Errore: Nessun conto trovato con questo ID. Riprova.")