# file-directory-renamer
Wrote this python file that renames images in a folder with subfolders to another folder (cuts and renames, not copies and renames). This works when the subfolders have dates as their names and it renames each image inside each subfolder to "(date) - (number)" ordered chronologically from earliest to latest by image modification date and time. 

## Hierarchy 
### Before Running the Code
```
├───samples
│   ├───February 6, 2022
│   │ 	├─── pic 1.jpg
│   │ 	├─── pic 2.jpg
│   │ 	├─── pic 3.jpg
│   │ 	└─── pic 4.jpg
│   └───June 15, 2022
│     	├─── pic 1.jpg
│   	├─── pic 2.jpg
│     	├─── pic 3.jpg
│    	└─── pic 4.jpg
├── final_output
├── rename_pls.py
└── README.md
```

### After Running the Code
```
├───samples
│   ├───February 6, 2022
│   ├───June 15, 2022
├── final_output
│   ├─── 02-06-2022 - 1.jpg
│   ├─── 02-06-2022 - 2.jpg
│   ├─── 02-06-2022 - 3.jpg
│   ├─── 02-06-2022 - 4.jpg
│   ├─── 06-15-2022 - 1.jpg
│   ├─── 06-15-2022 - 2.jpg
│   ├─── 06-15-2022 - 3.jpg
│   ├─── 06-15-2022 - 4.jpg
├── rename_pls.py
└── README.md
```

# To Run
```
python rename_pls.py <source folder> <target folder>
```

### Sample: 
```
python rename_pls.py samples final_output
```

# Windows Executable 
```
rename_pls.exe
```
Click the exe and an input prompt will show up, type the input and output folders to get it to work. Transformed the **"rename_pls_inputver.py"** into an .exe using:
```
pyinstaller --noconfirm --onefile --console 'rename_pls_inputver.py'
``` 

# To Do's
1. Make it a copy-rename instead of cut-rename 
2. Transform into a script so no python install required 
