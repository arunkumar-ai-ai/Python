import os
import shutil
folder_name = input("Enter folder name : ")
if not os.path.exists(folder_name):
    print("Folder not exist")
else:
   text_folder = os.path.join(folder_name,"TextFile")
   os.makedirs(text_folder,exist_ok=True)
   files = os.listdir(folder_name)
for f in files:
    if f.endswith(".txt"):
        source = os.path.join(folder_name, f)
        destination = os.path.join(text_folder, f)
        shutil.move(source, destination)
        print(f"Moved: {f}")
print("\n🎉 All .txt files moved to TextFiles folder!")