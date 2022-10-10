class Conto:
    def __init__(self, nome, conto) -> None:
        self.nome = nome
        self.conto = conto
    
class ContoCorrente(Conto):

    def __init__(self, nome, conto, importo) -> None:
        super().__init__(nome,conto)
        self.__saldo = importo
    
    @property
    def saldo(self):
        return self.__saldo
    @saldo.setter
    def saldo(self,importo):
        self.__saldo = importo

    def preleva(self,importo):
        self.saldo -= importo
    def deposita(self,importo):
        self.saldo += importo
    def descrizione(self):
        print(f" nome: {self.nome} \n \
            conto: {self.conto} \n \
            saldo: {self.saldo}\n")

class GestoreConti:
    
    @staticmethod
    def bonifico(a: ContoCorrente,b: ContoCorrente, importo):
        transazione = importo
        a.saldo -= transazione
        b.saldo += transazione

conto1 = ContoCorrente("pippo","BNL",100)
conto2 = ContoCorrente("paperino","Intesa Sanpaolo", -50)

conto1.descrizione()
conto2.descrizione()

GestoreConti.bonifico(conto1,conto2,50)

conto1.descrizione()
conto2.descrizione()
