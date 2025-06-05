def fibonaci(n):
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonaci(n - 1) + fibonaci(n - 2)
    
n = int(input("Unesite broj n: "))
print(f"Fibonacijev broj za {n} je: {fibonaci(n)}")