import os


def folder_contents(path):
    contents = os.listdir(path)
    new_contents = []
    for entry in contents:
        #print(entry[0:2])
        if entry[0:2] == "m_":
            new_contents.append(entry)
    return new_contents

def get_path():
    path_file = open("pwd.txt", "r+")
    current_path = path_file.readlines()[0].strip()
    return current_path


def 
