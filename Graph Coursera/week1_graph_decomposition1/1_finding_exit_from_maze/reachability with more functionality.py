#Uses python3

import sys

def reach(adj, x, y):
    #write your code here
    if len(adj[x]) == 0:
        return 0
    
    # home keeping variables
    visited = [0]*len(adj)
    predecessors = {}
    # we start from beginning and fill in the predecessors dictionary
    # we will then read this dictionary to see if a path exists from x to y
    predecessors[x] = None
    visited[x] = 1
    explore(adj, adj[x], x, visited, predecessors)
    
    if y in predecessors:
        return 1
    else:
        return 0
    ## below is extra work not required for assignment
    ##print(f'after exploration predecessors dictionary is {predecessors}')
    ##path = get_path(x,y,predecessors)
    ##print(f'path to reach y->{y} from x->{x} is {path}')
    

def explore(adj, start, parent, visited, predecessors):
    #visited[start] = 1
    for neighbour in start:
         if not visited[neighbour]:
             visited[neighbour] = 1
             predecessors[neighbour] = parent
             explore(adj, adj[neighbour], neighbour, visited, predecessors)         
    return

def get_path(start, goal, predecessors):
    if start == goal or goal not in predecessors:
        return 0
    
    path = []
    current = goal
    while current != start:
        path.append(current)
        current = predecessors[current] 
    
    path.append(start)
    #return(path.reverse()) ## This returns None..2 steps required
    #first reverse then return the path as reverse is in place modification returns none
    path.reverse()
    return path
        
# enter ctrl + z after entering the input in the format specified in pdf e.g.

 # PS C:\Users\asati\Documents\Coursera Graph\Week1\week1_graph_decomposition1\1_finding_exit_from_maze> & C:/Users/asati/AppData/Local/Programs/Python/Python310/python.exe "c:/Users/asati/Documents/Coursera Graph/Week1/week1_graph_decomposition1/1_finding_exit_from_maze/reachability.py"
 #   4 2
 #   1 2
 #   3 2
 #   1 4
 #   ^Z to end input on a line of its own
 #   0 return value of reach

    
if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    print(data)
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    print(edges)
    x, y = data[2 * m:] # i.e. x, y is the start, end of search and located at last starting index is 2*m (number of edges)
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1 # since indexes are zero based adjust 
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))
