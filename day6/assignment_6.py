# function and moduls

# 1.
'''Write a program that defines a function to calculate the area of a rectangle. The
function should take the length and width of the rectangle as input parameters and
return the area.'''

def rectangle_area(length , width):
    return length*width

length=float(input("Enter length : "))
width=float(input("Enter width : "))
area=rectangle_area(length , width)
print("the area of rectangle : ",area)

# 2.
'''Write a program that defines a function to calculate the factorial of a number.
The function should take a single input parameter and return the factorial of that number.'''

def factorial_num(x):
   if x ==1:
       return 1
   else:
       return (x*factorial_num(x-1))

x=int(input("enter your number : "))
result=factorial_num(x)
print("The factorial of", x, "is", result)


# 3.
'''Write a program that defines a function to calculate the sum of a list of numbers.
The function should take a list of numbers as input and return the sum of those numbers.'''

def calculate_sum(sum_list):
       total=0
       for sum_list in number:
           total+=sum_list
       return total
number=list(map(int,input("enter your list : ").split()))
result=calculate_sum(number)
print("the sum of all number : ",result)


# 4.
'''Write a program that defines a function to calculate the nth Fibonacci number.
The function should take a single input parameter and return the nth Fibonacci number.'''

def fibonacci(n):
    if n < 0:
        print("Incorrect input")
        return None
    elif n <= 1:
        return n
    else:
        fib_arr = [0] * (n + 1)
        fib_arr[1] = 1

        for i in range(2, n + 1):
            fib_arr[i] = fib_arr[i - 1] + fib_arr[i - 2]

        return fib_arr[n]

n=int(input("enter your number : "))
result=fibonacci(n)
print("number " , n ,"fibonacci number" , result)


# 5.
'''Create a module called my_module that defines a function to calculate the square
of a number. Import the module into a new program and use the function to calculate
the square of a number.'''

from module import square

n=int(input("enetr a number " ) )
result=square(n)
print(n,"square is ",result)      
















    
