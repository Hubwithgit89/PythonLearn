import os
import shutil

source_path='D:\Test1'
destiation_path='D:\Test2'

def file_copy(src, dest):

    for item in os.listdir(src):
        file_path = os.path.join(src, item)

        # if item is a file, copy it
        if os.path.isfile(file_path):
            shutil.copy(file_path, dest)

        # else if item is a folder, recurse
        elif os.path.isdir(file_path):
            new_dest = os.path.join(dest, item)
            os.mkdir(new_dest)
            recursive_copy(file_path, new_dest)

file_copy(source_path, destiation_path)
print('file  copied')
