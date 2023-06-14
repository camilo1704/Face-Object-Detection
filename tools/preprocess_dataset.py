import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import numpy as np
import argparse



from os import listdir
from os.path import isfile, join




def preprocess_labels(dataset_root_path:str):
    """
    Dataset folder structure:
    --dataset_root_path
      |--annotations
        |--FDDB-folds
      |--images
        |--2002
    """


    labels_path = join(dataset_root_path,'annotations', 'FDDB-folds')
    images_path = join(dataset_root_path,'images')

    label_list = [f for f in listdir(labels_path) if isfile(join(labels_path, f))]
    label_list = [label_file for label_file in label_list if "ellipse" in label_file ]

    image_bboxes = {}

    for label_file in label_list:
        crs = open(join(labels_path, label_file), "r")
        i=0
        name = False
        number_bboxes = 0
        
        for columns in ( raw.strip().split() for raw in crs ):  

            if i==0:
                if name==False:
                    image_name = columns[0]
                    image_bboxes[image_name] = []
    
                    name=True
                else:
                    number_bboxes = int(columns[0])
                    
                    i+=1
                    
            elif i<=number_bboxes:
                image_bboxes[image_name].append(columns)
                i+=1
                if i>number_bboxes:
                    i=0
                    name=False

        
        crs.close()
    key = list(image_bboxes.keys())[0]
    #print(list(image_bboxes.keys())[0])
    key = "2002/07/25/big/img_100"
    print(image_bboxes[key])
    pil_img = Image.open(join(images_path, key+ ".jpg"))
    draw = ImageDraw.Draw(pil_img)
    for bbox in image_bboxes[key]:
        x_center = int(float(bbox[3]))
        y_center = int(float(bbox[4]))
        r_x = int(float(bbox[0]))
        r_y = int(float(bbox[1]))
        draw.rectangle(((x_center-r_x, y_center-r_y), (x_center+r_x, y_center+r_y)), fill=None)
    plt.imshow(np.array(pil_img))
    plt.show()
   # print(image_bboxes[list(image_bboxes.keys())[0]])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('--dataset_root_path', type=str)

    args, _ = parser.parse_known_args()
    print(args.dataset_root_path)

    preprocess_labels(args.dataset_root_path)
