def CityTraffic(strArr):

    city_map ={}
    
    for entry in strArr:
        city, adjacent_cities_str = entry.split(':')
        adjacent_cities = adjacent_cities_str.strip('[]').split(',')
        city_map[city] = adjacent_cities
    city_traffic ={}

    for city in city_map:

        visited = [city]
        neighbors = city_map[city]
        num_roots = len(neighbors)
        Traffic = [0]*num_roots

        for n in range(num_roots):

            current_city = neighbors[n]
            stack = [current_city]

            while stack:

                current_city = stack.pop()

                if current_city not in visited:

                    Traffic[n] += int(current_city)
                    visited.append(current_city)

                    for Neighbors in city_map[current_city]:

                        if Neighbors not in visited:
                            stack.append(Neighbors)
        
        city_traffic[city] = max(Traffic)
        
    sorted_city_traffic = dict(sorted(city_traffic.items(), key=lambda item: int(item[0])))
    
    output_string = ','.join([f"{city}:{traffic}" for city, traffic in sorted_city_traffic.items()])

    return output_string
       

Input = ["1:[5]","4:[5]","3:[5]","5:[1,4,3,2]","2:[5,15,7]","7:[2,8]","8:[7,38]","15:[2]","38:[8]"]


print(CityTraffic(Input))
