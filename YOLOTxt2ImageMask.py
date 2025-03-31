import cv2
import numpy as np
from glob import glob
from tqdm import tqdm
from pathlib import Path
import shutil

folderNameaJPG = sorted(glob(r'C:\Users\AbhishekAB\Desktop\New folder\*.JPG'))
for imgPath in tqdm(folderNameaJPG):
    try:
        imgName = Path(imgPath).stem
        imgNameCopy = Path(imgPath).name
        img = cv2.imread(imgPath)
        h, w = img.shape[:2]
        blackImg = np.zeros((h, w, 3), dtype=np.uint8)
        with open(rf'C:\Users\AbhishekAB\Desktop\New folder\{imgName}.txt', 'r') as f:
            yolo_txt = f.read()    
        annotations = yolo_txt.strip().split('\n')
        for annotation in annotations:
            parts = annotation.split(' ')
            classID = int(parts[0])
            points = []

            for i in range(1, len(parts), 2):
                if parts[i] == '':
                    continue
                x = float(parts[i]) * w
                y = float(parts[i + 1]) * h
                points.append([int(float(x)), int(float(y))])
            # cv2.fillPoly(blackImg, pts=[np.array(points)], color=[255, 255, 255])
            if classID == 0:
                cv2.fillPoly(blackImg, pts=[np.array(points)], color=[0, 255, 0])
            elif classID == 1:
                cv2.fillPoly(blackImg, pts=[np.array(points)], color=[255, 0, 0])
            elif classID == 2:
                cv2.fillPoly(blackImg, pts=[np.array(points)], color=[0, 0, 255])
        shutil.copy(rf'C:\Users\AbhishekAB\Desktop\New folder\{imgNameCopy}', rf'{imgNameCopy}')
        cv2.imwrite(rf'{imgName}_Mask.jpg', blackImg)
        # break
    except Exception as e:
        print(e)
