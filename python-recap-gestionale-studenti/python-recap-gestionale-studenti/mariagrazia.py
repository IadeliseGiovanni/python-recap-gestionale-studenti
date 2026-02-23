def inserisci():
    nome=input('inserire corso')
    corso=input('inserire nome')
    with open("studenti.csv","a") as file:
        riga= nome + ',' + corso + '\n'
        file.write(riga)
        print(riga,'aggiunta con successo')

def leggifile():
    with open("studenti.txt", "r") as file:
        lista_righe = file.readlines() #legge il file etrasforma ogni riga in una lista
    return lista_righe
def modifica():
    nome_da_modificare=input('inserire nome da modificare')
    corso_da_modificare=input('inserire corso da modificare')
    with open("studenti.csv","a") as file:
        riga= nome_da_modificare + ',' + corso_da_modificare + '\n'
        file.write(riga)
        print(riga,'modificato con successo')

def ordina():
    lista_righe=lista_righe.sort(key=lambda x: x[1])
    return lista_righe
