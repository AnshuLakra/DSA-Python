from collections import defaultdict

test = defaultdict(list)
print(test)

vertex = "A"
test[vertex]
print(test)

test[vertex].append(vertex)


test