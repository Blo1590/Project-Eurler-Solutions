from ast import Return


toplam = 0
a = 1
b = 1
fibonacci = [a, b]
while b<4000001:
    a, b = b, a + b
    if a%2 == 1:
        toplam = toplam + a
        print(a)
    else:
        Return
print(toplam+1)
