"""HW02 — Courier Handoffs (BFS Shortest Path)

Provides bfs_path(graph, s, t) which returns a shortest path (fewest edges)
from s to t as a list of nodes, or None when no path exists.

Complexity: O(V + E) time, O(V) extra space for parent/visited.
"""

from collections import deque


def bfs_path(graph, s, t):
    """Return a shortest path (fewest edges) from s to t as a list of nodes.

    If s == t, return [s]. If s or t not in graph, return None.
    """

    # Quick checks
    if s == t:
        return [s] if s in graph else None

    if s not in graph or t not in graph:
        return None

    q = deque([s])
    visited = {s}
    parent = {}  # child -> parent mapping for path reconstruction

    while q:
        node = q.popleft()
        for nbr in graph.get(node, []):
            if nbr in visited:
                continue
            parent[nbr] = node
            if nbr == t:
                # reconstruct path from s to t
                path = [t]
                while path[-1] != s:
                    path.append(parent[path[-1]])
                path.reverse()
                return path
            visited.add(nbr)
            q.append(nbr)

    return None
