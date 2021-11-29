import PySimpleGUI as sg
import os
import time
from os import listdir
from datetime import date
from os.path import isfile, join,exists     

layout = [sg.Text("Choose a folder: "), sg.InputText(key='-IN-'), sg.FolderBrowse(key="-IN-")], [sg.Submit()]

window = sg.Window('Window Title', layout)    

event, values = window.read()    
window.close()

fileDict = {
            'js' : 'javascript',
            'docx' : 'documents',
            'html' : 'web',
            'css' : 'web',
            'zip' : 'compressed',
            'py' : 'python',
            'img' :'images',
            'png' :'images',
	    'jpg' :'images',
            'txt' :'text',
            'exe' : 'executable file',
            'class':'class',
            'java': 'java'}

mypath = values['-IN-']    

onlyfiles = [f for f in listdir(mypath) if isfile(join(mypath, f))]
for i in onlyfiles:
    file_extension = os.path.splitext(i)[1]
    file_extension = file_extension[1:]
    try:
        file_extension = fileDict[file_extension]
    except KeyError:
         pass
    os.chdir(mypath)
    if os.path.exists(file_extension):
       print(file_extension," folder is exist")
    else:
       os.mkdir(file_extension)
       print(file_extension,"folder is created")
    print("modified: %s" % time.ctime(os.path.getmtime(i)))
    year = time.ctime(os.path.getmtime(i))[-4:]
    print(year)
    if os.path.exists(year):
       print(year," folder is exist")
    else:
       os.mkdir(year)
       print(year,"folder is created")
    os.replace(i,file_extension+"/"+i)
   