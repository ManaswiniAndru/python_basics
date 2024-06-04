
#cut the watermelon into two piceses using even num weight
'''a=int(input("enter the numner:"))
if(a%2==0):
    if a==2:
        print("no")
    else:
        print("yes")
else:
    print("no")




if(a%2!=0 or a==2):
    print("no")
else:
    print("yes")'''

#ELEFANT 
'''x=int(input("enter the number"))
if(x<=5):
    print(1)
elif(x%5==0):
    print(x//5)
else:
    print(x//5+1)'''

'''n=float(float(input("enter the numbers:")))
print(round(n,-1))'''

#using list

'''n=int(input("enter the number:"))
n1=list (map(int,input().split(",")))#int---for store as integer
print(n,n1)'''

#a police recruits
'''n=int(input())
availableOffecicers = 0
untreatedCrimes = 0
for _ in range(n):
    event = int(input())
    if event == -1:
        if availableOfficers > 0:
            availableOfficers -= 1
        else:
            untreatedCrimes += 1
    else:
        availableOfficers +=event
print(untreatedCrimes)'''

#sum of natural numbers
'''n=int(input("enter the number:"))
sum=0
for i in range(1,n+1):
    sum=sum+i#sum +=i
print("sum of first", n, "natural numbers:",sum)'''

#fibanociseries
'''n=int(input("enter the number of terms:"))
a, b = 0, 1
for i in range(n):
    print(a, end=" ")
    a, b = b, a+b'''
#number of digits
'''num = int(input("enter a number:"))
count = 0
while num !=0:
    num//= 10
    count += 1
print("Number of digits:", count)'''

#multiplication table

'''num = int(input("enter a number: "))
print("Multiplication Table of", num)
for i in range(1, 11):
    print(num, "x", i,'''

#reverse number
'''num = int(input("enter a number:" ))
rev = 0
while num > 0:
    digit = num% 10
    rev = rev * 10 + digit
    num = num // 10
print("reversed number:",rev)'''

#bear of big brother

'''a=int(input("enter a value: "))
b=int(input("enter a value: "))
year=0
while (a<b):
    a*=3
    b*=2
    year += 1
print(year)'''








































#DAY 3

#TIME COMPLEXITY:

#FOR OPTIMAL SOLUTION(#BRUTE FORCE)"IF THERE IS EVEN ONES THEN IT IS 0"
#"IF THERE IS ODD ONES THEN IT IS 1"
'''n=9
x=0
for i in range(1,n+1):
    x=x^i
print(x)'''

#2)
'''n=int(input("enter the value:"))#using pattren dividing with 4
if(n%4==1):
    print(1)
if(n%4==2):
    print(n+1)
if(n%4==3):
    print(0)
if(n%4==0):
    print(n)'''

'''l=int(input("enter the number:"))
r=int(input("enter the number:"))
x=0
for i in range(l,r+1):#between 3 to 6
    x=x^i
print(x)'''


'''l = [10, 11, 12, 13, 14, 15, 16]
print(l[::2])  prints all the two elements from the list with step 2
(index+2 elements)from  the beginning'''

'''l = [10, 11, 12, 13, 14, 15,16]
print(l[::-1])'''

'''n1 = ['python', 'flask', 'gijango', 'tkinter']
n2 = n1
n3 = n1[:2]
n2[0] = 'scipy'
n3[1] = 'numpy'
s = 10
for i in (n1 , n2, n3):
    if i[0] == 'python':
        s += 1
    if i[1] == 'phyton':
        s += 2
print(s)'''


a = input()
b = input()
Username = "Manaswini_andru"
Password = "Manaswini@4"
if (a == Username):
    print("enter password:")
    







































                     




































































            
          
          
          







































        

        








































