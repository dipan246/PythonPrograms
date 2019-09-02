def fibo(n):
    l = []
    a = b = 1
    while a <= n:
        l.append(a)
        a,b = a+b,a
    if n in l:
        return n

print(fibo(14))
