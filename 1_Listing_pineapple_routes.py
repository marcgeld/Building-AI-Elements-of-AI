import itertools

portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]


def permutations(route, ports):
    for p in list(itertools.permutations(ports)):
        li = list(p)
        li.insert(0, 0)
        print(' '.join([portnames[i] for i in li]))


# this will start the recursion with 0 as the first stop
permutations([0], list(range(1, len(portnames))))