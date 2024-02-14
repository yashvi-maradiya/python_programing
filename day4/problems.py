# problems_statement_and solution

# problem 1.

'''Problem Description
Print a Pattern According to The Given Value of A.

Example: For A = 3 pattern looks like:
1 0 0
1 2 0
1 2 3

Problem Constraints
1 <= A <= 1000

Input Format
The first and only argument is an integer denoting A.

Output Format
Return a two-dimensional array where each row in the returned array represents a row in the pattern.
'''

A=int(input("Enter your number : "))
for i in range(1, A+1):
   for j in range(1, A+1):
       if j <= i:
         print(j, end=" ")
       else:
           print(0,end=" ")
   print()

# problem 2.
'''Problem Description:

You are given an array of integers A of size N.
Return the difference between the maximum among all even numbers of A and the minimum among all odd numbers in A.

Problem Constraints
2 <= N <= 1e5
-1e9 <= A[i] <= 1e9
There is atleast 1 odd and 1 even number in A

Input Format
The first argument given is the integer array, A.

Output Format
Return maximum among all even numbers of A - minimum among all odd numbers in A.
'''
#1
array=[13,15,84]
min_odd = min(x for x in array if x % 2 != 0)
max_even = max(x for x in array if x % 2 == 0)
print("diff : ",max_even - min_odd)

#2
array1=[13,14,67,56,245,123,678]
even=[]
odd=[]
for i in array1:
    if i%2==0:
        even.append(i)
    else:
         odd.append(i)

diff=max(even)-min(odd)
print("diff between max even and min odd : ",diff)


# problem 3.
'''Problem Description
Given an array of integers A, every element appears twice except for one. Find that integer that occurs once.
NOTE: Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory? Hint: X-OR



Problem Constraints
1 <= |A| <= 2000000
0 <= A[i] <= INTMAX

Input Format
The first and only argument of input contains an integer array A.

Output Format
Return a single integer denoting the single element.
'''
x=[1,2,34,2,34]
num=0
for i in x:
    num=num^i
print(num)


# Problem 4: Q4. Time to equality
'''
Problem Description
Given an integer array A of size N. In one second, you can increase the value of one element by 1.
Find the minimum time in seconds to make all elements of the array equal.

Problem Constraints
1 <= N <= 1000000
1 <= A[i] <= 1000

Input Format
First argument is an integer array A.

Output Format
Return an integer denoting the minimum time to make all elements equal.'''

B=[2 , 3 , 4 , 5 , 3 , 2]
maximum=max(B)
count=0
for i in B:
    count+=maximum - i
print("the time reqired will be ",count ,"second")



   
