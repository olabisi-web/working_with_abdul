# Setting Up

from pathlib import Path               # It is user to input path into pathlib.

workspace = Path("workspace_files")    # It is user to creat a Folder.
workspace.mkdir(exist_ok=True)         # To know maybe the folder exist.
file_path = workspace / "notes.txt"    # It is user to creat a File.
file_path

# (A) Create or overwrite using 'w'
f = open(file_path, "w", encoding="utf-8")
f.write("This is the first line in notes.txt\n")
f.close()

# (B) Safe-create using 'x' (uncomment to try once)
# f = open(workspace / "created_once.txt", "x", encoding="utf-8")
# f.write("This file will only be created if it doesn't exist.\n")
# f.close()
