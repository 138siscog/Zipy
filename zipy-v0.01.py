from zipfile import ZipFile

files = []

while True:
    toZip = input("What file would you like to Zip?: ")
    files.append(toZip)

    with ZipFile(f'{toZip}.zip', 'w') as zipf:
        for file in files:
            zipf.write(file)
            print(f"Added {file} to zip")
    another = input("Would you like to zip anopther file? (Y/N)").upper()
    if  another != "Y":
        break
    else:
        files = files = []
        continue
