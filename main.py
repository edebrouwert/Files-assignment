__winc_id__ = "ae539110d03e49ea8738fd413ac44ba8"
__human_name__ = "files"

#Exercise 1
import os
import shutil
def clean_cache():
    current_directory = os.getcwd()
    new_directory = os.path.join(current_directory, r'cache')
    if os.path.exists(new_directory):
        shutil.rmtree(new_directory)
    os.mkdir(new_directory)

#Exercise 2
def cache_zip(zipfilepath, cachedirpath):
    shutil.unpack_archive(zipfilepath, cachedirpath)

#Exercise 3
def cached_files():
    filelist = [os.path.abspath(i) for i in os.scandir(r"C:\Users\erwin\Documents\Winc\files\cache")]
    return filelist

#Exercise 4
def find_password(filepathlist):
    password = ""
    for filepath in filepathlist:       #loop over the files in the list of file paths
        file = open(filepath)           #open file
        filecontent = file.readlines()  #put every line in the file into a list of strings
        for i in filecontent:           #loop over list and check if the word password is in item. If so, set password
            if "password" in i:        
                password = i
    return password

