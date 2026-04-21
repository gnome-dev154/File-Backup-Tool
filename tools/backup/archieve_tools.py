import shutil

from .copy_tools import copy_files_meta


def zip_archieve(dest: str,target,*,is_file_list=False,delete_target=False) -> str:
    if is_file_list:
        target = copy_files_meta(dest,target)

    shutil.make_archive(dest,'zip',target)
    
    if delete_target:
        shutil.rmtree(target)
    
    return dest + '.zip'
