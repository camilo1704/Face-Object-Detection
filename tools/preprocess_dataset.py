import matplotlib.pyplot as plt
from PIL import Image, ImageDraw
import numpy as np
from random import shuffle
import argparse
from os import listdir
from os.path import isfile, join
from typing import Text, Dict, List


def split_dataset(images_keys:List, train_perc=.7, valid_perc=.2)->Dict:
    """
    return dataset split
    """
    assert train_perc+valid_perc<1

    shuffle(images_keys)
    dataset_split = {
        "training_set": images_keys[:int(train_perc*len(images_keys))],
        "validation_set": images_keys[int(train_perc*len(images_keys)):int((train_perc+valid_perc)*len(images_keys))],
        "test_set": images_keys[int((train_perc+valid_perc)*len(images_keys)):]
    }
    return dataset_split

def save_processed_yolo_dataset(dataset_dict:Dict, raw_dataset_path:Text, save_dataset_path:Text):
    for split in dataset_dict.keys():
        save_path = join(save_dataset_path, split)
        for key in dataset_dict[split]:
            pil_img = Image.open(join(raw_dataset_path, "images", key+ ".jpg"))
            x_l, y_l = pil_img.size
            yolo_img_key = "images/"+key.replace("/","%")+".jpg"
            pil_img.save(join(save_path, yolo_img_key))
            yolo_labels_file_name = yolo_img_key.replace("images", "labels").replace("jpg", "txt")
            f = open(join(save_path,yolo_labels_file_name), "a")
            for bbox in image_bboxes[key]:
                x_center = int(float(bbox[3]))
                y_center = int(float(bbox[4]))
                r_y = int(float(bbox[0]))
                r_x = int(float(bbox[1]))
                line = "0 " + str(x_center/x_l)+" "+str(y_center/y_l) + " "+str(2*r_x/x_l) + " " +str(2*r_y/y_l)+"\n"
                f.write(line)
            f.close()


def get_images_keys_with_annotations(dataset_root_path:str):
    """
    Dataset folder structure:
    --dataset_root_path
      |--annotations
        |--FDDB-folds
      |--images
        |--2002
    """


    labels_path = join(dataset_root_path,'annotations', 'FDDB-folds')

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
                if name is False:
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
    
    images_keys = list(image_bboxes.keys())
    return images_keys

#     #print(list(image_bboxes.keys())[0])
#     key = "2002/07/25/big/img_15"
#     print(image_bboxes[key])
#     pil_img = Image.open(join(images_path, key+ ".jpg"))
#     draw = ImageDraw.Draw(pil_img)
#     x_l, y_l = pil_img.size
#     yolo_img_key = "images/"+key.replace("/","%")+".jpg"
#     pil_img.save(join(save_root_path, yolo_img_key))
#     yolo_labels_file_name = yolo_img_key.replace("images", "labels").replace("jpg", "txt")
#     f = open(join(save_root_path,yolo_labels_file_name), "a")
#     for bbox in image_bboxes[key]:
#         x_center = int(float(bbox[3]))
#         y_center = int(float(bbox[4]))
#         r_y = int(float(bbox[0]))
#         r_x = int(float(bbox[1]))
#         line = "0 " + str(x_center/x_l)+" "+str(y_center/y_l) + " "+str(2*r_x/x_l) + " " +str(2*r_y/y_l)+"\n"
#         f.write(line)
#         print(x_center, y_center)
#         draw.rectangle(((x_center-r_x, y_center-r_y), (x_center+r_x, y_center+r_y)), fill=None)
#     f.close()
#     plt.imshow(np.array(pil_img))
#     plt.show()
#    # print(image_bboxes[list(image_bboxes.keys())[0]])


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument('dataset_root_path', type=str)
    parser.add_argument('save_root_path', type=str)

    args, _ = parser.parse_known_args()

    images_keys = get_images_keys_with_annotations(args.dataset_root_path)
    dataset_split = split_dataset(images_keys)
    save_processed_yolo_dataset(dataset_split, args.dataset_root_path, args.save_root_path )
