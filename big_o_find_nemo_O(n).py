import timeit
import functools

nemo = ["nemo"]
everyone = ['dory', 'bruce', 'marlin', 'nemo', 'gill',
            'bloat', 'nigel', 'squirt', 'darla', 'hank']
large = nemo * 10000


def findNemo(fishes):
    for fish in fishes:
        if fish == "nemo":
            print("Found NEMO!")

# t = timeit.Timer(functools.partial(findNemo, large))

# print("The time to find Nemo took", t.timeit(5))


findNemo(large) # O(n) --> Linear Time n:number of inputs, in this case number of fish



