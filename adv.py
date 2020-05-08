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
# map_file = "maps/test_loop_fork.txt"
map_file = "maps/main_maze.txt"

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
# visited = {}
# traversal_graph = Graph()

# Graph of traversed rooms (it's really just a dictionary shh)
traversal_graph = {}
# Path for backtracking
current_path = []
# Dictionary containing opposite directions (useful for backtracking)
reverse = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}

# helper fn to pick a direction that returns None if there aren't
# any more directions to travel in
def get_next_dir(current_room):
    # loop through the directions in the room
    for key, val in current_room.items():
        # check for '?' value
        if val is '?':
            # return the key for the direction
            return key
    # if there are no more '?' return None
    return None


while len(traversal_graph) != len(world.rooms):
    # grab the current room
    curr_room = player.current_room
    # grab the id of the room
    curr_room_id = player.current_room.id
    # setup ref to prev room
    prev_room_id = None

    # if the curr room is not in the traversal graph
    if curr_room_id not in traversal_graph:
        # grab all the possible directions
        traversal_graph[curr_room_id] = {
            direction: '?' for direction in player.current_room.get_exits()}

    # call get_next_dir() to find a new direction to travel in
    direction = get_next_dir(traversal_graph[curr_room_id])

    # if the direction is None and nowhere else to go
    if direction is None:
        new_path = current_path.pop()
        player.travel(reverse[new_path])
        traversal_path.append(reverse[new_path])
        continue

    # set prev_room to current room before traveling
    prev_room_id = player.current_room.id
    # move player to the next room
    player.travel(direction)
    # add the move to the traversal path
    traversal_path.append(direction)
    # and add it to the current_path for back tracking
    current_path.append(direction)
    # set curr_room to the new current_room
    curr_room = player.current_room
    # and update the id
    curr_room_id = player.current_room.id

    # check if the new room is in the traversal graph
    if curr_room_id not in traversal_graph:
        # get the possible directions from the new room
        traversal_graph[curr_room_id] = {
            direction: '?' for direction in player.current_room.get_exits()}

    # link the rooms together
    if traversal_graph[curr_room_id][reverse[direction]] == '?':
        # eg {n: 1, ...} {..., s: 0, ...}
        traversal_graph[curr_room_id][reverse[direction]] = prev_room_id
        traversal_graph[prev_room_id][direction] = curr_room_id


# second attempt
# visited = traversal_graph.rooms

# # while visited is less than # of rooms
# while len(visited) < len(room_graph):
#     current_room = player.current_room.id
#     exits = player.current_room.get_exits()
#     prev_room = None
#     next_direction = None

#     # store room in our traversal graph if it has not yet been visited
#     if current_room not in traversal_graph.rooms:
#         # add room to traversal graph along with untravelled pointers
#         traversal_graph.add_room(
#             current_room, {points: '?' for points in exits})

#     # store reference to unvisited directions
#     unvisited_directions = [
#         point for point in visited[current_room] if visited[current_room][point] == '?']

#     # if there unvisisted directions, pick one and travel
#     if len(unvisited_directions) > 0:
#         # pick first untravelled direction
#         next_direction = unvisited_directions[0]
#         # travel that direction
#         player.travel(next_direction)
#         # grab the new room's id
#         next_room = player.current_room.id
#         # add it to our traversal graph
#         traversal_graph.add_room(
#             next_room, {points: '?' for points in player.current_room.get_exits()})
#         # update the edges
#         traversal_graph.update_points(current_room, next_room, next_direction)
#         # append the move to the traversal_path
#         traversal_path.append(next_direction)

#     else:
#         # travel to untravelled path
#         break
#     print(visited)


# # first attempt
# # while visited is less than # of rooms
# while len(visited) < len(room_graph):
#     # store current room id
#     current_room = player.current_room.id
#     # store prev room id
#     prev_room = player.current_room.id
#     # store next direction to travel
#     next_direction = None
#     # store the room exits available for travel
#     exits = player.current_room.get_exits()

#     print(f'\nPlayer\'s current room: {current_room}')
#     print(f'Current room\'s exits: {exits}\n')

#     # if current_room has not been visited we want to
#     # add the current_room to our visited dictionary
#     if current_room not in visited:
#         # add current room to visited dict by room id
#         # value is a dict that will store directional info
#         # '?' for paths that haven't yet been traversed and
#         # room id if it has
#         visited[current_room] = {points: '?' for points in exits}

#         print("Visited:")
#         print(f'{visited}\n')

#     # create list of unvisited directions that need traversed
#     unvisited_directions = [
#         point for point in visited[current_room] if visited[current_room][point] == '?']
#     print("Unvisited directions in room:")
#     print(f'{unvisited_directions}\n')

#     if len(unvisited_directions) > 0:
#         # next direction to travel will be the first in
#         # the unvisited directions list
#         next_direction = unvisited_directions[0]

#         # store the direction opposite of the next direction
#         # for previous
#         prev_direction = get_opposite_direction(next_direction)

#         # move player to next room
#         player.travel(next_direction)
#         traversal_path.append(next_direction)

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
