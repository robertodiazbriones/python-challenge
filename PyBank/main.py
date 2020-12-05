import csv

#Reading budget data file
file =list(csv.reader(open("Resources/budget_data.csv", "r")))

#Initializing variables
i=0
b=0
c=0
d=0
profit=0
Greatest_Aux=0
Greatest_Inc=0
Greatest_Dec=0
SumChange=0.0
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
    SumChange=SumChange+Greatest_Aux
    last_row=row
AvgChange=SumChange/(b-1)

#Printing results
print("Financial Analisis")
print("------------------")
print("Total Months:"+str(b))
print("Total: $"+str(profit))
print("Average Change: $"+str(round(AvgChange,2)))
print("Greatest Increase in profits: "+str(file[c][0])+" ($"+str(Greatest_Inc)+")")
print("Greatest Decrease in profits: "+str(file[d][0])+" ($"+str(Greatest_Dec)+")")

#Create Results file to export results
ResultsFile=open("analysis/Results.txt", "w")

ResultsFile.write("Financial Analisis")
ResultsFile.write("------------------")
ResultsFile.write("Total Months:"+str(b)+"\n")
ResultsFile.write("Total: $"+str(profit)+"\n")
ResultsFile.write("Average Change: $"+str(round(AvgChange,2))+"\n")
ResultsFile.write("Greatest Increase in profits: "+str(file[c][0])+" ($"+str(Greatest_Inc)+")\n")
ResultsFile.write("Greatest Decrease in profits: "+str(file[d][0])+" ($"+str(Greatest_Dec)+")\n")

ResultsFile.close()
