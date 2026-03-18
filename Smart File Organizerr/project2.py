import os
import shutil

# Folder jahan files organize karni hain
source_folder = "C:/Users/YourName/Downloads"

# File type categories
file_types = {
    "Images": [".png", ".jpg", ".jpeg", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Documents": [".pdf", ".docx", ".txt", ".pptx"],
    "Music": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}

# Folder organize function
def organize_files():

    for file in os.listdir(source_folder):

        file_path = os.path.join(source_folder, file)

        if os.path.isfile(file_path):

            file_ext = os.path.splitext(file)[1]

            moved = False

            for folder, extensions in file_types.items():

                if file_ext.lower() in extensions:

                    target_folder = os.path.join(source_folder, folder)

                    if not os.path.exists(target_folder):
                        os.makedirs(target_folder)

                    shutil.move(file_path, os.path.join(target_folder, file))
                    print(f"Moved: {file} → {folder}")

                    moved = True
                    break

            if not moved:
                other_folder = os.path.join(source_folder, "Others")

                if not os.path.exists(other_folder):
                    os.makedirs(other_folder)

                shutil.move(file_path, os.path.join(other_folder, file))
                print(f"Moved: {file} → Others")


organize_files()

print("✅ Files organized successfully!")

print ("Done Successfully ")

setImmediate(()=>console.log("hello javascript"))