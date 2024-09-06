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

def brute_force_tsp(dotCount, debug):
    points = [(i, j) for i in range(dotCount) for j in range(dotCount)]
    alphabet = string.ascii_uppercase
    letterIndex = 0
    if debug:
        print(f"Пути для точек:")
        for i in range(0, dotCount ** 2):
            if i % dotCount == 0:
                print(f"\nПути для точки {letterIndex}")
                letterIndex += 1
                
            print(f"{points[i]}")
    
    all_paths = list(itertools.permutations(range(dotCount)))
    min_distance = float('inf')
    best_path = None

    for path in all_paths:
        distance = total_distance(path, points)
        if distance < min_distance:
            min_distance = distance
            best_path = path

    return best_path, min_distance


def main():
    dotMin = 4
    dotMax = 10

    x = []
    y = []
    
    print("МЕТОД ПЕРЕБОРА\n")
    for i in range(dotMin, dotMax + 1):
        print(f"------------------ {i} ТОЧКИ(-ЕК) ------------------")
        start_time = time.time()
        best_path, min_distance = brute_force_tsp(i, False)
        print("Лучший путь:", best_path)
        print("Минимальная дистанция:", min_distance)
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
