# open('filename','mode')
# file = open('name.txt','r') 

# print(file.read())
# print(file.read(5))
# print(file.read(10))
# print(file.readline())
# print(file.readline())
# print(file.readlines())

# file = open('name.txt','a') # creates a new file if it does not exist
# file = open('name.txt','w') # overwrites the file if it exists, or creates a new one if it doesn't
# file = open('name.txt','w') # append mode
# file = open('name.txt','a')  # creates a new file if it does not exist

# file.write("viki\n")
# file.write("sree\n")
# file.write("athul\n")
# file.write("nidhi\n")
# file.writelines(["viki\n","sree\n","athul\n","nidhi\n"])

# file = open('students.txt','x') # creates a new file if it does not exist
# file.close()   # closes the file after writing to it

with open('name.txt','w') as file:  
    print(file.read(4))
    # print(file.read(10))
    print(file.tell())
    file.seek(10)           # returns the 
    print(file.read(5))
    
    
    
    
# import os
# print(os.path.exists('name.txt'))  # checks if the file exists or not
