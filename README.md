# yoloTools

## 1.Sort.py
> Just batch compress images, and organize them into Yolo directory format.

### Input directory:
    .
    ├── classes.txt
    ├── images/
    └── labels/
### Output directory:
    .
    ├── classes.txt
    ├── train/
    │   ├── images/
    │   └── labels/
    ├── valid/
    │   ├── images/
    │   └── labels/
    └── test/
        ├── images/
        └── labels/
### Usage:
#### 1.Organize your files into input directory pattern.
#### 2.Modify your root path.
#### 3.Set dataset ratio of train, valid, test.
#### 4.Just run!
    pip3 install -r requirements.txt
    python3 sort.py
    
## 2.validPlot.py
> Directly write box in the original image, using .json label files.
