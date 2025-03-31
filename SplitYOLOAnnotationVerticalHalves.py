import cv2
from glob import glob
from tqdm import tqdm
from pathlib import Path
import os

pathOverall = r'\\10.15.1.24\Video1\08.SOFTWARE DEPARTMENT\Abhi\Dates\2024\December\31\Set01_New' 
outputPath = r'\\10.15.1.24\Video1\08.SOFTWARE DEPARTMENT\Abhi\Dates\2024\December\31\Set_01_FirstHalf'

folderPath = glob(f'{pathOverall}/*.txt')
for tFile in tqdm(folderPath):
    try:
        fileName = Path(tFile).stem
        imgFile = cv2.imread(pathOverall + '//' + f'{fileName}.jpg')
        h, w = imgFile.shape[:2]
        inTop = False
        inBottom = False
        overallTop = []
        overallBottom = []

        with open(tFile, 'r') as file:
            lines = file.readlines()
            annotations = [line.strip().split() for line in lines]
            for annotation in annotations:        
                firstHalf = []
                secondHalf = []
                cls_name, point = annotation[0], annotation[1:]
                i = 0
                pointList = []
                while i < len(point):
                    pointList.append((int(float(point[i]) * w), int(float(point[i + 1]) * h)))
                    i += 2
                for ip in pointList: 
                    if ip[1] < h // 2:
                        inTop = True
                    elif ip[1] >= h // 2:
                        inBottom = True
                
                newH = h // 2
                if inTop == True and inBottom == False:
                    inTop = False
                    inBottom = False
                    for j in range(len(pointList)):
                        firstHalf.extend([pointList[j][0] / w, pointList[j][1] / newH])
                elif inTop == False and inBottom == True:
                    inTop = False
                    inBottom = False
                    for j in range(len(pointList)):
                        secondHalf.extend([pointList[j][0] / w, (pointList[j][1] - newH) / newH])
                elif inTop == True and inBottom == True:
                    inTop = False
                    inBottom = False
                    for j in range(len(pointList)):
                        if pointList[j][1] < (h // 2):
                            firstHalf.extend([pointList[j][0] / w, (pointList[j][1]) / newH])
                    for j in range(len(pointList)):
                        if pointList[j][1] > (h // 2):
                            secondHalf.extend([pointList[j][0] / w, (pointList[j][1] - newH) / newH])
                overallTop.append([cls_name] + firstHalf)
                overallBottom.append([cls_name] + secondHalf)

        if len(overallTop) > 0:
            imgFirstHalf = imgFile[0 : h//2, :]
            for annotation in overallTop:
                txt = ''
                if len(annotation) > 1:
                    for item in annotation:
                        txt += str(item) + ' '
                    with open(outputPath + '//' + f'20240508_143553_{fileName}_FirstHalf.txt', 'a') as file:
                        file.write(txt + '\n')
            if os.path.isfile(outputPath + '\\' + f'20240508_143553_{fileName}_FirstHalf.txt'):
                cv2.imwrite(outputPath + '//' + f'20240508_143553_{fileName}_FirstHalf.jpg', imgFirstHalf)

        if len(overallBottom) > 0:
            imgSecondHalf = imgFile[h//2 : , :]
            for annotation in overallBottom:
                txt = ''
                if len(annotation) > 1:
                    for item in annotation:
                        txt += str(item) + ' '
                    with open(outputPath + '//' + f'20240508_143553_{fileName}_SecondHalf.txt', 'a') as file:
                        file.write(txt + '\n')
            if os.path.isfile(outputPath + '\\' + f'20240508_143553_{fileName}_SecondHalf.txt'):      
                cv2.imwrite(outputPath + '//' + f'20240508_143553_{fileName}_SecondHalf.jpg', imgSecondHalf)
    except Exception as e:
        pass
