# Tarjan's Algorithm

## Concept
Tarjan's Algorithm is a **Depth-First Search (DFS)** based algorithm used to find **Strongly Connected Components (SCCs)** in a directed graph in **O(V + E)** time.  
It is also used (with slight modifications) to find **Bridges** and **Articulation Points** in an undirected graph.

---

## Intuition (SCCs)
- During DFS, each node is assigned a unique **discovery index**.
- Maintain a `low-link` value that represents the smallest discovery index reachable from that node.
- Nodes are pushed onto a stack when visited.
- When `low[v] == index[v]`, it means `v` is the root of an SCC — pop all nodes until `v` to form that SCC.

---

## Steps (Tarjan for SCCs)
1. Build an adjacency list for the graph.
2. Initialize:
   - `index = 0`
   - `index[v] = -1` for all nodes (unvisited)
   - `low[v] = 0`
   - `stack = []`
   - `onStack[v] = False`
   - `sccs = []`
3. For each unvisited node `v`, call `dfs(v)`:
   - `index[v] = low[v] = index; index += 1`
   - Push `v` to stack, mark `onStack[v] = True`
   - For each neighbor `w`:
     - If `index[w] == -1`: recursively `dfs(w)` and update `low[v] = min(low[v], low[w])`
     - Else if `onStack[w]`: update `low[v] = min(low[v], index[w])`
   - If `low[v] == index[v]`: pop nodes from stack until `v` to form an SCC.
4. Return all SCCs.

---

## Tarjan SCC Pseudocode

```
function TarjanSCC(G):
    index = 0
    stack = empty stack
    for v in V:
        index[v] = -1

    for v in V:
        if index[v] == -1:
            dfs(v)

function dfs(v):
    index[v] = index
    low[v] = index
    index += 1
    push v onto stack
    onstack[v] = true

    for w in neighbors(v):
        if index[w] == -1:
            dfs(w)
            low[v] = min(low[v], low[w])
        else if onstack[w]:
            low[v] = min(low[v], index[w])

    if low[v] == index[v]:
        component = []
        repeat
            w = pop stack
            onstack[w] = false
            add w to component
        until w == v
        output component
```
---

## Tarjan Bridges Pseudocode (low-link variant)

```
function findBridges(G):
    time = 0
    for v in V:
        disc[v] = -1

    for v in V:
        if disc[v] == -1:
            dfs(v, parent = -1)

function dfs(u, parent):
    disc[u] = low[u] = time
    time += 1
    for v in neighbors(u):
        if v == parent: continue
        if disc[v] == -1:
            dfs(v, u)
            low[u] = min(low[u], low[v])
            if low[v] > disc[u]:
                record (u, v) as a bridge
        else:
            low[u] = min(low[u], disc[v])
```

---

## Time and Space Complexity
- **Time Complexity**: `O(V + E)`  
  Each vertex and edge is visited exactly once.
- **Space Complexity**: `O(V)`  
  For recursion stack, stack, and auxiliary arrays.

---

## LeetCode / Practice Problems Using Tarjan’s Algorithm
1. **LeetCode 1192 - Critical Connections in a Network** → Find all bridges.  
2. **Find Strongly Connected Components** → Standard Tarjan SCC implementation.  
3. **Articulation Points in a Graph** → Low-link based DFS variant.

---
