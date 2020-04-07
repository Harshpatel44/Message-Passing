__author__ = 'Harsh'
import os
import shutil
print(os.getcwd())
new="sample.txt"
def moving(new):
    os.chdir("""C:\\Users\\Harsh\\Desktop""")
    name,ext=os.path.splitext(new)
    name=name+"_2"+ext
    return name
    #print(name)
    #print(ext)
moving(new)
