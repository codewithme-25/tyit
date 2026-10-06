graph = {
    'S': ({'A': 2, 'E': 3}, 6),
    'A': ({'S': 2, 'D': 1}, 3),
    'B': ({'C': 3, 'D': 3}, 2),
    'C': ({'B': 3, 'G': 2}, 2),
    'D': ({'A': 1, 'B': 3, 'G': 2}, 4),
    'E': ({'S': 3, 'G': 2}, 5),
    'G': ({}, 0)
}


def greedy_search_rec(graph, prev, dest, path, q):

    neighbours = graph[prev][0].keys()

    for n in neighbours:
        if n not in path:
            q[n] = graph[n][1]
            print(n, "->", q[n])

    while q:

        mn = min(q, key=q.get)

        print("Taking minimum h(n) vertex:", mn)

        if dest == mn:
            return path + [dest]

        del q[mn]

        new_path = greedy_search_rec(
            graph,
            mn,
            dest,
            path + [mn],
            q
        )

        if new_path:
            return new_path

    return []


source = input("Enter source vertex: ")

if source not in graph:
    print("Invalid source vertex")
else:
    result = greedy_search_rec(
        graph,
        source,
        'G',
        [source],
        {}
    )

    if result:
        print("Resulting path:", result)
    else:
        print("Path not found")
