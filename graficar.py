import itertools
import io
from string import ascii_uppercase
from matplotlib.transforms import TransformNode
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
import matplotlib.ticker as ticker
import os
from os import remove
import math
import webbrowser
import sys
from sys import argv
from sympy import expand, matrix2numpy

o = sys.argv[1].split()
e = sys.argv[2].split()
cte = sys.argv[3].split()
cont = sys.argv[4].split()
num = sys.argv[5].split()
opcion=int(o[0])
eje=str(e[0])
c=float(cte[0])
contador=int(cont[0])
n=int(num[0])

def labels_gen():
    size = 1
    while True:
        for s in itertools.product(ascii_uppercase, repeat=size):
            yield "".join(s)
        size +=1

ruta = "poligono.txt"

def actualizarCoordenadas(matriz, ruta):
    file = open(ruta, "w")
    file.write("x y\n")
    file.close()

    #Ciclo para obtener las coordenadas
    for i in range(0, n):
        #coordenada en x
        x=matriz[i][0]
        #coordenada en y
        y= matriz[i][1]
        #cadena para agregar a un archivo de texto del cual se leerá la coordenada
        cadena=str(x)+" "+str(y)
        #se abre el archivo en a para append(añadir)
        with open(ruta, 'a') as f:
            #se inserta la cadena al archivo
            f.write(cadena+"\r")
            f.close()


matriz = [[0] * 2 for i in range(n)]

with open(ruta) as coordenadas:
    listaAux = coordenadas.readlines()
coordenadas.close()
#print(listaAux)
for i in range(len(listaAux)):
    listaAux[i]=listaAux[i].rstrip("\n")
#print(listaAux)
for i in range(len(matriz)):
    matriz[i]=listaAux[i+1].split(" ")
for i in range(len(matriz)):
    for j in range(len(matriz[i])):
        matriz[i][j]=float(matriz[i][j])
#print("Holassssss")
#print(matriz)
actualizarCoordenadas(matriz, ruta)
#print(matriz)



def graficar(contador):
    # Cargamos el csv
    data=pd.read_csv(ruta ,header=0,delim_whitespace=True)

    # Cálculo del centroide
    centroide = np.mean(data, axis=0)

    # Cáculo del ángulo polar
    aux = data - centroide
    polar_angles = np.arctan2(aux.y, aux.x)

    # Obtenemos un nuevo DataFrame con los vértices ordenados
    data = data.reindex(polar_angles.argsort())


    ax = plt.subplot(111)

    # Creamos el polígono
    plygon = plt.Polygon(data, fill=True, facecolor="#ffb3b3", edgecolor='#ff0000', alpha=1, zorder=1)
    ax.add_patch(plygon)

    # Creamos los vértices
    ax.scatter(data.x, data.y, c='b', zorder=2)

    # Etiquetas para cada vértice y arista
    etiquetas = labels_gen()
    for i, vertice in enumerate(data.values):
        lb = next(etiquetas)
        ax.annotate(str(lb), xy=vertice + 0.1)
        punto_medio = (vertice +  data.values[(i + 1) % (data.shape[0])]) / 2
        ax.annotate(str(lb.lower()), xy=punto_medio)

    # Mostramos los ejes centrados en el origen
    ax.spines['left'].set_position('zero')
    ax.spines['right'].set_color('none')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_color('none')
    ax.xaxis.set_ticks_position('bottom')
    ax.yaxis.set_ticks_position('left')

    # Configuramos la rejilla
    ax.grid(color='gray', linestyle='dashed', linewidth=1, alpha=0.4)

    # Escalamos la gráfica
    ax.autoscale_view()
    ax.xaxis.set_major_locator(ticker.MultipleLocator(1))

    
    #Guardamos la gráfica
    nombreGrafica="grafica"+str(contador)+".png"
    plt.savefig(nombreGrafica)
    # Mostramos la gráfica
    plt.close()
    return nombreGrafica

def multiplicarMatrices(matriz, matriz2):

    multiplicacion = [[0] * 2 for i in range(len(matriz))]
    for i in range(len(multiplicacion)):
        for j in range(len(multiplicacion[i])):
            for k in range(len(matriz2)):
                multiplicacion [i][j] = multiplicacion [i][j] + matriz[i][k]*matriz2[k][j]
    #print("ES acaaaaaaaaaaaaaaaaaaaaaa")
    #print(multiplicacion)

    return multiplicacion


