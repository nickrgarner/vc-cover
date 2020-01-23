import sys
import copy
import collections

"""
This code is for the following tasks in 
Part 2: Vertex Cover – Reduction and Verification:

Task II
Task III.I


"""

def main():
    gfilename = sys.argv[1]
    cfilename = sys.argv[2]
    k = int(sys.argv[3])

    graph = load_graph(gfilename)
    candidates = load_candidates(cfilename)

    """
    Your code here. (You can add your own helper functions elsewhere)
    This code should output "yes"/"no" for each candidate if it's a vertex cover of size k.
    (i.e. If there are 5 candidate, print 5 "yes"/"no", seperated by new lines)
    """
    for soln in candidates:
        graph = load_graph(gfilename)
        if len(soln) != k:
            print("no")
            continue
        else:
            invalidVertex = False
            # If vertex in candidate is not a graph vertex, reject
            for vertex in soln:
                if vertex not in graph:
                    invalidVertex = True
                    print("no")
                    break
            if invalidVertex:
                continue
            # Iterate through vertices in candidate and remove edges in graph
            for vertex in soln:
                if vertex in graph:
                    graph.pop(vertex)
                for value in graph.values():
                    if vertex in value:
                        value.remove(vertex)
                # Delete any zero-order vertices
                deleteList = []
                for node in graph:
                    if len(graph[node]) == 0:
                        deleteList.append(node)
                for node in deleteList:
                    graph.pop(node)
            # When all edges in solution are removed, check for remaining edges and print result
            if len(graph.values()) == 0:
                print("yes")
            else:
                print("no")

def load_candidates(filename):
    candidates = []
    adj_list = collections.defaultdict(set)
    with open(filename, "r") as fin:
        for line in fin:
            candidates.append([int(v) for v in line.strip().split()])
    return candidates


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
