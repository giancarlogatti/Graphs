# Write a function that takes a 2D binary array and returns 
# the number of 1 islands. An island consists of 1s that are 
# connected to the north, south, east or west. For example:
# islands = [[0, 1, 0, 1, 0],
#            [1, 1, 0, 1, 1],
#            [0, 0, 1, 0, 0],
#            [1, 0, 1, 0, 0],
#            [1, 1, 0, 0, 0]]
# island_counter(islands) # returns 4

def island_counter(graph):
    # iterate through each list in matrix
    # add each element (vertex) to a set of visited vertices (tuple)
    # if the current value is a 1, add to a count of 1 islands, and do
    # a breadth first search for 1s connected (north, south, east, west) to current 1
    # until there are no more vertices in the island left to visit. add each vertex to the set of
    # visited vertices
    # return counter
    def dfs_for_1(graph, i, j, visited):
        if i >= 0 and i < len(graph) and j >= 0 and j < len(graph):
            if graph[i][j] != 1:
                visited.add((i, j))
            elif (i, j) not in visited:
                visited.add((i, j))
                dfs_for_1(graph, i + 1, j, visited) #north
                dfs_for_1(graph, i - 1, j, visited) #south
                dfs_for_1(graph, i, j + 1, visited) #east
                dfs_for_1(graph, i, j - 1, visited) #west

    visited = set()
    count = 0
    for i in range(0, len(graph)):
        for j in range(0, len(graph[i])):
            if (i, j) not in visited:
                if graph[i][j] == 0:
                    visited.add((i, j))
                else:
                    #when value is 1, do a bst, mark 1s found into visited set. 
                    dfs_for_1(graph, i, j, visited)
                    count += 1
    return count

    


islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

print(island_counter(islands))