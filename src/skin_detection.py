import cv2
import numpy as np

def detect_skin(img: np.ndarray):
    """Detect skin regions in an image using YCrCb color space."""
    img_ycrcb = cv2.cvtColor(img, cv2.COLOR_BGR2YCrCb)
    lower = np.array([0, 135, 85], dtype=np.uint8)
    upper = np.array([255, 180, 135], dtype=np.uint8)
    skin_mask = cv2.inRange(img_ycrcb, lower, upper)
    skin = cv2.bitwise_and(img, img, mask=skin_mask)
    return skin, skin_mask

def average_skin_color(img: np.ndarray, skin_mask: np.ndarray):
    """Calculate the average HSV color in the skin region."""
    skin_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(skin_hsv)

    h = np.ma.masked_array(h, mask=~(skin_mask > 0))
    s = np.ma.masked_array(s, mask=~(skin_mask > 0))
    v = np.ma.masked_array(v, mask=~(skin_mask > 0))

    h_mean = h.mean() if h.count() > 0 else 0
    s_mean = s.mean() if s.count() > 0 else 0
    v_mean = v.mean() if v.count() > 0 else 0

    return h_mean, s_mean, v_mean
