from dataclasses import dataclass

# attraverso questa annotazione va a creare un costruttore con tutti i parametri (init)
# repr offre la possibilità di stampare un oggetto con determinati attrabuti
# order fornisce la possibilità di confrontare due instanze della stessa classe
# frozen non permette di cambiare i valori dell'instanza dopo la costruzione dell'oggetto
@dataclass(init=True, repr=True, order=True, frozen=False)
class Strada:
    numero:int
    nome:str
    CAP:int

@dataclass(init=True, repr=True, order=True, frozen=False)
class Casa:
    nome:str
    via: Strada
    categoria:str
    prezzo:int

# le annotazioni di tipo possono servire per dare la possibilità
# all'ide di verificare i valori inseriti e aiutarci
# inoltre rendono il codice più leggibile
def somma(a:int, b:int, c:int, d:int) -> int:
    return a + b + c + d    

# attraverso questo metodo possiamo ottenere i tipi dei parametri e del valore di ritorno
# così è possibile fare una dobbia verifica
print(somma.__annotations__.get('return')) # alla fine ritorna un dizionario
print(somma.__annotations__)
miaCasa = Casa("mia", Strada(2,"Alfredo",12345), "C2",180000)
print(miaCasa)