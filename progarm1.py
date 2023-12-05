print("CALCULATION OF PER MONTH EXPENCES")
print("")
print("Enter the no.of years you want to calculate.!")
year=int(input(":- "))

i=1
total=0
average=0
while(i<=12):
    monthly_expence=int(input(f"Enter month {i} Expences :- "))

    i=i+1
    total=total+monthly_expence
    average=total/(year*12)
    

print("------------------------------")


print("your", year, "year average is :- ", average)


