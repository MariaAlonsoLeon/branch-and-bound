# Search methods

import search

ab = search.GPSProblem('A', 'B', search.romania)
problem = search.Problem
print("------------------A and B------------------\n")
print("Without Subestimation\n")
result = search.branch_and_bound_search(ab)
print("\tPath:", result.path())
print("\nWith Subestimation\n")
result2 = search.branch_and_bound_search_with_sub(ab)
print("\tPath:", result2.path())


zg = search.GPSProblem('Z', 'G', search.romania)
result = search.branch_and_bound_search(zg)
result2 = search.branch_and_bound_search_with_sub(zg)
print("------------------Z and G------------------\n")
print("Without Subestimation\n")
print("\tPath:", result.path())
print("\nWith Subestimation\n")
print("\tPath:", result2.path())
print("------------------------------------------------------")


bl = search.GPSProblem('B', 'L', search.romania)
result = search.branch_and_bound_search(bl)
result2 = search.branch_and_bound_search_with_sub(bl)
print("------------------B and L------------------\n")
print("Without Subestimation\n")
print("\tPath:", result.path())
print("\nWith Subestimation\n")
print("\tPath :", result2.path())

# print(search.branch_and_bound_search(ab).path()) # Result: [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>]
# print(search.branch_and_bound_search_with_sub(ab).path())

# print(search.breadth_first_graph_search(ab).path())
# print(search.depth_first_graph_search(ab).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450