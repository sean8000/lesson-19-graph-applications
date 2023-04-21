import networkx as nx
import matplotlib.pyplot as plt

"""
Done by Sean Johnson, seanjohn@udel.edu

The problem: The sidewalks to the library at UD have been declared unfit for use due to wear and decay. 
The university wants to build brick walkways this time instead, but they're very expensive! The university
had many interconnected sidewalks, but this is too expensive to do for brick walkways, so UD wants to have
the minimum number of walkways in order to get from some of the buildings on North and South campus to the library.

As the engineer contracted by UD your job is to cut costs to a minimum for the university. You are to use the 
smallest amount of bricks possible in order to make sure every building has a path to the library. You 
are also using the previous network of interconnected sidewalks to decide where to place your brick walkways. 

The Algorithm being used on the problem is Prim's algorithm in order to create a minimum spanning tree. The 
minimum spanning tree in the context of this problem would be the graph of brick walkways with the least
amount of bricks used. This would be a network of brick walkways(edges), with every building(node) 
having a path to the library(also a node), and having the smallest total edge weight compared to any other subgraph. 

I am Using networkx in order to create the graph, and matplotlib to plot it.


"""

G = nx.Graph()
"""
Tutorial: Adding Edges and nodes
G.add_node("Morris_Library")
G.add_node("Allison_Hall")
G.add_node("Smith_Hall")

G.add_edge("ML","AH", weight  = 5)
G.add_edge("AH","SH", weight = 10)


graph = {'A': {'B': {'weight': 10}, 'C': {'weight': 3}},
 'B': {'C': {'weight': 1}, 'D': {'weight': 2}},
 'C': {'B': {'weight': 4}, 'D': {'weight': 8}, 'E': {'weight': 2}},
 'D': {'E': {'weight': 7}},
 'E': {'D': {'weight': 9}}}

 """
#Using Adjacency list instead
graph = {
    'L': {'KB': {'weight': 4}, 'SH': {'weight': 8}, 'MH': {'weight': 1}, 'CR': {'weight': 4},
               'AHW': {'weight': 2}, 'AH': {'weight': 2}, 'TH': {'weight': 9}},
    'KB': {'PL': {'weight': 4}, 'EW': {'weight': 2}, 'TB': {'weight': 3}, 'SH': {'weight': 2}},
    'TB': {'WHS': {'weight': 6}, 'MD': {'weight': 7}, 'SH': {'weight': 4}, 'EW': {'weight': 4}},
    'MD': {'IW': {'weight': 10}, 'IE': {'weight': 10}, 'WHS': {'weight': 2}},
    'IE': {'IW': {'weight': 1}},
    'WHS': {'EW': {'weight': 5}, 'IW': {'weight': 13}},
    'EW': {'PL': {'weight': 1}},
    'PL': {'SH': {'weight': 4}},
    'SH': {'ISE': {'weight': 6}, 'PH': {'weight': 4}, 'GH': {'weight': 2}},
    'ISE': {'PH': {'weight': 3}},
    'PH': {'SL': {'weight': 4}},
    'SL': {'GH': {'weight': 1}},
    'GH': {'MH': {'weight': 2}, 'MH': {'weight': 3}},
    'AH': {'AHW': {'weight': 1}, 'TH': {'weight': 5}, 'PK': {'weight': 4}, 'CR': {'weight': 3}},
    'CR': {'LN': {'weight': 4}, 'PK': {'weight': 2}},
    'PK': {'LN': {'weight': 2}, 'TH': {'weight': 2}},
    'TH': {'LN': {'weight': 1}},
    'MH': {'TB': {'weight': 10}, 'PH': {'weight': 6}},

               }
"""
Meanings: L = Library, KB = Kirkrbide hall, SH = Smith hall, MH = Memorial hall, CR = Ceasar Rodney dining hall, 
AH = Allison hall, AHW = Allison hall west, TH = Thompson hall, LN = Lane hall, PL = Pernell hall, EW = Ewing hall, 
TB = Trabant, WHS = Willard educational hall, MD = McDowell hall, IE = Independence east, IW = Independence west, 
PH = Pearson hall, SL = Sharp lab, PK = Perkins, GH = Gore hall, ISE = Harker lab
"""

#Actual graph
G = nx.from_dict_of_dicts(graph)

#Minimum spanning tree
H = nx.algorithms.minimum_spanning_tree(G, weight = "weight", algorithm = "prim", ignore_nan = False)

#Generates initial graph
pos = nx.spring_layout(G, seed=4)
labels = nx.get_edge_attributes(G,'weight')
plt.figure(1,figsize=(12,12)) 
nx.draw_networkx(G,pos, node_size=70, node_color = "yellow", font_size=14, font_color = "red")
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.savefig("initial_graph.png")
#plt.show()

#Generates minimum spanning tree
pos = nx.spring_layout(H, seed=4)
labels = nx.get_edge_attributes(H,'weight')
plt.figure(2,figsize=(12,12)) 
nx.draw_networkx(H,pos, node_size=70, node_color = "yellow", font_size=14, font_color = "red")
nx.draw_networkx_edge_labels(H,pos,edge_labels=labels)
plt.savefig("minimum_spanning_tree")
#plt.show()

