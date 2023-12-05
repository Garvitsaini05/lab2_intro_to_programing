print("MONTHLY TEMPERATURE RECORD")
print("*--------------------------*")
print("")
print("Enter the no.of years you want to record.!")
year=int(input(":- "))

i=1
total=0
average=0
while(i<=year*12):
    
    temp_per_month=int(input(f"Temperature For {i} Month :- "))

    i=i+1

    total=total+temp_per_month
    

    average=total/(year*12)
    average_1st_year=total/(12)

print("------------------------------")


print("your", year, "year average Temperature is :- ", average)