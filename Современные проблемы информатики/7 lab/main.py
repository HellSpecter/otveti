import simpy
import numpy as np
import matplotlib.pyplot as plt

class ServiceSystem:
  def __init__(self, env, service_rate):
    self.env = env
    self.service_rate = service_rate
    self.server = simpy.Resource(env, capacity=1)
    self.queue_length = []

  def process_request(self, arrival_time, erlang = False):
    with self.server.request() as req:
      yield req
      service_time = np.random.exponential(1 / self.service_rate)
      yield self.env.timeout(service_time)

      if erlang:   
        self.queue_length.append(len(self.server.queue))

def generate_requests(env, arrival_rate, system):
  while True:
    arrival_time = env.now
    system.queue_length.append(len(system.server.queue))
    yield env.timeout(np.random.exponential(1 / arrival_rate))
    env.process(system.process_request(arrival_time))

def generate_requests_poisson(env, arrival_rate, system):
  while True:
    arrival_time = env.now
    system.queue_length.append(len(system.server.queue))
    yield env.timeout(np.random.poisson(1 / arrival_rate))
    env.process(system.process_request(arrival_time))

def generate_requests_erlang(env, arrival_rate, k, system):
  while True:
    arrival_time = env.now
    system.queue_length.append(len(system.server.queue))
    yield env.timeout(np.random.gamma(k, 1 / arrival_rate))
    env.process(system.process_request(arrival_time, True))

def run_simulation(arrival_rate, service_rate, num_requests, system_type):
  env = simpy.Environment()
  system = ServiceSystem(env, service_rate)

  if system_type == 'regular':
    env.process(generate_requests(env, arrival_rate, system))

  elif system_type == 'poisson':
    env.process(generate_requests_poisson(env, arrival_rate, system))
    
  elif system_type == 'erlang':
    k = 2
    env.process(generate_requests_erlang(env, arrival_rate, k, system))

  env.run(until = num_requests)
  return system.queue_length

def main():
  arrival_rate = 1.0
  service_rate = 0.95
  num_requests = 500

  regular_queue_length = run_simulation(arrival_rate, service_rate, num_requests, 'regular')
  poisson_queue_length = run_simulation(arrival_rate, service_rate, num_requests, 'poisson')
  erlang_queue_length = run_simulation(arrival_rate, service_rate, num_requests, 'erlang')

  plt.plot(regular_queue_length, label='Регулярный')
  plt.plot(poisson_queue_length, label='Пуассоновский')
  plt.plot(erlang_queue_length, label='Эрланг')
  plt.xlabel('Время')
  plt.ylabel('Длина очереди')
  plt.legend()
  plt.show()

if __name__ == "__main__":
  main()