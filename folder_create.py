import os
folder_name = input("Enter folder Name : ")
os.makedirs(folder_name,exist_ok=True)
print(f"folder,{folder_name}, is created")