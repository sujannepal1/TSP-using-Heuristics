import re
from matplotlib import pyplot as plt
import math
from random import choice


def get_digit_from_roll_number(roll_number, position) -> int:
    return int(str(roll_number)[position])


def get_min_index_of_list_that_are_not_visited(original_data, data_list, visited: list):
    temp = data_list.copy()
    index_of_sorted_value = 0
    unique_sorted_values = sorted(temp)

    for _ in range(len(unique_sorted_values)):
        minimum_value = unique_sorted_values[index_of_sorted_value]
        print(f"Minimum value: {minimum_value}")
        # getting indices when they are duplicate
        reversed_indexes = [
            i for i, x in enumerate(original_data) if x == minimum_value
        ]
        print(f"Reversed indexes: {reversed_indexes}")
        for reversed_index in reversed_indexes:
            if reversed_index not in visited:
                return reversed_index
        index_of_sorted_value += 1


Roll_number = 123456

A = 10 + 2 * get_digit_from_roll_number(Roll_number, -3)
B = 27 + get_digit_from_roll_number(Roll_number, -2)
C = 5 + 3 * get_digit_from_roll_number(Roll_number, -1)
D = 15 + 4 * get_digit_from_roll_number(Roll_number, -2)
E = 5 + 4 * get_digit_from_roll_number(Roll_number, -2)
F = 7 + 5 * get_digit_from_roll_number(Roll_number, -3)

print(f"A: {A}, B: {B}, C: {C}, D: {D}, E: {E}, F: {F}")
city_distance = [
    [0, A, 10, 12, 5, 4, 19, 14, 3, 18, 20, 28],
    [A, 0, 23, 45, B, 45, 24, 9, 34, 12, D, 21],
    [10, 23, 0, 34, 22, 12, C, 23, 22, 21, 4, 12],
    [12, 45, 34, 0, 12, 13, 26, 43, 33, 21, 17, 10],
    [5, B, 22, 12, 0, 25, 21, 5, 7, 22, 17, 22],
    [4, 45, 12, 13, 25, 0, 11, 22, 12, 10, 12, 3],
    [19, 24, C, 26, 21, 11, 0, 20, 33, 11, 24, 11],
    [14, 9, 23, 43, 5, 22, 20, 0, 6, 23, 10, 32],
    [3, 34, 22, 33, 7, 12, 33, 6, 0, 17, 20, 17],
    [18, 12, 21, 21, 22, 10, 11, 23, 17, 0, 21, E],
    [20, D, 4, 17, 17, 12, 24, 10, 20, 21, 0, F],
    [28, 21, 12, 10, 22, 3, 11, 32, 17, E, F, 0],
]


# now i have to solve this by 1st take a random node and travel to the nearest node and then repeat this process until i have visited all the nodes and then return to the starting node

total_cities = len(city_distance)
random_node = choice(range(0, 12))
print(f"Starting from node: {random_node}")
visited = [random_node]
total_distance = 0

while len(visited) < total_cities:
    print(f"Visited cities: {visited}")
    current_city = visited[-1]
    print(f"Current city: {current_city}")
    nearest_city = None
    nearest_distance = float("inf")
    val = [x for x in city_distance[current_city] if x is not None and x != 0]
    print(f"Distances from current city: {val}")
    if val:
        next_city = get_min_index_of_list_that_are_not_visited(
            city_distance[current_city], val, visited
        )
        print(next_city)
        if next_city or next_city == 0:
            visited.append(next_city)
            total_distance += city_distance[current_city][next_city]

# for this problem, we can use the nearest neighbor algorithm to find a solution. The algorithm starts at a random city and repeatedly visits the nearest unvisited city until all cities have been visited. Finally, it returns to the starting city.
# finally add the distance from the last city to the starting city to complete the tour
total_distance += city_distance[visited[-1]][visited[0]]
visited.append(visited[0])  # returning to the starting city
print(f"Final route of cities is: {visited}")
print(f"Total distance traveled: {total_distance}")

# now using two optt algorithm to optimize the route

# find two adjacent sides

# replace them wiith the other two sides

# calculate the distance of the new route


# accept the new route if it is shorter than the previous route
def calculate_route_distance(route, distance_matrix):
    total = 0
    n = len(route)

    for i in range(n - 1):
        total += distance_matrix[route[i]][route[i + 1]]

    # return to starting city
    total += distance_matrix[route[-1]][route[0]]

    return total


def two_opt_swap(route, i, k):
    return route[:i] + route[i : k + 1][::-1] + route[k + 1 :]


def two_opt(route, distance_matrix):
    best_route = route
    best_distance = calculate_route_distance(best_route, distance_matrix)

    for i in range(1, 500):
        for i in range(1, len(best_route) - 2):
            for k in range(i + 1, len(best_route)):
                new_route = two_opt_swap(best_route, i, k)
                new_distance = calculate_route_distance(new_route, distance_matrix)

                if new_distance < best_distance:
                    best_route = new_route
                    best_distance = new_distance

        route = best_route

    return best_route, best_distance


print("Nearest Neighbor Route:", visited)

initial_distance = calculate_route_distance(visited, city_distance)
print("Distance before 2-Opt:", initial_distance)

optimized_route, optimized_distance = two_opt(visited, city_distance)

print("Optimized Route:", optimized_route)
print("Distance after 2-Opt:", optimized_distance)
