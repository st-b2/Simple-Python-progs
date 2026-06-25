import datetime
import os
import sys
import time


TIME_BORDER = 87000 # время за которое собирается log.txt
CHECK_DIRECTORY = r'D:\PythonProjects'  # путь по умолчанию
FILE_LOG = r'D:\PythonProjects\viruses\log.txt'
DATE_FORMAT = '%d.%m.%Y %H:%M:%S' 

def clear_log():
    f = open(FILE_LOG, 'w')
    f.close()


def find_virus(find_directory):
    for root, dirs, files in os.walk(find_directory):
        for name in files:
           file = os.path.join(root,name)
           if check(file):
                add_to_log(file)


def check(file):
    current_ts = time.time()  
    change_time = get_change_file(file)
    if change_time is None:
        return False
    return current_ts - change_time < TIME_BORDER
    

def get_change_file(file):
    m_time = os.stat(file).st_mtime
    a_time = os.stat(file).st_atime
    c_time = os.stat(file).st_ctime  
    return max(m_time, a_time, c_time)  


def add_to_log(file):
    change_time = get_change_file(file)
    if change_time is None:
        return
    adding_string = file + '    :   ' + datetime.datetime.fromtimestamp(change_time).strftime(DATE_FORMAT) + '\n'
    f = open(FILE_LOG, 'a')
    f.write(adding_string)
    f.close()


if __name__=='__main__':
    clear_log()
    if len(sys.argv) > 1:
        directory = sys.argv[1]
        find_virus(directory)
    else:
        user_input = input("Введите путь к директории для проверки (или нажмите Enter для использования пути по умолчанию): ")
        if user_input.strip():
            directory = user_input.strip()
        else:
            directory = CHECK_DIRECTORY
        find_virus(directory)