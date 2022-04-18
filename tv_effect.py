import cv2
import numpy as np
import random
import imageio
import sys

if len(sys.argv) < 3 or len(sys.argv) > 4:
    print("2 arguments: image_to_modify output_name")
    print("Optional: -d  Displays the process")
    sys.exit()
else:
    if len(sys.argv) == 3:
        display = False
    else:
        display = True

im = cv2.imread(f"{sys.argv[1]}")
mask = np.zeros((im.shape[0],im.shape[1],3), np.uint8)
gif = []
cd = 0
while True:
    cd += 1
    c = 0
    row = random.randint(1, im.shape[0]-3)
    for y in range(2):
        for l in range(0, im.shape[0]-3,4):
            mask[y+l] = im[y+l]
            mask[y+l+1] = im[y+l+1]
            mask[y+l+2] = im[y+l+2]
        if c % 10 == 0:
            mask[row] = np.roll(mask[row], 5)       
            mask[row+1] = np.roll(mask[row+1], 5)
            mask[row+2] = np.roll(mask[row+2], 5)
        c += 1
        frame_rgb = cv2.cvtColor(mask, cv2.COLOR_BGR2RGB)
        if display:
            cv2.imshow("",mask)
            cv2.waitKey(50)
        gif.append(frame_rgb)
        mask = np.zeros((im.shape[0],im.shape[1],3), np.uint8)
    
    if cd ==20:
        imageio.mimsave(f"{sys.argv[2]}.gif",gif, fps=60)
        break
