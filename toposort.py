#Uses python3

import sys
def toposortUtil(v,used,stack,adj):
	used[v]=1
	for i in adj[v]:
		if used[i]==0:
			toposortUtil(i,used,stack,adj)
	stack.insert(0,v)

def toposort(adj):
	used=[0]*len(adj)
	stack=[]
	for i in range(len(adj)):
		if used[i]==0:
			toposortUtil(i,used,stack,adj)
	return stack

	
if __name__ == '__main__':
    #input = sys.stdin.read()
    #data = list(map(int, input.split()))
    data=[4,3,1,2,4,1,3,1]
    #data=[4,1,3,1]
    #data=[5,7,2,1,3,2,3,1,4,3,4,1,5,2,5,3]
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    adj = [[] for _ in range(n)]
    for (a, b) in edges:
        adj[a - 1].append(b - 1)
    order = toposort(adj)
    for x in order:
        print(x + 1, end=' ')

