import nodes
import edges
import networkx as nx
import matplotlib.pyplot as plt

punggol = nx.Graph()
punggol = nodes.insertAllNodes(punggol)
punggol = edges.insertAllEdges(punggol)

print(punggol.nodes.data())
print(nx.is_connected(punggol))

pos = nx.get_node_attributes(punggol, 'pos')
nx.draw(punggol, pos, with_labels=True)
plt.savefig("punggol.png")