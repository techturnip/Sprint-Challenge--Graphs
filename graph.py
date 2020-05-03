class Queue():
    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)

    def dequeue(self):
        if self.size() > 0:
            return self.queue.pop(0)
        else:
            return None

    def size(self):
        return len(self.queue)


class Stack():
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if self.size() > 0:
            return self.stack.pop()
        else:
            return None

    def size(self):
        return len(self.stack)


def get_opposite_direction(dir):
    opposite = None

    if not dir:
        return

    if dir == 'n':
        opposite = 's'
    elif dir == 'e':
        opposite = 'w'
    elif dir == 's':
        opposite == 'n'
    elif dir == 'w':
        opposite == 'e'

    return opposite


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

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        # create visit_queue and add starting_vertix to it
        visit_queue = Queue()
        visit_queue.enqueue(starting_vertex)
        # create a Set for visited_vertices
        visited_vertices = set()

        # While the vist_queue is not empty:
        while visit_queue.size() > 0:
            # dequeu first vertex on the queue
            current_vertex = visit_queue.dequeue()
        # if its not been visisted
            if current_vertex not in visited_vertices:

                # print the vertex
                print(current_vertex)
                # mark as visisted
                visited_vertices.add(current_vertex)
                # add all neighbors to the queue
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited_vertices:
                        visit_queue.enqueue(neighbor)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        # create a plan_to_visit stack and add starting_vertex to it
        visit_stack = Stack()
        visit_stack.push(starting_vertex)
        # create a Set for visited_vertices
        visited_vertices = set()
        # while the visit_stack stack is not Empty:
        while visit_stack.size() > 0:
            # pop the first vertex from the stack
            current_vertex = visit_stack.pop()
            # if its not been visited
            if current_vertex not in visited_vertices:
                # print the vertex
                print(current_vertex)
                # mark it as visited, (add it to visited_vertices)
                visited_vertices.add(current_vertex)
                # add all unvisited neighbors to the stack
                for neighbor in self.get_neighbors(current_vertex):
                    if neighbor not in visited_vertices:
                        visit_stack.push(neighbor)

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        # create a empty queue, and enqueue a PATH to the starting vertex
        path_queue = Queue()
        # queue.enqueue([starting_vertex])
        path_queue.enqueue([starting_vertex])
        # create a set for visited vertices
        visited_vertices = set()
        # while the queue is not empty
        while path_queue.size() > 0:
            # dequeue the first PATH
            current_path = path_queue.dequeue()
            # grab the last vertex in the path
            last_vertex = current_path[-1]
            # if it hasn't been visited
            if last_vertex not in visited_vertices:
                # check if its the target
                if last_vertex == destination_vertex:
                    return current_path

                # mark it as visited
                visited_vertices.add(last_vertex)
                # make new versions of the current path, with each neighbor added to them
                for neighbor in self.get_neighbors(last_vertex):
                    # duplicate the path
                    duplicate_path = current_path.copy()
                    # add the neighbor
                    duplicate_path.append(neighbor)
                    # add the new path to the queue
                    path_queue.enqueue(duplicate_path)

    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # create a stack
        s = Stack()

        # push a path to the starting vertex
        s.push([starting_vertex])

        # create a set to store visited vertices
        visited = set()

        # while stack is not empty
        while s.size() > 0:
            # pop first path
            path = s.pop()
            # grab vertex from end of path
            v = path[-1]

            # check if it has been visited
            if v not in visited:
                # mark as visited
                visited.add(v)
                # check if destination vert is reached
                if v == destination_vertex:
                    return path

                # enqueue path to all it's neighbors
                for neighbor in self.get_neighbors(v):
                    # copy path
                    path_copy = path.copy()
                    path_copy.append(neighbor)
                    # push copy
                    s.push(path_copy)

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

# SOCIAL GRAPH
# class Graph:
#     def __init__(self):
#         self.rooms = {}
#         self.adjacency = {}

#     def update_points(self, prev_room, current_room, dir_travelled):
#         """
#         Creates a bi-directional relationship
#         """
#         opposite_dir = get_opposite_direction(dir_travelled)

#         self.rooms[prev_room][dir_travelled] = current_room
#         self.rooms[current_room][opposite_dir] = prev_room

#     def add_room(self, id, pointers):
#         """
#         Add a new room with a room id and pointers
#         """
#         # automatically increment the ID to assign the new user
#         self.rooms[id] = pointers

#     def get_all_paths(self, room_id):
#         """
#         Takes a room's room_id as an argument

#         Returns a dictionary containing every user in that user's
#         extended network with the shortest friendship path between them.

#         The key is the friend's ID and the value is the path.
#         """
#         rooms_to_visit = Queue()
#         visited = {}  # Note that this is a dictionary, not a set
#         rooms_to_visit.enqueue([room_id])

#         while rooms_to_visit.size() > 0:
#             # dequeue the first path
#             current_path = rooms_to_visit.dequeue()
#             # grab the last vertex
#             current_vertex = current_path[-1]
#             # if it has not been visited
#             if current_vertex not in visited:
#                 # when we reach the unvisited vertex
#                 # add to visited dict
#                 # also, add the whole path that led us there
#                 visited[current_vertex] = current_path
#                 # get all neighbors and add the path + the neighbor
#                 # to the queue
#                 for neighbor in self.adjacency[current_vertex]:
#                     path_copy = current_path.copy()
#                     path_copy.append(neighbor)
#                     rooms_to_visit.enqueue(path_copy)

#         # !!!! IMPLEMENT ME
#         return visited
