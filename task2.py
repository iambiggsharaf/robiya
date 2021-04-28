cities = [
    ["Almaty", 100],
    ["Dushanbe", 5],
    ["France", 55],
    ["Germany", 25],
]

def find_city(cities, population):
    for i in cities:
        if i[1] == population:
            return i[0]
            break

def find_population(cities, city_name):
    low = 0
    high = len(cities) - 1
    mid = 0
 
    while low <= high:
 
        mid = (high + low) // 2
 
        # If city name is greater, ignore left half
        if cities[mid][0] < city_name:
            low = mid + 1
 
        # If city name is smaller, ignore right half
        elif cities[mid][0] > city_name:
            high = mid - 1
 
        # means x is present at mid
        else:
            return cities[mid][1]
 
    # If we reach here, then the element was not present
    return -1
    

print(find_city(cities, 5))
print(find_population(cities, "France"))
    



