def anotherFuChallenge(input):
    a = 5  # O(1)
    b = 10  # O(1)
    c = 50  # O(1)

    x, y, z = 0  # O(1)
    for i in range(len(input)):  # O(n)
        x += 1  # O(n)
        y += 1  # O(n)
        z += 1  # O(n)

    p, q = 0  # O(1)
    for j in range(len(input)):  # O(n)
        p = j * 2  # O(n)
        q = j * 2  # O(n)

    whoAmI = "I don't know"  # O(1)


anotherFuChallenge([1, 2, 3, 4, 5])

# BIG O(6 + 7*n)
