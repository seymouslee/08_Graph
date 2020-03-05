import openFile

def insertAllNodes(g):
    g = insertHDBNodes(g)
    g = insertBusNodes(g)
    g = insertLRTNodes(g)
    return g

def insertHDBNodes(g):
    data = openFile.openNode(r"Database\Final Node CSVs\hdb_nodes.csv")
    return insertNodes(g, data, "hdb")

def insertBusNodes(g):
    data = openFile.openNode(r"Database\Final Node CSVs\bus_stop_nodes.csv")
    return insertNodes(g, data, "bus")

def insertLRTNodes(g):
    data = openFile.openNode(r"Database\Final Node CSVs\lrt_nodes.csv")
    return insertNodes(g, data, "lrt")


def insertNodes(g, data, Nodetype):
    Nodes = getNodes(data)
    name = getName(data)
    latitude = getLatitude(data)
    longitude = getlongitude(data)
    for i in range(1, len(Nodes)):
        g.add_node(Nodes[i],
                   name=name[i],
                   latitude=latitude[i],
                   longitude=longitude[i],
                   type=Nodetype)

    return g

def getNodes(data):
    postal = data.id.tolist()
    return postal

def getName(data):
    name = data.name.tolist()
    return name

def getLatitude(data):
    latitude = data.latitude.tolist()
    return latitude

def getlongitude(data):
    longitude = data.longitude.tolist()
    return longitude