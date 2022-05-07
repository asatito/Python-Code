#Uses python3

import sys


def number_of_components(adj):
    result = 0
    #write your code here
    
 # home keeping variables
    visited = [0]*len(adj)
    component_num = 0
    
    # if the graph is connected then the first call itself will mar all nodes as visited
    # due to recursive calls made by explore, however for uncconected graphs the for loop
    # will enter the body of loop and increment the component number
    for node in range(len(adj)):
        if not visited[node]:
            visited[node] = 1
            component_num += 1            
            explore(adj, adj[node], visited)
    
    return component_num
    

def explore(adj, start, visited):
    for neighbour in start:
         if not visited[neighbour]:
             visited[neighbour] = 1
             # please see that this is dfs ..for the neighbour we start exploring its adjacency list adj[neighbour] 
             # as shown in the call below
             explore(adj, adj[neighbour], visited)         
    return

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
        adj[b - 1].append(a - 1)
    print(number_of_components(adj))
