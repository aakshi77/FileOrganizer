# Day 1

# import os
# import shutil  # This helps in highlevel file operations
# path = r"C:\Users\aaksh\OneDrive\Documents\FileOrganizer\TestDownloads"
# files = os.listdir(path)

# for file in files:
#     filename, extension = os.path.splitext(file)
#     extension = extension[1:]

#     if extension:
#         new_folder_path = os.path.join(path, extension)

#         if not os.path.exists(new_folder_path):
#             os.makedirs(new_folder_path)

#         old_file_path = os.path.join(path, file)
#         new_file_path = os.path.join(new_folder_path, file)
#         shutil.move(old_file_path, new_file_path)

#     print("File organization complete!")


# Day 3


import os
import shutil


# User Input for the Path
path = input("Enter the path of the directory you want to organize: ")

# Check if the provided path is a valid directory.
if not os.path.isdir(path):
    print("Error: The provided path is not a valid directory.")
    exit()

# Get a list of all files and directories in the specified path
# We wrap this in a try-except block to handle potential permission errors.
try:
    files = os.listdir(path)
except OSError as e:
    print(f"Error reading directory: {e}")
    exit()

# Loop over all the files in the directory
for file in files:
    # Construct the full path to the file to check if it's actually a file
    full_file_path = os.path.join(path, file)

    # We only want to process files, not directories
    if os.path.isfile(full_file_path):
        # Separate the filename from the extension
        filename, extension = os.path.splitext(file)

        # The extension includes the dot (e.g., '.pdf'), so we remove it using slicing [1:]
        # Use .lower() to group .JPG and .jpg together
        extension = extension[1:].lower()

        # If the file has no extension, we can skip it or move it to a specific folder
        if not extension:
            continue  # Skips the rest of the loop for this file

        # 2. Path Creation and File Movement
        # Create a path for the new folder (e.g., /path/to/downloads/pdf)
        new_folder_path = os.path.join(path, extension)

        # Create the extension-based folder if it doesn't already exist
        if not os.path.exists(new_folder_path):
            os.makedirs(new_folder_path)
            print(f"Created folder: {new_folder_path}")

        # Construct the new path for the file inside its destination folder
        new_file_path = os.path.join(new_folder_path, file)

        # Move the file from its original location to the new folder
        shutil.move(full_file_path, new_file_path)
        print(f"Moved '{file}' to '{new_folder_path}'")

print("\nFile organization complete! ✨")
