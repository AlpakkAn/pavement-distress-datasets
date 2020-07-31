import cv2
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input_dir', type=str, default='segmentation')
parser.add_argument('--output_dir', type=str, default='segmentation_contrast')
parser.add_argument('--level', type=int, default=100)
args = parser.parse_args()


def change_contrast(image):
	img = cv2.imread(image, 1)
	
	lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
	
	l, a, b = cv2.split(lab)
	
	clahe = cv2.createCLAHE(clipLimit=3.0, tileGridSize=(8,8))
	cl = clahe.apply(l)
	
	limg = cv2.merge((cl, a, b))
	
	final = cv2.cvtColor(limg, cv2.COLOR_LAB2BGR)
	cv2.imwrite(os.path.join(args.output_dir, filename), final)


if __name__ == '__main__':
	for filename in os.listdir(args.input_dir):
		if filename.endswith(".png"):
			change_contrast(os.path.join(args.input_dir, filename))
