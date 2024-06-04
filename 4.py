'''l = [1,2,['abc','hi',452],78,100,[124]]
l[5] += [20]
print(l[5])'''

#TAKE TWO INPUTS MERGE AND SORT THE INPUTS
'''a = input().split()
b = input().split()
c = a+b
c.sort()
print(c)'''

# TAKE A INPUT SORT BASED ON ITS LENGTH
'''l = input().split()
l.sort(key=len)
print(l)'''
#read the list and swap 1st elemet and last
'''a = input().split()
a[0],a[-1] = a[-1],a[0]
print(a)'''
# remove dublicate values
'''a = input().split()
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)'''

# print elemnts which are odd in the list
'''a = input().split()
b = []
for i in a:
    if a.count(i)%2  != 0 and i not in b:
        b.append(i)
print(b)'''
# read a list sum the first min elements
'''a = list(map(int,input().split()))
a. sort()
print(sum(a[:3]))'''

'''a = list(map(int,input().split()))
b = []
a. sort()
for i in a:
    if i%2 == 0:
        b.insert(0,i)
    else:
        b.append(i)
print(b)'''

'''a = list(map(int,input().split()))

even = []
odd = []
for i in a:
    if i%2 == 0:
        even.append(i)
    else:
        odd.append(i)
even.sort(reverse = True)
odd.sort()
print(even+odd)'''

#print product of the elements in the list which are within the given range
'''a = list(map(int,input().split()))
b = []
m,n = map(int,input().split())
for i in a:
    if i in range(m,n+1):
        b.append(i)
p = 1
for i in b:
    p *= i
print(p)'''

'''n = int(input())
a =[map(int,input().split()) for i in range(n)]
m = 0
for i in a:
    s = sum(i)
    if s > m:
        m = s
        ind = a.index(i)
print(ind)'''

#TUPLES-----
# removing specific index tuple
'''t = tuple(input("enter tuple eleements").split(','))
l = len(t)
print(l)
i = int(input("enter imdex to be deleted"))
t = t[:i] + t[i+1:]
print(t)'''

#to find the reapeated iteams of tuple

'''a =list(map(int, input().split()))
a=tuple(a)
c = 0
for i in a:
    if a.count(i)>c:
        c=a.count(i)
print(c)
print(type(a))'''


    
        
    





































    
































































