"""
Tarjan's Algorithm — Strongly Connected Components (SCCs)

Utility implementation suitable for directed graphs.
Given `n` nodes numbered 0..n-1 and a list of directed edges,
`stronglyConnectedComponents(n, edges)` returns a list of SCCs
(each SCC is a list of node indices).

Time Complexity: O(V + E)
Space Complexity: O(V)
"""

from typing import List

class Solution:
    def stronglyConnectedComponents(self, n: int, edges: List[List[int]]) -> List[List[int]]:
        adj = [[] for _ in range(n)]
        for u, v in edges:
            adj[u].append(v)

        index = 0
        indices = [-1] * n      # discovery index of node; -1 means unvisited
        low = [0] * n
        onstack = [False] * n
        stack = []
        sccs: List[List[int]] = []

        def dfs(v: int) -> None:
            nonlocal index
            indices[v] = index
            low[v] = index
            index += 1
            stack.append(v)
            onstack[v] = True

            for w in adj[v]:
                if indices[w] == -1:
                    dfs(w)
                    low[v] = min(low[v], low[w])
                elif onstack[w]:
                    low[v] = min(low[v], indices[w])

            # root of SCC
            if low[v] == indices[v]:
                comp = []
                while True:
                    w = stack.pop()
                    onstack[w] = False
                    comp.append(w)
                    if w == v:
                        break
                sccs.append(comp)

        for v in range(n):
            if indices[v] == -1:
                dfs(v)

        return sccs


# Example usage:
# sol = Solution()
# print(sol.stronglyConnectedComponents(5, [[0,1],[1,2],[2,0],[1,3],[3,4]]))
# Output: [[4], [3], [0,2,1]]
