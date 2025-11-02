import os
import shutil

source_folder = input("Enter folder to organize: ")

if not os.path.exists(source_folder):
    print("❌ Folder not found:", source_folder)
    exit()

# Extension-based folders (keys in lower case)
file_type = {
    ".pdf": "PDF_Files",
    ".mp3": "Music",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".docx": "Documents",
    ".doc": "Documents",
    ".txt": "TextFiles"
}

files = os.listdir(source_folder)

for entry in files:
    file_path = os.path.join(source_folder, entry)
    
    # Skip directories
    if os.path.isdir(file_path):
        continue

    # Get extension in lowercase for case-insensitive matching
    ext = os.path.splitext(entry)[1].lower()

    if ext in file_type:
        dest_folder = os.path.join(source_folder, file_type[ext])
    else:
        dest_folder = os.path.join(source_folder, "Others")  # unknown types

    os.makedirs(dest_folder, exist_ok=True)

    dest_path = os.path.join(dest_folder, entry)

    # If destination file exists, add a number suffix to avoid overwrite
    if os.path.exists(dest_path):
        base, extension = os.path.splitext(entry)
        count = 1
        while True:
            new_name = f"{base}_{count}{extension}"
            dest_path = os.path.join(dest_folder, new_name)
            if not os.path.exists(dest_path):
                break
            count += 1

    shutil.move(file_path, dest_path)
    print(f"Moved: {entry} → {os.path.basename(dest_folder)}")
