#Uppgift 8 – Prislista med rabatt
timmpris = 499
for i in range(1, 9):
            print("-------------------------------------------------------------")
            print("ordinarie pris: ", i * timmpris)
            print("antal timmar: ", i)
            print("pris per timme: ", timmpris, "kr")
            print("pris efter 15 procent rabbat: ", round(i * timmpris * 0.85))