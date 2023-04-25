import networkx as nx
import matplotlib.pyplot as plt

"""
Done by Benita Abraham, beniabra@udel.edu

The problem: The CS + Social Good (CS+SG) club is looking to collaborate with another club
for their next social good project. They're looking to collaborate with a club that that 
they have some connection with whether it be through a club member or a club member's other
clubs. In this way, it won't be that difficult to work with them. They want to generate a 
list of potential clubs that they could collaborate with based on a connection (path) existing
between the two clubs.

Their faculty advisor provided them with a graph based on survey data collected directly from
UD students. In this graph, the nodes are clubs at UD and the edges between those clubs
represent at least one student that is a part of both clubs.

As computer science students, they know that this problem could be easily solved by using graph
traversal, specifically breath-first-search, to find all the nodes that are in the same 
connected component as CS+SG.

I am Using networkx in order to create the graph, and matplotlib to plot it.

"""

G = nx.Graph()

""" Adding all 20 nodes"""
G.add_node("CS+SG") # Computer Science + Social Good
G.add_node("ACM") # Association for Computing Machinery
G.add_node("ACM-W") # Association for Computing Machinery - Council on Women
G.add_node("CPC") # Competitive Programming Club
G.add_node("CTF") # Blue Hens Capture The Flag
G.add_node("oSTEM") # Out in Science, Technology, Engineering, and Mathematics
G.add_node("MPC") # Music Production Club
G.add_node("Eta Kappa Nu") # Electrical & Computer Engineering
G.add_node("AMT") # Assistive Medical Technologies
G.add_node("AATCC") # Fashion x Textiles
G.add_node("IEEE") # Institute of Electrical and Electronics Engineers
G.add_node("WIB") # Women in Business
G.add_node("SWE") # Society of Women Engineers
G.add_node("Phi Chi Theta") # Co-ed business fraternity
G.add_node("E-CLUB") # Entrepreneurship Club
G.add_node("NSBE") # National Society of Black Engineers
G.add_node("ISA") # Indian Student Association
G.add_node("APSA") # Asian & Pacific Islander Student Association
G.add_node("SASA") # South Asian Student Association
G.add_node("ASME") # American Society of Mechanical Engineers
G.add_node("MMSC") # Medical and Molecular Sciences Club
G.add_node("Kamaal") # Dance group
G.add_node("VP") # Vocal Point



"""Adding all edges"""
G.add_edge("CS+SG","ACM-W")
G.add_edge("CS+SG","CPC")
G.add_edge("CS+SG","CTF")
G.add_edge("ACM-W","WIB")
G.add_edge("ACM","oSTEM")
G.add_edge("ACM","Eta Kappa Nu")
G.add_edge("CPC","ACM")
G.add_edge("NSBE","SWE")
G.add_edge("oSTEM","SWE")
G.add_edge("IEEE","SWE")
G.add_edge("CPC","CTF")
G.add_edge("oSTEM","ASME")
G.add_edge("oSTEM","Eta Kappa Nu")
G.add_edge("oSTEM","IEEE")
G.add_edge("IEEE","Eta Kappa Nu")
G.add_edge("WIB","Phi Chi Theta")
G.add_edge("WIB","Phi Chi Theta")
G.add_edge("ISA","SASA")
G.add_edge("E-CLUB","Phi Chi Theta")
G.add_edge("NSBE","ASME")
G.add_edge("NSBE","IEEE")
G.add_edge("NSBE","Eta Kappa Nu")
G.add_edge("WIB","E-CLUB")
G.add_edge("CTF","ACM")
G.add_edge("Kamaal","ISA")
G.add_edge("SASA","APSA")
G.add_edge("VP","MPC")
G.add_edge("ACM-W","SWE")
G.add_edge("MMSC","AMT")




"""Drawing the graph"""
pos = nx.spring_layout(G, seed=4, k=0.45)
labels = nx.get_edge_attributes(G,'weight')
plt.figure(1,figsize=(12,12)) 
nx.draw_networkx(G,pos, node_size=60, node_color="pink" ,font_size=10)
nx.draw_networkx_edge_labels(G,pos,edge_labels=labels)
plt.savefig("club_graph.png")
plt.show()

edges = nx.bfs_edges(G, 'CS+SG')
nodes = ['CS+SG'] + [v for u, v in edges]
for i in nodes:
    print(i)
