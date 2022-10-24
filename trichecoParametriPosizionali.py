def sottr(a:int,b:int,c:int) -> int:
    return a-b-c

# quando definisco una funzione e la richiamo
# posso assegnare i parametri con l'ordine a mio piacimento
# rispetto alla prima definizione 
print (sottr(10,10,20))
print (sottr(a=10,c=10,b=20))
print (sottr(b=10,c=10,a=20))

# per evitare che questo succeda oppure limitarlo posso mettere una / 
# nella definizione della funzione per dividere i parametri posizionali
# da quegli altri
def sottr(a:int,/,b:int,c:int) -> int:
    return a-b-c
# un operazione del genere non me la fa fare perchè ho dichiarato che il
# parametro a sarà sempre nella prima posizione dei parametri
# print (sottr(a=10,c=10,b=20))
print (sottr(10,c=10,b=20))


# questa è una cosa molto più particolare
# perché l'operatore := tricheco mi offre la possibilità di fare
# un assegnamento all'interno di un'altra operazione
# come in questo caso posso assegnare il valore della variabile a con 10
# e poi passarla e farci altre cose
print (sottr(a:=10,c=a,b=20))
print (sottr(a:=5,a*2,a*4))
list = [n for n in range(10) if n%2==0]
print()
for i in list:
    if((n:= i) > 3):
        print("valore:",n)
