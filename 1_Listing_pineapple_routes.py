import itertools

portnames = ["PAN", "AMS", "CAS", "NYC", "HEL"]


def permutations(route, ports):
    for p in list(itertools.permutations(ports)):
        l = list(p)
        l.insert(0, 0)
        print(' '.join([portnames[i] for i in l]))


# this will start the recursion with 0 as the first stop
permutations([0], list(range(1, len(portnames))))