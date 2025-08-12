S1 = {1,2,3,4,5,6}

S2 = {4,5,6,7,8,9}

print(len(S1))

S1.remove(4)

S2.pop()

union = S1.union(S2)

Intersection = S1.intersection(S2)
print(union)
print(Intersection)