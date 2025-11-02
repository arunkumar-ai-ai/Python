import os 
file_name = input("Enter file name for reading  : ")
with open(file_name,'r') as file:
    content = file.read()
print(f"\n file content : \n")
print(content)