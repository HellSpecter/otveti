import threading
import time

class PetriNet:
    def __init__(self):
        self.reading = 0
        self.writing = 0
        self.priority = 0
        self.read_mutex = threading.Semaphore(1)
        self.write_mutex = threading.Semaphore(1)
        self.priority_mutex = threading.Semaphore(1)

# Добавлены переменные для отслеживания числа операций
        self.read_operations = 0
        self.write_operations = 0

    def start_read(self):
            self.priority_mutex.acquire()
            if self.priority > 0:
                self.priority_mutex.release()
                return False
            self.priority_mutex.release()

            self.read_mutex.acquire()
            self.reading += 1
            if self.reading == 1:
                self.write_mutex.acquire()
            self.read_mutex.release()

    # Увеличиваем счетчик операций чтения
            self.read_operations += 1
            return True

    def end_read(self):
        self.read_mutex.acquire()
        self.reading -= 1
        if self.reading == 0:
            self.write_mutex.release()
        self.read_mutex.release()

    def start_write(self):
        self.priority_mutex.acquire()
        self.priority += 1
        self.priority_mutex.release()

        self.write_mutex.acquire()
        self.write_operations += 1 # Увеличиваем счетчик операций записи
        return True

    def end_write(self):
        self.write_mutex.release()

        self.priority_mutex.acquire()
        self.priority -= 1
        self.priority_mutex.release()

def simulate_system(max_readers, max_writers, runtime):
    net = PetriNet()
    stop_threads = threading.Event()
    
    def reader():
        while not stop_threads.is_set():
            if net.start_read():
                print("Чтение данных")
                time.sleep(2)
                net.end_read()
            time.sleep(1)
    
    def writer():
        while not stop_threads.is_set():
            if net.start_write():
                print("Запись данных")
                time.sleep(3)
                net.end_write()
            time.sleep(2)
    
    # Создаем потоки для чтения и записи
    read_threads = [threading.Thread(target=reader) for _ in range(max_readers)]
    write_threads = [threading.Thread(target=writer) for _ in range(max_writers)]
    
    # Запускаем потоки
    for thread in read_threads + write_threads:
        thread.start()
    
    for _ in range(runtime):
        time.sleep(1)
        print(f"Число операций чтения: {net.read_operations}")
        print(f"Число операций записи: {net.write_operations}")
        print(f"Число потоков чтения: {sum(thread.is_alive() for thread in read_threads)}")
        print(f"Число потоков записи: {sum(thread.is_alive() for thread in write_threads)}")
    
    stop_threads.set()# Активируем флаг остановки
    
    # Ожидаем завершения всех потоков
    for thread in read_threads + write_threads:
        thread.join()
        
    print("Конец")

simulate_system(max_readers = 4,max_writers = 2, runtime = 30)