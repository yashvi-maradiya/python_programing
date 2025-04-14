#problem day 5

#Problem 1: Array with consecutive elements
'''Problem Description
Given an array of positive integers A, check and return whether the array elements are consecutive or not.
NOTE: Try this with O(1) extra space.

Problem Constraints
1 <= length of the array <= 105
1 <= A[i] <= 109

Input Format
The only argument given is the integer array A.

Output Format
Return 1 if the array elements are consecutive else return 0.

Example Input
Input 1:
 A = [3, 2, 6, 4, 5]
Input 2:
 A = [1, 3, 2, 5]

[2, 3, 4, 5, 7, 8, 9, 10]

Example Output
Output 1:
 1
Output 2:
 0
'''
A=[1,2,3,4,6]
A.sort()
print(A)
B=()
for x in range(len(A)-1):
    if A[x]+1==A[x+1]:
         B=1
    else:
         B=0
         break
print(B)



#problem 2.
'''Given a number A, find if it is COLORFUL number or not.
If number A is a COLORFUL number return 1 else, return 0.

What is a COLORFUL Number:
A number can be broken into different consecutive sequence of digits. 
The number 3245 can be broken into sequences like 3, 2, 4, 5, 32, 24, 45, 324, 245 and 3245.

This number is a COLORFUL number, since the product of every consecutive sequence of digits is different

Problem Constraints
1 <= A <= 2 * 109


Input Format
The first and only argument is an integer A.

Output Format
Return 1 if integer A is COLORFUL else return 0.
'''

