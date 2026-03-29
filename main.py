import crea_utente
import verifica_conto
import deposito
import prelevare

def avvia_banca():
    conti = {} 
    
    while True:
        print("\n--- BENVENUTO NELLA BANCA M.I.C.E.N.E ---")
        print("1. Crea utente")
        print("2. Verifica conto")
        print("3. Deposita")
        print("4. Ritira")
        print("5. Chiudi")
        
        scelta = input("Seleziona un'opzione (1-5): ")
        
        # Sostituiamo gli if/elif con match/case
        match scelta:
            case '1':
                print("Hai scelto: Crea utente.")
                crea_utente.crea_utente_conto(conti)
            case '2':
                print("Hai scelto: Verifica conto.")
                verifica_conto.verifica(conti)
            case '3':
                print("Hai scelto: Deposita.")
                deposito.esegui_deposito(conti)
            case '4':
                print("Hai scelto: Ritira.")
                prelevare.esegui_prelievo(conti)
            case '5':
                print("Grazie per aver usato la Banca M.I.C.E.N.E")
                break 
            case _: 
                print("Scelta non valida. Riprova.")

# Avvia il programma
if __name__ == "__main__":
    avvia_banca()