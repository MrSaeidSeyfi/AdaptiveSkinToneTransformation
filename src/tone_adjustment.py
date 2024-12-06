import cv2
import numpy as np

def adjust_skin_tone(img: np.ndarray, skin_mask: np.ndarray, skin_tone: str):
    """Adjust the skin tone of the detected skin areas in an image."""
    img_hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    h, s, v = cv2.split(img_hsv)

    # Create masked arrays for skin areas
    h_skin = np.ma.masked_array(h, mask=~(skin_mask > 0))
    s_skin = np.ma.masked_array(s, mask=~(skin_mask > 0))
    v_skin = np.ma.masked_array(v, mask=~(skin_mask > 0))

    # Adjust based on desired skin tone using simple arithmetic operators
    if skin_tone == "black":
        s_skin = s_skin + 120
        v_skin = v_skin - 100
    elif skin_tone == "dark":
        s_skin = s_skin + 60
        v_skin = v_skin - 40
    elif skin_tone == "brown":
        s_skin = s_skin + 30
        v_skin = v_skin - 20
    elif skin_tone == "olive":
        s_skin = s_skin + 20
        # No brightness change for olive
    elif skin_tone == "light":
        s_skin = s_skin - 10
        v_skin = v_skin + 30
    elif skin_tone == "yellow":
        s_skin = s_skin - 15
        v_skin = v_skin + 10
    else:
        # If no valid tone is provided, no changes will be applied
        pass

    # Clip values to ensure they remain within valid HSV ranges
    h_skin = np.clip(h_skin, 0, 179)
    s_skin = np.clip(s_skin, 0, 255)
    v_skin = np.clip(v_skin, 0, 255)

    # Convert masked arrays back to normal arrays
    # filling masked elements with original values
    h = h_skin.filled(h).astype(np.uint8)
    s = s_skin.filled(s).astype(np.uint8)
    v = v_skin.filled(v).astype(np.uint8)

    # Merge and convert back to BGR
    final_hsv = cv2.merge([h, s, v])
    final_img = cv2.cvtColor(final_hsv, cv2.COLOR_HSV2BGR)
    return final_img
