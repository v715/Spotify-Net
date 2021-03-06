import pickle
import networkx as nx


def get_graph(attributes, edgelist):

    with open(attributes, 'rb') as f:
        attributes = pickle.load(f)

    with open(edgelist, 'rb') as f:
        G = nx.read_edgelist(f, create_using=nx.DiGraph)
        nx.set_node_attributes(G, attributes)

    return G
