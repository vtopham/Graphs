
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

    #find the earliest ancestor
    print(f"strating is {starting_node}")
    def find_earliest(current, path_length):
        print(f"current is {current}, path length is {path_length}")
        #run for ancestors
        #return if path_length is longer than current path length

        #end of the line? return. whoever called the function will compare.
        
        if g.get_neighbors(current) == set():
            return (current, path_length)
        else:
            best_parent_chain = (current, path_length)
            for parent in g.vertices[current]:
                
                current_parent_chain = find_earliest(parent, path_length + 1)
                #if equal in length but this one is lower
                if current_parent_chain[1] == best_parent_chain[1]:
                    if current_parent_chain[0] < best_parent_chain[0]:
                        best_parent_chain = current_parent_chain
                elif current_parent_chain[1] > best_parent_chain[1]:
                    best_parent_chain = current_parent_chain
                #if not betterk do nothing
                

            #return our champion
            return best_parent_chain

    if g.get_neighbors(starting_node) == set():
        return -1
    else:
        best = find_earliest(starting_node, 0)
        return(best[0])
test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 3))