# Computer Vision

*CURRENTLY UNDER CONSTRUCTION*

## Step-by-Step process to push to this repository

1. 'git add .' (Add all files but you can also add specify file)
2. 'git status' (optional)
3. 'git commit -m "Comment changes"
4. git remote -v (optional) 
5. git push -u origin master (origin is your remote link and branch is normally at master) (optionally you can create a new branch using 'git checkout -b new_branch')

NOTED: If you trying to snych directory, used git pull -u origin master

## Specify Code to remember
Specifiying path by using Path from pathlib
'path = Path("Folder1/Folder2/")
print(path.parent.absolute())'

'p = []' - To dynamically added list of folder
'for i in os.listdir(r'Faces\train'):' # Noted do its either as raw string literals  r ' ' or 'C:\\Direcxtory\\File
    p.append(i) 