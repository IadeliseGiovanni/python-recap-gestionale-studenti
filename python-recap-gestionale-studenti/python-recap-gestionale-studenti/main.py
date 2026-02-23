def registrazione():
    #PUNTO 2: L'utente inserisce i dati per crearsi un account
    nome = input("Scegli un nome utente: ")
    password = input("Scegli una password: ")
    
    # PUNTO 3: I dati vengono salvati nel file (uno per riga)
    with open("credenziali.txt", "a") as file:
        file.write(nome + "\n")
        file.write(password + "\n")
    print("Registrazione completata!")

def login():
    # PUNTO 1 L'utente inserisce i dati per entrare
    nome_login = input("Inserisci il tuo nome utente: ")
    pass_login = input("Inserisci la tua password: ")
    
    with open("credenziali.txt", "r") as file:
        righe = file.readlines()
        for i in range(0, len(righe), 2):
            # Controllo sicurezza: verifica che ci siano abbastanza righe nel file
            if i + 1 < len(righe):
                user_salvato = righe[i].strip()
                pass_salvato = righe[i+1].strip()
                if user_salvato == nome_login and pass_salvato == pass_login:
                    return True
    return False

def ins_mod_studenti():
    #PUNTO 5: Una volta dentro,  gestisce il file degli studenti
    print("\n--- GESTIONE STUDENTI ---")
    print("1. Aggiungi studente")
    print("2. Modifica (Sovrascrivi)")
    scelta = input("Scegli: ")
    
    if scelta == "1":
        nome = input("Nome studente: ")
        corso = input("CORSO: ")
        with open("studenti.csv", "a") as file:
            file.write(nome + "," + corso + "\n")
        print("Studente aggiunto con successo!")
    
    elif scelta == "2":
        nome = input("Nuovo nome: ")
        corso = input("Nuovo corso: ")
        with open("studenti.csv", "w") as file:
            file.write(nome + "," + corso + "\n")
        print("Lista aggiornata (Punto 5 completato)!")

# --- ESECUZIONE DEL PROGRAMMA ---

def main():
    #PUNTO 1  Il sistema che continua a girare finché non esci
    while True:
        print("\n--- BENVENUTO ---")
        print("1. Registrati")
        print("2. Login")
        print("3. Esci")
        scelta = input("Cosa vuoi fare? ")
        
        if scelta == "1":
            registrazione()
            
        elif scelta == "2":
            if login():
                print("\nLogin OK! Benvenuto nel sistema.")
                
                
                # QUI INIZIA IL PUNTO 4: Menu per utente loggato       
                '''---------------------------------------------'''
                 
                while True:
                    print("\n--- AREA RISERVATA (Punto 4) ---")
                    print("1. Inserisci o Modifica studenti (Task Giovanni)")
                    print("2. Stampa l'aula ordinata (Task Mariagrazia)")
                    print("3. Logout")
                    scelta_interna = input("Scegli un'opzione: ")
                    
                    if scelta_interna == "1":
                        ins_mod_studenti() # Richiama il tuo PUNTO 5
                        
                    elif scelta_interna == "2":
                        # Qui Mariagrazia collegherà il suo PUNTO 6
                        print("Funzione Stampa Aula di Mariagrazia in caricamento...")
                        
                    elif scelta_interna == "3":
                        print("Ritorno al menu principale...")
                        break # Esce dal Punto 4 e torna al menu di Benvenuto
            else:
                print("Credenziali non valide.")
                
        elif scelta == "3":
            print("Arrivederci!")
            break

main()