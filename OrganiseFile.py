import os

# Change thi dictionary to create folder of your choice

known_extension = {
    "Photos" : [".jpg",".jpeg",".png",".webp"],
    "Audio" : [".mp3",".wav"],
    "Videos" : [".mp4",".wmv"],
    "Executable" : [".exe",".apk"],
    "Code" : [".c", ".cpp", ".java", ".py", ".js", ".ts", ".php", ".html", ".css", ".json", ".xml",".md"],
    "Documents" : [".txt", ".pdf", ".doc", ".docx", ".xls", ".xlsx", ".ppt", ".pptx", ".odt", ".rtf"],
    "Others" : []
}

# it takes the file path as argument and return the respective folder name for file 

def folder_Name(file_path):
    head,ext = os.path.splitext(file_path)
    for name in known_extension:
        if ext in known_extension[name]:
            return name
    known_extension["Others"].append(ext)
    return "Others"

# It asks user what to do when finds out two file with same name ?
# Return True/False and new name depending on user
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
        print("Note the name shouldn't be in the given list and Exclude extension. =>",os.listdir(destination_path))
        name = input("Enter the name you want to give : ")
        return name+(os.path.splitext(current_path)[1]),True

# Organise folder and returns moves_count
def organise(path):
    moves_count = 0
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
                    print(f"File exists in the folder '{folder}' with same name as '{file}'")
                    new_name,flag = rename(current_path,folder_path)
                    destination_path = os.path.join(folder_path,new_name)

                try:
                    if flag is None:
                        os.rename(current_path, destination_path)
                        # print(f"{file} Successfully moved to destination folder.")
                        moves_count += 1
                        file_trace(path,file,folder)
                    else:
                        os.replace(current_path,destination_path)
                        # print(f"{file} Successfully moved to destination folder.")
                        file_trace(path,file,folder,new_name,flag)
                    
                except Exception as e:
                    print("="*80)
                    print(f"An error has occured during moving the file {e}")
                    print("="*80)
    return moves_count

# Used to log changes in moves.txt file

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

def main():

    print("="*80)
    print(f"{' Auto File Organiser ':-^80}")
    print("="*80)

    choice = input("Do you want to organise folder ? (y/n) : ").lower().strip()
    while True :
        print("="*80)
        if choice == "y":
            path = input("To Organise enter the folder path here (without double or single quotes) : ").strip()
            print("-"*80)
            if os.path.exists(path):
                if os.path.isdir(path):
                    moves_count = organise(path)
                    if moves_count > 0:
                        print(f"{moves_count} file/files has been moved to their respective folders.\nAlso saved the changes made in moves.txt file.")
                    else:
                        if not os.listdir(path):
                            print("The given folder is Empty.")
                        else:
                            print("The given folder path is already Organised.")                
                else:
                    print(" Given folder path is not a folder ")
            else:     
                print(" Path does not exists ")

        elif choice == "n":
            print(f"{' Exiting the program ':-^80}")
            print("="*80)
            break
        else:
            print(f'{" Invalid Choice ":-^80}')
        print("="*80)
        choice = input("Do you want to organise another folder ? (y/n) : ").lower().strip()


if __name__ == "__main__":
    main()