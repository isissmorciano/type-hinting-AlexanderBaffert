#Baffert Es type-hinting-template

#inizio

import random

#es1

def descrizione(nome, eta):

    print(f"{nome} ha {eta} anni.")

descrizione(nome = "Marco", eta= "16")

#es2

def numeri_casuali(numeri):

    print(f"Il numero generato e': {numeri}")

numeri_casuali(numeri=random.randint(0,99))

#es3

def descrizione_eta_casuale(nome):
    
    eta = random.randint(11,33)
    
    print(f"{nome} ha {eta} anni.")    

descrizione_eta_casuale("Gianni")

#es4

def descrizione_casuale2(nome):
    global lista #ho dovuto usarlo perche' dava dei problemi per la lista    
        
    lista = ["Gianni", "Maria", "Marco", "Elisa"]
    
    eta = random.randint(11,33)
    
    print(f"{nome} ha {eta} anni.")

descrizione_casuale2(nome = random.choice(lista))