
import datetime


class Veicolo():
    codice: int = 0
    marca = ''
    data: datetime

    # questo metodo stamperà il codice dell'ultima Veicolo
    @classmethod
    def ultimaVeicolo(cls):
        print(cls.codice)
    def __init__(self):
        Veicolo.codice += 1
        self.marca = ''
        self.data = datetime.datetime.now()
    def printClass(self):
        print(f"veicolo numero: {self.codice} \n \
        marca: {self.marca} \n \
        immatricolata il: {self.data}" )


class Macchina(Veicolo):
    nRuote = 4
    nPorte: int
    def __init__(self, nPorte=4):
        super().__init__()
        self.nPorte = nPorte
    def printClass(self):
        super().printClass()
        print(f"numero ruote: {self.nRuote} \n \
            numero porte: {self.nPorte}\n")

veicolo = Veicolo()
veicolo.marca = "mercedes"
veicolo.printClass()

macchina = Macchina(5)
macchina.marca = "ferrari"
macchina.printClass()
