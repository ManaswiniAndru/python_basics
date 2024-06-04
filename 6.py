



# DAY 6 

#String methonds and functions
'''string.upper():
    returns the string lower to upper'''

'''str="neha is my nickname"
print(str.partition())
str2="""hi
this
is neha"""'''

'''str="neha"
print(str.index('a'))
print(str.rindex('a'))


string.capitalize:
    return a word with its first character capitalized

len()
return the lenght of the string

max()
returns the highest'''

'''S='python'
print(S[:])
print(S[2:])
print(S[:5])
print(S[2:6])
print(S[-4:-2])
print(S[::2])
print(S[::-1])
print(S[1:4:6])'''



'''def len1(str1):
    count=0
    for char in str1:
        count +=1
    return count
str1=input()
print(len1(str1))


l=str(input("enter"))
print(l.upper())
print(l.lower())


str=input()
print("your input in upper case:",str.upper())
print("your input in lower case:",str.lower())

s1="my car is bnW"
s2="BmW"
s3=s1.replace(s2,s2.upper())
print(s3)

def swap(str1):
    re=""
    for i in str1:
        if i.supper():
            re+=i.lower()
        else:
            re+=i.upper()
    return


str=input("enter")
return =str[0]
for i in range(1,len(str)):
    if str[i] != result[-1]:
        result += str[i]
print(result)


s=input()
space=""
result=""
for char in s:
    if char=="":
        spaces+=char
    else:
        result +=char
final_string = spaces+result
print(final_string)
s1=input()
s2=input()
uncommon_chars="".join(set(s1)^set(s2))
print(uncommon_chars)

s = input()
max_char=max(s)
print(f"Maximum occurring character: {max_char}")

def check_prime():
    num=int(input("enter a number:"))
    if num>1:
        for i in range(2, int(num**0.5)+1):
            if num%i==0:
                print(num,"is not a prime number")
                break
        else:
            print(num,"is a prime number")
    else:
        print(num,"is not a prime number")
check_prime()

def student(firstname, lastname):
    print(firstname, lastname):

student(firstname='neha',lastname='kandhimalla')
student(lastname='kandhimalla',lastname='neha')

*args is called take any numbers

def my_sum(*args):
    result=0
    for x in args:
        result += x
    return result
print(my_sum(1,2,3,658))

'''
'''def concatenate(**words):
    result=""
    for arg in words.values():
        result+=arg
    return result
print(concatenate(a="neha",b="ammu",c="model"))

def recursive_factorial(n):
  if n == 1:
      return n
  else:
      return n*recursive_factorial(n-1)
    num=6
    if num<0:
        print("invaild input ! plz enter a postive number.")
    elif num == 0:
        print("factorial of number 0 is 1")
    else:
        print("factorial of number",num,"=",recursive_factorial(num))'''




#DAY 7   #(recursive)
'''def Fun(n):
    if(n>0):
        Fun(n-1)
        print(n)
        
n = int(input())
Fun(n)
#o/p:
5
1
2
3
4
5'''




'''def Fun(n):
    if(n>0):
        print(n)
        Fun(n-1)
        
        
n = int(input())
Fun(n)

#o/p
5
5
4
3
2
1'''






#BASIC TERMINOLOGIES OF OPPS
#class
#obejects
#methods
#constructors
#1st:create an instance of the class'''

'''class Person:
    def __init__(mani,name):#------
        mani.name = name#---------constructor
    def say_hi(mani):#-------
        print('Hello, my name is',mani.name)#------methods
p = Person(' mani ')#obect
p.say_hi()#----accessing method  using object
#o/p:Hello, my name is  mani 


class test:
    def __init__(self,a="Hello World"):
        self.a=a
    def display(self):
        print(self.a)#o/p=Hello World'''

'''class Test:
    def __init__(self):
        self.x = 0
class Derived_Test(Test):
    def __init__(self):
        Test. __init__(self)
        self.y = 1
def main():
    b = Derived_Test()
    print(b.x,b.y)
main()
#o/p:0 1  '''




'''class Animal:
    def __init__(self,name,species,sound):
        self.name = name
class Derived__Animal(Animal):
    def __init__(self):
        Animal. __init__(self)
        self.species = species
class Derived__Animal1(Animal):
    def __init__(self):
        Animal. __init__(self)
        self.sound = sound
def main()






























































    
    
        

 
















    
