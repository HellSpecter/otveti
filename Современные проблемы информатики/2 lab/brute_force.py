import itertools
import random
import time
import matplotlib.pyplot as plt

def generate_random_jobs(count, seed=None):
    random.seed(seed)
    return [(random.randint(1, 10), random.randint(1, 10)) for _ in range(count)]


def calculate_total_processing_time(order, jobs):
    machine_1_time = 0
    machine_2_time = 0

    for i in order:
        machine_1_time += jobs[i][0]
        machine_2_time = max(machine_1_time, machine_2_time) + jobs[i][1]

    return machine_2_time


def brute_force_johnson(jobs):
    n = len(jobs)
    all_orders = list(itertools.permutations(range(n)))
    
    min_total_time = float('inf')
    optimal_order = None
    
    for order in all_orders:
        total_time = calculate_total_processing_time(order, jobs)
        if total_time < min_total_time:
            min_total_time = total_time
            optimal_order = order
    
    return optimal_order


def main():
    # jobs - время обработки (x, y), где x - время на 1 станке, y - время на 2 станке
    min_job_count = 4
    max_job_count = 10
    seed_value = 41

    x = []
    y = []

    for i in range(min_job_count, max_job_count + 1):
        start_time = time.time()
        
        jobs =  generate_random_jobs(i, seed = seed_value)
        optimal_order = brute_force_johnson(jobs)

        end_time = time.time()
        execution_time = end_time - start_time
        x.append(i)
        y.append(execution_time)
        
        print(f"----------- {i} ДЕТАЛИ(-ЛЬ) -----------")
        print(f"Информация о деталях: {jobs}")   
        print(f"Оптимальный порядок выполнения задач: {optimal_order}")
        print(f"Время выполнения: {execution_time} сек.")
        print("\n")

    plt.xticks(range(min(x), max(x)+1, 1))
    plt.plot(x, y)
    plt.show()

if __name__ == "__main__":
    main()