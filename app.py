import os
import sys
import time

from tools.backup.archieve_tools import zip_archieve
from tools.backup.copy_tools import change_if_name_exists,copy_files_meta
from tools.search_tools import simple_search
#Bottom Up functions


def run_task(task,matches):
    if task == '0':
        return 

    cwd: str = os.getcwd()
    path_for_copy: str = os.path.join(cwd,'copy')
    path_for_copy = change_if_name_exists(path_for_copy) 
    os.mkdir(path_for_copy)
    
    if task == '1':
        path: str = copy_files_meta(path_for_copy,matches)
        print(f'Copied to {path}')
        
    elif task == '2':
        archieve_name: str = 'backup - ' + time.strftime('%Y-%m-%d_%H-%M-%S')
        dest: str = os.path.join(cwd,archieve_name)
        target_dir: str = copy_files_meta(path_for_copy,matches)
        path = zip_archieve(dest,target_dir,delete_target=True)
        print(f'Archieved path:{path}')
        
        
def get_task() -> str:
    commands = ('0','1','2')
    while True:
        command = (input(f'Copy - 1,Archieve - 2,Exit - 0\n>>'))
        if command in commands:
            return command
        print(f'Please read it carefully, commands:{commands}')


def get_search_params() -> tuple[str, str, int, float]:
    start_path = input('Enter path(empty input - cwd)\n>>') or os.getcwd()
    
    if not os.path.isdir(start_path):
        print('There is no such directory or wrong directory')
        sys.exit(1)
        
    query = input('Looking for\n>>')
    time_stamp = int(input('How much time was it created?(empty - search any file)\n>>') or 0)*3600
    time_now = time.time()
    
    return start_path,query,time_stamp,time_now


def main():
    params: tuple[str, str, int, float] = get_search_params()
    matches: list[str] = simple_search(*params)
    print(f'Found {len(matches)} files')
    
    if not matches:
        return 

    task= get_task()
    run_task(task,matches)
        
    return
        
if __name__ == '__main__':
    main()
    
