def boooo(n):
    for _ in range(len(n)):
        print("boooo!")


boooo([1, 2, 3, 4, 5])  # O(1)


def arrayOfHintTimes(n):
    hiList = []
    for _ in range(n):
        hiList.append("hi")
    return hiList


arrayOfHintTimes(6)  # O(n)
