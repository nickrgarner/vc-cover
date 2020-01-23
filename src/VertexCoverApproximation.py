import sys
import random
import collections

"""
This code is Part 1:Vertex Cover – Approximation
"""


def main():
    filename = sys.argv[1]
    algo = sys.argv[2]

    G = load_graph(filename)

    cover = []
    if algo == "greedy-vertex":
        cover = greedy_vertex(G)
    elif algo == "greedy-edge":
        cover = greedy_edge(G)
    else:
        print("Incorrect arguments")
        exit()

    output_cover(cover)

def output_cover(cover):
    with open("approxOutput.txt", "w") as fout:
        for v in cover:
            fout.write(str(v)+"\n")


def greedy_edge(adj_list):
    """
    Implement your code for greedy edge here.
    It should return a list of vertices that covers every edge.
    """
    output = []
    while len(adj_list.values()) > 0:
        # Grab first edge in dict
        keyList = []
        for key in adj_list:
            keyList.append(key)
        u = keyList[0]
        valueList = []
        for value in adj_list[u]:
            valueList.append(value)
        v = valueList[0]
        # Add to output if not duplicates
        uDupe = False
        vDupe = False
        for vertex in output:
            if vertex == u:
                uDupe = True
            if vertex == v:
                vDupe = True
        if not uDupe:
            output.append(u)
        if not vDupe:
            output.append(v)
        # Cycle through keys and values and remove adjacent edges
        adj_list.pop(u)
        adj_list.pop(v)
        for value in adj_list.values():
            if u in value:
                value.remove(u)
            if v in value:
                value.remove(v)
        # Delete any zero-order vertices
        deleteList = []
        for vertex in adj_list:
            if len(adj_list[vertex]) == 0:
                deleteList.append(vertex)
        for vertex in deleteList:
            adj_list.pop(vertex)
    return output

def greedy_vertex(adj_list):
    """
    Implement your code for greedy vertex here.
    It should return a list of vertices that covers every edge.
    """
    output = []
    while len(adj_list.values()) > 0:
        # Find highest order vertex, add to VC output
        highVertex = -1
        highVertexOrder = -1
        for vertex in adj_list:
            if len(adj_list[vertex]) > highVertexOrder:
                highVertexOrder = len(adj_list[vertex])
                highVertex = vertex
        output.append(highVertex)
        # Delete vertex from adj_list, remove adjacent edges
        adj_list.pop(highVertex)
        for value in adj_list.values():
            if highVertex in value:
                value.remove(highVertex)
        # Delete any zero-order vertices
        deleteList = []
        for vertex in adj_list:
            if len(adj_list[vertex]) == 0:
                deleteList.append(vertex)
        for vertex in deleteList:
            adj_list.pop(vertex)
    return output


def load_graph(filename):
    adj_list = collections.defaultdict(set)
    with open(filename, "r") as fin:
        for line in fin:
            u, v = [int(v) for v in line.strip().split()]
            adj_list[u].add(v)
            adj_list[v].add(u)
    return adj_list


if __name__ == "__main__":
    main()
