import os 
folder_name = input("Enter folder Name : ")
os.makedirs(folder_name,exist_ok=True)
print(f"Folder{folder_name}Created Sucessfully\n")

print("5 File creating....\n")
for i in range (1,6):
    file_name=os.path.join(folder_name,f'file{i}.txt')
    with open(file_name,'w') as file:
        file.write("This is file number 1 ")
    
print("File created sucessfully")
for i in range (1,6):
    file_name=os.path.join(folder_name,f'file{i}.txt')
with open(file_name,'a') as append:
    append.write("\n file updated.. ")
print("file updated")