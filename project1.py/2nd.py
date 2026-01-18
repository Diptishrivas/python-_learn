import os
import shutil
import time

# ===== CONFIG =====
SOURCE_FOLDER = os.path.expanduser("~/Downloads")
DEST_FOLDER = os.path.join(SOURCE_FOLDER, "Organized_Files")

FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Archives": [".zip", ".rar"]
}

SIZE_LIMIT = 5 * 1024 * 1024   # 5 MB
DAYS_LIMIT = 7 * 24 * 60 * 60  # 7 days


def create_folder(path):
    if not os.path.exists(path):
        os.makedirs(path)


def get_category(ext):
    for category, extensions in FILE_TYPES.items():
        if ext in extensions:
            return category
    return "Others"


def organize_files():
    create_folder(DEST_FOLDER)

    for file in os.listdir(SOURCE_FOLDER):
        file_path = os.path.join(SOURCE_FOLDER, file)

        if os.path.isfile(file_path):
            ext = os.path.splitext(file)[1].lower()
            category = get_category(ext)

            category_path = os.path.join(DEST_FOLDER, category)
            create_folder(category_path)

            # Extra rules for Documents
            if category == "Documents":
                file_size = os.path.getsize(file_path)
                modified_time = time.time() - os.path.getmtime(file_path)

                if file_size > SIZE_LIMIT:
                    category_path = os.path.join(category_path, "Large_Files")
                elif modified_time < DAYS_LIMIT:
                    category_path = os.path.join(category_path, "Recent_Files")

                create_folder(category_path)

            shutil.move(file_path, os.path.join(category_path, file))

    print("✅ Files organized successfully!")


if __name__ == "__main__":
    organize_files()
