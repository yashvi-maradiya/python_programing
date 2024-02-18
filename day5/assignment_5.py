#Making choice and Decision

# 1.
'''Write a program that takes a number as input from the user and displays whether the number is even or odd.'''

A=int(input("Enter your number : "))
if A%2==0:
    print(f"{A} is even number")
else:
    print(f"{A} is odd number")


# 2.
'''Write a program that takes a list of numbers as input from the user and displays the sum
of all the even numbers in the list.'''
numbers = list(map(int, input("Enter a list of numbers separated by space: ").split()))
total = 0
for num in numbers:
   if num % 2 == 0:
     total += num
     
print("The sum of even numbers is:", total)


# 3.
'''Write a program that displays the numbers from 1 to 10 using a for loop. (try with single line)
'''
print("The first 10 natural numbers are:")
for i in range(1, 11):
    print(i, end=" ")
print()


# 4.
'''Write a program that takes a number as input from the user and displays the multiplication table of the number using a while loop.
'''
table=int(input("The maltiplication table of : "))
count=1
while count <11:
    value = table*count
    print(table , 'x', count, '=',value)
    count = count + 1


# 5.
'''Write a program that takes a list of numbers as input from the user and displays only the odd numbers in the list using a for loop.
'''
list1= list(map(int, input("Enter a list of numbers separated by space: ").split()))
for num1 in list1:
    if num1 % 2 !=0:
      print(num1,end=" ")


# 6.
'''Write a program that takes a number as input from the user and displays whether the number is prime or not using a try-except block.
'''
#print("\n prime number")
try:
    prime = int(input("\nEnter a number: "))
    if prime < 2:
        print("The number is not prime.")
    else:
        for x in range(2, int(prime/2) + 1):
            if prime % x == 0:
                print("The number is not prime.")
                break
        else:
            print("The number is prime.")
except ValueError:
    print("Invalid input. Please enter a valid number.")
























