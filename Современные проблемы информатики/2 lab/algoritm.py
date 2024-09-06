import random
import time
import matplotlib.pyplot as plt

def generate_random_jobs(count, seed=None):
    random.seed(seed)
    return [(random.randint(1, 10), random.randint(1, 10)) for _ in range(count)]

def johnson_algorithm(jobs):
    machine_1 = []
    machine_2 = []
    
    for job in jobs:
        if job[0] <= job[1]:
            machine_1.append((job[0], job[1], jobs.index(job)))
        else:
            machine_2.append((job[0], job[1], jobs.index(job)))
    
    machine_1.sort(key=lambda x: x[0])
    
    machine_2.sort(key=lambda x: x[1], reverse=True)
    
    ordered_jobs = machine_1 + machine_2
    
    job_order = [job[2] for job in ordered_jobs]
    
    return job_order

def main():
    # jobs - время обработки (x, y), где x - время на 1 станке, y - время на 2 станке
    min_job_count = 1099
    max_job_count = 1101
    seed_value = 41

    x = []
    y = []

    for i in range(min_job_count, max_job_count + 1):
        start_time = time.time()
        
        jobs = generate_random_jobs(i, seed = seed_value)
        optimal_order = johnson_algorithm(jobs)

        end_time = time.time()
        execution_time = end_time - start_time
        x.append(i)
        y.append(execution_time)
        
        print(f"----------- {i} ДЕТАЛИ(-ЛЬ) -----------")
        # print(f"Информация о деталях: {jobs}")   
        # print(f"Оптимальный порядок выполнения задач: {optimal_order}")
        print(f"Время выполнения: {execution_time} сек.")
        print("\n")

    plt.xticks(range(min(x), max(x)+1, 1))
    plt.plot(x, y)
    plt.show()

if __name__ == "__main__":
    main()