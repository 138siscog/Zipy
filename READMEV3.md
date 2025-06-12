# Zipy - File compressor / Decompressor

**Zipy** is a simple file compressor that runs on python, this just in its early stages and can only compress files at this time but later will be able to decompress

## How to use

1. Files you would like to compress will need to be in the main directory of the project for now 
2. Run the app
3. type in the file name including the type tag (.txt, .py .iso (if its just a folder only the folder name will be needed))
4. once complete you will be asked if you would like to compress another file (If "Y" repeat the process, if "N" the program will close)

**Updates**
1. Logic Loops work as intended now
2. Now able to name your output folder instead of it taking the name of the original zip folder
3. added option 0 to show the begining 1,2,3 options

 ## TODO / Feature Wishlist
- [ ] **Be able to navigate for files instead of having them on main directory** 
- [ ] **be able to multi-select files to compress instead of having them all in a folder and compressing that folder** 
- [ ] **Work on a GUI for the app using TKinter**

## Requirements

- Python 3.x
- from zipfile import ZipFile