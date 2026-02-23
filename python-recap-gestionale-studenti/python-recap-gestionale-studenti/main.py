class Utente:
    def __init__(self):
        self.nome_loggato = None
        self.password_loggata = None

    # PUNTO 2 e 3: Registrazione gestita dalla classe
    def registrazione(self):
        nome = input("Scegli un nome utente: ")
        password = input("Scegli una password: ")
        with open("credenziali.txt", "a") as file:
            file.write(nome + "\n")
            file.write(password + "\n")
        print("Registrazione completata!")

    def modifica(self):
        nome_da_modificare = input('inserire nome da modificare: ')
        corso_da_modificare = input('inserire corso da modificare: ')
        with open("studenti.csv", "a") as file:
            riga = nome_da_modificare + ',' + corso_da_modificare + '\n'
            file.write(riga)
            print(riga, 'modificato con successo')

    # PUNTO 1: Login che salva il nome nell'oggetto
    def login(self):
        nome_login = input("Inserisci il tuo nome utente: ")
        pass_login = input("Inserisci la tua password: ")
        try:
            with open("credenziali.txt", "r") as file:
                righe = file.readlines()
                for i in range(0, len(righe), 2):
                    if i + 1 < len(righe):
                        user_salvato = righe[i].strip()
                        pass_salvato = righe[i+1].strip()
                        if user_salvato == nome_login and pass_salvato == pass_login:
                            self.nome_loggato = user_salvato
                            self.password_loggata = pass_salvato 
                            return True
        except FileNotFoundError:
            print("Errore: Nessun database utenti trovato.")
        return False

    # PUNTO 5: Gestione Studenti (Inserimento)
    def inserisci_studente(self):
        nome = input('Nome studente: ')
        corso = input('Corso: ')
        with open("studenti.csv", "a") as file:
            file.write(nome + "," + corso + "\n")
        print(f"Studente {nome} aggiunto!")

    # PUNTO 6: Lettura e Ordinamento (Mariagrazia)
    def ordina_e_stampa(self):
        try:
            with open("studenti.csv", "r") as file:
                righe = file.readlines()
            
            if not righe:
                print("L'aula è vuota.")
                return

            studenti = [r.strip().split(",") for r in righe]
            studenti.sort(key=lambda x: x[1]) # Ordina per corso

            print("\n--- ELENCO AULA ORDINATO ---")
            for s in studenti:
                print(f"Studente: {s[0]} | Corso: {s[1]}")
        except FileNotFoundError:
            print("File studenti non trovato.")

            
class Admin(Utente):
    def __init__(self): # Corretto: rimosso argomento obbligatorio e messi doppi underscore
        super().__init__() 
        
    def reset(self):
        with open("studenti.csv", "w") as file: # Coerente con .csv
            file.write("") # sovrascrive con il vuoto
        print("Reset eseguito.")

    def intervento_utente(self): # Aggiunto self
        motivazione = input('inserire motivazione reset: ')
        with open("sintervento_utente.txt", "w") as file:
            file.write(motivazione)
        print("Motivazione salvata.")

# ESECUZIONE DEL PROGRAMMA (Il Main richiama solo la classe)

def main():
    # Creiamo un'unica istanza (oggetto) della classe Utente
    sistema = Utente()
    admin = Admin() # Ora non darà più errore

    while True:
        print("\n--- BENVENUTO ---")
        print("1. Registrati")
        print("2. Login")
        print("3. Esci")
        scelta = input("Cosa vuoi fare? ")

        if scelta == "1":
            sistema.registrazione()

        elif scelta == "2":
            x = input("vuoi fare login come utente o come admin: ")
            if x == "utente":
                if sistema.login():
                    print(f"\nLogin OK! Benvenuto {sistema.nome_loggato}.")
                    
                    # PUNTO 4: Sotto-menu operativo
                    while True:
                        print(f"\n--- AREA RISERVATA ({sistema.nome_loggato}) ---")
                        print("1. Aggiungi studente")
                        print("2. Modifica Studente")
                        print("3. Stampa aula ordinata")
                        print("4. Logout")
                        scelta_interna = input("Scegli: ")

                        if scelta_interna == "1":
                            sistema.inserisci_studente()
                        elif scelta_interna == "2":
                            sistema.modifica()
                        elif scelta_interna == "3":
                            sistema.ordina_e_stampa()
                        elif scelta_interna == "4":
                            break
                else:
                    print("Login fallito.")

            elif x == "admin":
                y = input("vuoi resettare? Si / No: ") # Aggiunto input()
                if y == "Si": 
                    if admin.login(): # Richiede login admin prima di resettare
                        admin.reset()
                        admin.intervento_utente() 
                else:
                    print("Operazione annullata.")
            else:
                print("Accesso negato.")

        elif scelta == "3":
            print("Arrivederci!")
            break

if __name__ == "__main__":
    main()