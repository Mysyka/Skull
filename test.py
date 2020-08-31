N = input("N=")
Massiv = [i for i in range(N)]
Massiv = [x for x in filter(lambda i: i != 0, Massiv)]
print(Massiv)