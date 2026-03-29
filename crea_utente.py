import random
from conto_bancario import ContoBancario

def crea_utente_conto(conti):
    print("CREAZIONE NUOVO CONTO")
    nome = input("\nINSERISCI l'INTESTATARIO DEL CONTO ")

    while True:
        id_conto= str(random.randint(100,999))
        
        if id_conto not in conti: #not in vuol dire che non è presente
            break 
    
    nuovo_conto= ContoBancario(nome, id_conto)
    conti[id_conto] = nuovo_conto

    print(f"\nConto creato con successo! Benvenuto {nome}.")
    print(f"IL TUO NUMERO IDENTIFICATIVO (ID) ASSEGNATO È: {id_conto}")
    print("Conservalo con cura, ti servirà per le prossime operazioni!")