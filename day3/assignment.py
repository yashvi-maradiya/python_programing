#python data type and structures

# 1. Create an integer variable and a float variable, and add them together. Check output type

a=int(input("enter your integer variable = "))
b=float(input("enter your float variable = "))
print(a+b) #output type is float variable


# 2. Convert a string variable containing the value "123" to an integer.

x="123"
print(type(x))
convert_num=int(x)
print(type(convert_num))
print(x)

#3. Create a string variable containing your name, and concatenate it with a string variable containing your favorite color.

name="yashvi"
color="green"
print(f'{name} favorite color is {color}') #f-string makes it easy to print values and variables.


#4.  Create a list containing your favorite books

list=["think and grow rich" , "believe in yourself" , "atomic habits" , "gita"]
print(list)
print(type(list))

#5. create a tuple
tup=(1,3,5)
print(tup)
print(type(tup))


#6. Create a dictionary containing the key-value pairs for your name, age, and hometown.

dic={"name" : "yashvi", "age" : 20 , "hometown" : "surat"}
print(dic)
print(type(dic))
