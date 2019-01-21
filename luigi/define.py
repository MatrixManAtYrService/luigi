import json
import functools
import sys
import networkx as nx
from networkx.readwrite import json_graph
from networkx.drawing.nx_pydot import to_pydot


type_category = nx.MultiDiGraph()

def func(morphism, node_pair):
    from_node = node_pair[0]
    to_node = node_pair[1]

    # I add whitespace to the string to force the edges to be readably far apart when displayed by pydot
    # if you know how to tell pydot to add some padding to the edge labels, please let me know
    def pad(string):
        return string + "  "

    type_category.add_edge(from_node, to_node, func=morphism, label=pad(morphism.__name__))

    type_category.nodes[from_node]['label'] = pad(from_node.__name__)
    type_category.nodes[to_node]['label'] = pad(to_node.__name__)

def as_dot():
    return to_pydot(type_category).to_string()


