import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node("w")
G.add_node("x")
G.add_node("y")
G.add_node("z")

G.add_edge("w", "x")
G.add_edge("z", "w")
G.add_edge("w", "y")
G.add_edge("y", "z")
G.add_edge("x", "z")

G.add_edges_from([("x", "y"),("y", "x"), ("y", "z")])
nx.draw(G, with_labels = True)
plt.show()