def reflexion(matriz, eje, ruta):
    if(eje=="X" or eje=="x"):
        transformacion = [[0] * 2 for i in range(2)]
        transformacion[0][0]=-1
        transformacion[0][1]=0
        transformacion[1][0]=0
        transformacion[1][1]=1
        #print(transformacion)
        matriz=multiplicarMatrices(matriz, transformacion)
        #print(matriz)
    elif(eje=="Y" or eje=="y"):
        transformacion = [[0] * 2 for i in range(2)]
        transformacion[0][0]=1
        transformacion[0][1]=0
        transformacion[1][0]=0
        transformacion[1][1]=-1
        #print(transformacion)
        matriz=multiplicarMatrices(matriz, transformacion)
    
    actualizarCoordenadas(matriz, ruta)
    return matriz

def expandir(matriz, c, eje, ruta):
    if(eje=="X" or eje=="x"):
        transformacion = [[0] * 2 for i in range(2)]
        transformacion[0][0]=c
        transformacion[0][1]=0
        transformacion[1][0]=0
        transformacion[1][1]=1
        
        #print(transformacion)
        matriz=multiplicarMatrices(matriz, transformacion)
        #print(matriz)
    elif(eje=="Y" or eje=="y"):
        transformacion = [[0] * 2 for i in range(2)]
        transformacion[0][0]=1
        transformacion[0][1]=0
        transformacion[1][0]=0
        transformacion[1][1]=c
        #print("acakakaannna")
        #print(transformacion)
        matriz=multiplicarMatrices(matriz, transformacion)
    
    actualizarCoordenadas(matriz, ruta)
    return matriz

def cortar(matriz, c, eje, ruta):
    if(eje=="X" or eje=="x"):
        transformacion = [[0] * 2 for i in range(2)]
        transformacion[0][0]=1
        transformacion[0][1]=0
        transformacion[1][0]=c
        transformacion[1][1]=1
        #print(transformacion)
        matriz=multiplicarMatrices(matriz, transformacion)
        #print(matriz)
    elif(eje=="Y" or eje=="y"):
        transformacion = [[0] * 2 for i in range(2)]
        transformacion[0][0]=1
        transformacion[0][1]=c
        transformacion[1][0]=0
        transformacion[1][1]=1
        #print(transformacion)
        matriz=multiplicarMatrices(matriz, transformacion)
    
    actualizarCoordenadas(matriz, ruta)
    return matriz

def rotar(matriz, c, eje, ruta):
    
    transformacion = [[0] * 2 for i in range(2)]
    transformacion[0][0]=math.cos(math.radians(c))
    transformacion[0][1]=math.sin(math.radians(c))
    transformacion[1][0]=math.sin(math.radians(c))*(-1)
    transformacion[1][1]=math.cos(math.radians(c))
    #print(transformacion)
    matriz=multiplicarMatrices(matriz, transformacion)
    #print(matriz)
    
    actualizarCoordenadas(matriz, ruta)
    return matriz

def main(opcion, matriz, eje, ruta, contador):
    Graficas=[]
    if(contador==0):
        Graficas.append(graficar(contador))
        contador=int(contador)+1
    
    if(opcion==1):
        
        matriz=reflexion(matriz, eje, ruta)
        Graficas.append(graficar(contador))
        contador=int(contador)+1
    elif(opcion==2):
        
        matriz=expandir(matriz, c, eje, ruta)
        Graficas.append(graficar(contador))
        contador=int(contador)+1
    elif(opcion==3):
        
        matriz=cortar(matriz, c, eje, ruta)
        Graficas.append(graficar(contador))
        contador=int(contador)+1
    elif(opcion==4):
        
        matriz=rotar(matriz, c, eje, ruta)
        Graficas.append(graficar(contador))
        contador=int(contador)+1
    elif(opcion==5):
        Graficas.append(graficar(contador))
        contador=int(contador)+1
        
    print(contador)

main(opcion, matriz, eje, ruta, contador)
