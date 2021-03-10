# def q1():
#     name=input("enter your name :")
#     age=int(input("enter your age :"))
#     year=int(100-age) + 2021
#     print("you will be 100 years old in "+str(year))

# def q2():
#     number=int(input("enter your number :"))
#     if number%2==0:
#         print("it is an even number")
#     else :
#         print("it is an odd number")

# def q3():
#     a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#     for x in a:
#         if x<5:
#             print(x,end=" ") #print ketepi

# def q4():
#     x=int(input("enter your number"))
#     for y in range (1,x+1) :
#         if x%y==0 :
#             print(y)


def q5():
    a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
    b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
    same=[]
    for x in a:
        for y in b:
            if x==y:
                same.append(x)
    print(same)

def q6():
    user=input("insert your statements")
    check"";
        for a in user:
            check=check+a
        if (check==user):
            print(user+"it is a palindrome")
        else:
            print(user+"it is not a palindrome")
            
    
#q1()
#q2()
#q3()
#q4()
 q5()