from pathlib import Path
from attr import dataclass
from matplotlib.axes import Axes
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
    dictDati = {}
    listaOrologi = []
    for line in f.readlines():
        line = line.replace("\n","")
        if(line.startswith('##!')):
            orologio = Orologio(dictDati['color'],
                int(dictDati['total']),int(dictDati['colored']),dictDati['title'])
            listaOrologi.append(orologio)
        if(not line.startswith('#')):
            text = ''
            line = line.split()
            for word in line:
                if(line.index(word) > 1):
                    text += word
                    if(len(line) > 3): # nomeValore = Valore
                        text += ' '
            dictDati[line[0]] = text
    # print(dict)
    return listaOrologi

def scritturaConfig(f,listaOrologi: list) -> None:
    for orologio in listaOrologi:
        f.write(f"color = {orologio.color}")
        f.write(f"total = {orologio.total}")
        f.write(f"colored = {orologio.colored}")
        f.write(f"title = {orologio.title}")
        f.write(f"##!")

def mypie(ax:list[Axes],color: str,total: int,colored: int,title: str,numeroOrologi :int):
    slices = [1 for i in range(total)]
    pie_wedge_collection = ax[numeroOrologi].pie(slices, labeldistance=1.05)#labels=labels, autopct=make_autopct(slices))

    ax[numeroOrologi].set_title(title)

    count = 0
    for pie_wedge in pie_wedge_collection[0]:
        if(count < colored):
            pie_wedge.set_facecolor(color)
        else:
            pie_wedge.set_facecolor('white')
        count += 1
        pie_wedge.set_edgecolor('black')
        pie_wedge.set_linewidth(4)

    return ax,pie_wedge_collection

def main():    
    while True:
        with open(path,'rt') as f:
            listOrologi = letturaConfig(f)
            print (listOrologi)
        numeroOrologi = len(listOrologi)
        fig,ax = plt.subplots(1,numeroOrologi)
        for orologio in listOrologi:
            mypie(ax,orologio.color,orologio.total,orologio.colored,orologio.title, numeroOrologi - 1)
            numeroOrologi -= 1
        plt.show()
main()