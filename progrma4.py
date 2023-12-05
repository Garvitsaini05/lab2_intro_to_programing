myNumbers=[6,4,9,12,17,22,27,33,44]
print(myNumbers)
for z in range(0,8):

    for i in range(0,8):
        if myNumbers[i] > myNumbers[i+1]:
            a = myNumbers[i]
            myNumbers[i+1] = myNumbers[i]
            myNumbers[i] = a
            
print(myNumbers)