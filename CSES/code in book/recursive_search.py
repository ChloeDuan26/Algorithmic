def search(k, n, subset):
    if k == n:
        print(subset)
    else:
        search(k + 1, 3, subset)
        subset.append(k)
        search(k + 1, 3, subset)
        subset.pop()

subset = []
search(0, 3, subset)
