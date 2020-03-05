import nodes
import edges
import networkx as nx
import matplotlib.pyplot as plt

punggol = nx.Graph()
punggol = nodes.insertAllNodes(punggol)
punggol = edges.insertAllEdges(punggol)

print(punggol.nodes.data())
