from re import I


number = int(input("Enter the number "))
for i in range(1,11):
    #print(str(number) + " X " + str(i)+ " = " + str(number*i))
    print(f"{number} X {i} = {number*i}")