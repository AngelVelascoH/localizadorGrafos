import networkx as nx

import matplotlib.pyplot as plt 
g = nx.Graph()


g.add_node(1,pos=(0,6))
g.add_node(2,pos=(8,0))
g.add_node(3,pos=(11,4))
g.add_node(4,pos=(6,11))
g.add_node(5,pos=(15,0))
g.add_node(6,pos=(16,6))
g.add_node(7,pos=(17,10))
g.add_node(8,pos=(10,15))
g.add_node(9,pos=(16,13))
g.add_node(10,pos=(20,8))

g.add_edge(1,4,weight=900)
g.add_edge(4,8,weight=319)
g.add_edge(4,7,weight=900)
g.add_edge(8,9,weight=200)
g.add_edge(9,7,weight=30)
g.add_edge(7,10,weight=50)
g.add_edge(4,6,weight=700)
g.add_edge(6,10,weight=200)
g.add_edge(1,3,weight=510)
g.add_edge(1,2,weight=320)
g.add_edge(2,3,weight=176)
g.add_edge(3,6,weight=290)
g.add_edge(3,5,weight=200)
g.add_edge(5,6,weight=320)

pos = nx.get_node_attributes(g,'pos')
labels = nx.get_edge_attributes(g,'weight')

nx.draw(g,pos, with_labels=True,node_color='c')

nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)
nodes = list(g.nodes)
for i in nodes:
    for j in nodes:
        print(f"from {i} to {j} = {nx.dijkstra_path_length(g,i,j)}")
#plt.show()

"""
import matplotlib.pyplot as plt
G = nx.karate_club_graph()
pos = nx.spring_layout(G)
nx.draw(G,pos,node_color='k')
# draw path in red
path = nx.shortest_path(G,source=14,target=16)
path_edges = list(zip(path,path[1:]))
nx.draw_networkx_nodes(G,pos,nodelist=path,node_color='r')
nx.draw_networkx_edges(G,pos,edgelist=path_edges,edge_color='r',width=10)
plt.axis('equal')
plt.show()
"""