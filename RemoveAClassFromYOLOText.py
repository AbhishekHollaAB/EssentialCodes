from glob import glob
from pathlib import Path
from tqdm import tqdm

txtFolder = glob(r'\\10.15.1.24\Video1\08.SOFTWARE DEPARTMENT\Abhi\Patches Images\Image_Annotations\*.txt')
for eachText in tqdm(txtFolder):
    fileName = Path(eachText).name
    inputFile = eachText

    with open(inputFile, 'r') as file:
        lines = file.readlines()

    filteredLines = [line for line in lines if not line.startswith('1')]

    with open(rf'\\10.15.1.24\Video1\08.SOFTWARE DEPARTMENT\Abhi\Dates\2024\July\26\Images\{fileName}', 'w') as file:
        file.writelines(filteredLines)

