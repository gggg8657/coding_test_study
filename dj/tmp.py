from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write

def dfs(edges, v, visited):
    stack = [v]
    while stack:
        node = stack.pop()
        if not visited[node]:
            visited[node] = True
            print(f"{node} ")
            stack.extend(reversed(edges[node]))  # reverse to simulate recursive DFS order

def bfs(edges, v, visited):
    queue = deque([v])
    visited[v] = True
    while queue:
        node = queue.popleft()
        print(f"{node} ")
        for neighbor in edges[node]:
            if not visited[neighbor]:
                queue.append(neighbor)
                visited[neighbor] = True

if __name__ == '__main__':
    n, m, v = map(int, input().split())
    edges = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b = map(int, input().split())
        edges[a].append(b)
        edges[b].append(a)

    for edge_list in edges:
        edge_list.sort()

    visited = [False] * (n + 1)
    dfs(edges, v, visited)
    print('\n')
    visited = [False] * (n + 1)
    bfs(edges, v, visited)
    print('\n')
