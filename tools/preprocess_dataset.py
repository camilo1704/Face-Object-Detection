import matplotlib.pyplot as plt
from PIL import Image

from os import listdir
from os.path import isfile, join

dataset_root_path = '/home/cuchuflito/Documents/repos/Face-Object-Detection/dataset'
labels_path = join(dataset_root_path,'FDDB-folds')


label_list = [f for f in listdir(labels_path) if isfile(join(labels_path, f))]
label_list = [label_file for label_file in label_list if "ellipse" in label_file ]




crs = open(join(labels_path, label_list[0]), "r")
image_bboxes = {}
i=0
name = False
for columns in ( raw.strip().split() for raw in crs ):  
    print(columns)
    if i==0:
        if name==False:
            image_name = columns[0]
            image_bboxes[image_name] = []
            print(image_name)

            name=True
        else:
            number_bboxes = int(columns[0])
            print(number_bboxes)
            i+=1
    elif i<number_bboxes:
        image_bboxes[image_name].append(columns)
        i+=1
    else: 
        i=0
        name=False
key = list(image_bboxes.keys())[0]
print(image_bboxes.keys())