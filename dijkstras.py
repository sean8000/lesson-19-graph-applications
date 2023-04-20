import networkx as nx
import matplotlib.pyplot as plt

"""
Done by Joy Mwaria, jkmwaria@udel.edu

Informal Description: 

The problem: You enter Ceasar Rodney Dining Hall from Academy Street, but they are serving your favorite meal all the way on the other side of the dining hall.
It is dinner time so the dining hall is packed. You need need to find the quickest way to get to your desired food station so you won't be late to 
your next class. 

Thankfully, the dining hall display the amount of student traffic between different stations in the dining hall on a TV at the enterance.

*define algo being used what nodes and vertexs represent, input and output

I am using ***

"""

graph1 = {
    'enterance': {'home': {'weight': 4}, 'balance': {'weight': 2}, 'salad': {'weight': 1}},
    'home': {'kosher': {'weight': 2}, 'grill': {'weight': 5}, 'coffee': {'weight': 1}},
    'balance': {'desert': {'weight': 3}, 'vegan': {'weight': 1}},
    'salad': {'infused water': {'weight': 2}, 'wrap': {'weight': 2}, 'panini': {'weight': 2}, 'vegan': {'weight': 1}, 'fruit bar': {'weight': 3}},
    'kosher': {'halal': {'weight': 3}},
    'grill': {'sizzling': {'weight': 3}, 'nachos': {'weight': 2}, 'desert': {'weight': 1}},
    'coffee': {'cereal': {'weight': 1}},
    'desert': {'fruit bar': {'weight': 1}, 'icecream': {'weight': 3}, 'nachos': {'weight': 3}},
    'vegan': {},
    'fruit bar': {'smoothie': {'weight': 1}},
    'infused water': {},
    'wrap': {'panini': {'weight': 1}},
    'panini': {},
    'halal': {'sizzling': {'weight': 5}},
    'sizzling': {'pizza': {'weight': 6}},
    'nachos': {'soda': {'weight': 3}},
    'icecream': {'smoothie': {'weight': 4}},
    'cereal': {},
    'soda': {},
    'smoothie': {},
    'pizza': {}
}

#Actual graph
G1 = nx.from_dict_of_dicts(graph1)

pos = nx.spring_layout(G1, seed=4)
labels = nx.get_edge_attributes(G1,'weight')
plt.figure(1,figsize=(12,12)) 
nx.draw_networkx(G1,pos, node_size=60, font_size=8)
nx.draw_networkx_edge_labels(G1,pos,edge_labels=labels)
plt.savefig("initial_graph1.png")
plt.show()