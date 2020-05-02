from room import Room
from player import Player
from world import World
from graph import Graph

import random
from ast import literal_eval

# Load world
world = World()


# You may uncomment the smaller graphs for development and testing purposes.
# map_file = "maps/test_line.txt"
# map_file = "maps/test_cross.txt"
# map_file = "maps/test_loop.txt"
map_file = "maps/test_loop_fork.txt"
# map_file = "maps/main_maze.txt"

# Loads the map into a dictionary
room_graph = literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
traversal_path = []
# Track of visited rooms
visited = {}

# while visited is less than # of rooms
while len(visited) < len(room_graph):
    # store current room id
    current_room = player.current_room.id
    # store the room exits available for travel
    exits = player.current_room.get_exits()

    print(f'\nPlayer\'s current room: {current_room}')
    print(f'Current room\'s exits: {exits}\n')

    # if current_room has not been visited we want to
    # add the current_room to our visited dictionary
    if current_room not in visited:
        # add current room to visited dict by room id
        # value is a dict that will store directional info
        # '?' for paths that haven't yet been traversed and
        # room id if it has
        visited[current_room] = {points: '?' for points in exits}
        print(visited)

    # create list of unvisited directions that need traversed
    unvisited_directions = [
        point for point in visited[current_room] if visited[current_room][point] == '?']
    print(unvisited_directions)

    if len(unvisited_directions) > 0:
        # next direction to travel will be the first in
        # the unvisited directions list
        next_direction = unvisited_directions[0]

        # move player to next room
        player.travel(next_direction)


# TRAVERSAL TEST - DO NOT MODIFY
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(
        f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
else:
    print("TESTS FAILED: INCOMPLETE TRAVERSAL")
    print(f"{len(room_graph) - len(visited_rooms)} unvisited rooms")


#######
# UNCOMMENT TO WALK AROUND
#######
# player.current_room.print_room_description(player)
# while True:
#     cmds = input("-> ").lower().split(" ")
#     if cmds[0] in ["n", "s", "e", "w"]:
#         player.travel(cmds[0], True)
#     elif cmds[0] == "q":
#         break
#     else:
#         print("I did not understand that command.")
