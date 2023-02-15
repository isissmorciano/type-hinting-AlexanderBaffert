#Baffert Es type-hinting-template

#inizio

import random

#es1

#Creare una funzione descrizione() con due parametri nome ed eta. La funzione restituisce una stringa formattata nel seguente modo: "nome ha eta anni." descrizione("Pippo",23)

def descrizione(nome: str, eta: int):

    print(f"{nome} ha {eta} anni.")

descrizione(nome = "Marco", eta= 16)

#es2
#Creare una funzione(?) numero_casuale() che restituisce un numero casuale tra 0 e 99. La funzione restituisce il numero generato numero_casuale()

def numeri_casuali(numeri):

    print(f"Il numero generato e': {numeri}")

numeri_casuali(numeri=random.randint(0,99))

#es3
#Creare una funzione descrizione_eta_casuale() con un parametro nome. L'eta e' calcolata in modo casuale La funzione restituisce una stringa formattata nel seguente modo: "nome ha eta anni." descrizione_eta_casuale("Pippo")

def descrizione_eta_casuale(nome: str):
    
    eta = numeri_casuali()
    
    print(f"{nome} ha {eta} anni.")    

descrizione_eta_casuale("Gianni")

#es4
#Creare una funzione(?) descrizione_casuale(). Il nome e' scelto in modo casuale da una lista di nomi interna alla fuzione. L'eta e' calcolata in modo casuale La funzione restituisce una stringa formattata nel seguente modo: "nome ha eta anni." descrizione_casuale()

def descrizione_casuale2(nome):
    global lista #ho dovuto usarlo perche' dava dei problemi per la lista    
        
    lista = ["Gianni", "Maria", "Marco", "Elisa"]
    
    nome = random.choice(lista)
    
    eta = numeri_casuali()
    
    print(f"{nome} ha {eta} anni.")

descrizione_casuale2(nome, eta)
