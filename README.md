# AdaptiveSkinToneTransformation
This Python project provides tools for detecting, adjusting, and transferring human skin tones in images. It uses OpenCV for image processing and can be easily integrated into other image processing pipelines.


## Key Features:
- **Skin Detection:** Automatically identify skin areas in images.
- **Tone Adjustment:** Modify skin tone to various predefined categories (e.g., dark, brown, light).
- **Color Transfer:** Transfer skin color from one image to another, making the target image's skin tone closely match the source.

## Methodology

1. **Skin Detection:**  
   - Convert the input image to a suitable color space (like YCrCb) where skin tones are more easily distinguishable.  
   - Apply a predefined threshold to isolate skin regions, generating a binary mask that highlights these areas.

2. **Skin Tone Analysis:**  
   - Once the mask is created, focus on the skin pixels and convert them to HSV color space.  
   - Calculate the average HSV values of the detected skin region to understand its current tonal characteristics.

3. **Tone Adjustment or Color Transfer:**  
   - **Tone Adjustment:**  
     Based on user input (e.g., "brown", "light"), adjust the HSV channels (mainly saturation and brightness) within the masked region. This allows shifting the skin tone towards the desired target.
     
   - **Color Transfer:**  
     For transferring a skin tone from one image to another, compute the average skin color of the source and target images. Then, adjust the target image’s skin pixels so their HSV values match the source image’s average skin tone.

4. **Reconstruction:**  
   - After applying these adjustments, merge the modified HSV channels back into a complete image.  
   - Convert the result back to the BGR color space for final output.

## Usage:
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Adjust skin tone:
   ```bash
   python main.py --mode adjust --input path_to_input_image.jpg --output output.jpg --tone brown
   ```
3. Transfer skin color:
   ```bash
   python main.py --mode transfer --input source_image.jpg --target target_image.jpg --output output.jpg
   ```
## Results:

    Example outputs are provided using CFD database images, which were utilized as test samples for this project. 


   ![image](https://github.com/user-attachments/assets/d9c4bd5e-94d1-4e33-bfe0-d4d348bec3a5)


   ![image](https://github.com/user-attachments/assets/aca170e8-b436-4841-874d-317397d3b177)

   ![image](https://github.com/user-attachments/assets/8c2368e5-11a5-49d6-bcfe-8ec052b2daf7)


