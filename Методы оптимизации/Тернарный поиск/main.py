import os
import math



def f(x):
    return x * x - 6 * x
# res: 3



def main():
    os.system("clear")

    l = 0.
    r = 10.
    phi = (1 + 5**0.5) / 2
    resphi = 2 - phi
    EPS = 1e-6;

    x1 = r - resphi * (r - l)
    x2 = l + resphi * (r - l)
    f1 = f(x1)
    f2 = f(x2)

    while r - l >= EPS:
        if f1 > f2:
            r = x2
            x2 = x1
            f2 = f1
            x1 = r - resphi * (r - l)
            f1 = f(x2)
            
        else:
            l = x1
            x1 = x2
            f1 = f2
            x2 = l + resphi * (r - l)
            f2 = f(x1)

        print(f"r: {r} l: {l} x1: {x1} x2: {x2}\n")

    result = (l + r) / 2

    print(result)
    

if __name__ == "__main__":
    main()
