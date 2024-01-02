import os
import shutil

def organize_files_by_extension(directory_path):
    files = os.listdir(directory_path)

    for file in files:
        file_path = os.path.join(directory_path, file)

        if os.path.isfile(file_path):
            _, extension = os.path.splitext(file)
            extension = extension[1:]

            destination_folder = os.path.join(directory_path, extension)

            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            shutil.move(file_path, os.path.join(destination_folder, file))

if __name__ == "__main__":
    while True:
        path = input("Enter Path (type 'exit' to quit): ")

        if path.lower() == 'exit':
            break

        if os.path.exists(path) and os.path.isdir(path):
            organize_files_by_extension(path)
            print("Files organized successfully!")
        else:
            print("Invalid directory path. Please provide a valid directory.")
