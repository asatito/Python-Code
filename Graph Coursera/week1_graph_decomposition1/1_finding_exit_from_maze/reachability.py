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
    

def explore(adj, start, parent, visited, predecessors):
    #visited[start] = 1
    for neighbour in start:
         if not visited[neighbour]:
             visited[neighbour] = 1
             predecessors[neighbour] = parent
             explore(adj, adj[neighbour], neighbour, visited, predecessors)         
    return


if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    x, y = data[2 * m:]
    adj = [[] for _ in range(n)]
    x, y = x - 1, y - 1
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(reach(adj, x, y))