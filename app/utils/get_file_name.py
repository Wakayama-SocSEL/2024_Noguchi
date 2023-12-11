import os

def get_file_name(directory):
    FILE_NAME_LIST = []
    for filename in os.listdir(directory):
        if filename.endswith(".txt"):
            file_name = os.path.splitext(filename)[0]
            FILE_NAME_LIST.append(file_name)
    
    return FILE_NAME_LIST