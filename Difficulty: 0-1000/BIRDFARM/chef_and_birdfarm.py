for i in range(int(input())):
    x,y,z = map(int, input().split())
    if(z%x != 0 and z%y != 0): #if the total no of legs(z) are not divisible by any then the farm has none of both birds
        print("none")
    elif(z%x == 0 and z%y == 0): #if z id divisible by both x and y then the farm has both chicken and duck
        print("any")
    elif(z%x == 0 and z%y != 0): #if z is divisible by any one x and y then the farm has the respective bird
        print("chicken")
    else:
        print("duck")
