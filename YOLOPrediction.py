from ultralytics import YOLO
import cv2
import glob
from pathlib import Path
from tqdm import tqdm
import os
import pandas as pd
import numpy as np

folderName = 'Image-3'
outputFolder = f'Output_{folderName}'
os.makedirs(outputFolder, exist_ok=True)
model = YOLO('runs/segment/ACP_Adam2/weights/best.pt')
folderPath = glob.glob(f'For_Inference/{folderName}/*.JPG')

colors = [(0, 255, 0), (255, 0, 0), (0, 0, 255)]
for eachPath in tqdm(folderPath):
    try:
        imgName = Path(eachPath).stem
        img = cv2.imread(eachPath)
        saveOImg = img.copy()
        imgH, imgW = img.shape[0], img.shape[1]
        imgh1 = img[0:imgH//2, :]
        imgh2 = img[imgH//2:imgH, :]
        imgList = [imgh1, imgh2]
        outList = []
        for j, img in enumerate(imgList):
            saveImg = img.copy()
            imgHM = img.copy()
            # img = cv2.GaussianBlur(img, (3, 3), 0)
            results = model.predict(img, save=False, stream=True, conf=0.03, iou=0.1, verbose = False, max_det=10000)
            for r in results:
                try:
                    masks = r.masks.xy	   
                    for i, mask in enumerate(masks):
                        boxes = r.boxes
                        box = boxes[i]
                        conf = box.conf
                        if len(mask.astype('int32')) == 0:
                            continue         
                        cv2.drawContours(saveImg, [mask.astype('int32')], 0, colors[int(box.cls)], -1)                        
                    outList.append(saveImg)
                except Exception as e:
                    outList.append(saveImg)
                    continue
        vcon = cv2.vconcat(outList)
        out = cv2.hconcat([saveOImg, vcon])
        cv2.imwrite(f'{outputFolder}/{imgName}_out.jpg', out)
    except Exception as e:
        print(e)
        cv2.imwrite(f'{outputFolder}/{imgName}_out.jpg', img)
