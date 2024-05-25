import read_data
import networkx as nx
import matplotlib.pyplot as plt

def graphing():
    G = nx.Graph()

    upload_to_graph = read_data.format_data()
    for key,values in upload_to_graph.items():
        G.add_node(key)

        for value in values:
            if value != None:
                G.add_edge(key, value)


    print(upload_to_graph)
    nx.draw(G, with_labels = True)
    plt.show()

graphing()