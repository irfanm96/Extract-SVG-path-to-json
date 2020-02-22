import json
import os

from xml.dom import minidom


def parse(svg_file):
    svg = minidom.parse(svg_file)
    paths = svg.getElementsByTagName('path')
    node = paths[0]
    path = str(node.getAttributeNode('d').nodeValue)
    return path


def main():
    data = {}
    dirpath = os.getcwd()
    directory = os.fsencode(dirpath + "/svg/")

    for file in os.listdir(directory):
        filename = os.fsdecode(file)
        if filename.endswith(".svg"):
            data[str(filename).split(".svg")[0]] = parse("svg/" + filename)
            continue
        else:
            continue
    with open('data.json', 'w') as outfile:
        json.dump(data, outfile)


main()
