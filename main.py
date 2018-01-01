from time import time
from uuid import uuid4
import re
import os
import argparse
import graphviz as gv

parser = argparse.ArgumentParser(description="Extended Markdown")
parser.add_argument('file', type=str, help='Path of the file to load')
args = parser.parse_args()
test = ""

with open(args.file, 'r') as f:
    test = f.read()

source_file_name = args.file.split('.')[0]
path = 'data/{}'.format(source_file_name)
if not os.path.isdir(path):
    os.mkdir(path)

def process_graph(match):
    if not match:
        return ''
    graph = gv.Digraph(format='svg')
    filename = 'graph' + str(uuid4())
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

    graph.render("{}/{}".format(path, filename))

    return "\n![{}]({}/{}.svg)".format(filename, path, filename)

test = re.sub(r"--+\n((?:\w+ -> \w+\n?)+)\n--+", process_graph, test, flags=re.MULTILINE)

with open("{}.md".format(source_file_name), 'w') as f:
    f.write(test)

print(test)
