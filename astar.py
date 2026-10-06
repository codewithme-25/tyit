graph = {
    'A': ({'B': 5, 'C': 1}, 6),
    'B': ({'C': 1}, 2),
    'C': ({'E': 2}, 5),
    'D': ({'E': 1}, 3),
    'E': ({'F': 2}, 2),
    'F': ({}, 0)
}


def get_min(q):
    mn = None
    min_value = float('inf')

    for i in q:
        value = q[i][0] + q[i][1]

        if value < min_value:
            min_value = value
            mn = i

    return mn


def a_star(graph, prev, dst, path, pcost, q):
    mn = get_min(q)

    if mn is None:
        return []

    q.pop(mn)

    print("Connected nodes of current node", prev, "with h(n) value")

    for n in graph[prev][0]:

        if n not in path:

            h = graph[n][1]
            edge_cost = graph[prev][0][n]

            q[n] = (h, edge_cost)

            print(n, "-->", q[n])

            add1 = h + edge_cost
            path_cost = pcost + add1

            print("A* value for", n, "is:", path_cost)

    while q:

        mn = get_min(q)

        print("Selecting minimum vertex:", mn)
        print("------------------------------")

        if dst == mn:
            return path + [dst]

        pc = pcost + q[mn][1]

        print("Previous path cost:", pc)

        new_path = a_star(
            graph,
            mn,
            dst,
            path + [mn],
            pc,
            q
        )

        if new_path:
            return new_path

    return []


source = input("Enter source vertex: ")
dest = input("Enter destination vertex: ")
heuristic = int(input("Enter given heuristic value for source: "))

if source not in graph or dest not in graph:
    print("Invalid source or destination vertex")
else:
    path = a_star(
        graph,
        source,
        dest,
        [],
        0,
        {source: (heuristic, 0)}
    )

    if path:
        print("Path:", path)
    else:
        print("Path not found")
