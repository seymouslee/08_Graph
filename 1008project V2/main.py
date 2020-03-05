import nodes
import networkx as nx

punggol = nx.Graph()
punggol = nodes.insertHDBNodes(punggol)
punggol = nodes.insertBusNodes(punggol)
punggol = nodes.insertLRTNodes(punggol)

print(punggol.nodes.data())