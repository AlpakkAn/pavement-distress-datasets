from PIL import Image
import os
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--input_dir', type=str, default='valid_tk')
parser.add_argument('--output_dir', type=str, default='valid_tk_contrast')
parser.add_argument('--level', type=int, default=100)
args = parser.parse_args()


def change_contrast(img, level):
    factor = (259 * (level + 255)) / (255 * (259 - level))
    def contrast(c):
        value = 128 + factor * (c - 128)
        return max(0, min(255, value))
    return img.point(contrast)


if __name__ == '__main__':
    for filename in os.listdir(args.input_dir):
        if filename.endswith(".png"):
            image = change_contrast(Image.open(os.path.join(args.input_dir, filename)), 125)
            image.save(os.path.join(args.output_dir, filename))
