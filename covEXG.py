import cv2
import numpy as np
import os

def savePlants(savename,plantimg,exgimg,exgimgblurred,original,notblurred,blurred,otsu,extension):
    cv2.imwrite(savename+'/'+original+extension,plantimg)
    cv2.imwrite(savename+'/'+notblurred+extension,exgimg)
    cv2.imwrite(savename+'/'+blurred+extension,exgimgblurred)

    ret2,th2 = cv2.threshold(exgimgblurred,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    cv2.imwrite(savename+'/'+otsu+extension,th2)

def convert(filepath,filename,extension,savepath):
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

    if not os.path.exists(savepath+filename):
        os.makedirs(savepath+filename)

    savePlants(savepath+filename,plantimg,exgimg,exgimgblurred,'original','notblurred','blurred','otsu','.png')
