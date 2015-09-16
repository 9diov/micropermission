from micropermission import Permission

class MyFolder(object):
    def __init__(self, name):
        self.name = name
        self.children = []

    def add_child(self, child):
        self.children.append(child)

class MyFile(object):
    def __init__(self, name):
        self.name = name

root = MyFolder('/')
root_file = MyFile('a file')
root_folder = MyFolder('a folder')
nested_file = MyFile('a nested file')

root.add_child(root_file)
root.add_child(root_folder)
root_folder.add_child(nested_file)

p = Permission()
