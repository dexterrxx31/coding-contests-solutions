# problem url : https://www.codechef.com/submit/INTEST
n , k  = input().split()
n = int(n)
k = int(k)
counter = 0 
for i in range(n):
  number = int(input())
  if(number % k == 0 ):
    counter = counter + 1
print(counter)
