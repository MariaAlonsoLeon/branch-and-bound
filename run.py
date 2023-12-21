# Search methods

import search

problem = search.Problem

# ROMANIA

ab = search.GPSProblem('A', 'B', search.romania)
print("------------------A y B------------------\n")
print("Sin Subestimación\n")
result = search.branch_and_bound_search(ab)
print("\tPath:", result.path())
print("\nCon Subestimación\n")
result2 = search.branch_and_bound_search_with_sub(ab)
print("\tCalidad de la solución (1 / longitud de la solución más corta): ", round(1 / len(result2.path()), 2))
#print("\tComparación con anchura: ", round(1 / len(search.breadth_first_graph_search(ab).path()), 2))
# print("\tComparación con profundidad: ", round(1 / len(search.depth_first_graph_search(ab).path()), 2))
print("\tPath:", result2.path())

zg = search.GPSProblem('Z', 'G', search.romania)
print("\n------------------Z y G------------------\n")
print("Sin Subestimación\n")
result = search.branch_and_bound_search(zg)
print("\tPath:", result.path())
print("\nCon Subestimación\n")
result2 = search.branch_and_bound_search_with_sub(zg)
print("\tCalidad de la solución (1 / longitud de la solución más corta): ", round(1 / len(result2.path()), 2))
# print("\tComparación con anchura: ", round(1 / len(search.breadth_first_graph_search(zg).path()), 2))
# print("\tComparación con profundidad: ", round(1 / len(search.depth_first_graph_search(zg).path()), 2))
print("\tPath:", result2.path())

bl = search.GPSProblem('B', 'L', search.romania)
print("\n------------------B y L------------------\n")
print("Sin Subestimación\n")
result = search.branch_and_bound_search(bl)
print("\tPath:", result.path())
print("\nCon Subestimación\n")
result2 = search.branch_and_bound_search_with_sub(bl)
print("\tCalidad de la solución (1 / longitud de la solución más corta): ", round(1 / len(result2.path()), 2))
# print("\tComparación con anchura: ", round(1 / len(search.breadth_first_graph_search(bl).path()), 2))
# print("\tComparación con profundidad: ", round(1 / len(search.depth_first_graph_search(bl).path()), 2))
print("\tPath:", result2.path())


# print(search.branch_and_bound_search(ab).path()) # Result: [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>]
# print(search.branch_and_bound_search_with_sub(ab).path())
#print(search.breadth_first_graph_search(ab).path())
#print(search.depth_first_graph_search(ab).path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450


# Australia
ab = search.GPSProblem('WA', 'V', search.australia)
print("------------------WA y V------------------\n")
print("Sin subestimación\n")
result = search.branch_and_bound_search(ab)
print("\tPath:", result.path())
print("\nCon Subestimación\n")
result2 = search.branch_and_bound_search_with_sub(ab)
print("\tCalidad de la solución (1 / longitud de la solución más corta): ", round(1 / len(result2.path()), 2))
# print("\tComparación con anchura: ", round(1 / len(search.breadth_first_graph_search(ab).path()), 2))
# print("\tComparación con profundidad: ", round(1 / len(search.depth_first_graph_search(ab).path()), 2))
print("\tPath:", result2.path())

zg = search.GPSProblem('NT', 'NSW', search.australia)
print("\n------------------NT and NSW------------------\n")
print("Sin Subestimación\n")
result = search.branch_and_bound_search(zg)
print("\tPath:", result.path())
print("\nCon Subestimación\n")
result2 = search.branch_and_bound_search_with_sub(zg)
print("\tCalidad de la solución (1 / longitud de la solución más corta): ", round(1 / len(result2.path()), 2))
# print("\tComparación con anchura: ", round(1 / len(search.breadth_first_graph_search(zg).path()), 2))
# print("\tComparación con profundidad: ", round(1 / len(search.depth_first_graph_search(zg).path()), 2))
print("\tPath:", result2.path())

bl = search.GPSProblem('Q', 'V', search.australia)
print("\n------------------Q y V------------------\n")
print("Sin Subestimación\n")
result = search.branch_and_bound_search(bl)
print("\tPath:", result.path())
print("\nCon Subestimación\n")
result2 = search.branch_and_bound_search_with_sub(bl)
print("\tCalidad de la solución (1 / longitud de la solución más corta): ", round(1 / len(result2.path()), 2))
# print("\tComparación con anchura: ", round(1 / len(search.breadth_first_graph_search(bl).path()), 2))
# print("\tComparación con profundidad: ", round(1 / len(search.depth_first_graph_search(bl).path()), 2))
print("\tPath:", result2.path())


print("______________________________________Comparación______________________________________")
ab = search.GPSProblem('A', 'B', search.romania)

print("-Profunidad\n")
#print(search.depth_first_graph_search(ab).path())
print("\tCalidad de la solución (1 / longitud de la solución más corta): ", round(1 / len(search.depth_first_graph_search(ab).path()), 2))

print("-Anchura\n")
#print(search.breadth_first_graph_search(ab).path())
print("\tCalidad de la solución (1 / longitud de la solución más corta): ", round(1 / len(search.breadth_first_graph_search(ab).path()), 2))

print("-B&B sin subestimación\n")
#print(search.branch_and_bound_search(ab).path())
print("\tCalidad de la solución (1 / longitud de la solución más corta): ", round(1 / len(search.branch_and_bound_search(ab).path()), 2))

print("-B&B con subestimación\n")
#print(search.branch_and_bound_search_with_sub(ab).path())
print("\tCalidad de la solución (1 / longitud de la solución más corta): ", round(1 / len(search.branch_and_bound_search_with_sub(ab).path()), 2))