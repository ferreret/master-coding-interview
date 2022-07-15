# Log all pairs of array
boxes = ["a", "b", "c", "d", "e"]


def list_all_pairs(boxes):
    for i in range(len(boxes)):
        for j in range(len(boxes)):
            if i != j and i < j:
                print(boxes[i], boxes[j])


list_all_pairs(boxes)

# O(n * n)
# O(n^2) --> Quadratic Time