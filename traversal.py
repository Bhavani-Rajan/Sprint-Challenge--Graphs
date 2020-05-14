#     player.current_room.id
#     player.current_room.get_exits()
#     player.travel(direction)
from util import *
from player import Player
from room import Room
import random
class RoomGraph:
    def __init__(self):
        self.vertices = {}  # This is our adjacency list
        self.order_rooms = []
    def generate_room_graph(self,player):
        starting_room = player.current_room
        visited = set()
        # Create a Stack and push starting vertex
        ss = Stack()
        ss.push([starting_room])
        # While Queue is not empty:
        while ss.size() > 0:
        # pop the last added vertex
            path = ss.pop()
            room = path[-1]
            if room not in visited:
                # DO THE THING!!!!!!!
                self.order_rooms.append(room.id)
                self.vertices[room.id] ={}
                for exit in room.get_exits():
                    self.vertices[room.id][room.get_room_in_direction(exit).id]= exit
                # mark as visited
                visited.add(room)
                    # push all neightbors
                exits = room.get_exits()
                for i in range(len(exits)):
                    direction = random.choice(exits)
                    exits.remove(direction)
                    new_path = list(path)
                    new_path.append(room.get_room_in_direction(direction))
                    ss.push(new_path)
        return self.vertices,self.order_rooms

    def search(self, starting_vertex, destination_vertex):
            """
            Return a list containing the shortest path from
            starting_vertex to destination_vertex in
            breath-first order.
            """
            graph = self.vertices
            # Create a q and enqueue starting vertex
            qq = Queue()
            qq.enqueue([starting_vertex])
            # Create a set of traversed vertices
            visited = set()
            # While queue is not empty:
            while qq.size() > 0:
                # dequeue/pop the first vertex
                path = qq.dequeue()
                # if not visited
                if(path[-1] == destination_vertex):
                    return path
                if path[-1] not in visited:
                    # DO THE THING!!!!!!!
                    # mark as visited
                    visited.add(path[-1])
                    # enqueue all neightbors
                    for next_vert in graph[path[-1]].keys():
                        new_path = list(path)
                        new_path.append(next_vert)
                        qq.enqueue(new_path)
    
    def get_path(self):
        order = self.order_rooms
        graph = self.vertices
        traversal_path =[]
        i = 0
        while(i < (len(order) - 1)):
            if(order[i+1] in graph[order[i]].keys()):
                traversal_path.append(graph[order[i]][order[i+1]])
            else:
                path = self.search(order[i],order[i+1])
                j=0
                while(j < (len(path)-1)):
                    # if(path[j+1] in graph[path[j]].keys()):
                    traversal_path.append(graph[path[j]][path[j+1]])
                    # else:
                    #     traversal_path.append('?')
                    j += 1
            i += 1
        return traversal_path