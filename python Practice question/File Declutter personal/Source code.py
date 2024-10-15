import os
directory ='E:\. photos'
def filerename(file_name,i):
    name, extension = os.path.splitext(file_name)
    file_name = f'su{i}{extension}'
    return file_name
                           
def open(directory):
    file_list = os.listdir(directory)
    for i, filename in enumerate(file_list, start=1):
        if filename.endswith('_thumb.jpg'):
            try:
               os.remove(filename)
            except FileNotFoundError:
                continue
        if filename.endswith((".jpg",".png")):
            old_path = os.path.join(directory,filename)
            new_file_name = filerename(filename,i)
            new_path = os.path.join(directory,new_file_name)
            os.rename(old_path,new_path)
            print(f"{old_path} --> {new_path}")
open(directory)
