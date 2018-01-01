from time import time
import re
import argparse
import graphviz as gv


parser = argparse.ArgumentParser(description="Extended Markdown")
parser.add_argument('file', type=str, help='Path of the file to load')
args = parser.parse_args()
test = ""

with open(args.file, 'r') as f:
    test = f.read()

def process_graph(match):
    if not match:
        return ''
    graph = gv.Digraph(format='svg')
    filename = 'test' + 'graph' + str(int(time()))
    nodes = set()

    for pair in match.group(1).strip().split('\n'):
        pair = pair.split(' ')
        first_id = pair[0]
        last_id = pair[-1]

        if first_id not in nodes:
            graph.node(first_id)
        if last_id not in nodes:
            graph.node(last_id)
        nodes |= {first_id, last_id}

        graph.edge(first_id, last_id)

    graph.render("data/" + filename)

    return "[{}](data/{}.svg)".format(filename, filename)

test = re.sub(r"--+\n((?:\w+ -> \w+\n?)+)\n--+", process_graph, test, flags=re.MULTILINE)

print(test)
