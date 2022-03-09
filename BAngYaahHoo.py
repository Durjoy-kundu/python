for i in range(1,51):
    if(i%3==0 and i%5 == 0): 
        print("BangYooHoo")
    elif i%3 == 0:
        print("bang")
    elif i%5 == 0:
        print("YooHoo")
    elif (i%3==0 and i%5 == 0): 
        print("BangYooHoo")
    else:
        print(i)