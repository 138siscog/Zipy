from zipfile import ZipFile


print("Welcome to Zipy, select what you would like to do:")
print("1: Compress a file")
print("2: Decompress a file")
print("3: Exit")

selection = int(input("Make a selection: 1, 2, or 3:"))

match selection:
    case 1:
        files = []

        while True:
            toZip = input("What file would you like to Zip?: ")
            files.append(toZip)

            with ZipFile(f'{toZip}.zip', 'w') as zipf:
                for file in files:
                    zipf.write(file)
                print(f"Added {file} to zip")
            another = input("Would you like to zip another file? (Y/N)").upper()
            if  another != "Y":
                break
            else:
                files = files = []
                continue

    case 2:

        zip_path = input('Enter the name of your Zip File (example.zip): ')  
        extract_path = '.'        

        with ZipFile(zip_path, 'r') as zip_ref:
            zip_ref.extractall(extract_path)
            print(f"Extracted all contents of {zip_path} to {extract_path}")

    case 3:
        exit()