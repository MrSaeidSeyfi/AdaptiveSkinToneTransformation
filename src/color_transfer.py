import cv2
import numpy as np
from .skin_detection import detect_skin, average_skin_color

def transfer_skin_color(source_img: np.ndarray, target_img: np.ndarray):
    """Transfer the skin color from source image to target image."""
    # Detect skin in source and target
    source_skin, source_mask = detect_skin(source_img)
    target_skin, target_mask = detect_skin(target_img)

    # Compute average HSV of source and target
    source_h_mean, source_s_mean, source_v_mean = average_skin_color(source_img, source_mask)
    target_h_mean, target_s_mean, target_v_mean = average_skin_color(target_img, target_mask)

    # Adjust target skin to match source skin color
    return adjust_target_skin_color(target_img, target_mask, (source_h_mean, source_s_mean, source_v_mean))

def adjust_target_skin_color(img: np.ndarray, skin_mask: np.ndarray, target_hsv):
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(img_hsv)

    h_skin = np.ma.masked_array(h, mask=~(skin_mask > 0))
    s_skin = np.ma.masked_array(s, mask=~(skin_mask > 0))
    v_skin = np.ma.masked_array(v, mask=~(skin_mask > 0))

    h_diff = target_hsv[0] - h_skin.mean() if h_skin.count()>0 else 0
    s_diff = target_hsv[1] - s_skin.mean() if s_skin.count()>0 else 0
    v_diff = target_hsv[2] - v_skin.mean() if v_skin.count()>0 else 0

    h_skin += h_diff
    s_skin += s_diff
    v_skin += v_diff

    h_skin = np.clip(h_skin, 0, 179)
    s_skin = np.clip(s_skin, 0, 255)
    v_skin = np.clip(v_skin, 0, 255)

    h = h_skin.filled(h).astype(np.uint8)
    s = s_skin.filled(s).astype(np.uint8)
    v = v_skin.filled(v).astype(np.uint8)

    adjusted_hsv = cv2.merge([h,s,v])
    final_img = cv2.cvtColor(adjusted_hsv, cv2.COLOR_HSV2BGR)
    return final_img
