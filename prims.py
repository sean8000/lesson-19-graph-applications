import networkx as nx
import matplotlib.pyplot as plt

"""
Done by Sean Johnson, seanjohn@udel.edu

The problem: The sidewalks to the library at UD have been declared unfit for use due to wear and decay. 
The university wants to build brick walkways this time instead, but they're very expensive! The university
had many interconnected sidewalks, but this is too expensive to do for brick walkways, so UD wants to have
the minimum number of walkways in order to get from the buildings on North and South campus to the library.

As the engineer contracted by UD your job is to cut costs to a minimum for the university. You are to use the 
smallest amount of bricks possible in order to make sure every major building has a path to the library. You 
are also using the previous network of interconnected sidewalks to decide where to place your brick walkways. 

The Algorithm being used on the problem is Prim's algorithm in order to create a minimum spanning tree. The 
minimum spanning tree in the context of this problem would be the graph of brick walkways with the least
amount of bricks used. This would be a network of brick walkways(edges), with every building(node) 
having a path to the library(also a node), and having the smallest total edge weight compared to any other subgraph. 

I am Using networkx in order to create the graph, and matplotlib to plot it.


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

