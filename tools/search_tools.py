import os

def simple_search(
    path: str, query: str,time_stamp: int | None = None,time_now: float | None = None
) -> list[str]:
    matches = []
    for address, dirs, files in os.walk(path):
        for file in files: 
            if query not in file:
                continue
            
            full_path = os.path.join(address, file)  # Формируем полный путь к файлу
            
            if is_correct_search(full_path,time_stamp,time_now):
                matches.append(full_path)
                
    return matches 


def is_correct_search(full_path: str,time_stamp: int | None,time_now: float | None) -> bool:
    if os.path.islink(full_path):  # Если симлинк пропускаем
        return False
                
    if time_stamp and time_now:  # Если есть временной диапазон проверяем
        return time_now - os.path.getctime(full_path) < time_stamp
    
    return True
   