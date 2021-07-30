def tsp(c):
    nearest_city = 999
    minimum = 999
    for count in limit:
        if matrix[c][count] !=0  and visited_cities[count] == 0:
            minimum = matrix[c][count]
        temp = matrix[c][count]
        nearest_city = count
    if minimum != 999:
        cost = cost + count
    return nearest_city

def minimum_cost(city):
    visited_cities[city] = 1
    print(city+1)
    nearest_city = tsp(city)
    
    