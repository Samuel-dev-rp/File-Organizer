import os
import shutil

download_folder = os.path.expanduser("~/Downloads")

for file in os.listdir(download_folder):
    filename, file_extension = os.path.splitext(file)
    file_extension = file_extension[1:]
    
    folder_to_organize = f"{download_folder}/{file_extension}"
    
    if not os.path.exists(folder_to_organize):
        os.makedirs(folder_to_organize)
        
    shutil.move(f"{download_folder}/{file}", f"{folder_to_organize}/{file}")