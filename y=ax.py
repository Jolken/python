x = float(input("Введите х: "))
if x <= 0 :
    print(2)
else:
    a = float(input("Введите а: "))
    if a < 0:
        print(2 * a * x)
    else:
        print(a * x)
