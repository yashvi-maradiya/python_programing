#interactiv program

# 1.
'''Write a program that takes two numbers as input from the user and displays their sum.'''

a=input("enter your first number : ")
b=input("enter your second number : ")
sum=int(a) + int(b)
print("sum is :",sum)


# 2.
'''Write a program that takes a string as input from the user and displays it in uppercase letters.'''

string=input("Enter your string : ")
upper_case=string.upper()
print("uppercase string : ",upper_case)

'''str1=input("Enter your string : ")
up_str=""
for ch in str1:
    asc=ord(ch)
    if asc > 96 and asc < 123:
        up_str=str1+chr(asc-32)
    else:
        up_str=str1+chr(asc)
print("uppercas is : " , up_str)'''


# 3.
'''Write a program that displays the following text, using triple quotes:
    Programming is fun. 
    I love Python.'''
text='''programing is fun.
i love python.'''
print(text)

# 4.
'''Write a program that displays the following text, using escape characters:
She said, "Hello, world!" '''

print('she said , "hello world!"')


# 5.
'''Write a program that takes a sentence as input from the user and displays the number of words in the sentence.'''

A=input("enter your sentence : ")
countwords=len(A.split())
print("the number of words in string : " , countwords)



