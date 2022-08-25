summary = 0
for i in range(1000):   
    if i%3 == 0 and i%5 == 0:
        toplam = toplam + i
    elif i%5 == 0:
        toplam = toplam + i
    elif i%3 == 0:
        toplam = toplam + i
    else:
        continue
print(summary)
    

