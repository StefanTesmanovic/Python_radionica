def faktorijel(n):
    if n < 0:
        return -1
    elif n == 0 or n == 1:
        return 1
    else:
        rezultat = 1
        for i in range(2, n + 1):
            rezultat *= i
        return rezultat

def nad(n, m):
    return faktorijel(n)/(faktorijel(m)*faktorijel(n-m))

print(nad(5, 2)) 