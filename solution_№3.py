def f(x):
    a = [1] * (x + 1)
    for i in range(2, x + 1):
        a[i] = a[i - 1] + a[i - 2]
    return sum(a)

def perimeter(n):
    return(f(n)) * 4