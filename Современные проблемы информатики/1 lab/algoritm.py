import itertools
import string
import time
import matplotlib.pyplot as plt

def calculate_distance(point1, point2):
    return ((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)**0.5

def total_distance(path, points):
    distance = 0
    for i in range(len(path) - 1):
        distance += calculate_distance(points[path[i]], points[path[i + 1]])
    distance += calculate_distance(points[path[-1]], points[path[0]])
    return distance
    
def nearest_neighbor_tsp(dotCount):
    points = [(i, j) for i in range(dotCount) for j in range(dotCount)]
    unvisited = set(range(dotCount))
    current_point = 0
    path = [current_point]
    unvisited.remove(current_point)

    while unvisited:
        nearest_point = min(unvisited, key=lambda x: calculate_distance(points[current_point], points[x]))
        path.append(nearest_point)
        unvisited.remove(nearest_point)
        current_point = nearest_point

    path.append(path[0]) # Замыкаем цикл
    total_distance_nn = total_distance(path, points)
    return path, total_distance_nn

def main():
    dotMin = 4
    dotMax = 10

    x = []
    y = []
    
    print("МЕТОД БЛИЖАЙШИЕ СОСЕДИ\n")
    for i in range(dotMin, dotMax + 1):
        print(f"------------------ {i} ТОЧКИ(-ЕК) ------------------")
        start_time = time.time()
        
        nn_path, nn_distance = nearest_neighbor_tsp(i)
        print("Лучший путь:", nn_path)
        print("Минимальная дистанция:", nn_distance)
        
        end_time = time.time()
        execution_time = end_time - start_time
        
        x.append(i)
        y.append(execution_time)
        
        print(f"Время выполнения: {execution_time} сек.")
        print("\n")

    plt.xticks(range(min(x), max(x)+1, 1))
    plt.plot(x, y)
    plt.show()

if __name__ == "__main__":
    main()