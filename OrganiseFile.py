import os

known_extension = {
    "Photo" : [".jpg",".jpeg",".png",".webp"],
    "Audio" : [".mp3",".wav"],
    "Video" : [".mp4",".wmv"],
    "Executable" : [".exe",".apk"],
    "Code" : [".c", ".cpp", ".java", ".py", ".js", ".ts", ".php", ".html", ".css", ".json", ".xml",".md"],
    "Documents" : [".txt", ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".odt", ".rtf"],
    "Others" : []
}

def isdir(path):
    return os.path.isdir(path)

def folder_Name(path):
    head,tail = os.path.splitext(path)
    for name in known_extension:
        if tail in known_extension[name]:
            return name
    known_extension["Others"].append("tail")
    return "Others"

def rename(current_path,destination_path):
    print(f"Do you want to change its name OR want to overwrite it ?")
    choice = input("(Y/N) : ").lower().strip()

    if choice == "n":
        print("Overwriting the file. New file will be saved")
        return os.path.split(current_path)[1]

    else:
        if not (choice == "y"):
            print ("Invalid Choice. Renaming it")
        print("Exclude extension.")
        print("Note the name should not be in the given list. =>",os.listdir(destination_path))
        name = input("Enter the name you want to give : ")
        return name+(os.path.splitext(current_path)[1])

def organise(path):
    for child in os.listdir(path):
        current_path = os.path.join(path,child)
        if child == ".git" or child.startswith(".git"):
            continue
        if isdir(current_path):
            organise(current_path)
        else:
            folder = folder_Name(current_path)
            folder_path = os.path.join(path,folder)
            if not os.path.exists(folder_path):
                os.mkdir(folder_path)
            
            destination_path = os.path.join(folder_path,child)
            if os.path.exists(destination_path):
                print(f"File exists in the folder {folder} with same name i.e {child}")
                file = rename(current_path,destination_path)
                destination_path = os.path.join(folder_path,file)
            try:
                os.rename(current_path, destination_path)
            except Exception as e:
                print("An error has occured during moving the file",e)
                