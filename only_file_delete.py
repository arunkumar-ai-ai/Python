import os 
file_name= input("Enter file name : ")
files= os.listdir(file_name)
print("file inside the folder\n")
for f in files:
    print(f)

print("\n only .txt file deleting...")

for f in files:
    if f.endswith(".txt"):
        file_path = os.path.join(file_name,f)
        os.remove(file_path)
print("File deleted successfful")