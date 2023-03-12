import os 
import zipfile


# Changing the CWD 
os.chdir('E:\TA Filoger\Solving\Shayan') 
    
dir = os.getcwd() 
list_of_folder = os.listdir(dir)

list_of_all_folders = []#main folders
for i in range(0,len(list_of_folder)):
    list_of_all_folders.append(list_of_folder[i])


path = []
file = []#'E:\\TA Filoger\\Solving\\Shayan\\۲۲۸۳۷۸۱۹۳۰\\درگاه پاسخPythonEx01'
note_books = [] # 'E:\\TA Filoger\\Solving\\Shayan\\۲۲۸۳۷۸۱۹۳۰\\درگاه پاسخPythonEx01\\FCVS_Feb23_Python_Ex01_Arman_Vahedipour_Tabrizi.ipynb'
parent_dir = os.getcwd()
for j in range(0,len(list_of_all_folders)):
    path.append(os.path.join(parent_dir,list_of_all_folders[i]))
    for k in os.listdir(path[j]):
        file.append(os.path.join(path[j], k))        
        for z in os.listdir(file[j]):
            note_books.append(os.path.join(file[j], z))
            if os.path.isfile(note_books[j]):
                print(note_books[j])
            
for m in range(0,len(file)):
    for file in os.listdir(file[m]):
        if file.endswith(".zip"):
            with zipfile.ZipFile(file, "r") as zip_file:
                zip_file.extractall()


