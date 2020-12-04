import csv

file =list(csv.reader(open("Resources/budget_data.csv", "r")))

print(file[1])
i=0
b=0
c=0
d=0
profit=0
Greatest_Aux=0
Greatest_Inc=0
Greatest_Dec=0
last_row=0

for row in file:
    i+=1
    if i>=2:
        b=b+1
        profit=profit+int(row[1])
    if i>=3:
        Greatest_Aux=int(row[1])-int(last_row[1])
        if Greatest_Aux>Greatest_Inc:
            Greatest_Inc=Greatest_Aux
            c=i-1
        elif Greatest_Aux < Greatest_Dec:
            Greatest_Dec=Greatest_Aux
            d=i-1
    last_row=row
        
print (int(b))
print(int(profit))
print(Greatest_Inc)
print(Greatest_Dec)
print("Greatest Increase in profits: "+str(file[c][0]))
print("Greatest Decrease in profits: "+str(file[d][0]))

