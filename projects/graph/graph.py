"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
       self.vertices[vertex_id] = set()
      

    def add_edge(self, v1, v2):
        if v1 not in self.vertices:
            print("Rejected, no vert")
        else:
            self.vertices[v1].add(v2)
        

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        # We will do this using a Queue

        visited = []

        q = Queue()
        q.enqueue(starting_vertex)
        while q.size() > 0:
            cur = q.queue[0]
            visited.append(cur)
            # if the current neighbors haven't been visited, add them to the queue to explore
            for v in self.get_neighbors(cur):
                if v not in visited:
                    q.enqueue(v)
            q.dequeue()
        
        # print(f"final visited is {visited}")
        # return visited
        for x in visited:
            print(x)

    def dft(self, starting_vertex):
        #this one we'll do with a stack
        visited = []
        s = Stack()
        s.push(starting_vertex)
        while s.size() > 0:
            
            cur = s.pop()
            if cur not in visited:
                visited.append(cur)
            

            for v in self.get_neighbors(cur):
                
                if v not in visited:
                    s.push(v)
            
        # print(f"final visited with dft is {visited}")
        # return visited
        for x in visited:
            print(x)

    def dft_recursive(self, starting_vertex):
        
    
        visited = set()
        def dft_guts(starting_vertex, visited):
            # print(f"visited is {visited} and starting is {starting_vertex}")
            visited.add(starting_vertex)
            for x in self.get_neighbors(starting_vertex):
                if x not in visited:
                    visited.union(dft_guts(x, visited))
            # print(f"returning {visited}")
            return visited

        results = dft_guts(starting_vertex, visited)
        for x in results:
            print(x)



    def bfs(self, starting_vertex, destination_vertex):
        # We will do this using a Queue

     

        q = Queue()
       
        q.enqueue([starting_vertex])
        while q.size() > 0:
            path = q.dequeue()

            cur = path[-1]

            if cur == destination_vertex:
                return path
            for neighbor in self.get_neighbors(cur):
                new_path = list(path)
                new_path.append(neighbor)
                q.enqueue(new_path)
        
        
        

    def dfs(self, starting_vertex, destination_vertex):
        s = Stack()
        s.push([starting_vertex])

        while s.size() > 0:
            path = s.pop()

            cur = path[-1]

            if cur == destination_vertex:
                return path
            for neighbor in self.get_neighbors(cur):
                new_path = list(path)
                new_path.append(neighbor)
                s.push(new_path)


    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
