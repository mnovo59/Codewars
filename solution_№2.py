def ips_between(start, end):
    a1, a2, a3, a4 = map(int, start.split('.'))
    b1, b2, b3, b4 = map(int, end. split('.'))
    w1 = a1 * 256**3 + a2 * 256**2 + a3 * 256 + a4
    w2 = b1 * 256**3 + b2 * 256**2 + b3 * 256 + b4
    if w1 >= w2:
        w = w1 - w2
    else:
        w = w2 - w1
    return w
print(ips_between('10.0.0.0', '10.0.1.0'))
