from zipfile import ZipFile


print("Welcome to Zipy, select what you would like to do:")
print("1: Compress a file")
print("2: Decompress a file")
print("3: Exit")

while True:
    print('\n')
    selection = int(input("Make a selection: 1, 2, 3 or 0 for options:\n"))

    match selection:
        case 0:
            print("1: Compress a file")
            print("2: Decompress a file")
            print("3: Exit")
            continue
        case 1:
            files = []

            while True:
                toZip = input("What file would you like to Zip?:\n ")
                files.append(toZip)

                with ZipFile(f'{toZip}.zip', 'w') as zipf:
                    for file in files:
                        zipf.write(file)
                    print(f"Added {file} to zip")
                another = input("Would you like to zip another file? (Y/N)\n").upper()
                if  another != "Y":
                    break
                else:
                    files = []
                    continue

        case 2:
            while True:
                zip_path = input('Enter the name of your Zip File (example.zip):\n')  
                extract_path = input('Name your output foler:\n')        

                with ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(extract_path)
                    print(f"Extracted all contents of {zip_path} to {extract_path}")
                another = input("Would you like to unzip another file? (Y/N)\n").upper()
                if  another != "Y":
                    break
                else:
                    continue
        case 3:
            exit()