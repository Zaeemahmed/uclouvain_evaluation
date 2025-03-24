def reachable(adj_list, start_node):
    """ Compute the nodes reachable from a start node

    For the above example, reachable([[1, 3], [2], [0], [4], [3], []], 0)) must return {0, 1, 2, 3, 4}
    and reachable([[1, 3], [2], [0], [4], [3], []], 3) must return {3, 4}

    Parameters:
    -----------
    adj_list : the adjacency list of the graph
    start_node: the index of the start node

    Returns:
    --------
    reachable: set(int) the set of nodes reachable from start_node


    """
    
    reachableNodes = set()
    
    def depthFirstSearch(node):
        if node not in reachableNodes:
            reachableNodes.add(node)
            for neighbor in adj_list[node]:
                depthFirstSearch(neighbor)
                
    depthFirstSearch(start_node)
    return reachableNodes