#Sample Input :
 6
 1 2 3 4 10 11
#Sample Output : 31
#Explanation : 1+2+3+4+10+11 = 31 

#We print the sum of the array's elements: .
ar_count = int(input())
ar = list(map(int ,input().split()))
a=0
for i in ar :
   a+=i
print(a)
