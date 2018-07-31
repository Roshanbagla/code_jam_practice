def containsNearbyDuplicate(nums, k):
    unique = []
    results = []
    for index in nums:
        if index not in unique:
            unique.append(index)
    for index in unique:
        g = [i for i, e in enumerate(nums) if e == index]
        length = len(g)
        if length != 1:
            for indices in range(0, length):
                for l in range(indices+1, length):
                    diff = abs(g[indices] - g[l])
                    if diff <= k:
                        results.append('True')
                    else:
                        results.append('False')
        else:
            continue
    if 'True' not in results:
        return False
    else:
        return True

print(containsNearbyDuplicate([1,2,3,1,2,3], 2))
