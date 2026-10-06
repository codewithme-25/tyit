graph = {
    'A': ({'B': 5, 'C': 1}, 6),
    'B': ({'C': 1}, 2),
    'C': ({'E': 2}, 5),
    'D': ({'E': 1}, 3),
    'E': ({'F': 2}, 2),
    'F': ({}, 0)
}


def get_min(q):
    mn = (0, (0, float('inf')))

    for i in q:
        if sum(q[i]) < sum(mn[1]):
            mn = (i, q[i])

    return mn[0]


def a_star(graph, prev, dst, path, pcost, q):
    mn = get_min(q)
    q.pop(mn)

    print("Connected nodes of current node", prev, "with h(n) value")

    for n in graph[prev][0]:
        if n not in path:
            q[n] = (graph[n][1], graph[prev][0][n])

            print(n, "-->", q[n])

            add1 = sum(q[n])
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

path = a_star(
    graph,
    source,
    dest,
    [],
    0,
    {source: (heuristic, 0)}
)

if path:
    print(path)
else:
    print("Path not found")
