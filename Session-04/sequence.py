from pathlib import Path
filename = 'ADA.txt'
file_contents = Path(filename).read_text().split('\n')[1:]
new_file = file_contents.remove('\n')
print(len('new_file'))
