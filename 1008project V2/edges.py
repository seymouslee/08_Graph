import openFile

def insertAllEdges(g):
    g = insertBusEdges(g)
    g = insertLRTEdges(g)
    g = insertWalkEdges(g)
    return g

def insertBusEdges(g):
    data = openFile.openEdge(r"Database\Final Edge CSVs\bus_edges.csv")
    return insertEdges(g, data, "bus")

def insertLRTEdges(g):
    data = openFile.openEdge(r"Database\Final Edge CSVs\lrt_edges.csv")
    return insertEdges(g, data, "lrt")

def insertWalkEdges(g):
    data = openFile.openEdge(r"Database\Final Edge CSVs\bus_to_hdb_walk_edges.csv")
    g = insertEdges(g, data, "walk")
    data = openFile.openEdge(r"Database\Final Edge CSVs\bus_to_lrt_walk_edges.csv")
    g = insertEdges(g, data, "walk")
    data = openFile.openEdge(r"Database\Final Edge CSVs\lrt_to_bus_walk_edges.csv")
    g = insertEdges(g, data, "walk")
    data = openFile.openEdge(r"Database\Final Edge CSVs\lrt_to_hdb_walk_edges.csv")
    g = insertEdges(g, data, "walk")
    return g


def insertEdges(g, data, Edgetype):
    start = getStart(data)
    end = getEnd(data)
    distance = getDistance(data)
    time = getTime(data)
    service = getService(data)

    for i in range(1, len(start)):
        g.add_edge(start[i],
                   end[i],
                   distance=distance[i],
                   time=time[i],
                   service=service[i],
                   type=Edgetype)
    return g


def getStart(data):
    start = data.start.tolist()
    return start

def getEnd(data):
    end = data.end.tolist()
    return end

def getDistance(data):
    distance = data.distance.tolist()
    return distance

def getTime(data):
    time = data.time.tolist()
    return time

def getService(data):
    service = data.service.tolist()
    return service