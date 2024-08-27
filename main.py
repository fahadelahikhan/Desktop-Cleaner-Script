# The code is a script that organizes files in a specific folder by moving them into sub_folders based on
# their file extensions. It uses modern path handling (pathlib.Path) and checks for existing files to
# avoid overwriting them. The structure is clean, with clear separation of concerns (creating folders,
# moving files, and validating paths), making it easy to maintain and extend.


import os
import shutil
from pathlib import Path


def create_sub_folder_if_needed(parent_folder: Path, sub_folder_name: str) -> Path:
    sub_folder_path = parent_folder / sub_folder_name
    if not sub_folder_path.exists():
        sub_folder_path.mkdir(parents=True)
    return sub_folder_path


def clean_folder(directory_path: Path):
    for filename in os.listdir(directory_path):
        file_path = directory_path / filename
        if file_path.is_file():
            file_extension = filename.split('.')[-1].lower()
            if file_extension:
                sub_folder_name = f"{file_extension.upper()} Files"
                sub_folder_path = create_sub_folder_if_needed(directory_path, sub_folder_name)
                new_location = sub_folder_path / filename
                if not new_location.exists():
                    shutil.move(str(file_path), str(sub_folder_path))
                    print(f"Moved: {filename} -> {sub_folder_name}/")
                else:
                    print(f"Skipped: {filename} already exists in {sub_folder_name}/")


if __name__ == "__main__":
    print("Desktop Cleaner Script")
    target_folder = Path(r'E:\New folder')  # Enter the path of the directory you want to rearrange.
    if target_folder.is_dir():
        clean_folder(target_folder)
        print("Rearranging Completed!!.")
    else:
        print("Invalid folder path. Please ensure the path is correct and try again.")
