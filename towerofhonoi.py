A = [3, 2, 1]
B = []
C = []

def display():
    print("\nA:", A)
    print("B:", B)
    print("C:", C)


rods = {'A': A, 'B': B, 'C': C}
moves = 0

while C != [3, 2, 1]:
    display()

    source = input("\nMove from (A/B/C): ").upper()
    destination = input("Move to (A/B/C): ").upper()

    if source not in rods or destination not in rods:
        print("Invalid rod! Choose A, B, or C")
        continue

    if not rods[source]:
        print("Source rod is empty!")
        continue

    if rods[destination] and rods[destination][-1] < rods[source][-1]:
        print("Invalid Move! Larger disk cannot be placed on a smaller disk.")
        continue

    disk = rods[source].pop()
    rods[destination].append(disk)
    moves += 1

display()

print("\nCongratulations! You solved the Tower of Hanoi!!!")
print("Total moves:", moves)
