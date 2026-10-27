#Uppgift 7 – Valfri gångertabell
gangertabell = int(input("vilken ganger tabell: "))
rader = int(input("hur manga rader: "))
for i in range(1, rader + 1):
        print(i, "*", gangertabell, "=", i * gangertabell)
