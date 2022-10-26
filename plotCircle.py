from pathlib import Path
from attr import dataclass
import numpy as np
import matplotlib.pyplot as plt

numberCircle = 0
cwd = Path.cwd()
print(cwd)
path = Path(cwd,"risorse","config.txt")

@dataclass
class Orologio():
    color: str 
    total: int
    colored: int
    title: str

def letturaConfig(f) -> list[Orologio]:
    dict = {}
    listaOrologi = []
    for line in f.readlines():
        if(line.startswith('##!')):
            orologio = Orologio(dict['colors'],
                int(dict['total']),int(dict['colored']),dict['title'])
            listaOrologi.append(orologio)
        if(not line.startswith('#')):
            dict[line.split()[0]] = line.split()[-1]
    # print(dict)
    return listaOrologi

def scritturaConfig(f,listaOrologi: list) -> None:
    for orologio in listaOrologi:
        f.write(f"colors = {orologio.colors}")
        f.write(f"total = {orologio.total}")
        f.write(f"colored = {orologio.colored}")
        f.write(f"title = {orologio.title}")
        f.write(f"##!")

def mypie(ax,colors,total,colored,title):
    global numberCircle
    slices = []
    for i in range(total):
        slices.append(1)
    pie_wedge_collection = ax[numberCircle].pie(slices, labeldistance=1.05)#labels=labels, autopct=make_autopct(slices))

    ax[numberCircle].set_title(title)

    numberCircle += 1
    count = 0
    for pie_wedge in pie_wedge_collection[0]:
        if(count < colored):
            pie_wedge.set_facecolor(colors[0])
        else:
            pie_wedge.set_facecolor('white')
        count += 1
        pie_wedge.set_edgecolor('black')
        pie_wedge.set_linewidth(4)

    return ax,pie_wedge_collection





# slices = [37, 39, 39] #, 38, 62, 21, 15,  9,  6,  7,  6,  5,  4, 3
# cmap = plt.cm.prism
# colors = cmap(np.linspace(0., 1., len(slices)))
# labels = [u'TI', u'Con', u'FR'] #, u'TraI', u'Bug', u'Data', u'Int', u'KB', u'Other', u'Dep', u'PW', u'Uns', u'Perf', u'Dep'

f = open(path,'rt')

listOrologi = letturaConfig(f)
if(listOrologi != []):
    print(listOrologi)
    numeroOrologi = len(listOrologi)
    print(f"ci sono a disposizione già {numeroOrologi} orologi")
    risposta = input("Vuoi iniziare da zero? s/n\n")
    if(risposta.lower() == "n"):
        fig,ax = plt.subplots(1,numeroOrologi)
        for orologio in listOrologi:
            mypie(ax,orologio.color,orologio.total,orologio.colored,orologio.title)  
else:
    print(f"vuota {listOrologi}")
# fig,ax = plt.subplots(1,5)
# colors = ['red']

# mypie(ax,colors,10,1,"battaglia")
# mypie(ax,colors,10,3,"caduta")

plt.show()