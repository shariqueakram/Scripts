import os
import shutil

# Define paths
downloads_folder = os.path.expanduser('~/Downloads')
destination_folder = os.path.expanduser('~/Documents/SortedDownloads')

# Create destination folders if they don't exist
file_types = {
    'images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'documents': ['.pdf', '.csv', '.docx', '.json', '.txt', '.xlsx', '.xlsm'],
    'videos': ['.mp4', '.mkv', '.avi'],
    'audio': ['.mp3', '.wav'],
    'scripts': ['.py', '.js', '.html', '.sh'],
    'decks': ['pptx']
}

for folder in file_types.keys():
    path = os.path.join(destination_folder, folder)
    if not os.path.exists(path):
        os.makedirs(path)

# Move files based on their type
for filename in os.listdir(downloads_folder):
    file_path = os.path.join(downloads_folder, filename)
    if os.path.isfile(file_path):
        file_extension = os.path.splitext(filename)[1].lower()
        moved = False
        for folder, extensions in file_types.items():
            if file_extension in extensions:
                destination_path = os.path.join(
                    destination_folder, folder, filename)
                shutil.move(file_path, destination_path)
                print(f'Moved {filename} to {destination_path}')
                moved = True
                break
        if not moved:
            # If no match found, keep in Downloads
            destination_path = os.path.join(downloads_folder, filename)
            shutil.move(file_path, destination_path)
            print(f'No matching folder for {filename}. Kept in Downloads')

print("Files sorted.")
