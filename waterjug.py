from collections import deque

def is_visited(state, visited):
    return state in visited

def water_jug_bfs():
    max_a, max_b = 6, 5
    visited = set()
    queue = deque()

    queue.append((0, 0))

    while queue:
        a, b = queue.popleft()

        if (a, b) in visited:
            continue

        visited.add((a, b))
        print(f"Jug A: {a}L, Jug B: {b}L")

        if a == 3 or b == 3:
            print("Found a solution!")
            return

        # All possible actions from current state
        possible_states = [
            (max_a, b),
            (a, max_b),
            (0, b),
            (a, 0),
            (min(a + b, max_a), b - (min(a + b, max_a) - a)),
            (a - (min(a + b, max_b) - b), min(a + b, max_b))
        ]

        for state in possible_states:
            if state not in visited:
                queue.append(state)

    print("No solution found!")

water_jug_bfs()
