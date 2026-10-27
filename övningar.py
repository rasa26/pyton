temperatur = int(input("ge mig temperatur: "))
if temperatur<0: 
    print("det ar minus grader")
elif temperatur<20 and temperatur>0:
    print("det ar svalt")
else:
    print("det ar varmt")
