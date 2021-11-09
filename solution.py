from collections import defaultdict

# DFS implementation: https://stackoverflow.com/a/29321323
def DFS(G, v, seen=None, path=None):
    if seen is None: seen = []
    if path is None: path = [v]

    seen.append(v)

    paths = []
    for t in G[v]:
      if t not in seen:
        t_path = path + [t]
        paths.append(tuple(t_path))
        paths.extend(DFS(G, t, seen[:], t_path))
    return paths


def solve(startTimes, endTimes):
  # Create the Adjecency Graph
  graph = defaultdict(list)
  n = len(startTimes)

  for i in range(n):
    start = startTimes[i]
    end = endTimes[i]
    graph[start].append(end)
  
  # Add starting node to all nodes because any event can be the first event
  graph[0] = startTimes

  # Run DFS
  all_paths = DFS(graph, 0)
  # Remove two becuase we are counting the edges, not the nodes (-1) and we want to remove
  # the first edge from node 0 to the starting node, because that was only used in the DFS
  # phase and not in the final schedule.
  max_len   = max(len(p) for p in all_paths) - 2

  print("Most events visited:")
  print(max_len)


if __name__ == "__main__":
  startTimes = [1, 1, 2, 3, 4]
  endTimes = [5, 4, 3, 4, 5]
  solve(startTimes, endTimes)
