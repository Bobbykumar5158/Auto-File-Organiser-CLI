import os

known_extension = {
    "Photos" : [".jpg",".jpeg",".png",".webp"],
    "Audio" : [".mp3",".wav"],
    "Videos" : [".mp4",".wmv"],
    "Executable" : [".exe",".apk"],
    "Code" : [".c", ".cpp", ".java", ".py", ".js", ".ts", ".php", ".html", ".css", ".json", ".xml",".md"],
    "Documents" : [".txt", ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".odt", ".rtf"],
    "Others" : []
}

def isdir(path):
    return os.path.isdir(path)

def folder_Name(path):
    head,ext = os.path.splitext(path)
    for name in known_extension:
        if ext in known_extension[name]:
            return name
    known_extension["Others"].append(ext)
    return "Others"

def rename(current_path,destination_path):
    print("="*80)
    print("Do you want to change its name ?(Y/N)\nIf no then it will overwrite the file")
    choice = input("Enter your Choice : ").lower().strip()

    if choice == "n":
        print("\nOverwriting the file ....")
        print("="*80)
        return os.path.split(current_path)[1],False

    else:
        if not (choice == "y"):
            print ("\nInvalid Choice. Going to Rename it")
        print("Exclude extension.")
        print("Note the name should not be in the given list. =>",os.listdir(destination_path))
        name = input("Enter the name you want to give : ")
        print("="*80)
        return name+(os.path.splitext(current_path)[1]),True


def organise(path):
    for root,dirs,files in os.walk(path):
        if any(folder in root for folder in ["Code", "Documents","Executable", "Photos","Audio", "Videos", "Others"]):
            continue

        for file in files:
            current_path = os.path.join(root,file)

            if file == "moves.txt":
                continue
            else:
                folder = folder_Name(current_path)
                folder_path = os.path.join(path,folder)
                if not os.path.exists(folder_path):
                    os.mkdir(folder_path)
            
                destination_path = os.path.join(folder_path,file)
                flag = None
                if os.path.exists(destination_path):
                    print("="*80)
                    print(f"File exists in the folder {folder} with same name i.e {file}")
                    new_name,flag = rename(current_path,folder_path)
                    destination_path = os.path.join(folder_path,new_name)

                try:
                    if flag is None:
                        os.rename(current_path, destination_path)
                        print(f"{file} Successfully moved to destination folder.")
                        file_trace(path,file,folder)
                    else:
                        os.replace(current_path,destination_path)
                        print(f"{file} Successfully moved to destination folder.")
                        file_trace(path,file,folder,new_name,flag)
                    
                except Exception as e:
                    print("*"*80)
                    print(f"An error has occured during moving the file {e}")
                    print("*"*80)

def file_trace(path,file,move_to,new_name = None,renamed = None):
    moves = os.path.join(path,"moves.txt")
    with open(moves,"a") as f:
        if renamed is True:
            move = f"\n '{file}' is moved to folder '{move_to}' & renamed to '{new_name}'\n"
        elif renamed is False:
            move = f"\n '{file}' is moved to folder '{move_to}' & Overwrite the existing file in '{move_to}'\n"
        else:
            move = f" '{file}' is moved to folder '{move_to}'\n"
        f.write(move)
