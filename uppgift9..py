#Uppgift 9 – Beräkna en summa
tal = int(input("skriv ett heltal: "))
summan = 0
for i in range(tal + 1):
    if(i!=0):
        summan = summan + i

    print("Summan: ", summan)