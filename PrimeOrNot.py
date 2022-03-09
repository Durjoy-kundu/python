num = int(input("Enter the numbber: "))
prime = True #12>>2,3,4
for i in range(2,num):
    if (num % i == 0):
        prime = False
        break
if prime == False:
    print("Not prime")
else:
    print("prime") 