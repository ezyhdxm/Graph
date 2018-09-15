#Uses python3

import sys

def acyclic(adj):
    lst=[]
    queue=[]
    for node in range(len(adj)):
        if len(adj[node])==0:
            queue.append(node)
    while len(queue)>0:
        node=queue.pop()
        lst.append(node)
        for n in range(len(adj)):
            if node in adj[n]:
                adj[n].remove(node)
                if len(adj[n])==0:
                    if n not in lst:
                        queue.append(n)
    for node in range(len(adj)):
        if len(adj[node])>0:
            return 1
    return 0

if __name__ == '__main__':
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    #data=[5,7,1,2,2,3,1,3,3,4,1,4,2,5,3,5]
    #data=[4,4,1,2,4,1,2,3,3,1]
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    print(acyclic(adj))
