"""
HW02 — Courier Handoffs (BFS Shortest Path)

Implement:
- bfs_path(graph, s, t)
"""

from collections import deque

def bfs_path(graph, s, t):
    """Return a shortest path (fewest edges) from s to t as a list of nodes.

    If s == t, return [s].
    If s or t not in the graph, return None.
    """

    # ---------------- Pseudocode / Plan ----------------
    # 1. If s == t and s is in graph → return [s].
    # 2. If s or t is not in graph → no path → return None.
    # 3. Use BFS:
    #       queue = start with s
    #       visited = set containing s
    #       parent = dictionary to rebuild path at the end
    #
    # 4. Loop while queue not empty:
    #       pop current node
    #       go through its neighbors
    #       if neighbor not visited:
    #           record parent[neighbor] = current
    #           if neighbor == t → rebuild & return path
    #           mark visited and add to queue
    #
    # 5. If BFS ends without finding t → return None.
    # ----------------------------------------------------

    # Case: start equals target
    if s == t:
        return [s] if s in graph else None

    # Invalid nodes
    if s not in graph or t not in graph:
        return None

    # Initialize BFS structures
    q = deque([s])
    visited = {s}
    parent = {}   # child → parent

    # BFS loop
    while q:
        node = q.popleft()

        for nbr in graph.get(node, []):
            if nbr in visited:
                continue

            parent[nbr] = node

            # Found t → reconstruct path
            if nbr == t:
                path = [t]
                while path[-1] != s:
                    path.append(parent[path[-1]])
                path.reverse()
                return path

            visited.add(nbr)
            q.append(nbr)

    # No path found
    return None


if __name__ == "__main__":
    # optional manual test
    graph = {
        'A': ['B', 'C'],
        'B': ['D'],
        'C': ['D', 'E'],
        'D': ['F'],
        'E': [],
        'F': []
    }
    print(bfs_path(graph, 'A', 'F'))  # Example
