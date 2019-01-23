import json
import functools
import sys
import os
import networkx as nx
from networkx.readwrite import json_graph
from networkx.drawing.nx_pydot import to_pydot
from yattag import Doc, indent
from luigi.js import draw_diagram

type_category = nx.MultiDiGraph()

def func(morphism, node_pair):
    from_node = node_pair[0]
    to_node = node_pair[1]

    # I add whitespace to the string to force the edges to be readably far apart when displayed by pydot
    # if you know how to tell pydot to add some padding to the edge labels, please let me know
    def pad(string):
        return string + "   "

    type_category.add_edge(from_node, to_node,
            func=morphism,
            label=morphism.__name__,
            labelfontcolor="red"
            )

    type_category.nodes[from_node]['label'] = from_node.__name__
    type_category.nodes[to_node]['label'] = to_node.__name__

def write_svg():
    f_name = '.luigi.typegraph.svg'
    dot = to_pydot(type_category)
    dot.write_svg(f_name)
    print("Types: file://{}/{}".format(os.getcwd(), f_name), file=sys.stderr)

def write_html():
    f_name = '.luigi.typegraph.html'
    doc, tag, text = Doc().tagtext()
    with tag('html'):
        with tag('head'):
            doc.stag('meta', charset='utf-8')
            with tag('script'):
                text(draw_diagram)
        with tag('body', onload="draw_diagram()"):
            with tag('script', src='https://cdnjs.cloudflare.com/ajax/libs/d3/3.4.11/d3.min.js'):
                text("")
            doc.stag('svg', width='200', height='200', id="svg1")
            doc.stag('svg', width='200', height='200', id="svg2")

    result = indent(doc.getvalue())
    with open(f_name, 'w') as f:
        f.write(result)
    print("Types: file://{}/{}".format(os.getcwd(), f_name), file=sys.stderr)

def write_dot():
    return to_pydot(type_category).to_string()


