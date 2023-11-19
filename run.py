# Search methods

import search

problem = search.Problem

ab = search.GPSProblem('A', 'B', search.romania)
print("------------------A and B------------------\n")
print("Without Subestimation\n")
result = search.branch_and_bound_search(ab)
print("\tPath:", result.path())
print("\nWith Subestimation\n")
result2 = search.branch_and_bound_search_with_sub(ab)
print("\tQuality Solution (1 / shortest solution length): ", round(1 / len(result2.path()), 2))
print("\tComparison with breadth_first: ", round(1 / len(search.breadth_first_graph_search(ab).path()), 2))
print("\tComparison with depth_first: ", round(1 / len(search.depth_first_graph_search(ab).path()), 2))
print("\tPath:", result2.path())

zg = search.GPSProblem('Z', 'G', search.romania)
print("\n------------------Z and G------------------\n")
print("Without Subestimation\n")
result = search.branch_and_bound_search(zg)
print("\tPath:", result.path())
print("\nWith Subestimation\n")
result2 = search.branch_and_bound_search_with_sub(zg)
print("\tQuality Solution (1 / shortest solution length): ", round(1 / len(result2.path()), 2))
print("\tComparison with breadth_first: ", round(1 / len(search.breadth_first_graph_search(zg).path()), 2))
print("\tComparison with depth_first: ", round(1 / len(search.depth_first_graph_search(zg).path()), 2))
print("\tPath:", result2.path())

bl = search.GPSProblem('B', 'L', search.romania)
print("\n------------------B and L------------------\n")
print("Without Subestimation\n")
result = search.branch_and_bound_search(bl)
print("\tPath:", result.path())
print("\nWith Subestimation\n")
result2 = search.branch_and_bound_search_with_sub(bl)
print("\tQuality Solution (1 / shortest solution length): ", round(1 / len(result2.path()), 2))
print("\tComparison with breadth_first: ", round(1 / len(search.breadth_first_graph_search(bl).path()), 2))
print("\tComparison with depth_first: ", round(1 / len(search.depth_first_graph_search(bl).path()), 2))
print("\tPath:", result2.path())


# print(search.branch_and_bound_search(ab).path()) # Result: [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>]
# print(search.branch_and_bound_search_with_sub(ab).path())
#print(search.breadth_first_graph_search(ab).path())
#print(search.depth_first_graph_search(ab).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450