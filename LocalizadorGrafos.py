#librerias utilizadas para la interfaz grafica, la obtención del archivo y la manipulación del grafo y su matriz
from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import filedialog as fd
import networkx as nx
import matplotlib.pyplot as plt 
import numpy as np
import os
from math import inf
#creamos la ventana de la interfaz gráfica
root = tk.Tk()
root.title("Localizador con Grafos")
canvas = tk.Canvas(root, width=600, height=300)
canvas.grid(columnspan=3, rowspan=6)

#imagen de mapa, elemento estético solamente.
logo = Image.open('mapa.png')
logo = ImageTk.PhotoImage(logo)
imagen_mapa = tk.Label(image=logo)
imagen_mapa.image = logo
imagen_mapa.grid(column=1, row=0)

#instrucciones de carga de archivo, etiqueta.
instrucciones = tk.Label(root, text="Selecciona el archivo csv para obtener el grafo del mapa.", font="Bahnschrift")
instrucciones.grid(columnspan=3, column=0, row=1)

#función que abre el archivo gml y representa ese grafo con ayuda de networkx
def open_file():
    boton_buscar.set("Cargando...")
    #especificamos el archivo como tipo GML, este fue creado para la demostración.
    file = fd.askopenfilename(parent=root,  title="Choose a file", filetypes=[("Archivo GML", "*.gml")])
    filename = os.path.basename(file)
    if file:
        
        #creamos un grafo  y le asignamos el que estamos leyendo del archivo.
        global G
        G = nx.read_gml(file)
        #en las siguientes instrucciones se crean elementos visuales del gráfico, la posición de los nodos y sus etiquetas
        global pos
        pos = nx.get_node_attributes(G,'pos')
        global labels
        labels = nx.get_edge_attributes(G,'weight')
        #Se dibuja el grafo y se grafica con ayuda de matplotlib
        nx.draw(G,pos, with_labels=True,node_color='c')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        boton_buscar.set(f"{filename}")
        plt.show(block=False)
        botonMin.configure(state=NORMAL,bg="#00aaff")
        botonMax.configure(state=NORMAL,bg="#00aaff")
        #llamamos a la función que calculara la distancia total de los nodos del grafo que creamos
        global distancias 
        distancias = []
        distancias = distanciaTotal(G)

#función para calculara la distancia total de los nodos del grafo.
def distanciaTotal(grafo):
    #obtenemos la matriz de adyacencia de nuestro grafo
    adj_matrix = nx.to_numpy_matrix(grafo)
    #la convertimos en una lista, para aplicar el algoritmo de dijkstra que ya habiamos realizado
    adj_matrix = adj_matrix.tolist()
    #mandamos a llamar a la función de dijkstra para cada nodo del grafo
    for x in range(len(grafo.nodes)):
        distancias.append(dijkstra_distancia(adj_matrix,x))
    return distancias
    
#función que obtendrá los caminos mínimos a todos los demás nodos, dandole como parametro la matriz de ady y el nodo inicial.
def dijkstra_distancia(wmat,start,end=-1):
    #algorimto de dijkstra, utilizando la matriz de adyacencia y obteniendo el costo minimo para todos los nodos de la red
    n = len(wmat)
    dist = [inf]*n
    dist[start] = wmat[start][start]  # 0
    spVertex = [False]*n
    parent = [-1]*n
    path = [{}]*n
    for count in range(n-1):
        minix = inf
        u = 0
        for v in range(len(spVertex)):
            if spVertex[v] == False and dist[v] <= minix:
                minix = dist[v]
                u = v

        spVertex[u] = True
        for v in range(n):
            if not(spVertex[v]) and wmat[u][v] != 0 and dist[u] + wmat[u][v] < dist[v]:
                parent[v] = u
                dist[v] = dist[u] + wmat[u][v]

    for i in range(n):
        j = i
        s = []
        while parent[j] != -1:
            s.append(j)
            j = parent[j]
        s.append(start)

        path[i] = s[::-1]
    suma = 0
    for x in dist:
        suma = suma + x 
    return (dist[end], path[end]) if end >= 0 else (suma)



#función para calcular la mediana del grafo, es decir el nodo con la distancia total mínima de la red.
def cercano():
    botonMinimo.set("Calculando")
    #obtenemos el minimo de la lista de costos obtenida
    minimo = min(distancias)
    print(distancias)
    index = []
    #obtenemos los nodos que tienen ese valor, ya que puede que mas de 1 tenga la misma distancia total
    for x in range(len(distancias)):
        if(distancias[x]==minimo):
            index.append(x + 1)
    print(index)
    color_map = []
    #asignamos color rojo a los nodos que estan dentro de la solución
    for x in index:
        for node in G:
            
            if int(node) == x:
                color_map.append('red')
            else: 
                color_map.append('c')   
    #re-dibujamos el plot para mostrar nuevamente el gráfico, ya con el resultado escrito y visual
    plt.clf()
    plt.title(f"Se puede ubicar en los siguientes nodos (rojo) con distanica total de {distancias[index[0]-1]}")
    nx.draw(G,pos, with_labels=True,node_color=color_map)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()
    botonMinimo.set("Cercano")

#función para calcular la antimediana del grafo, es decir el nodo con la distancia total máxima de la red.
#misma funcionalidad que la función cercano() pero ahora usaremos el max()
def lejano():
    botonMaximo.set("Calculando")
    maximo = max(distancias)
    print(distancias)
    index = []
    for x in range(len(distancias)):
        if(distancias[x]==maximo):
            index.append(x + 1)
    print(index)
    color_map = []
    
    for x in index:
        for node in G:
            
            if int(node) == x:
                color_map.append('red')
            else: 
                color_map.append('c')   
    plt.clf()
    plt.title(f"Se puede ubicar en los siguientes nodos (rojo) con distanica total de {distancias[index[0]-1]}")
    nx.draw(G,pos, with_labels=True,node_color=color_map)
    nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()
    botonMaximo.set("Lejano")


#boton para buscar el archivo
boton_buscar= tk.StringVar()
botonBuscar = tk.Button(root, textvariable=boton_buscar, command=lambda:open_file(), font="Bahnschrift", bg="#00AAFF", fg="white", height=2, width=30)
boton_buscar.set("Buscar")
botonBuscar.grid(column=1, row=2)

#instrucciones de opciones de localización
instrucciones2 = tk.Label(root, text="Selecciona el tipo de ubicación que prefieres.", font="Bahnschrift")
instrucciones2.grid(columnspan=3, column=0, row=3)

#botones para seleccionar la localización deseada
botonMinimo= tk.StringVar()
botonMin = tk.Button(root, textvariable=botonMinimo, command=lambda:cercano(), font="Bahnschrift", bg="gray", fg="white", height=2, width=15, state=DISABLED)
botonMinimo.set("Cercano")
botonMin.grid( column=1, row=4,padx=0, pady=25)
botonMaximo= tk.StringVar()
botonMax = tk.Button(root, textvariable=botonMaximo, command=lambda:lejano(), font="Bahnschrift", bg="gray", fg="white", height=2, width=15 ,state=DISABLED)
botonMaximo.set("Lejano")
botonMax.grid( column=1, row=5 ,padx=15, pady=0)

#Miembros del equipo.
creditos = tk.Label(root, text="SERVÍN MARTINEZ, RODRIGUEZ CUATIANQUIZ Y VELASCO HUERTA", font="Bahnschrift")
creditos.grid(columnspan=3, column=0, row=6, pady=20)
#Ejecutamos la interfaz gráfica creada
root.mainloop()