
 
import math
from grid import Occupation
from collections import defaultdict
 
def calculate_g_value(n_node, start): #Calculates the g value 
    
    g_value = abs(int(n_node[0]) - int(start[0])) + abs(int(n_node[1]) - int(start[1]))
 
    return g_value
 
def calculate_h_value(n_node, end): #Calculates the h value 
    
 
    x_square = (int(n_node[0]) - int(end[0]))**2
    y_square = (int(n_node[1]) - int(end[1]))**2
    h_value = math.sqrt(x_square + y_square)
    
    return h_value
    
 
def reconstruct(came_from, current): #Recunstructs the shortes found path
    """ Vägen till målet """
    total_path = [current]
    for a in range(len(came_from)):
        if current in came_from:
            current = came_from[current]
            total_path.append(current)
    return total_path[::-1]
    
 
def generate_neighbors(current):# Generates neigbours for the current node
    
    neighbors = []
    
    neighbors.append((current[0] + 1, current[1])) # Right
    neighbors.append((current[0], current[1] + 1)) # Up
    neighbors.append((current[0] - 1, current[1])) # Left
    neighbors.append((current[0], current[1] - 1)) # Down
 
    return neighbors
 
def a_star (grid, start, goal):
    
    open_list = [start]
 
    came_from = {} # Empty dict for the tuples from end to start
 
    gscore = defaultdict(lambda: math.inf)#infinite size
    gscore[start] = calculate_g_value(start, start)
 
    fscore = defaultdict(lambda: math.inf)#Infinite size
    fscore[start] = calculate_h_value(start, goal)
 
    closed_list = [] # Closed list for evaluated nodes
 
    current = start #start is the only known node
 
    while len(open_list) > 0:
 
        current = open_list[0] #start is the only node in open list originaly
 
        for i in open_list:
            if fscore[i] < fscore[current]:
                continue
        
        
        if current == goal: #if goal is found recreate the path
            return reconstruct(came_from, current)
 
        open_list.remove(current)	#remove current from open list 
        closed_list.append(current) #add current to the open list, because it is evalueated 
 
        neighbors = generate_neighbors(current) #GEnerate a list of the current nodes niegbours
 
        temporary_neighbour_list = [] #Temporary check list for the neigbours
 
        for nodes in neighbors: #Checks so the nodes are in the grid
            if 14 >= nodes[0] and nodes[0] >= 0 and 14 >= nodes[1] and nodes[1] >= 0:
                temporary_neighbour_list.append(nodes)
 
        neighbors = temporary_neighbour_list
 
        # Checks if the path is blocked
        for j in neighbors: 
            if grid[j[0]][j[1]] == Occupation.BLOCKED:
                closed_list.append(j)
 
            if j in closed_list:
                continue

            temp_gScore = 1 + gscore[j] 
            if temp_gScore < gscore[j] or j not in open_list:
                gscore[j] = temp_gScore
                fscore[j] = calculate_g_value(j, goal)
                came_from[j] = current
        
                if open_list.count(j) == 0 and closed_list.count(j) == 0:
                    open_list.append(j)
        
    return None