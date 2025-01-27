import os
import shutil
import time

# Folder to clean
folder_to_clean = ""

# Destination folders for organized files
arranges_folder = {
    "images": "C:/path/to/images",
    "documents": "C:/path/to/documents",
    "videos": "C:/path/to/videos",
    "others": "C:/path/to/others"
}

# File extensions for categories
file_types = {
    "images": [".jpg", ".png", ".jpeg"],
    "documents": [".pdf", ".docx", ".txt", ".xlsx"],
    "videos": [".mp4", ".mov", ".avi"]
}

# File age limit (e.g., 7 days in seconds)
file_age_limit = 2 * 365 * 24 * 60 * 60  # 2 years

# Ensure destination folders exist
for folder in folders_by_type.values():
    os.makedirs(folder, exist_ok=True)

def clean_folder():
    current_time = time.time()
    
    for filename in os.listdir(folder_to_clean):
        file_path = os.path.join(folder_to_clean, filename)

        # Skip directories
        if os.path.isdir(file_path):
            continue

        # Delete old files
        file_age = current_time - os.path.getmtime(file_path)
        if file_age > file_age_limit:
            print(f"Deleting old file: {filename}")
            os.remove(file_path)
            continue

        # Move files based on their extension
        file_extension = os.path.splitext(filename)[1].lower()
        moved = False
        for category, extensions in file_types.items():
            if file_extension in extensions:
                shutil.move(file_path, folders_by_type[category])
                print(f"Moved {filename} to {folders_by_type[category]}")
                moved = True
                break

        # Move uncategorized files to "others"
        if not moved:
            shutil.move(file_path, folders_by_type["others"])
            print(f"Moved {filename} to {folders_by_type['others']}")

if __name__ == "__main__":
    print("Starting folder cleaner...")
    clean_folder()
    print("Folder cleaning completed!")
