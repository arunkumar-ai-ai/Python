import os
folder_remove = input("Enter Remove folder Name : ")
os.rmdir(folder_remove)
print(f"folder,{folder_remove},deleted sucessfull")