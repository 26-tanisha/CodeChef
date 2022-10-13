for i in range(int(input())): #taking input for t test cases
    x = int(input()) #input income
    if(x>100):
        print("{}".format(x-10)) #deducting rs10 from x if its greater than 100
    else:
        print(x)
