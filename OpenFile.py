import os, sys
import tkinter as tk
from tkinter import filedialog
# get all the filenames
def getList(path):
    dirs = os.listdir( path )
    dirnames =[]
    for file in dirs:
        dirnames.append(path +'/'+ file)
    return dirnames

root = tk.Tk()
root.withdraw()
#root.filename =  filedialog.askopenfilename(initialdir = "/",title = "Select file",filetypes = (("jpeg files","*.jpg"),("all files","*.*")))
folder_path = filedialog.askopenfilename()# os.getcwd()
# This would print all the files
print("path:"+folder_path)
print ("Path: "+root.filename)
'''
dirnames = getList(folder_path)

for file in dirnames:

   print(file)'''
