import openFile

def insertHDBNodes(g):
    data = openFile.openfile(r"Database\Final Node CSVs\hdb_nodes.csv")
    return insertNodes(g, data, "hdb")

def insertBusNodes(g):
    data = openFile.openfile(r"Database\Final Node CSVs\bus_stop_nodes.csv")
    return insertNodes(g, data, "bus")

def insertLRTNodes(g):
    data = openFile.openfile(r"Database\Final Node CSVs\lrt_nodes.csv")
    return insertNodes(g, data, "lrt")


def insertNodes(g, data, Nodetype):
    Nodes = openFile.getNodes(data)
    name = openFile.getName(data)
    latitude = openFile.getLatitude(data)
    longitude = openFile.getlongitude(data)
    for i in range(1, len(Nodes)):
        g.add_node(Nodes[i],
                   name=name[i],
                   latitude=latitude[i],
                   longitude=longitude[i],
                   type=Nodetype)

    return g
