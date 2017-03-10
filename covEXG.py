import cv2
import numpy as np
import os

def convert(filepath,filename,extension,savepath):
    # filepath = 'CRBD/Images/'
    # filename = 'crop_row_001'
    # extension = '.JPG'
    # savepath = 'CRBD-converted/'
    directory = filepath+filename+extension
    plantimg = cv2.imread(directory)

    width, height, channels = plantimg.shape
    size = (w, h, channels) = (width, height, 1)
    savesize = (w, h, channels) = (width*3, height, 1)
    exgimg = np.zeros(size, np.uint8)

    for wimg in range(0,width):
        for himg in range(0,height):
            blue = plantimg.item(wimg,himg,0)
            green = plantimg.item(wimg,himg,1)
            red = plantimg.item(wimg,himg,2)
            exg = 2*green-red-blue;
            exgimg.itemset((wimg,himg,0),exg)


    exgimgblurred = cv2.GaussianBlur(exgimg,(5,5),0)
    cv2.imshow('original', plantimg)
    cv2.imshow('not blurred', exgimg)
    cv2.imshow('blurred', exgimgblurred)
    if not os.path.exists(savepath+filename):
        os.makedirs(savepath+filename)
    cv2.imwrite(savepath+filename+'/original.png',plantimg)
    cv2.imwrite(savepath+filename+'/notblurred.png',exgimg)
    cv2.imwrite(savepath+filename+'/blurred.png',exgimgblurred)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
