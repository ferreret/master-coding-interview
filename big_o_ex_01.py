def funChallenge(input):
    a = 10  # O(1)
    a = 50 + 3  # O(1)

    for i in range(len(input)):  # O(n) n -> Size of input
        anotherFunction()  # O(n)
        stranger = True  # O(n)
        a += 1  # O(n)

    return a  # O(1)


def anotherFunction():
    pass


funChallenge([1, 2, 3, 4, 5])

# 3 single steps + n + n + n + n
# BIG O(3 + 4*n)
