import os

known_extension = {
    "Photo" : ["jpg","jpeg","png","webp"],
    "Audio" : ["mp3","wav"],
    "Video" : ["mp4","wmv"],
    "Executable" : ["exe","apk"],
    "Code" : ["c", "cpp", "java", "py", "js", "ts", "php", "html", "css", "json", "xml"],
    "Documents" : ["txt", "pdf", "doc", "docx", "xls", "xlsx", "ppt", "pptx", "odt", "rtf"],
    "Others" : []
}

def isdir(p):
    return os.path.isdir(p)

def folder_Name(p):
    head,tail = os.path.splitext(p)
    for name in known_extension:
        if tail in known_extension[name]:
            return name
    known_extension["Others"].append("tail")
    return "Others"

