# RLKA-Net 

### Official codes for Paper "Recurrent Large Kernel Attention Network for Efficient Single Infrared Image Super-Resolution" 

## Environment 
- [Pytorch >= 1.8](https://pytorch.org/)
- [BasicSR >= 1.3.5](https://github.com/xinntao/BasicSR-examples/blob/master/README.md)

## Introduction 
### Architecture 
![image](git_images\pic_arc.png) Overview of the architecture of RLKA-Net 

### Recurrent Learning Stragety
![image](git_images\RLS3.png) 

### Experiment Result on CVC09 Dataset (x4)
![image](git_images\result.png)

## Training
### Dataset:
### Original Infrared Images
- [OSU](http://vcipl-okstate.org/pbvs/bench/Data/01/download.html) 
- [FLIR](https://www.flir.com/oem/adas/adas-dataset-form/)
- [CVC09](http://adas.cvc.uab.es/elektra/enigma-portfolio/item-1/)
- [LLVIP](https://bupt-ai-cz.github.io/LLVIP/) 
### Downsample
Apply bicubic or lanczos downsample to obtain LR infrared images (Scale = 0.25 or 0.5).

' python scripts\infrared_multiscale.py --input \GT_IMAGE_PATH --output \LR_IMAGE_PATH --scale 0.5(or 0.25) --method bicubic(or lanczos)'
### Traning command
BasicSR framework is utilized to train our RLKA-Net.

' python basicsr/train.py -opt options/train/RLKAN/train_rlkan_flir_x4_r.yml '

Before running this training command, you should prepared the paired FLIR infrared images.

### Pre-trained models
Part of the Pre-trained models is avaliable [here](https://drive.google.com/file/d/1phi_J5IOHf4vEk8V6vriuGsntSkiqYAG/view?usp=sharing) (Google Drive).

### Infrared SR Performance
![image](git_images\result_pic1.png)
![image](git_images\result_pic2.png)


## Acknowledgements
We'd like to thank [MAN](https://github.com/icandle/MAN) and [BasicSR](https://github.com/XPixelGroup/BasicSR) for their enlightening work, and thank the author of OSU, FLIR, CVC09 and LLVIP for provide open-source infrared images!
