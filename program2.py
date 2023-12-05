print("RECORD OF DAILT CALORIE INTAKE")
print("-------------------------------")
print("")
initial_calorie=int(input("Starting Day Calorie intake :- "))
percent_to_decrease=int(input("percentage to be decreased :- "))
days=int(input("In how many days :- "))

i=1
while (i<=days):
    initial_calorie = initial_calorie-initial_calorie*(percent_to_decrease/100)
    print(f"Day {i} :- ", initial_calorie)
    i=i+1

    if initial_calorie <= 1200:
        print("You can't loose more calories")
        break
    else:
        print("")