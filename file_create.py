import os
file_name = input("Enter File Name : ")
with open(file_name,'w') as file:
    file.write(" this is my first file!!")
print(f"file created succesfull")