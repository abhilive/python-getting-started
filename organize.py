import os
import shutil

def organize_files_on_desktop(desktop_path):
    # Define categories and their corresponding file extensions
    categories = {
        'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.svg'],
        'Documents': ['.txt', '.pdf', '.doc', '.docx', '.xls', '.xlsx', '.ppt', '.pptx'],
        'Archives': ['.zip', '.rar', '.7z']
    }
    
    # Create subfolders for each category if they don't exist
    for category in categories:
        category_path = os.path.join(desktop_path, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)
    
    # Iterate through files on desktop and move them to corresponding subfolders
    for file_name in os.listdir(desktop_path):
        file_path = os.path.join(desktop_path, file_name)
        if os.path.isfile(file_path):
            # Get file extension
            _, extension = os.path.splitext(file_name)
            extension = extension.lower()  # Convert to lowercase for comparison
            
            # Check if the file extension matches any category
            for category, extensions in categories.items():
                if extension in extensions:
                    destination_folder = os.path.join(desktop_path, category)
                    shutil.move(file_path, destination_folder)
                    print(f"Moved '{file_name}' to '{category}' folder.")
                    break

if __name__ == "__main__":
    desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")
    organize_files_on_desktop(desktop_path)
