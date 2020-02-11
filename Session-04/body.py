from pathlib import Path
filename = 'U5.txt'
file_contents = Path(filename).read_text().split('\n')[1:]
for i in file_contents:

    print('Body of the U5.txt file:',i)