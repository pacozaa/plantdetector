import cv2
import numpy as np
import os


def calEXG(red,green,blue):
    result = 2*green-red-blue
    return result

def calEXR(red,green,blue):
    result = 1.5*red-green-blue
    return result

def savePlants(savename,plantimg,exgimg,exgimgblurred,original,notblurred,blurred,otsu,extension):
    cv2.imwrite(savename+'/'+original+extension,plantimg)
    cv2.imwrite(savename+'/'+notblurred+extension,exgimg)
    cv2.imwrite(savename+'/'+blurred+extension,exgimgblurred)

    ret2,th2 = cv2.threshold(exgimgblurred,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)
    cv2.imwrite(savename+'/'+otsu+extension,th2)

def convertGreen(rawimg):
    width, height, channels = rawimg.shape
    size = (w, h, channels) = (width, height, 1)
    processedimg = np.zeros(size, np.uint8)
    for wimg in range(0,width):
        for himg in range(0,height):
            blue = rawimg.item(wimg,himg,0)
            green = rawimg.item(wimg,himg,1)
            red = rawimg.item(wimg,himg,2)
            exg = calEXG(red,green,blue)
            if(exg > 50):
                processedimg.itemset((wimg,himg,0),exg)

    return processedimg

def convertRed(rawimg):
    width, height, channels = rawimg.shape
    size = (w, h, channels) = (width, height, 1)
    processedimg = np.zeros(size, np.uint8)
    for wimg in range(0,width):
        for himg in range(0,height):
            blue = rawimg.item(wimg,himg,0)
            green = rawimg.item(wimg,himg,1)
            red = rawimg.item(wimg,himg,2)
            exg = calEXR(red,green,blue)
            if(exg > 50):
                processedimg.itemset((wimg,himg,0),exg)

    return processedimg



def convertTofile(filepath,filename,extension,savepath):
    directory = filepath+filename+extension
    plantimg = cv2.imread(directory)

    exgimg = convertGreen(plantimg)
    exgimgblurred = cv2.GaussianBlur(exgimg,(5,5),0)

    if not os.path.exists(savepath+filename):
        os.makedirs(savepath+filename)

    savePlants(savepath+filename,plantimg,exgimg,exgimgblurred,'original','notblurred','blurred','otsu','.png')
