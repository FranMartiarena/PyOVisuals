import cv2
import sys
import imageio


#Shape is rows, columns, channels.
#Pixel access is the same.

if len(sys.argv) != 3:
    print("2 arguments: image_to_modify.x output_name.x")
    print("Where x is the extention")
    sys.exit()
    
im = cv2.imread(f"{sys.argv[1]}")

for y in range(im.shape[0]):
    for x in range(im.shape[1]):
        im[y,x][0] = int(('0b' + bin(im[y,x][0])[-1] + bin(im[y,x][0])[3:-1] + bin(im[y,x][0])[2])  ,2)
        im[y,x][1] = int(('0b' + bin(im[y,x][1])[-1] + bin(im[y,x][1])[3:-1] + bin(im[y,x][1])[2])  ,2)
        im[y,x][2] = int(('0b' + bin(im[y,x][2])[-1] + bin(im[y,x][2])[3:-1] + bin(im[y,x][2])[2])  ,2)
cv2.imwrite(f"{sys.argv[2]}", im)

