def firstDuplicateValue(l):
    duplicates = {}
    more_than_one = []
    if not l or len(l) == len(set(l)):
        return -1

    for e in set(l):
        if l.count(e) > 1:
            more_than_one.append(e)

    for e in more_than_one:
        duplicates[l.index(e, l.index(e) + 1)] = e
    return duplicates[min(list(duplicates.keys()))]
