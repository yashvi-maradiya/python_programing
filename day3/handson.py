# handson

#list manipulation

list1=[4,2,5,1,7,2,4,8,5,9]
print("The original list is " , list1)
#1 remove duplicate
#if duplicates are remove from the list then used set() method
print("after remove duplicated " ,set(list1))
#2 sort in decendinfg order
list1.sort(reverse=True)
print("list in decending order " ,list1 )
#3 total of all element
total=sum(list1)
print("sum of all element in list : ",total)



#Tuple opreation

#1create tuple
tuple1=("India","Greece","US","spain","Russia")
print("tuple length is : ",len(tuple1))
#2 check the contry in present in tuple
if "mali" in tuple1:
    print("Yes , 'mali' is in the tuple")
else:
    print("No , 'mali is not present is in the tuple")
#3 add anothrer tuple in first tuple
# another methods like sum() , list()and extend() , tuple() etc....
tuple2=("yemen","japan","brazil","chaina","UK")
res=tuple1 + tuple2
print("tuple after concatention is : " , res)
#4 how to modify tuple
#Tuple are unchangeable or immuttable but we can modify the tuple , first you can convert tuple into list ,change the list and convert the list back into the tuple.
x=list(tuple1)
x[2]="yashvi"
tuple1=tuple(x)
print("after modifying the tuple : " , tuple1)


#Dictionary manipulation

#1 create a dicitonary
dic={"pasta" : 11 , "egg" : 20 , "flour" : 13 , "rice" : 23}
print(dic)
#2 add a new item in dic
dic["cheess"]=45
print("after add new item " , dic)
#3 update the item
dic.update({"flour" : 54})
print("after update items : " , dic)

#4 remove the item in stock
dic.pop("rice")
print("after remove the one item id dic : " , dic)
#5 sort dic in alphabetically order
alpha=sorted(dic.items())
print(alpha)


#list comprehension

#square of even number between 1to 20 using list
square_ofeven=[x**2 for x in range(2,21,2)]   #range(start , stop , step)
print("square of even number is : " , square_ofeven)

square_ofodd=[y**2 for y in range(1,20) if y % 2 != 0]
print("square of odd number is : ",square_ofodd)


#Dictionary Intration

#create a dictionary representing population of five diff cities. write a python program that print the city with the highest population along with its population
cities={"surat" : 3456,"mumbai" : 324,"gandhinagar" : 987,"vapi": 567}
highestcity=(max(cities,key=cities.get))
citypopulation=max(cities.values())
print(f"the highest city is {highestcity} and there population is {citypopulation}")


#tuple unpacking

#determines a valid triangle.if it dose print its type like equilateral , isosceles and scalene
x=int(input("Enter X : "))
y=int(input("Enter y : "))
z=int(input("Enter Z : "))
tup=(x,y,z)
print(type(tup))
if x==y==z:
    print("triangle is equilateral")
elif x==y or y==z or z==x:
    print("triangle is isosceles")
else:
    print("triagle is scalene")


#list sorting

#find out the top three student in list
studentName=[("mini",54),("sili",44),("mac",87),("rona",67),("jack",95),("lina",88)]
sort=sorted(studentName,key=lambda x:x[1],reverse=True)
topThree=[student[0] for student in sort[:3]]
print("The top three student Name : ",topThree)


#Dictionary filtering

# create the dict key as a items and value as a price 
item_prices = {"apple": 0.75,"chocalate": 0.60,"rice": 0.90,"grapes": 2.50,"milk": 1.20,"bread": 1.50}

# threshold price
threshold_price = 1.00

#print the items and there price with less than threshold price
print("Items with prices less than" , threshold_price)
for item, price in item_prices.items():
    if price<threshold_price:
      print(f"{item}: {price}")



#dictinary sorting

ages_dict = {"lila": 25,"devid": 30,"sisa": 20,"mac": 35,"kitty": 28}
print(ages_dict)
#soet the age dictionary
sorted_ages = sorted(ages_dict.items(), key=lambda x: x[1])
print("After ascending the age dict : ",sorted_ages)
# after find the oldest and youngest person in dict
print("Oldest person:", sorted_ages[-1][0])
print("Youngest person:", sorted_ages[0][0])


#list operation

list2=[2,4,6,9,12]
list3=[3,5,2,9,14]
print(list2)
print(list3)
print("intersection" , list(set(list2)&set(list3)))
print("union" , list(set(list2)|set(list3)))
print("difference first list not second list" , list(set(list2)-set(list3)))






















