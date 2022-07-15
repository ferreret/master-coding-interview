def printAllNumbersThenAllPairSums(numbers):
    print("These are the numbers:")
    for num in numbers:
        print(num)

    print("And these are their sums:")

    for num in numbers:
        for num2 in numbers:
            print(num + num2)


printAllNumbersThenAllPairSums([1, 2, 3, 4, 5])

# O(n + n^2)) -> O(n^2) always take worst case scenario if the array grows