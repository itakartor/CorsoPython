
numbers = [1,2,3,4,5,6,7,8,9]

# creato un generatore che mi prende i numeri dispari e li eleva al quadrato
gen = (n*n for n in numbers if n%2== 1)

def funzioneGen():
    for i in numbers:
        if(i%2==1):
# la parola chiave yield mette a disposizione il valore fuori dalla funzione
            yield i*i

print("prima scrittura")
for i in gen:
    print(i)
# scrivo due volte per far notare che scriverà solo la prima
# perché il generatore o una funzione generatore fornisce una sola lettura
# è come se avesse solo il numero successivo ed una volta finiti non ne ha più
print("seconda scrittura")
for i in gen:
    print(i)

print("terza scrittura con funzione")
gen2 = funzioneGen()
for i in gen2:
    print(i)
