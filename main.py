from time import time
from uuid import uuid4
import re
import os
import argparse
import graphviz as gv

parser = argparse.ArgumentParser(description="Extended Markdown")
parser.add_argument('file', type=str, help='Path of the file to load')
args = parser.parse_args()
file_data: str

with open(args.file, 'r') as f:
    file_data = f.read()

source_file_name = args.file.split('.')[0]
path = f'data/{source_file_name}'
if not os.path.isdir(path):
    os.mkdir(path)

def process_graph(match):
    if not match:
        return ''
    graph = gv.Digraph(format='svg')
    filename = f'graph-{uuid4()}'
    nodes = set()

    for pair in match.group(1).strip().split('\n'):
        pair = pair.split(' ')
        source = pair[0]
        destination = pair[-1]

        if source not in nodes:
            graph.node(source)
        if destination not in nodes:
            graph.node(destination)
        nodes |= {source, destination}

        graph.edge(source, destination)

    graph.render(f"{path}/{filename}")

    return f"\n![{filename}]({path}/{filename}.svg)".format(filename, path, filename)

file_data = re.sub(r"--+\n((?:\w+ -> \w+\n?)+)\n--+", process_graph, file_data, flags=re.MULTILINE)

with open(f"{source_file_name}.md", 'w') as f:
    f.write(file_data)
