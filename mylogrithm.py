e = 2.71828

def ln(x):
    n = 1000.0
    return n * ((x ** (1/n)) - 1)

def mylog(b, a = e):
    x = ln(b)/ln(a)
    return x

print(round(mylog(4096, 2)))

def myLog2(x, b):
    if x < b:
        return 0  
    return 1 + myLog2(x/b, b)

print(myLog2(25, 5))