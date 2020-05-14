from room import Room
from player import Player
from world import World
from util import Queue,Stack
from traversal import *

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
room_graph=literal_eval(open(map_file, "r").read())
world.load_graph(room_graph)

# Print an ASCII map
world.print_rooms()
graph_r = RoomGraph()
player = Player(world.starting_room)
graph,order = graph_r.generate_room_graph(player)
# order = get_path(graph)
# print(order)
traversal_path =[]
i = 0
while(i < (len(order) - 1)):
    if(order[i+1] in graph[order[i]].keys()):
        traversal_path.append(graph[order[i]][order[i+1]])
    else:
        path = graph_r.search(order[i],order[i+1])
        j=0
        while(j < (len(path)-1)):
            if(path[j+1] in graph[path[j]].keys()):
                traversal_path.append(graph[path[j]][path[j+1]])
            else:
                traversal_path.append('?')
            j += 1
    i += 1
    

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
# traversal_path = []


# 959
# traversal_path = ['n', 's', 's', 'w', 'e', 'n', 'w', 'w', 's', 'w', 's', 's', 'n', 'n', 'e', 'n', 'e', 'n', 'w', 'w', 's', 'n', 'w', 's', 's', 's', 'w', 'n', 'w', 'w', 'w', 'e', 'e', 'e', 's', 'w', 'w', 's', 'w', 'n', 's', 'e', 'n', 'e', 'e', 'e', 's', 'w', 'w', 'e', 's', 'w', 'e', 'n', 'e', 's', 's', 's', 's', 'w', 's', 's', 's', 'n', 'n', 'w', 's', 's', 'w', 'e', 'n', 'w', 'e', 'n', 'e', 'n', 'e', 's', 's', 's', 'e', 'e', 's', 's', 'e', 'w', 's', 'w', 'e', 'n', 'n', 'n', 'w', 's', 'n', 'w', 's', 'w', 'e', 'n', 'n', 'n', 'n', 'n', 'n', 'w', 'w', 'w', 'w', 'n', 'w', 'n', 'n', 'w', 'n', 'e', 'n', 'w', 'w', 'e', 'n', 's', 'e', 'n', 's', 'e', 'e', 'e', 'n', 'e', 'n', 'w', 'w', 'w', 'n', 'n', 's', 'w', 'w', 's', 'n', 'w', 'e', 'e', 'n', 'n', 's', 'w', 'w', 'w', 'e', 'e', 'e', 's', 'e', 's', 'w', 'e', 'e', 'e', 'e', 'e', 'n', 's', 'e', 'e', 'e', 'e', 'e', 's', 's', 's', 'e', 's', 'n', 'w', 's', 'w', 's', 's', 's', 's', 's', 's', 's', 's', 's', 's', 'n', 'n', 'n', 'n', 'n', 'w', 'w', 's', 'e', 's', 's', 's', 'n', 'n', 'n', 'w', 'w', 's', 'n', 'e', 's', 'n', 'n', 'w', 'n', 's', 'e', 'e', 'n', 'w', 'e', 'n', 'w', 'e', 'n', 'w', 'w', 's', 'n', 'e', 'e', 'n', 'n', 'w', 'e', 's', 'w', 'e', 'n', 'e', 'e', 's', 'e', 's', 's', 'n', 'n', 'e', 's', 'e', 'n', 'e', 's', 's', 'n', 'n', 'w', 's', 'w', 's', 's', 's', 's', 'e', 'w', 'n', 'n', 'n', 'e', 's', 'e', 'w', 's', 'e', 'e', 'e', 'e', 'w', 'w', 'w', 'w', 'n', 'n', 'w', 'n', 'n', 'w', 'w', 's', 's', 's', 's', 'n', 'e', 's', 's', 's', 'e', 's', 'e', 'e', 's', 's', 'n', 'n', 'w', 's', 's', 'n', 'n', 'w', 's', 's', 'n', 'n', 'n', 'e', 'e', 'n', 'e', 'e', 'e', 'w', 's', 's', 'e', 'w', 's', 's', 'n', 'n', 'n', 'n', 'w', 's', 's', 'n', 'n', 'w', 's', 'w', 'w', 'w', 's', 's', 'w', 's', 'n', 'e', 's', 's', 'n', 'n', 'n', 'n', 'n', 'w', 's', 's', 'n', 'n', 'e', 'n', 'n', 'w', 'n', 'n', 'n', 'n', 'n', 'n', 'e', 'w', 'n', 'e', 'n', 'n', 'n', 'n', 'n', 's', 's', 'e', 'n', 'n', 's', 's', 'w', 's', 's', 'e', 'n', 'e', 'n', 'e', 'n', 'n', 'e', 'n', 'n', 'e', 'e', 'e', 'e', 'w', 'n', 's', 'w', 'n', 's', 'w', 'n', 's', 'w', 's', 's', 'w', 'n', 's', 's', 's', 'w', 'n', 'n', 'n', 's', 's', 's', 's', 'w', 's', 'w', 's', 'e', 'e', 'e', 'e', 's', 'e', 'e', 'e', 'e', 'w', 'n', 's', 'w', 'w', 'w', 'n', 'e', 'e', 'w', 'w', 'w', 's', 'n', 'w', 'n', 'e', 'e', 'e', 'e', 'e', 'e', 's', 'n', 'w', 'w', 'w', 'w', 'w', 'n', 'e', 'n', 'n', 'e', 'n', 'n', 'e', 'e', 'e', 's', 'n', 'w', 'w', 'w', 's', 's', 'e', 'n', 'e', 'w', 's', 'w', 'w', 's', 'e', 's', 'n', 'e', 's', 'e', 'e', 'e', 's', 'n', 'w', 'w', 'w', 'n', 'e', 'n', 'e', 'w', 's', 'e', 'w', 'w', 'w', 'w', 's', 'w', 's', 'w', 's', 'w', 's', 's', 's', 'n', 'n', 'e', 's', 'e', 'e', 'e', 'e', 'e', 'w', 'w', 'w', 's', 'e', 'e', 's', 'n', 'e', 'w', 'w', 'w', 's', 's', 's', 's', 'e', 'e', 'w', 'w', 'n', 'e', 'e', 'w', 'w', 'n', 'e', 'e', 'w', 'n', 's', 'w', 'n', 'n', 'n', 'w', 'w', 's', 'e', 'w', 'n', 'n', 'w', 'n', 'w', 'w', 'n', 'w', 'n', 'w', 'e', 'n', 'w', 'w', 'w', 'n', 'n', 'w', 'n', 's', 'e', 's', 's', 'w', 'w', 'n', 'w', 'w', 'w', 'e', 'e', 'n', 'n', 'n', 'n', 'w', 'e', 'n', 'n', 's', 's', 's', 's', 's', 'w', 'w', 'w', 'w', 's', 'w', 'e', 'n', 'w', 'e', 'e', 'e', 'n', 'n', 'n', 's', 's', 'w', 'e', 's', 'e', 'n', 'n', 's', 's', 'e', 's', 'e', 'n', 'n', 'n', 'n', 's', 's', 's', 's', 's', 'e', 'n', 's', 'e', 'e', 'e', 'n', 'w', 'n', 's', 'e', 'n', 'n', 'w', 'n', 's', 'w', 'n', 'w', 'e', 's', 'e', 'e', 's', 's', 's', 'e', 'n', 's', 'e', 's', 'n', 'n', 'n', 'n', 'e', 'e', 'w', 'w', 'n', 'e', 'e', 'n', 's', 'e', 'e', 'w', 'n', 'e', 'n', 'e', 'n', 's', 'e', 'n', 's', 'e', 'w', 'w', 'w', 's', 'e', 'w', 'w', 'n', 'n', 'n', 'n', 's', 's', 'e', 'n', 'e', 'n', 'n', 's', 'e', 's', 'n', 'e', 'w', 'w', 's', 'w', 'n', 's', 's', 'w', 's', 'w', 'n', 'n', 'n', 'n', 'e', 'e', 'w', 'w', 's', 'w', 'n', 'w', 'w', 'e', 'e', 's', 'w', 's', 's', 's', 'e', 'n', 'n', 's', 's', 'w', 'w', 'w', 'w', 'w', 's', 'w', 'e', 'n', 'w', 'w', 'n', 's', 'e', 'n', 's', 'e', 'e', 'n', 'w', 'n', 'n', 'w', 'e', 's', 's', 'e', 'n', 'n', 'n', 's', 's', 's', 's', 'e', 'e', 'n', 'w', 'n', 's', 'e', 'n', 's', 's', 'e', 's', 'e', 'w', 's', 's', 's', 'w', 'n', 'n', 'w', 'n', 'e', 'w', 'w', 'e', 's', 'e', 's', 's', 'e', 's', 's', 'w', 's', 's', 'w', 'w', 'n', 's', 'w', 'n', 's', 'w', 'w', 'n', 'w', 'n', 'w', 'e', 's', 'w', 'e', 'e', 's', 's', 's', 'n', 'w', 'w', 'w', 'e', 'e', 's', 'w', 'w', 'w', 's', 'w', 'w', 'e', 's', 'e', 's', 's', 'w', 'n', 'w', 'e', 's', 'e', 'e', 's', 'w', 'w', 's', 'w', 's', 'n', 'e', 'n', 'e', 'e', 'e', 'n', 's', 'e', 'e', 's', 'w', 's', 'w', 's', 'n', 'e', 'n', 'w', 'w', 's', 'w', 'w', 'e', 'e', 's', 'w', 's', 'w', 'e', 's', 'w', 'e', 's', 'w', 'w', 'e', 'e', 's', 'n', 'n', 'n', 'n', 'w', 'w', 'w', 'e', 'e', 'e', 'e', 's', 's', 's', 'e', 'w', 's', 'e', 'w', 'n', 'n', 'n', 'n', 'n', 'n', 'w']
   
# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)


# # Create a Stack and push starting vertex
# ss = Stack()
# ss.push([player.current_room])

#     # While Queue is not empty:
# while ss.size() > 0:
#     # pop the last added vertex
#     path = ss.pop()
#     # if not visited
#     if path[-1] not in visited_rooms:
#         # DO THE THING!!!!!!!
#         # print(path[-1].id)
#         # mark as visited
        
#         visited_rooms.add(path[-1])
#             # push all neightbors
#         for direction in path[-1].get_exits():
#             new_path = list(path)
#             new_path.append(path[-1].get_room_in_direction(direction))
#             traversal_path.append(direction)
#             ss.push(new_path)

# print(traversal_path)
for move in traversal_path:
    player.travel(move)
    visited_rooms.add(player.current_room)

if len(visited_rooms) == len(room_graph):
    print(f"TESTS PASSED: {len(traversal_path)} moves, {len(visited_rooms)} rooms visited")
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
