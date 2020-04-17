import os

class radio_file_browser():
    
    file_tree = []
    current_file_contents = []
    current_path = ""
    
    def __init__(self):
        self.current_path = self.get_init_path()
        self.current_file_contents = self.get_folder_contents(self.current_path)
    
    def get_current_path(self):
        return self.current_path
    
    def get_current_contents(self):
        return self.current_file_contents
    
    def get_file_tree(self):
        return self.file_tree
    
    def get_folder_contents(self, path):
        contents = os.listdir(path)
        new_contents = []
        for entry in contents:
            #print(entry[0:2])
            if entry[0:2] == "m_":
                new_contents.append(entry)
        if len(new_contents) == 0:
            new_contents = contents
        return new_contents

    def get_init_path(self):
        path_file = open("pwd.txt", "r+")
        current_path = path_file.readlines()[0].strip()
        return current_path
    
    def get_new_path(self, file_name):
        self.current_path = self.current_path + "/" +file_name
        self.file_tree.append(self.current_path)
        self.current_file_contents = self.get_folder_contents(self.current_path)
        
    def get_previous_path(self):
        if len(self.file_tree) == 1:
            self.file_tree.pop()
            return self.get_init_path()
        if len(self.file_tree) == 0:
            return self.current_path
        else:
            self.file_tree.pop()
            self.current_path = self.file_tree[-1]
            self.current_file_contents = self.get_folder_contents(self.current_path)

rfb = radio_file_browser()
print(rfb.get_current_path())
print(rfb.get_current_contents())
print(rfb.get_file_tree())
def test_adding_to_path():
    rfb.get_new_path(rfb.get_current_contents()[1])
    return (rfb.get_current_path())
def test_removing_from_path():
    rfb.get_new_path(rfb.get_current_contents()[1])
    print("Pre: " + rfb.get_current_path())
    rfb.get_previous_path()
    return (rfb.get_current_path())

print(test_adding_to_path())
print("Post: " + test_removing_from_path())