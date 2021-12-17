import string


n=int(input())

a=[]

for i  in range(0,n):
     a.append(input())   


a_set = set(a)
x = len(a_set)
print(x)

for k in (0,n-1):
    print(a.count(a[k]))







