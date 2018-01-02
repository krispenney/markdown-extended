from time import time
from uuid import uuid4
from equations import equation_to_png
import re
import os
import argparse
import graphviz as gv

parser = argparse.ArgumentParser(description="Extended Markdown")
parser.add_argument('file', type=str, help='Name of the file to load')
parser.add_argument('path', type=str, help='Path of the file to load')
args = parser.parse_args()
print(args.file)
print(args.path)
file_data: str

with open(args.file, 'r') as f:
    file_data = f.read()

source_file_name = args.file.split('.')[0]
data_path = f'data/{source_file_name}'
path = args.path
if not os.path.isdir(f"{path}/{data_path}"):
    os.mkdir(data_path)

def process_graph(match):
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

    graph.render(f"{path}/{data_path}/{filename}")

    return f"\n![{filename}]({data_path}/{filename}.svg)"

file_data = re.sub(r"--+\n((?:\w+ -> \w+\n?)+)\n--+", process_graph, file_data, flags=re.MULTILINE)

def process_latex(match):
    filename = f"latex-{uuid4()}"
    with open(f"{path}/{data_path}/{filename}.png", 'wb') as f:
        equation_to_png(' '.join(match.group(1).split('\n')), f)

    return f"![{filename}]({data_path}/{filename}.png)"

file_data = re.sub(r"\$\$+\n((?:.+\n?)+)\n\$\$+", process_latex, file_data)
file_data = re.sub(r"\$\$(.+?)\$\$", process_latex, file_data)

with open(f"{path}/{source_file_name}.md", 'w') as f:
    f.write(file_data)
