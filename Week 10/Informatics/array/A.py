n=int(input())
a=[]
x=input().split(' ')
for i in range (0,n):
	a.append(int(x[i]))
for i in range (0, len(a), 2):
	print(a[i],end=" ")

