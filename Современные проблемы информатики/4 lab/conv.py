import simpy
import random
import time
import matplotlib.pyplot as plt

class AsyncConveyor:
    def __init__(self, env, num_steps, buffer_capacity, processing_mean, processing_variance):
        self.env = env
        self.buffer = simpy.Store(env, capacity=buffer_capacity)
        self.steps = [simpy.Store(env) for _ in range(num_steps)]
        self.processing_mean = processing_mean
        self.processing_variance = processing_variance

    def generate_data(self, num_elements):
      for i in range(num_elements):
          yield self.env.timeout(1)
          data = f"Element {i}"
          yield self.buffer.put(data)

    def process_data(self, step):
        while True:
            data = yield self.buffer.get()
            processing_time = random.normalvariate(self.processing_mean, self.processing_variance)
            yield self.env.timeout(processing_time)
            yield self.steps[step].put(data)

    def run(self, num_elements):
        self.env.process(self.generate_data(num_elements))

        for i in range(len(self.steps)):
            self.env.process(self.process_data(i))

        start_time = time.time()
        self.env.run()
        end_time = time.time()
        return end_time - start_time

class SyncConveyor:
    def __init__(self, env, num_steps, buffer_capacity, processing_mean, processing_variance):
        self.env = env
        self.buffer = simpy.Store(env, capacity=buffer_capacity)
        self.steps = [simpy.Store(env) for _ in range(num_steps)]
        self.processing_mean = processing_mean
        self.processing_variance = processing_variance

    def generate_data(self, num_elements):
      for i in range(num_elements):
          yield self.env.timeout(1)
          data = f"Element {i}"
          yield self.buffer.put(data)

    def process_data(self, step):
        while True:
            data = yield self.buffer.get()
            processing_time = random.normalvariate(self.processing_mean, self.processing_variance)
            yield self.env.timeout(processing_time)
            yield self.steps[step].put(data)

    def run(self, num_elements):
        self.env.process(self.generate_data(num_elements))

        for i in range(len(self.steps)):
            self.env.process(self.process_data(i))

        start_time = time.time()
        self.env.run()
        end_time = time.time()
        return end_time - start_time

def simulate_async_conveyor(num_steps):
    buffer_capacity = 10
    processing_mean = 5
    processing_variance = 1

    env = simpy.Environment()
    conveyor = AsyncConveyor(env, num_steps, buffer_capacity, processing_mean, processing_variance)

    return conveyor.run(num_elements=100)

def simulate_sync_conveyor(num_steps):
    buffer_capacity = 10
    processing_mean = 5
    processing_variance = 1

    env = simpy.Environment()
    conveyor = SyncConveyor(env, num_steps, buffer_capacity, processing_mean, processing_variance)

    return conveyor.run(num_elements=2000)
# Test different numbers of steps
num_steps_list = []

for i in range(0, 5):
  num_steps_list.append(i)

sync_times = []
async_times = []

for num_steps in num_steps_list:
    sync_conveyor = SyncConveyor(simpy.Environment(), num_steps, 10, 5, 1)
    async_conveyor = AsyncConveyor(simpy.Environment(), num_steps, 10, 5, 1)

    sync_times.append(sync_conveyor.run(num_elements=100))
    async_times.append(async_conveyor.run(num_elements=100))

# Plot the results
plt.plot(num_steps_list, sync_times, label='sync', marker='o')
plt.plot(num_steps_list, async_times, label='async', marker='o')
plt.title('Async/Sync Time Ratio vs Number of Steps')
plt.xlabel('Number of Steps')
plt.ylabel('Async/Sync Time Ratio')
plt.legend()
plt.show()
