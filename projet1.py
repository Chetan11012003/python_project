from ast import Break


l1=["ETIRG","AHNTEPLE","RIOLGAL","OLNI","EREB"]

for i in l1:
    print("Arrange the letters to form a valid word:")

    print(l1[0])
    t=input("Enter Your Word:- ")
    if t=="TIGER":
        print("Correct")
        a=1
        print()
    else:
        print("Wrong")
        a=-1
        print()

    print("Arrange the letters to form a valid word:")

    print(l1[1])
    e=input("Enter Your Word:- ")
    if e=="ELEPHANT":
        print("Correct")
        a+=1
        print()
    else:
        print("Wrong")
        a-=1
        print()

    print("Arrange the letters to form a valid word:")    

    print(l1[2])
    g=input("Enter Your Word:- ")
    if g=="GORILLA":
        print("Correct")
        a+=1
        print()
    else:
        print("Wrong")
        a-=1
        print()

    print("Arrange the letters to form a valid word:")    

    print(l1[3])
    l=input("Enter Your Word:- ")
    if l=="LION":
        print("Correct")
        a+=1
        print()
    else:
        print("Wrong")
        a-=1
        print()

    print("Arrange the letters to form a valid word:")

    print(l1[4])
    b=input("Enter Your Word:- ")
    if b=="BEER":
        print("Correct")
        a+=1
        print()
    else:
        print("Wrong")
        a-=1
        print()

    print("Net Score is:- ",a)
    break
     




    