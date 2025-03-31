import os
from tqdm import tqdm

def countAnnotations(annotationDir):
    classCounts = {}

    for filename in tqdm(os.listdir(annotationDir)):
        if filename.endswith('.txt'):
            with open(os.path.join(annotationDir, filename), 'r') as file:
                for line in file:
                    classId = line.split()[0]  
                    if classId in classCounts:
                        classCounts[classId] += 1
                    else:
                        classCounts[classId] = 1

    return classCounts

annotationPath = r'\\10.15.1.24\Video1\08.SOFTWARE DEPARTMENT\Vyshak\TransconomyImageryData\Data\ForTraining\1st_Stage_Training_Mar28\Mar31\OTHERS'

classCounts = countAnnotations(annotationPath)

for classId, count in classCounts.items():
    print(f'Class {classId}: {count} annotations')
