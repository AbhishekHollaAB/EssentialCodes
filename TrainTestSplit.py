import os
from tqdm import tqdm
import shutil
from sklearn.model_selection import train_test_split as tt

txt_path = r'Z:\08.SOFTWARE DEPARTMENT\Abhi\Dates\2024\December\16\ForUNET'

dire = [i for i in os.listdir(txt_path) if i.endswith('_Mask.jpg')]
print(len(dire))

train, val=tt(dire, train_size=0.83, test_size=0.17, random_state=204)
print(len(train), len(val))

os.makedirs('Z:/08.SOFTWARE DEPARTMENT/Abhi/Dates/2024/December/18/data/train/images', exist_ok=True)
os.makedirs('Z:/08.SOFTWARE DEPARTMENT/Abhi/Dates/2024/December/18/data/train/masks', exist_ok=True)
os.makedirs('Z:/08.SOFTWARE DEPARTMENT/Abhi/Dates/2024/December/18/data/test/images', exist_ok=True)
os.makedirs('Z:/08.SOFTWARE DEPARTMENT/Abhi/Dates/2024/December/18/data/test/masks', exist_ok=True)

for trfile in tqdm(train):
    try:
        # print(trfile[:-9], ' ' ,trfile)
        # break
        try:    
            shutil.copy(f'{txt_path}/{trfile[:-9]}.jpg', 'Z:/08.SOFTWARE DEPARTMENT/Abhi/Dates/2024/December/18/data/train/images/')
        except:
            shutil.copy(f'{txt_path}/{trfile[:-9]}.JPG', 'Z:/08.SOFTWARE DEPARTMENT/Abhi/Dates/2024/December/18/data/train/images/')
        shutil.copy(f'{txt_path}/{trfile}', 'Z:/08.SOFTWARE DEPARTMENT/Abhi/Dates/2024/December/18/data/train/masks/')
    except Exception as e:
        print(e)

for vafile in tqdm(val):
    try:
        try:
            shutil.copy(f'{txt_path}/{vafile[:-9]}.jpg', 'Z:/08.SOFTWARE DEPARTMENT/Abhi/Dates/2024/December/18/data/test/images/')
        except:
            shutil.copy(f'{txt_path}/{vafile[:-9]}.JPG', 'Z:/08.SOFTWARE DEPARTMENT/Abhi/Dates/2024/December/18/data/test/images/')
        shutil.copy(f'{txt_path}/{vafile}', 'Z:/08.SOFTWARE DEPARTMENT/Abhi/Dates/2024/December/18/data/test/masks')
    except Exception as e:
        print(e)
