class Utente:
    def __init__(self):
        self.nome_loggato = None
        self.password_loggata = None

class Admin(Utente):
    def init(self,nome_loggato):
        self.nome_loggato=nome_loggato
        super().init()
    def reset(self):
        with open("studenti.txt", "w") as file:
            file.write("") #sovrascrive con il vuoto
    def intervento_utente():
        motivazione=input('inserire motivazione reset')
        with open("sintervento_utente.txt", "w") as file:
            file.write(motivazione)

    # PUNTO 2 e 3: Registrazione gestita dalla classe
    def registrazione(self):
        nome = input("Scegli un nome utente: ")
        password = input("Scegli una password: ")
        with open("credenziali.txt", "a") as file:
            file.write(nome + "\n")
            file.write(password + "\n")
        print("Registrazione completata!")

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

# ESECUZIONE DEL PROGRAMMA (Il Main richiama solo la classe)

def main():
    # Creiamo un'unica istanza (oggetto) della classe Utente
    sistema = Utente()

    while True:
        print("\n--- BENVENUTO ---")
        print("1. Registrati")
        print("2. Login")
        print("3. Esci")
        scelta = input("Cosa vuoi fare? ")

        if scelta == "1":
            sistema.registrazione()

        elif scelta == "2":
            if sistema.login():
                print(f"\nLogin OK! Benvenuto {sistema.nome_loggato}.")
                
                # PUNTO 4: Sotto-menu operativo
                while True:
                    print(f"\n--- AREA RISERVATA ({sistema.nome_loggato}) ---")
                    print("1. Aggiungi studente (Giovanni)")
                    print("2. Stampa aula ordinata (Mariagrazia)")
                    print("3. Logout")
                    scelta_interna = input("Scegli: ")

                    if scelta_interna == "1":
                        sistema.inserisci_studente()
                    elif scelta_interna == "2":
                        sistema.ordina_e_stampa()
                    elif scelta_interna == "3":
                        break
            else:
                print("Accesso negato.")

        elif scelta == "3":
            print("Arrivederci!")
            break

if __name__ == "__main__":
    main()