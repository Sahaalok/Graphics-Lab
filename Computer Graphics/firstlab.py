 #wap to print "hello world"
# print("Hello world")
#wap to print the sum of two numbers
# num1=int(input("Enter the first number"))
# num2=int(input("Enter the second number"))
# sum=num1+num2
# print(sum)
#wap to check if a number is odd or even
# num1=int(input("enter the number "))
# if (num1%2==0):
#     print("Even number")
# else:
#     print("odd number")
#same as q4.but using a function
# def main():
#     check()

# def check():
#     num1 = int(input("enter a number"))
#     if(num1%2==0):
#         print("Even number")
#     else:
#         print("odd number")

# if __name__=="__main__":
#     main()
#wap to take an input 'n' & print upto n
# n=int(input("Enter n range to print number up to that range"))
# for i in range(1,n):
#     print(i)
#     i=i+1
#wap to find the sum of odd numbers upto n
# def sumofodd():
#     sum=0
#     num=int(input("enter range of odd numbers"))
#     for i in range(1,num+1):
#         if(i%2!=0):
#             sum=sum+i
#     print("sum=",sum)
#     return sum
# a=sumofodd()
# print(a)
#wap to find whether a number is palindrome or not
# def palindrome():
#     n = int(input("enter the number to check if the number is palindrome or not"))
#     m=n
#     rev=0
#     while(n!=0):
#         b=n%10
#         rev=rev*10+b
#         n=n//10
#     if(m==rev):
#         print("palindrome")
#     else:
#         print("not palindrome")
# palindrome()
#wap to input two coordinate & find the distance between them
# import math
# def distance():
#     x1=int(input("Enter x1 coordinate "))
#     y1=int(input("Enter y1 coordinate "))
#     x2=int(input("Enter x2 coordinate"))
#     y2=int(input("Enter y2 coordinate "))
#     d=math.sqrt(pow(x2-x1,2)+pow(y2-y1,2))
#     return d
# a=distance()
# print(a)
import datetime
def age():
    x = datetime.datetime.now()
    print(x)
    name=input("Enter the name of the person")
    address=input("Enter the address of the person")
    dob=int(input("enter the date of birth of a person"))
    y=x.year-dob
    if(y>=18):
        print("you can vote")
    else:
        print("you cannot vote because you are under 18")
age()


