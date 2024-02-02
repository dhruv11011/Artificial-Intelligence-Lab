def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b % a, a)

m = int(input("Enter the capacity of first jug: "))
n = int(input("Enter the capacity of second jug: "))
goal = int(input("Enter the goal number: "))

if goal % gcd(m, n) != 0:
    print("Solution Not possible")
else:
    x = 0
    y = 0
    a = m
    b = n

    if (b > a):
        a, b = b, a

    while (x+y != goal):
        print(f"{x} {y}")
        if (x == 0):
            x = a
            continue
        if (y != b):
            temp = min(x, b-y)
            x -= temp
            y += temp
            continue
        if (y == b):
            y = 0
            continue
    print(f"{x} {y}")