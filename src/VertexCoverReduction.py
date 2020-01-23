import sys
import collections
import networkx as nx


"""
This code is for the following tasks in 
Part 2: Vertex Cover – Reduction and Verification:

Task I
Task III.2


"""

def main():
    filename = sys.argv[1]
    k = int(sys.argv[2])

    G = load_graph(filename)

    # |V| in G
    n = len(G)

    # Vertices in G
    Gverts = set(G.keys())

    # k' = |V| - k
    kprime = n - k

    graph = nx.Graph()

    # Build complement graph
    GComp = collections.defaultdict(set)
    for vertex in G:
        values = set(G.get(vertex))
        edges = Gverts.difference(values)
        edges.remove(vertex)
        GComp[vertex] = edges

    # Output edge list
    write_graph("complement.graph", GComp)

    # Add edges to graph object
    for u in GComp:
        for v in GComp[u]:
            graph.add_edge(u, v)

    # Find all cliques, check for one of size k'
    cliquelist = list(nx.find_cliques(graph))
    solve = False
    for clique in cliquelist:
        if len(clique) == kprime:
            solve = True
            print("yes")
            break
    if not solve:
        print("no")

    """
    
    This code should print  "yes"/"no" if there's a vertex cover of size k. 
    (As long as there's a vertex cover of size k, print "yes"
     Note that this code prints only one "yes" or "no")

    Also, the code should write the complement graph of the input to a .txt file.
    You can write the graph to .txt with this command: 
    write_graph("complement.graph", YOUR_complement GRAPH)
    

    This code should use the "reduction from clique" idea to come up with 
    the answer. 
    
    You can find cliques with this command:   nx.find_cliques(graph)
    """

def write_graph(filename, adj_list):
    with open(filename, "w") as fout:
        for u in adj_list:
            for v in adj_list[u]:
                if u < v:
                    fout.write(str(u)+" "+str(v)+"\n")


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
