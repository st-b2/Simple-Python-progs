import os

DIRECTORY = r'D:\PythonProjects'

def rename_files (firnd_directory):
    for root, dirs, files in os.walk(firnd_directory):
        for name in files:
            rename_file(root,name)

def rename_file(root, name):
    # print(name)
    # print(root)
    valid_name = get_valid_name(name)
    old_file = os.path.join(root,name)
    new_file = os.path.join(root,valid_name)
    os.rename(old_file, new_file)
    # print(old_file)
    # os.rename


def get_valid_name(name):
    name = name.replace('_Diff.', '_BC')
    if not name.startswith('A_'):
        name = 'A_' + name
    return name

if __name__=='__main__':
    rename_files(DIRECTORY)