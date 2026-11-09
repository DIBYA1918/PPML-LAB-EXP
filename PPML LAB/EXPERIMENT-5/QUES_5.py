A = {10, 20, 30, 40, 50}
B = {30, 40, 50, 60, 70}

print("Union:", A | B)
print("Intersection:", A & B)
print("Difference A-B:", A - B)
print("Difference B-A:", B - A)
print("Symmetric Difference:", A ^ B)
print("Is A subset of B:", A.issubset(B))
print("Is A superset of B:", A.issuperset(B))
print("Are A and B disjoint:", A.isdisjoint(B))