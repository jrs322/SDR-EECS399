import os

class radio_file_browser():
    
    file_tree = []
    current_file_contents = []
    current_path = ""
    def __init__():
        self.current_path = self.get_init_path()
        self.current_file_contents = self.get_folder_contents(self.current_path)
                
    def get_folder_contents(self, path):
        contents = os.listdir(path)
        new_contents = []
        for entry in contents:
            #print(entry[0:2])
            if entry[0:2] == "m_":
                new_contents.append(entry)
        return new_contents

    def get_init_path(self):
        path_file = open("pwd.txt", "r+")
        current_path = path_file.readlines()[0].strip()
        return current_path
    
    def get_new_path(self, file_name):
        self.current_path = self.current_path + "/" +file_name
        self.file_tree.append(self.current_path)
        
    def get_previous_path(self):
        if size(self.file_tree) == 1:
            self.file_tree.pop()
            return self.get_init_path()
        if size(self.file_tree) == 0:
            return self.current_path
        else:
            self.file_tree.pop()
            return self.file_tree[-1]
            