import json
import os
from tqdm import tqdm

def convert_json_to_yolo(json_file, output_dir, class_map):
    with open(json_file, 'r') as file:
        data = json.load(file)
    
    image_width = data['imageWidth']
    image_height = data['imageHeight']
    
    yolo_lines = []
    
    for shape in data['shapes']:
        label = shape['label']
        points = shape['points']
        class_id = class_map.get(label, -1)
        
        if class_id == -1:
            continue  

        normalized_points = []
        for point in points:
            x = point[0] / image_width
            y = point[1] / image_height
            normalized_points.extend([x, y])
        
        yolo_line = f"{class_id} " + " ".join([f"{p:.8f}" for p in normalized_points])
        yolo_lines.append(yolo_line)
    
    image_path = data['imagePath']
    image_name = os.path.splitext(os.path.basename(image_path))[0]
    output_file = os.path.join(output_dir, f"{image_name}.txt")
    
    with open(output_file, 'w') as file:
        file.write("\n".join(yolo_lines))

json_directory = r"\\10.15.1.24\Video1\08.SOFTWARE DEPARTMENT\Vyshak\TransconomyImageryData\Data\ForTraining\1st_Stage_Training_Mar28\Mar31\OTHERS"
output_directory = r"\\10.15.1.24\Video1\08.SOFTWARE DEPARTMENT\Vyshak\TransconomyImageryData\Data\ForTraining\1st_Stage_Training_Mar28\Mar31\OTHERS"
class_mapping = {"Cracking LOW": 0, "Cracking MOD": 1, "Cracking HIGH": 2}  

os.makedirs(output_directory, exist_ok=True)

for json_filename in tqdm(os.listdir(json_directory)):
    if json_filename.endswith(".json"):
        json_file = os.path.join(json_directory, json_filename)
        convert_json_to_yolo(json_file, output_directory, class_mapping)
