import os
import shutil


def copy_files_meta(dest: str,file_paths: list[str]):
    base_copy_files(dest,file_paths)
    return dest


def copy_files(dest: str,file_paths: list[str]):
    base_copy_files(dest,file_paths,is_meta=False)
    return dest


def base_copy_files(dest: str,file_paths: list[str],is_meta=True):
    for file in file_paths:
        file_name = file.rsplit(os.path.sep,maxsplit=1)[-1]
        dest_file_name = os.path.join(dest,file_name)
        dest_file_name = change_if_name_exists(dest_file_name)
        if is_meta:
            shutil.copy2(file,dest_file_name)
        else:
            shutil.copy(file,dest_file_name)
    
    
def change_if_name_exists(dest_name: str,is_file=False):
    destination,name =  dest_name.rsplit(os.path.sep,maxsplit=1)
    count = 2
    while os.path.exists(dest_name):
        if is_file:
            new_name = name.replace('.',f'({count}).',count=1)
        else:
            new_name = name + f"({count})"
        dest_name = os.path.join(destination,new_name)
        count +=1
        
    return dest_name