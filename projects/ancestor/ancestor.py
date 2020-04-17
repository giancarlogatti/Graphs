def earliest_ancestor(ancestors, starting_node):
    # create a set where you map each node to their parents, 
    # since the input maps each node to their children. 
    parent_mapping = dict()

    for pair in ancestors:
        if pair[1] not in parent_mapping:
            parent_mapping[pair[1]] = [pair[0]]
        else:
            parent_mapping[pair[1]].append(pair[0])
    
    max_size = 0        
    ancestor = -1
    #from the starting node, perform a depth first traversal, where we keep
    #track of the path, we also have a variable that maintains the count of each path
    def dfs_ancestor(node, ancestor_dict, size = 1):
        if node not in ancestor_dict:
            return (size - 1, node)
        
        nonlocal max_size
        nonlocal ancestor
        parents = ancestor_dict[node]
        for n in parents:
            val = dfs_ancestor(n, ancestor_dict, size + 1)
            if val != None and val[0] > max_size:
                max_size = val[0]
                ancestor = val[1]

    dfs_ancestor(starting_node, parent_mapping)
    return ancestor