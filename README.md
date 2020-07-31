# Datasets for Asphalt quaLity Prediction with Automated Computer vision Assessment (ALPACA)

This repository contains the annotated datasets used for my Master's thesis for my degree in Computer Science at the Norwegian University of Science and Technology (NTNU).

## Dataset for Detection
The annotated dataset for object detection of pavement distress will be available soon after removing all personal information.

## Dataset for Segmentation
The "segmentation" folder contains the annotated dataset for semantic segmentation of pavement distress.

## Dataset for Forecasting
The "forecasting" folder contains the dataset for time series forecasting of pavement distress severity.

## Contrast Enhancement
For global contrast enhancement, run

```
python3 contrast_global.py --input_dir <INPUT_DIR> --output_dir <OUTPUT_DIR> --level <LEVEL>
```

For contrast enhancement with Contrast Limited Adaptive Histogram Equalization (CLAHE), run

```
python3 contrast_clahe.py --input_dir <INPUT_DIR> --output_dir <OUTPUT_DIR>
```