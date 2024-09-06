import simpy
import random
import matplotlib.pyplot as plt

class ServiceSystem:
    def __init__(self, env, num_servers, service_rate):
        self.env = env
        self.server = simpy.Resource(env, num_servers)
        self.service_rate = service_rate
        self.queue_length = []
    
    def service(self, arrival_time):
        with self.server.request() as req:
            yield req
            yield self.env.timeout(random.expovariate(self.service_rate))
            self.queue_length.append(len(self.server.queue))

def customer_arrival(env, system):
    while True:
        yield env.timeout(random.expovariate(1.0)) # Время обслуживания на человека генерируется рандомно
        # yield env.timeout(0.1) # Время обслуживания на человека константное
        env.process(system.service(env.now))

def run_simulation(num_servers_list, service_rates):
    for system_id in range(0, 2):
      env = simpy.Environment()
      system = ServiceSystem(env, num_servers_list[system_id], service_rates[system_id])
      env.process(customer_arrival(env, system))
      env.run(until=500)
      plt.plot(system.queue_length, label=f'Приборы: {num_servers_list[system_id]};\nИнтенсивность: {service_rates[system_id]}\nДлина очереди: {system.queue_length[-1]}')

    plt.xlabel('Время')
    plt.ylabel('Длина очереди')
    plt.legend()
    plt.show()

num_servers_list = [1, 3]
service_rates = [0.9, 0.3]

run_simulation(num_servers_list, service_rates)