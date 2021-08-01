'Stuff to make sure the working directory is whereever this script is
Set objShell = CreateObject("Wscript.Shell")
strPath = Wscript.ScriptFullName
Set objFSO = CreateObject("Scripting.FileSystemObject")
Set objFile = objFSO.GetFile(strPath)
strFolder = objFSO.GetParentFolderName(objFile) 

objShell.CurrentDirectory = strFolder

'This starts the python script without a cmd window popping up (0 as second parameter = hidden)
CreateObject("Wscript.Shell").Run "python shadowplay_hotkeys.py", 0