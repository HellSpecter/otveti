import random
import math
import matplotlib.pyplot as plt

def throw_needle(l, a):
  x = random.uniform(0, a / 2)
  theta = random.uniform(0, math.pi / 2)
  if x <= l * math.sin(theta) / 2:
    return True
  else:
    return False

def experimental_probability(N, l, a):
  success_count = 0
  for _ in range(N):
    if throw_needle(l, a):
      success_count += 1
  return success_count / N

def normalized_deviation(P, P_exp):
  return abs(P - P_exp) / P

def calculate_delta_vs_N(N_values, l, a):
  deltas = []
  P = 2 * l / (math.pi * a)

  print(P)

  for N in N_values:
    P_exp = experimental_probability(N, l, a)
    print(f"{P_exp}")
    delta = normalized_deviation(P, P_exp)
    deltas.append(delta)
  return deltas

def main():
  # Длина иглы
  l = 2

  # Расстояние между линиями
  a = 2

  # Кол-во бросков
  N_values = [100, 250, 500, 750, 1000, 1500, 2000, 2500, 3000, 4000, 5000, 10000]

  deltas = calculate_delta_vs_N(N_values, l, a)

  plt.plot(N_values, deltas, marker='o')
  plt.xlabel('Число бросков (N)')
  plt.ylabel('Нормированное отклонение (Δ)')
  plt.title('Зависимость Δ от числа бросков')
  plt.grid(True)
  plt.show()

if __name__ == "__main__":
  main()
