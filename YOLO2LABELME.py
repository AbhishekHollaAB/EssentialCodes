import json
from glob import glob
from pathlib import Path
import cv2
import tqdm


def yolo_to_labelme_file(input_file, output_file, image_width, image_height):
    with open(input_file, 'r') as f:
        yolo_txt = f.read()    
    labelme_json = yolo_to_labelme(yolo_txt, image_width, image_height)
    with open(output_file, 'w') as f:
        json.dump(labelme_json, f, indent=4)

def yolo_to_labelme(yolo_txt, image_width, image_height):
    annotations = yolo_txt.strip().split('\n')

    class_id_to_name = {
        '0': 'low',
        '1': 'moderate',
        '2': 'high'
    }

    labelme_json = {
        "version": "5.2.1",
        "flags": {},
        "shapes": [],
        "imagePath": f'{str(indFileName)}.JPG',
        "imageData": None,
        "imageHeight": image_height,
        "imageWidth": image_width
    }
    
    for annotation in annotations:
        parts = annotation.split(' ')
        class_id = int(parts[0]) 
        points = []
        
        for i in range(1, len(parts), 2):
            if parts[i] == '':
                continue
            x = float(parts[i]) * image_width
            y = float(parts[i+1]) * image_height
            points.append([x, y])

        shape = {
            "label": class_id_to_name[str(class_id)],
            "points": points,
            "group_id": None,
            "shape_type": "polygon",
            "flags": {}
        }
        
        labelme_json["shapes"].append(shape)
    
    return labelme_json

overallFolder = r'\\10.15.1.24\Video1\08.SOFTWARE DEPARTMENT\Abhi\Dates\2024\December\25\Cracks JSON'
imageFolder = glob(f'{overallFolder}/*')
for imgPath in tqdm.tqdm(imageFolder):
    if imgPath.endswith('.jpg') or imgPath.endswith('.JPG'):
        indFileName = Path(imgPath).stem
        input_file = f'{overallFolder}/{indFileName}.txt'
        output_file = f'//10.15.1.24/Video1/08.SOFTWARE DEPARTMENT/Abhi/Dates/2024/December/25/Cracks JSON/{indFileName}.json'
        image_file = f'{overallFolder}/{indFileName}.JPG'
        img = cv2.imread(image_file, 0)
        image_height, image_width = img.shape[0], img.shape[1] 
        yolo_to_labelme_file(input_file, output_file, image_width, image_height)

print("Conversion complete.")
