#python data type and structures

# 1. create an integer variable and float variable and add them togather.check out type
a=int(input("enter your integer variable = "))
b=float(input("enter your float variable = "))
print(a+b) #output type is float variable


# 2. convert string variable into integer
x="123"
print(type(x))
convert_num=int(x)
print(type(convert_num))
print(x)

#3. create a string variable your name and concatenate with string your favorite color
name="yashvi"
color="green"
print(f'{name} favorite color is {color}') #f-string makes it easy to print values and variables. 

#4. create a list
list=["think and grow rich" , "believe in yourself" , "atomic habits" , "gita"]
print(list)
print(type(list))

#5. create a tuple
tup=(1,3,5)
print(tup)
print(type(tup))


#6. create a dictionary
dic={"name" : "yashvi", "age" : 20 , "hometown" : "surat"}
print(dic)
print(type(dic))
