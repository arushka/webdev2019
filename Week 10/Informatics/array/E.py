n = int(input())
a = []
c=0
numbers = input().split(' ')
bool=False
for i in range(0, n):
    a.append(int(numbers[i]))
for i in range(1, len(a)):
    if (a[i]>0 and a[i - 1]>0 or a[i]<0 and a[i - 1]<0): bool=True

if (bool==True): print("YES")
else: print("NO")