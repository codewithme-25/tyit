def associative():
    # Associative Law for Addition
    print("Associative law for Addition")

    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    c = int(input("Enter value of c: "))

    lhs = a + (b + c)
    rhs = (a + b) + c

    if lhs == rhs:
        print("LHS =", lhs)
        print("RHS =", rhs)
        print("Associative law satisfied")
    else:
        print("Associative law not satisfied")


    # Associative Law for Multiplication
    print("Associative law for Multiplication")

    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    c = int(input("Enter value of c: "))

    lhs = a * (b * c)
    rhs = (a * b) * c

    if lhs == rhs:
        print("LHS =", lhs)
        print("RHS =", rhs)
        print("Associative law satisfied")
    else:
        print("Associative law not satisfied")


    # Associative Law for Boolean AND
    print("Associative law for Boolean AND")

    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    c = int(input("Enter value of c: "))

    lhs = a and (b and c)
    rhs = (a and b) and c

    if lhs == rhs:
        print("Associative law satisfied")
    else:
        print("Associative law not satisfied")


    # Associative Law for Boolean OR
    print("Associative law for Boolean OR")

    a = int(input("Enter value of a: "))
    b = int(input("Enter value of b: "))
    c = int(input("Enter value of c: "))

    lhs = a or (b or c)
    rhs = (a or b) or c

    if lhs == rhs:
        print("Associative law satisfied")
    else:
        print("Associative law not satisfied")


associative()
