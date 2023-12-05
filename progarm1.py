print("RECORD OF TEMPERATURE")
print("*---------------------*")
print("")
print("NO. OF YEARS TO BE RECORDED")
year=int(input(":- "))


i=1
z=1
total=0
average=0

while(i<=year*12):
    temp_month=int(input(f"TEMPERATUE FOR  {z}  MONTH :- "))
    i=i+1
    total=total+temp_month
    average=total/(year*12)
    average2=total/(year)


print("------------------------------")

print("YEARLY AVERAGE TEMPERATURE :- ", average2)
print("TOTAL AVERAGE TEMPERATUER IS :- ", average)