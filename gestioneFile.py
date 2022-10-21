from pathlib import Path

home = Path.home()
print(home)
cwd = Path.cwd()
print(cwd)
path = Path(cwd,"risorse","isolamisteriosa.txt")
print(path)
# ogni volta che devo gestire un file devo aprirlo con il path
# poi a fine di ogni elaborazione devo chiuderlo
f = open(path,"rt")
# la funzione read legge il contenuto del file
# posso inserire un argomento e quello indicherà il numero massimo di caratteri da leggere
print(f.read())
f.close()

# altrimenti posso usare pure il costrutto with
# in sostanza chiude il puntatore al file correttamente
# una volta che sono state elaborate tutte le istruzioni all'interno del with
# le modalità di apertura di un file sono
    #r per lettura
    #a per append
    #t per dire che andrò ad operare con del testo
    #b per dire che andrò ad operare con un file binario
    #w per scrittura e sovrascrittura
    #x per scrivere se un file non esiste altrimenti alza un'eccezione
with open(path,"rt") as f:
    text = f.readlines()
    print(len(text))
    print(text[3])

count = 0
with open(path,"rt") as f:
    textIt = (line for line in f.readlines())
    for line in textIt:
        print(f"{count} -> {line}")
        count = count + 1
    print(f"numero linee nel file: {count}")

count = 1
with open(path,"rt") as fr:
    path = Path(cwd,"risorse","output.txt")
    with open(path, "wt") as fw:
        text = fr.readlines()
        for line in text:
            if(count%2==1):
                fw.write(f"{count}: {line}")
            count += 1