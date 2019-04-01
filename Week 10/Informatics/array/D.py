n = int(input())
a = []
c=0
numbers = input().split(' ')
for i in range(0, n):
    a.append(int(numbers[i]))
for i in range(1, len(a)):
    if (a[i] > a[i - 1]): c+=1
print(c)