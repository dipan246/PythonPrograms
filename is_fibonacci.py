def fibo(n):
    l = []
    a = b = 1
    while a <= n:
        l.append(a)
        a,b = a+b,a
    return l

n = int(input("Enter number n >> "))
fibo_list=fibo(n)
if n in fibo_list:
    print("it is a fibonacci number")
