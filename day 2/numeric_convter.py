#number system convert

def int_to_binary(num):
  return bin(num)[2:] # index value represant
print(" 34 binary number is : ",int_to_binary(34))
print("56 binary number is : ",int_to_binary(56))
print(" 67 binary number is : ",int_to_binary(67))


# def int_to_binary(num):
#     return bin(num)[2:]  # Removing '0b' prefix

# # Taking multiple inputs from the user
# numbers = list(map(int, input("Enter numbers separated by space: ").split()))

# # Converting each number to binary and printing
# for num in numbers:
    # print(f"{num} binary number is: {int_to_binary(num)}")