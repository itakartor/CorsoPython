class ContoCorrente:

    def __init__(self, nome, conto, importo) -> None:
        self.nome = nome
        self.conto = conto
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

conto1 = ContoCorrente("pippo","BNL",100)
conto2 = ContoCorrente("paperino","Intesa Sanpaolo", -50)

conto1.descrizione()
conto1.preleva(20)
conto1.descrizione()
conto1.preleva(50) # li da a paperino
conto2.descrizione()
conto2.deposita(50)
conto1.descrizione()
conto2.descrizione()
