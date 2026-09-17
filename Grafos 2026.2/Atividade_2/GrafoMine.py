import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

G.add_node("Graveto"     )
G.add_node("Açucar"      )
G.add_node("Madeira"     )
G.add_node("Vidro"       )
G.add_node("Teia"        )
G.add_node("Ferro"       )
G.add_node("Redstone"    )
G.add_node("Corante"     )
G.add_node("OlhoDeAranha")
G.add_node("Cogumelo"    )

G.add_edge("Vidro", "Vidro"  )
G.add_edge("Vidro", "Corante")

G.add_edge("Ferro", "Ferro"   )

G.add_edge("Açucar", "Cogumelo")

G.add_edge("Graveto", "Graveto" )
G.add_edge("Graveto", "Madeira" )
G.add_edge("Graveto", "Ferro"   )
G.add_edge("Graveto", "Redstone")
G.add_edge("Graveto", "Teia"    )

G.add_edge("Madeira", "Madeira" )
G.add_edge("Madeira", "Redstone")
G.add_edge("Madeira", "Ferro"   )
G.add_edge("Madeira", "Teia"    )

G.add_edge("Redstone", "Redstone")
G.add_edge("Redstone", "Ferro"   )

G.add_edge("OlhoDeAranha", "Açucar"  )
G.add_edge("OlhoDeAranha", "Cogumelo")

plt.figure(figsize=(10, 8))
posicao = nx.circular_layout(G)
nx.draw(G, pos=posicao, with_labels=True, node_color='lightgreen', node_size=2500, font_weight='bold', font_size=9)

plt.show()
