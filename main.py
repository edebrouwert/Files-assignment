__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

import os
import shutil

cwd = os.getcwd()
path_to_cache = os.path.join(cwd, r'cache')

#Exercise 1
def clean_cache():
    if os.path.exists(path_to_cache):
        shutil.rmtree(path_to_cache)
    os.mkdir(path_to_cache)

#Exercise 2
def cache_zip(zipfilepath, cachedirpath):
    shutil.unpack_archive(zipfilepath, cachedirpath)

#Exercise 3
def cached_files():
    filelist = [os.path.abspath(i) for i in os.scandir(path_to_cache)]
    return filelist

#Exercise 4
def find_password(filepathlist):
    password = ""
    for filepath in filepathlist:       #loop over the files in the list of file paths
        file = open(filepath)           #open file
        filecontent = file.readlines()  #put every line in the file into a list of strings
        for i in filecontent:           #loop over list and check if the word password is in item. If so, set password
            if "password" in i:        
                password = i.split()[1]
    return password
