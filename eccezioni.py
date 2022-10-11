
def div(a,b):
    return a // b

def interupt():
    return div(4,0)

def main():
    c = 0
    while c != 1:
        try:
            a = input("inserisci un numero\n")
            b = input("inserisci un numero\n")
            c = div(int(a),int(b))
        except ZeroDivisionError as e:
            print(f"Divisione per zero --> {e}")
        else:
            print(f"risultato divisione: {c}")
    # in caso che un funzionalità non venga gestita con questo costrutto allora
    # termina l'esecuzione del programma  
    d = div(4,0)

main()