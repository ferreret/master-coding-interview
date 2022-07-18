# Given 2 arrays, create a function that
# let's a user know (true/false) wheteher these two arrays contain any common items

# For example:

list1 = ["a", "b", "c", "x"]
list2 = ["z", "y", "i"]
# should return false
# -----------------------------------------------------------------------------------
list3 = ["a", "b", "c", "x"]
list4 = ["z", "y", "x"]
# should return true


def common_items(list1, list2):
    common = set(list1) & set(list2)
    return len(common) > 0


print(common_items(list1, list2))
print(common_items(list3, list4))
