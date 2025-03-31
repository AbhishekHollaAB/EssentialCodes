from PIL import Image
from glob import glob
from tqdm import tqdm
from pathlib import Path

def compress_image_retain_exif(input_path, output_path, quality=70):
    with Image.open(input_path) as img:
        exif_data = img.info.get('exif')
        img.save(output_path, format='JPEG', quality=quality, subsampling=0, optimize=True, exif=exif_data)

outputImagePath = r'\\10.15.1.23\Video 2\Teleqo_Tech\Project-25_Miami_2024\01.INPUT\Miami\Miami Collection Deliverables\C\PANOS\Ladybug_Panoramic_6_Compress'
imgFolder = glob(r'\\10.15.1.23\Video 2\Teleqo_Tech\Project-25_Miami_2024\01.INPUT\Miami\Miami Collection Deliverables\C\PANOS\Ladybug_Panoramic_6\*.jpg')
for imgPath in tqdm(imgFolder):
    imgName = Path(imgPath).name
    compress_image_retain_exif(imgPath, f'{outputImagePath}/{imgName}', quality=70)
