import os
import json
from tqdm import tqdm

folderPath = r"\\10.15.1.24\Video1\08.SOFTWARE DEPARTMENT\Vyshak\TransconomyImageryData\Data\ForTraining\1st_Stage_Training_Mar28\Without_Correction_Jsons"

uniqueLabels = set()

for filename in tqdm(os.listdir(folderPath)):
    if filename.endswith(".json"):
        filePath = os.path.join(folderPath, filename)
        
        with open(filePath, "r") as f:
            try:
                data = json.load(f)

                if "shapes" in data:
                    for shape in data["shapes"]:
                        label = shape.get("label")
                        if label:
                            uniqueLabels.add(label)
            
            except Exception as e:
                print(f"Error reading {filename}: {e}")

print("Unique labels found in the folder:")
for label in sorted(uniqueLabels):
    print(label)
