import openFile
import networkx as nx

def insertNodes():
    colnames = ['latitude', 'longtitude', 'searchval', 'blk_no', 'road_name', 'buidling', 'address']

    punggol = nx.Graph()
    data = openFile.openfile()
    Nodes = openFile.getNodes(data)
    latitude = openFile.getLatitude(data)
    longtitude = openFile.getlongtitude(data)
    blk_no=openFile.getblk_no(data)
    road_name = openFile.getroad_name(data)
    address = openFile.getroad_name(data)

    openFile.serachLatitude("latitude", "1.397946168")

    for i in range(1,len(Nodes)):
        punggol.add_node(Nodes[i],
                         latitude=latitude[i],
                         longtitude=longtitude[i],
                         blk_no=blk_no[i],
                         road_name=road_name[i],
                         address=address[i])

    return punggol



