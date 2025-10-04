"""
Tarjan’s Algorithm Variant — Articulation Points (Cut Vertices)

Concept:
--------
An articulation point (or cut vertex) in an undirected graph is a vertex
whose removal increases the number of connected components.

We use DFS with discovery time (disc) and low-link values:
- Root vertex is articulation point if it has >1 DFS children.
- Non-root vertex u is articulation point if there exists a child v such that:
    low[v] >= disc[u]

Time Complexity: O(V + E)
Space Complexity: O(V)
"""

from typing import List

class Solution:
    def articulationPoints(self, n: int, edges: List[List[int]]) -> List[int]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        disc = [-1] * n
        low = [0] * n
        parent = [-1] * n
        visited = [False] * n
        ap = [False] * n  # articulation point flags
        time = 0

        def dfs(u: int):
            nonlocal time
            visited[u] = True
            disc[u] = low[u] = time
            time += 1
            child_count = 0

            for v in adj[u]:
                if not visited[v]:
                    parent[v] = u
                    child_count += 1
                    dfs(v)
                    low[u] = min(low[u], low[v])

                    # Condition 1: u is root and has more than one child
                    if parent[u] == -1 and child_count > 1:
                        ap[u] = True

                    # Condition 2: u is not root and low[v] >= disc[u]
                    if parent[u] != -1 and low[v] >= disc[u]:
                        ap[u] = True
                elif v != parent[u]:
                    # Back edge
                    low[u] = min(low[u], disc[v])

        for i in range(n):
            if not visited[i]:
                dfs(i)

        return [i for i, is_ap in enumerate(ap) if is_ap]


# Example:
# sol = Solution()
# print(sol.articulationPoints(5, [[0,1],[0,2],[1,2],[0,3],[3,4]]))
# Output: [0, 3]
# Explanation: Removing 0 or 3 increases the number of connected components.
