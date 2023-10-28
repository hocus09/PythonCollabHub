import os
import shutil

# Function to create a directory if it doesn't exist
def create_directory(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

# Function to move files to the appropriate directory
def organize_files(source_dir, target_dir):
    for filename in os.listdir(source_dir):
        file_path = os.path.join(source_dir, filename)
        if os.path.isfile(file_path):
            # Get the file extension (e.g., .jpg, .pdf)
            file_extension = filename.split('.')[-1].lower()
            # Define destination directory based on the file extension
            destination = os.path.join(target_dir, file_extension)
            create_directory(destination)
            # Move the file to the destination directory
            shutil.move(file_path, os.path.join(destination, filename))

if __name__ == "__main__":
    source_directory = "path_to_your_source_directory"
    target_directory = "path_to_your_target_directory"

    organize_files(source_directory, target_directory)
    print("Files organized successfully.")
