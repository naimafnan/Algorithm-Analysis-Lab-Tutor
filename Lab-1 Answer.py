import random
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


# def q5():
#     a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#     b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#     same=[]
#     for x in a:
#         for y in b:
#             if x==y:
#                 same.append(x)
#     print(same)

# def q6():
#     user=input("insert your statements")
#     check =0
#     for i in range(0,int(len (user)/2)):
#         if user[i] !=user[len(user)-i-1] :
#             check=1
#     if check==0:
#         print("it is palyndrome")
#     else:
#         print("it is not palyndrome")

# def q7():
#     a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
#     for x in a:
#         if x%2==0:
#             print(x,end=" ")

# def q8():
#     flag=True
#     while flag==True:
#         player1=eval(input("P1-Rock=[1] , Paper=[2] , Scissor=[3] ?"))
#         print()
#         player2=eval(input("P2-Rock=[1] , Paper=[2] , Scissor=[3] ?"))
#         if (player1==1 and player2==1) or (player1==2 and player2==2) or (player1==3 and player2==3):
#             print("player 1 and player 2 draw")
#         elif (player1==1 and player2==3) or (player1==2 and player2==1) and (player1==3 and player2==2):
#             print("Player 1 win")
#         elif (player1==1 and player2==2) or (player1==2 and player2==3) or (player1==3 and player2==1):
#             print("player 2 win")
#         print()
#         check=input("do you want to play again? [Y,N] :")
#         if (check=="N"):
#             flag=False
# def q9():
#     randomNumber=random.randint(1,9)
#     print(randomNumber)
#     user=int(input("Guess the random number: "))
#     if (randomNumber==user):
#         print("your guessed is exactly the same")
#     elif (randomNumber>user):
#         print("your guessed too Low, it's incorrect")
#     else:
#         print("your guessed too High, it's incorrect")
    
# def q10():
#     user=eval(input("enter a number: ")) #7
#     divisor=user-1                       #7-1=6
#     flag=True

#     for divisor in range(divisor,1,-1):  #(6,1,-1)
#         if(user!=1):
#             if user%divisor==0: 
#                 flag=False
#     if flag==True:
#         print(str(user)+ "is a prime number")
#     else:
#         print(str(user)+"is NOT a prime number")

#Q11()
# a = [5, 10, 15, 20, 25]
# def firstLast(a):
#     a = [5, 10, 15, 20, 25]
#     b=[]
#     b.append(a.pop(len(a)-1))
#     return b
# print(firstLast(a))

#Q12
# x=eval(input("enter the value of X: "))

# def Fibonance(x):
#     list=[0,1]
#     for y in range(1,x-1,+1):
#         list.append(list[y-1]+list[y])
#         return list
# print(Fibonance(x))

#Q13
# a=[2,4,6,8,10,2,4,6]
# def Unduplicate():
#     newList=[]
#     for i in a:
#         if i not in newList:
#             newList.append(i)
#     return newList
# print(Unduplicate())

#Q14
# sentence=input("enter any statement: ")
# a=sentence.split()
# b=""
# for i in a:
#     b=i+" "+b
# print(b)

#Q15
import time
import string
import random

# lowercase
# uppercase
# numbers
# symbol

# printable - contains letter(uppercase&lowercase) + digits + punctuation


def get_random_password(pass_len):
    pass_char = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(pass_char)
                       for i in range(pass_len))
    return password


Starttime = time.time()
pass_len = random.randint(10, 20)
print("Password length : " + str(pass_len))
print("Password : " + get_random_password(pass_len))
Endtime = time.time()
print("Time taken (s): " + str((Endtime - Starttime)*1000))
#q1()
#q2()
#q3()
#q4()
#q5()
#q6()
#q7()
#q8()
#q9()
#q10()
#firstLast(a)   
