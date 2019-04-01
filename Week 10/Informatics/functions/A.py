def my_min(a,b,c,d):
    if (a<b and a<c and a<d): return a 
    elif (b<a and b<c and b<d): return b
    elif (c<a and c<b and c<d): return c
    elif (d<a and d<b and d<c): return d

x=int(input())
y=int(input())
z=int(input())
f=int(input())
print(my_min(x,y,z,f))

 