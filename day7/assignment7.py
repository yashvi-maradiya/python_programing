#assigenment 7

# 1.
'''Write a program that opens a text file and reads the contents of the file.'''

f = open('file.txt' ,'r')
for line in f:
    print(line)

# 2.
'''Write a program that opens a text file and writes some text to the file.
'''
'''file = open('file.txt','a+')
print("abcd")'''
    

# 3.
'''Write a program that opens a binary file and reads the first 10 bytes of the file.
'''
file = open('file.txt','rb')
binary = file.read(4)
print(binary)


# 4.
'''Write a program that creates a new text file, writes some text to the file, and then renames the file.
'''
#import os
#os.rename('file.bin', 'new_file.bin')




# 5.
'''Write a program that deletes a text file.'''
#os.remove('new_file.txt')'''
