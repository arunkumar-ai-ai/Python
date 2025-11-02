import os
file_name = input("Enter file name : ")
with open(file_name,'a') as file:
    file.write(" \ni add extra text")
print("file updated sucessfull")