class MyClass():
    def __new__(cls, name, surname):
        print(" sto costruendo \n")
        istanza = super().__new__(cls)
        print(f"{istanza}\n")
        return istanza

    def __init__(self, name, surname):
        print(" ho inizializzato \n")
        self.name = name
        self.surname = surname
    def desc(self):
        print(f"{self.name} {self.surname}\n")

myclass = MyClass("carmine", "vitiello")
myclass.desc()