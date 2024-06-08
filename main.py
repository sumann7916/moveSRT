import os
import shutil
import subprocess
import sys

def find_matching_folder(file_path, movie_dir):
    file_name = os.path.splitext(os.path.basename(file_path))[0]
    folders = [folder for folder in os.listdir(movie_dir) if os.path.isdir(os.path.join(movie_dir, folder))]
    similarity_scores = {folder: similarity(file_name, folder) for folder in folders}
    sorted_folders = sorted(folders, key=lambda folder: similarity_scores[folder], reverse=True)
    return sorted_folders[0]

def similarity(str1, str2):
    return sum(1 for char in str1 if char in str2)

def move_srt_file(file_path, folder, movie_dir):
    destination_path = os.path.join(movie_dir, folder)
    try: 
        shutil.move(file_path, destination_path)
        print(f"Moved '{file_path}' to '{destination_path}'.")
    except shutil.Error:
        print(f"Error: Failed to move '{file_path}' to '{destination_path}'.")

def main(source_dir, movie_dir):
    if not os.path.exists(source_dir):
        print(f"Error: The source directory '{source_dir}' does not exist.")
        sys.exit(1)
    if not os.path.exists(movie_dir):
        print(f"Error: The movie directory '{movie_dir}' does not exist.")
        sys.exit(1)
    
    file_extension = '.srt'
    process = subprocess.Popen(['inotifywait', '-m', '-e', 'create', source_dir], stdout=subprocess.PIPE)
    
    try:
        for line in iter(process.stdout.readline, b''):
            file_name = line.decode('utf-8').strip().split()[-1]
            if file_name.endswith(file_extension):
                matching_folder = find_matching_folder(os.path.join(source_dir, file_name), movie_dir)
                move_srt_file(os.path.join(source_dir, file_name), matching_folder, movie_dir)
    finally:
        process.stdout.close()

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python move_files.py <source_dir> <movie_dir>")
    
    source_dir = sys.argv[1]
    movie_dir = sys.argv[2]
    
    main(source_dir, movie_dir)
