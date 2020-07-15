
def earliest_ancestor(ancestors, starting_node):
    #make a graph out of the ancestors provided
    from graph import Graph

    g = Graph()
    #first check to see if both vertices are there, then add them, then edges
    #0 is ancestor of 1
    for pair in ancestors:
        parent = pair[0]
        child = pair[1]
        if parent not in g.vertices:
            g.add_vertex(parent)
        if child not in g.vertices:
            g.add_vertex(child)
        if parent not in g.vertices[child]:
            g.add_edge(child, parent)


    return(g.vertices)

    #find the earliest ancestor


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 3))