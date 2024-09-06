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









import os

def f(x, y):
    return x * x - 6 * x + y * y - 8 * y

# res: x=3 y=4

# x*x - 6*x + 2* y * y - 8 * y
# (x - 2)(x - 2) + (x - y * y) * (x - y * y)

def search_y(x_fixed, left_y, right_y, eps):
    phi = (1 + 5**0.5) / 2
    resphi = 2 - phi

    y1 = right_y - resphi * (right_y - left_y)
    y2 = left_y + resphi * (right_y - left_y)
    f1 = f(x_fixed, y1)
    f2 = f(x_fixed, y2)

    while right_y - left_y >= eps:
        if f1 > f2:
            right_y = y2
            y2 = y1
            f2 = f1
            y1 = right_y - resphi * (right_y - left_y)
            f1 = f(x_fixed, y1)
        else:
            left_y = y1
            y1 = y2
            f1 = f2
            y2 = left_y + resphi * (right_y - left_y)
            f2 = f(x_fixed, y2)

    return (left_y + right_y) / 2



def search_x(left_x, right_x, left_y, right_y, eps):
    phi = (1 + 5**0.5) / 2
    resphi = 2 - phi

    x1 = right_x - resphi * (right_x - left_x)
    x2 = left_x + resphi * (right_x - left_x)

    y1 = search_y(x1, left_y, right_y, eps)
    y2 = search_y(x2, left_y, right_y, eps)

    f1 = f(x1, y1)
    f2 = f(x2, y2)

    while right_x - left_x >= eps:
        if f1 > f2:
            right_x = x2
            x2 = x1
            f2 = f1
            x1 = right_x - resphi * (right_x - left_x)
            y1 = search_y(x1, left_y, right_y, eps)
            f1 = f(x1, y1)
        else:
            left_x = x1
            x1 = x2
            f1 = f2
            x2 = left_x + resphi * (right_x - left_x)
            y2 = search_y(x2, left_y, right_y, eps)
            f2 = f(x2, y2)

    return (left_x + right_x) / 2, search_y((left_x + right_x) / 2, left_y, right_y, eps)




def main():
    os.system("clear")

    left_x = -10   
    right_x = 10   
    left_y = -10   
    right_y = 10   
    eps = 1e-6     

    minimum_x, minimum_y = search_x(left_x, right_x, left_y, right_y, eps)
    print(f"x = {minimum_x}, y = {minimum_y}")



if __name__ == "__main__":
    main()