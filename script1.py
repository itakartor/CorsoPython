import sys
sys.path.append(r"moduli")
# devo aggiungere il path realtivo o quello assoluto della cartella dei moduli

import modulo1

print(modulo1.sum(2,3))

# serve per vedere i path dove sono presenti 
# le cartelle dove poter mettere moduli
# import sys
# for i in sys.path:
#     print(i)