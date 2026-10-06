def associative():
    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    c = int(input("Enter value of c: "))

    # Addition
    print("Associative law for Addition")
    lhs = a + (b + c)
    rhs = (a + b) + c

    if lhs == rhs:
        print("LHS =", lhs)
        print("RHS =", rhs)
        print("Associative law satisfied")
    else:
        print("Associative law not satisfied")

    # Multiplication
    print("Associative law for Multiplication")
    lhs = a * (b * c)
    rhs = (a * b) * c

    if lhs == rhs:
        print("Associative law satisfied")
    else:
        print("Associative law not satisfied")

    # Boolean AND
    print("Associative law for Boolean AND")
    lhs = a and (b and c)
    rhs = (a and b) and c

    if lhs == rhs:
        print("Associative law satisfied")
    else:
        print("Associative law not satisfied")

    # Boolean OR
    print("Associative law for Boolean OR")
    lhs = a or (b or c)
    rhs = (a or b) or c

    if lhs == rhs:
        print("Associative law satisfied")
    else:
        print("Associative law not satisfied")


associative()
