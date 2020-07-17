#hmmmm

from room import Room
from player import Player
from world import World

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

player = Player(world.starting_room)

# Fill this out with directions to walk
# traversal_path = ['n', 'n']
def is_it_done(graph):
    
    for room in graph:
        for door in graph[room]:
            
            if graph[room][door] == "?":
                return False
    return True

def inv_direction(dir_travelled):
    if dir_travelled == 'n':
        return 's'
    if dir_travelled == 's':
        return 'n'
    if dir_travelled == 'e':
        return 'w'
    if dir_travelled == 'w':
        return 'e'

graph = {}

def get_path_baby(player, room_from, dir_travelled, graph, traversal_path):
    #just get a depth first traversal working
    #Get a dictionary ready to go of all rooms, starting with
    print(f"moving {dir_travelled}")
    
    
    cur_room = player.current_room.id
    #unless we're starting, move the player
    if dir_travelled != None:
        traversal_path.append(dir_travelled)
        player.travel(dir_travelled)
        cur_room = player.current_room.id
    print(f"we are in room {cur_room}")
    #if this room isn't in the graph then let's populate it, totally blank
    if cur_room not in graph:
        rooms = player.current_room.get_exits()
        graph[cur_room] = {}
        for room in rooms:
            graph[cur_room][room] = "?"
       
    #add the edges for this room and the room that we came from
    if room_from != None:
        graph[room_from][dir_travelled] = cur_room
        graph[cur_room][inv_direction(dir_travelled)] = room_from

    
    for direction in graph[cur_room]:
        if graph[cur_room][direction] == "?":
            returned_path = get_path_baby(player, cur_room, direction, graph, traversal_path)
            # print(f"the returned path is {returned_path}")
            #undo the movement after this runs
            # traversal_path.extend(returned_path)
            inv = inv_direction(direction)
            
            print(is_it_done(graph))
            skip = is_it_done(graph)
            if skip == False:
                traversal_path.append(inv)
                player.travel(inv)
    
    # return traversal_path
    return traversal_path

    
    #for each direction, if you can go in that direction, recurse


   
    

traversal_path = []

result = get_path_baby(player, None, None, graph, traversal_path)
print(result)
# print(len(result))





# TRAVERSAL TEST
visited_rooms = set()
player.current_room = world.starting_room
visited_rooms.add(player.current_room)

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
