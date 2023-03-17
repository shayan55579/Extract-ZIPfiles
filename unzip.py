import os 
import zipfile


# Changing the CWD 
os.chdir('E:\TA Filoger\Solving\Test\Ex07') #get the folder

dir = os.getcwd() 
list_of_folder = os.listdir(dir)

list_of_all_folders = [] #main folders: 1272248461
for i in range(0,len(list_of_folder)):
    list_of_all_folders.append(list_of_folder[i])





parent_dir = os.getcwd()

path = [] #'E:\\TA Filoger\\Solving\\Test\\Ex05\\1272248461'
for j in range(0,len(list_of_all_folders)):
    path.append(os.path.join(parent_dir, list_of_all_folders[j]))

list_dir_path = []
for i in range(0, len(path)):
    list_dir_path.append(os.listdir(path[i]))
name_ex = list_dir_path[1] #درگاه پاسخPythonEx01

file = []#'E:\\TA Filoger\\Solving\\Shayan\\۲۲۸۳۷۸۱۹۳۰\\درگاه پاسخPythonEx01'
for q in path:
    file.append(os.path.join(q, name_ex[0]))

zips = []            
for m in range(0, len(file)):
    for f in os.listdir(file[m]):
        if f.endswith(".zip"):
            #add path of zip file
            zips.append(os.path.join(file[m], f))



for q in range(0,len(zips)):
    with zipfile.ZipFile(zips[q], "r") as zip_file:
        zip_file.extractall(r'C:\Users\Shayan\Desktop\fi') # folder that saves files
