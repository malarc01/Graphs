"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy


class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""

    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            raise IndexError("That vertex does not exist!")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]
    # Part 2: Implement Breadth-First Traversal

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """
        # create a plan_to_visit queue and add staring_vertex to it
        plan_to_visit = Queue()
        plan_to_visit.enqueue(starting_vertex)
        #  create a Set for visited_vertices
        visited_vertices = set()
        # while the plan_to_visit queue is not Empty:
        while plan_to_visit.size() > 0:
            # dequeue the first vertex on the queue
            current_vertex = plan_to_visit.dequeue()
            # if it not been visited
            if current_vertex not in visited_vertices:
                # print the vertex
                print(current_vertex)
                # mark it as visited, (add it to visited vertices)
                visited_vertices.add(current_vertex)
                # add all the neighbors to the queue
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited_vertices:
                        plan_to_visit.enqueue(neighbor)
    # Part 3: Implement Depth-First Traversal with a Stack

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create a plan_to_visit queue and add staring_vertex to it
        plan_to_visit = Stack()
        plan_to_visit.push(starting_vertex)
        #  create a Set for visited_vertices
        visited_vertices = set()
        # while the plan_to_visit queue is not Empty:
        while plan_to_visit.size() > 0:
            # dequeue the first vertex on the queue
            current_vertex = plan_to_visit.pop()
            # if it not been visited
            if current_vertex not in visited_vertices:
                # print the vertex
                print(current_vertex)
                # mark it as visited, (add it to visited vertices)
                visited_vertices.add(current_vertex)
                # add all the neighbors to the queue
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited_vertices:
                        plan_to_visit.push(neighbor)

    # Part 4: Implement Depth-First Traversal using Recursion

    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        def dft_recursive_helper(current_node):

            while current_node not in visited:

                visited.add(current_node)
                print(current_node)
                # recusion call
                for neighbor in self.get_neighbors(current_node):
                    dft_recursive_helper(neighbor)

        # Check if the node has been visited
        current_node = starting_vertex
        visited = set()
        # Call helper function
        dft_recursive_helper(starting_vertex)

        # visited.add(starting_vertex)

        # edges = self.get_neighbors(starting_vertex)

        # if len(edges) == 0:
        #     return
        # else:
        #     for edge in edges:
        #         if edge not in visited:
        #             self.dfs_recursive(edge, visited)
        #         else:
        #             return

    # Part 5: Implement Breadth-First Search
    # always returns shortest path

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create a empty queue, and enqueue a PATH to the starting vertex
        neighbors_to_visit = Queue()
        neighbors_to_visit.enqueue([starting_vertex])
        # create a set for visited vertices
        visited_vertices = set()
        # while the queue is not empty
        while neighbors_to_visit.size() > 0:
            # dequeue the first PATH in the queue
            current_path = neighbors_to_visit.dequeue()
            # grab the last vertex in the path
            current_vertex = current_path[-1]
            # if it hasn't been visited
            if current_vertex not in visited_vertices:
                # check if its the target
                if current_vertex == destination_vertex:
                    return current_path
                    # Return the path
                # mark it as visited
                visited_vertices.add(current_vertex)
                # make new versions of the current path, with each neighbor added to them
                for next_vertex in self.get_neighbors(current_vertex):
                    # duplicate the path
                    new_path = list(current_path)
                    # add the neighbor
                    new_path.append(next_vertex)
                    # add the new path to the queue
                    neighbors_to_visit.enqueue(new_path)

    # Part 6: Implement Depth-First Search

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        neighbors_to_visit = Stack()
        visited_vertices = set()
        neighbors_to_visit.push((starting_vertex, []))
        while neighbors_to_visit.size() > 0:
            current_vertex_plus_path = neighbors_to_visit.pop()
            current_vertex = current_vertex_plus_path[0]
            if current_vertex not in visited_vertices:
                if current_vertex == destination_vertex:
                    updated_path = current_vertex_plus_path[1] + [
                        current_vertex]
                    return updated_path
                # mark ti as visited
                visited_vertices.add(current_vertex)
                # add neighboors to the stack
                for neighbor in self.get_neighbors(current_vertex):
                    updated_path = current_vertex_plus_path[1] + [
                        current_vertex]
                    neighbors_to_visit.push((neighbor, updated_path))

    # Part 7: Implement Depth-First Search using Recursion

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        def dfs_recursive_helper(current_path):
            # If not...
            if current_path[-1] not in visited:
                # Mark it as visited, and print
                visited.add(current_path[-1])
                # if it's a match, return
                if current_path[-1] == destination_vertex:
                    return current_path
                # Call dft_recursive on each neighbor
                for neighbor in self.get_neighbors(current_path[-1]):
                    path_copy = current_path.copy()
                    path_copy.append(neighbor)
                    possible_answer = dfs_recursive_helper(path_copy)
                    if (possible_answer is not None):
                        return possible_answer
            # return None

        # Check if the node has been visited
        current_path = [starting_vertex]
        visited = set()
        # Call helper function
        return dfs_recursive_helper(current_path)


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

    print("graph.vertices=>", graph.vertices)

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
    print("DFT")

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
    # print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print("graph.dfs(1, 6)=>", graph.dfs(1, 6))
    print(graph.dfs_recursive(1, 6))
