import os

source = 'main.txt'

dest = 'newfile.txt'

os.rename(source, dest)

print("The file has been successfully renamed!")