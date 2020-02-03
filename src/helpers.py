import os

def get_files_and_folders(folder):
        folder_list = []
        files_list = []
    
        for root, dirs, filenames in os.walk(folder):
            for dirname in dirs:
                folder_list.append(os.path.join(dirname))
                
            for filename in filenames:
                files_list.append(os.path.abspath(os.path.join(root, filename)))
                
            break
         
        return folder_list, files_list