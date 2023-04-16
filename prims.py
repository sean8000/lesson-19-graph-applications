import networkx as nx
import matplotlib.pyplot as plt

"""
Done by Sean Johnson, seanjohn@udel.edu

The problem I have created is 

The Algorithm I am using on the problem is Prim's algorithm in order to create a minimal spanning tree.

I am Using networkx in order to create the graph


"""

G = nx.Graph()
"""
Tutorial: Adding Edges
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
graph = {'AH': {'ML': {'weight': 5}, 'SH': {'weight': 10}},
          'ML': {'GH': {'weight': 4}, 'MH': {'weight': 3}, 'SH': {'weight': 1}},
          'SH': {'GH': {'weight': 2}, 'NX': {'weight': 8}}
          }


G = nx.from_dict_of_dicts(graph)

#Minimum spanning tree
# G = nx.algorithms.minimum_spanning_tree(G, weight = "weight", algorithm = "prim", ignore_nan = False)

pos = nx.spring_layout(G)
nx.draw_networkx(G,pos)
labels = nx.get_edge_attributes(G,'weight')
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.show()

