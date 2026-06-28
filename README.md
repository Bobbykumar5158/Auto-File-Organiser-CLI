# Auto-File-Organiser-CLI
A command line interface to Organise the files in there respective folder according to the extension.

# Features
* Organise the folder by taking the path of that folder
* Create subfolder with title Code,Documents,Photos,Videos etc.
* Ask from the user if two files are present in the folder, to rename it or to overwrite it.
* Also checks if the given folder is already organished.
* Also checks if the path is present or not.

* Error Handling :
  * Invalid path given
  * Empty folder
  * Given path target to file
  * Files with same name

# Installation
## Clone the Repository

```bash
git clone https://github.com/Bobbykumar5158/Auto-File-Organiser-CLI
```

## Open Project Folder

```bash
cd Auto-File-Organiser-CLI
```
# Running the Program
```bash
python OrganiseFile.py
```

# What if you want to move some specific files to a folder ?
Just change the extension dictionary in OrganiseFile.py add item with folder name as key and list of extension in the value then all the file with same extension will be saved to the folder. 
Example
```bash
extension = { ......
              folder_name : [".ext1",".ext2", .....]
            }
```
