# Face-Object-Detection

Face detection model train with model **YOLOv8**
# Trained model

The model was trained using a NVIDIA GeForce GTX 1070. 
An example using the trained model on images from the validation set is shown below.

&nbsp;


![training metrics](./results/val_output_1.jpg)

## Dataset and preprocessing tools

[FDDB (Face Detection Data Set)](http://vis-www.cs.umass.edu/fddb/) was used to train the model. The script tools/preprocess_dataset.py process and transform images and labels to the yolov8 dataset format.

```
./tools/preprocess_dataset.py --dataset_root_path --save_root_path
```

## Training metrics 
Training metrics are shown bellow with P, R, F1 and PR curves.
<p align="middle">
<img src="./results/metrics.png" width="900" /> 
<img src="./results/losses.png" width="900" />
</p>

<p align="middle">
<img src="./results/P_curve.png" width="300" /> 
<img src="./results/R_curve.png" width="300" />
</p>

<p align="middle">
<img src="./results/F1_curve.png" width="300" />
<img src="./results/PR_curve.png" width="300" />
</p>
