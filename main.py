a = [float(input("Введите элементы списка")) for i in range(1,6)]
b=[int(a[i]) for i in range(len(a))]
print(b)