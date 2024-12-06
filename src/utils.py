import cv2
import os

def load_image(path: str):
    if not os.path.exists(path):
        raise FileNotFoundError(f"Image not found: {path}")
    img = cv2.imread(path)
    if img is None:
        raise ValueError(f"Could not read image: {path}")
    return img

def save_image(img, path: str):
    cv2.imwrite(path, img)
