import networkx as nx
import matplotlib.pyplot as plt

"""
Done by Matthew Hansen, mghansen@udel.edu

The problem: Freshman Mechanical Engineering student Steve wants to take the class Heat Transfer (MEEG342) as soon as possible
but there are a bunch of prerequisites for the class, and those classes have their own prerequisites, and so on. He wants to see
a list of classes in topological order of the classes leading up to MEEG342. He figures he can put the entire cirriculum as a directed
graph with prerequisites pointing towards further classes. 

I am Using networkx in order to create the graph, and matplotlib to plot it.

"""

G = nx.DiGraph()

G.add_nodes_from(["EGG101", "CHEM103/133", "MATH241", "CISC106", "MEEG102", "PHYS207", "MATH242", "MEEG104", "MEEG210", "MEEG241", "MATH243", "MATH351", "PHYS245", "MEEG211", "MEEG215", "MSEG201", "MATH352", "MATH353", "MEEG301", "MEEG311", "MEEG321", "MEEG331", "MEEG332", "MEEG342", "MEEG401"])
G.add_edges_from([("CHEM103/133", "MSEG201"), ("MATH241", "MATH242"), ("CISC106", "MATH353"),("MEEG102", "MEEG301"),("PHYS207", "PHYS245"),("PHYS207", "MSEG201"),("MATH242", "MATH243"),("MATH242", "MEEG241"),("MEEG210", "MEEG215"),("MEEG210", "MEEG331"),("MEEG210", "MEEG211"),("MEEG241", "MEEG342"),("MATH351", "MATH352"),("MATH351", "MATH353"),("MATH351", "MEEG331"),("MEEG211", "MEEG301"),("MEEG211", "MEEG311"),("MEEG215", "MEEG304"),("MEEG215", "MEEG321"),("MSEG201", "MEEG321"),("MATH352", "MEEG332"),("MATH352", "MEEG342"),("MEEG301", "MEEG304"),("MEEG331", "MEEG332"),("MEEG304", "MEEG401")])

for layer, nodes in enumerate(nx.topological_generations(G)):
    # `multipartite_layout` expects the layer as a node attribute, so add the
    # numeric layer value as a node attribute
    for node in nodes:
        G.nodes[node]["layer"] = layer

plt.figure(1,figsize=(12,12)) 
pos = nx.multipartite_layout(G, subset_key="layer")
nx.draw_networkx(G, pos, node_size=1800, with_labels=True, arrows=True, node_color="lightblue", font_size=10)
#plt.show()
plt.savefig("dfs_graph.png")

# seen = set()
# def get_prerequisites(G, node):
#     prerequisites = []
#     for predecessor in G.predecessors(node):
#         if predecessor not in seen:
#             seen.add(predecessor)
#             prerequisites += get_prerequisites(G, predecessor)  
#     prerequisites.append(node)
#     return prerequisites

# prerequisites = get_prerequisites(G, "MEEG342")
# print(prerequisites)


prerequisites = nx.ancestors(G, "MEEG342")

# Topologically sort the ancestors
prerequisites_sorted = list(nx.topological_sort(G.subgraph(prerequisites)))

print(list(prerequisites_sorted))
